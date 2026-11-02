"""Independent finite checks for the clique census of matrix idempotents.
Run: python verify.py. Uses only the Python standard library.
"""
from itertools import product, combinations
from math import factorial, prod
from collections import Counter


def gl_order(n,q,s):
    if n == 0: return 1
    assert s % q == 0
    t=s//q
    return t**(n*n)*prod(q**n-q**i for i in range(n))


def tuples(n,k,q,s):
    g=[gl_order(i,q,s) for i in range(n+1)]
    h=2**k
    # polynomial coefficient of (sum_i z^i/g_i)^h, multiplied by g_n
    from fractions import Fraction
    poly=[Fraction(0)]*(n+1);poly[0]=Fraction(1)
    for _ in range(h):
        nxt=[Fraction(0)]*(n+1)
        for a in range(n+1):
            for b in range(n-a+1):
                nxt[a+b]+=poly[a]*Fraction(1,g[b])
        poly=nxt
    result=g[n]*poly[n]
    assert result.denominator==1
    return result.numerator


def signed_stirling(k):
    # s(k,j) signed Stirling numbers of the first kind
    row=[1]
    for z in range(1,k+1):
        old=row;row=[0]*(z+1)
        for j in range(z+1):
            row[j]=(old[j-1] if j else 0)-(z-1)*(old[j] if j<len(old) else 0)
    return row


def clique_counts_formula(n,q,s):
    values=[tuples(n,k,q,s) for k in range(2**n+1)]
    out=[]
    for k in range(2**n+1):
        count=sum(v*values[j] for j,v in enumerate(signed_stirling(k)))
        assert count % factorial(k)==0
        out.append(count//factorial(k))
    return out


def finite_ring(q,s,mul,add=None):
    return {'q':q,'s':s,'mul':mul,'add':add or (lambda a,b:(a+b)%s)}


def prod_sum(A,B,i,j,n,ring):
    val=0
    for k in range(n):
        val=ring['add'](val,ring['mul'](A[i*n+k],B[k*n+j]))
    return val

def matmul(A,B,n,ring):
    mul=ring['mul'];q=ring['s']
    return tuple(prod_sum(A,B,i,j,n,ring) for i in range(n) for j in range(n))


def idem_graph(n,ring):
    ids=[]
    for v in product(range(ring['s']),repeat=n*n):
        if matmul(v,v,n,ring)==v:ids.append(v)
    adj=[set() for _ in ids]
    for i in range(len(ids)):
        for j in range(i):
            if matmul(ids[i],ids[j],n,ring)==matmul(ids[j],ids[i],n,ring):
                adj[i].add(j);adj[j].add(i)
    return ids,adj


def all_clique_sets(adj):
    # Recurse on increasing vertex sequences. Small cases only.
    out=Counter({0:1})
    def rec(prefix,candidates):
        for index,v in enumerate(candidates):
            out[len(prefix)+1]+=1
            rec(prefix+(v,),[w for w in candidates[index+1:] if w in adj[v]])
    rec(tuple(), list(range(len(adj))))
    return out


def maximal_cliques(adj):
    result=[]
    def bron(R,P,X):
        if not P and not X:
            result.append(frozenset(R));return
        for v in list(P):
            bron(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
    bron(set(),set(range(len(adj))),set())
    return result


f2=finite_ring(2,2,lambda a,b:a*b)
f3=finite_ring(3,3,lambda a,b:a*b)
z4=finite_ring(2,4,lambda a,b:a*b)
f2eps=finite_ring(2,4,lambda a,b:((a&1)*(b&1))%2 + 2*((((a&1)*(b>>1))+((a>>1)*(b&1)))%2),lambda a,b:a^b)
f2twodual=finite_ring(2,8,lambda a,b:((a&1)*(b&1))%2+2*((((a&1)*((b>>1)&1))+(((a>>1)&1)*(b&1)))%2)+4*((((a&1)*((b>>2)&1))+(((a>>2)&1)*(b&1)))%2),lambda a,b:a^b)

for label,n,ring in [('F2/2',2,f2),('F3/2',2,f3),('Z4/2',2,z4),('F2eps/2',2,f2eps),('F2twodual/2',2,f2twodual),('F2/3',3,f2)]:
    ids,adj=idem_graph(n,ring)
    measured=all_clique_sets(adj) if len(ids)<=30 else None
    if measured is None:
        # Enumerate from maximal cliques to avoid unnecessary recursion over many shared branches
        maxes=maximal_cliques(adj)
        sets=set()
        for C in maxes:
            arr=sorted(C)
            for mask in range(1<<len(arr)):
                sets.add(tuple(arr[i] for i in range(len(arr)) if mask>>i&1))
        measured=Counter(map(len,sets))
    else:
        maxes=maximal_cliques(adj)
    pred=clique_counts_formula(n,ring['q'],ring['s'])
    assert [measured.get(k,0) for k in range(len(pred))]==pred,(label, measured, pred)
    gn=gl_order(n,ring['q'],ring['s'])
    g1=gl_order(1,ring['q'],ring['s'])
    assert len(maxes)==gn//(factorial(n)*g1**n)
    assert all(len(C)==2**n for C in maxes)
    if n==2:
        N=gn//g1**2
        assert len(ids)==N+2
        assert sorted(len(A) for A in adj)==[3]*(N)+[N+1]*2
    print(label, 'idempotents',len(ids),'clique counts',pred, 'maximal',len(maxes))
print('VERIFY_OK')
