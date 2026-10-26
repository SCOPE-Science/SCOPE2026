"""Finite verification of adjoint ranks for graph Lie algebras.

Uses direct edge-bracket matrices and independent polynomial transfer enumeration.
Run: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def matrix_rank_mod_p(rows, p, ncols):
    a = [list(map(lambda z: z % p, row)) for row in rows]
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv*z) % p for z in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                mul = a[i][col]
                a[i] = [(u-mul*v) % p for u,v in zip(a[i], a[rank])]
        rank += 1
    return rank


def adjoint_rank(x, edges, p):
    n = len(x)
    rows=[]
    for u,v in edges:
        row=[0]*n
        row[u] = (-x[v]) % p
        row[v] = x[u] % p
        rows.append(row)
    return matrix_rank_mod_p(rows,p,n)


def support_rank(x, edges):
    n=len(x)
    s={i for i,z in enumerate(x) if z}
    if not s:
        return 0
    closed=set(s)
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
        if u in s: closed.add(v)
        if v in s: closed.add(u)
    seen=set(); components=0
    for u in s:
        if u in seen: continue
        components+=1; stack=[u]; seen.add(u)
        while stack:
            for v in adj[stack.pop()] & s:
                if v not in seen:
                    seen.add(v); stack.append(v)
    return len(closed)-components


def poly_add(x,y):
    z=Counter(x)
    for deg,c in y.items(): z[deg]+=c
    return {deg:c for deg,c in z.items() if c}


def poly_mul(x,y):
    z=Counter()
    for i,a in x.items():
        for j,b in y.items(): z[i+j]+=a*b
    return {deg:c for deg,c in z.items() if c}


def transfer_hist(n,q):
    # States 00,01,10,11. A transition from ab to bc weighs
    # (q-1)^a t^(a + 1_{abc=100}).
    pairs=[(0,0),(0,1),(1,0),(1,1)]
    M=[[{} for j in range(4)] for i in range(4)]
    for i,(a,b) in enumerate(pairs):
        for c in (0,1):
            j=pairs.index((b,c))
            M[i][j]={a+int((a,b,c)==(1,0,0)):(q-1)**a}
    identity=[[({0:1} if i==j else {}) for j in range(4)] for i in range(4)]
    P=identity
    for _ in range(n):
        P=[[poly_add(*[poly_mul(P[i][k],M[k][j]) for k in range(4)]) if False else
            sum_polys(poly_mul(P[i][k],M[k][j]) for k in range(4))
            for j in range(4)] for i in range(4)]
    ans=sum_polys(P[i][i] for i in range(4))
    ans=poly_add(ans,{n-1:(q-1)**n,n:-(q-1)**n})
    return Counter({k:v for k,v in ans.items() if v})


def sum_polys(ps):
    a=Counter()
    for p in ps:
        for k,v in p.items():a[k]+=v
    return {k:v for k,v in a.items() if v}


def cycle_rank_by_patterns(binary):
    n=len(binary)
    return sum(binary)+sum(binary[i] and not binary[(i+1)%n] and
                         not binary[(i+2)%n] for i in range(n)) - int(all(binary))


def hist_exact(n,edges,q):
    ans=Counter()
    for x in product(range(q),repeat=n):
        r=adjoint_rank(x,edges,q)
        assert r==support_rank(x,edges),(x,r,support_rank(x,edges))
        ans[r]+=1
    return ans


def moments(n,q,h):
    num=q**n
    m1=Fraction(sum(k*v for k,v in h.items()),num)
    var=Fraction(sum((k*k)*v for k,v in h.items()),num)-m1*m1
    p=Fraction(q-1,q); r=1-p
    mu=p*(1+r*r)
    sig=p*r*(5*p**4-15*p**3+21*p*p-14*p+4)
    expected=n*mu-p**n
    expected_var=n*sig+p**n*(1-p**n)-2*n*(1-mu)*p**n
    assert m1==expected,(n,q,m1,expected)
    assert var==expected_var,(n,q,var,expected_var)
    return m1,var


def main():
    fixtures=[(4,[(0,1),(1,2),(2,3),(3,0)]),
              (5,[(i,(i+1)%5) for i in range(5)]),
              (6,[(i,(i+1)%6) for i in range(6)]),
              (5,[(i,i+1) for i in range(4)]),
              (5,[(0,i) for i in range(1,5)]),
              (5,[(0,1),(1,2),(3,4)]),
              (5,[(0,1),(1,2),(2,0),(3,4)])]
    ct=0
    for n,edges in fixtures:
        for q in (2,3):
            if q**n>8000: continue
            h=hist_exact(n,edges,q)
            if len(edges)==n and all(len([1 for e in edges if i in e])==2 for i in range(n)):
                th=transfer_hist(n,q)
                assert h==th,(n,q,h,th)
                if n>=5: moments(n,q,h)
            print('OK',n,q,'edges',len(edges),'hist',sorted(h.items()))
            ct+=1
    for n in range(4,11):
        for q in (2,3,4,5,9):
            pred=transfer_hist(n,q)
            count=Counter()
            for bits in product((0,1),repeat=n):
                k=cycle_rank_by_patterns(bits)
                count[k]+=(q-1)**sum(bits)
            assert pred==count,(n,q,pred,count)
            assert sum(pred.values())==q**n
    print('VERIFY_OK',ct,'direct matrix checks, 35 symbolic transfer checks')

if __name__=='__main__':main()
