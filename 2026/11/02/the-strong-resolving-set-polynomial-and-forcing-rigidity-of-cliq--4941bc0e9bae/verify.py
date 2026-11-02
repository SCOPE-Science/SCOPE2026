#!/usr/bin/env python3
"""Independent finite checks of strong-resolving-set enumeration for K_q square C_n."""
import itertools, math
from collections import Counter

def graph(q,n):
    N=q*n
    adj=[set() for _ in range(N)]
    def idx(a,j):return a*n+j
    for a in range(q):
        for j in range(n):
            u=idx(a,j)
            for b in range(q):
                if b!=a: adj[u].add(idx(b,j))
            adj[u].add(idx(a,(j+1)%n));adj[u].add(idx(a,(j-1)%n))
    return adj

def original_distance(q,n,u,v):
    a,j=divmod(u,n); b,k=divmod(v,n)
    d=abs(j-k)
    return (a!=b)+min(d,n-d)

def mmd_adj(q,n):
    adj=graph(q,n); N=q*n
    bits=[0]*N
    for u in range(N):
        for v in range(u+1,N):
            d=original_distance(q,n,u,v)
            if all(original_distance(q,n,w,v)<=d for w in adj[u]) and all(original_distance(q,n,w,u)<=d for w in adj[v]):
                bits[u]|=1<<v;bits[v]|=1<<u
    return bits

def poly_mul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans

def poly_add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def poly_odd(q,n):
    # Cyclic trace of transfer matrix with E, singleton-color, and heavy states.
    heavy=[0,0]+[math.comb(q,r) for r in range(2,q+1)]
    # Decompose q+2 state matrix into a 3x3 symmetric block and q-1 eigenvalues t.
    B=[[ [1],[0,q],heavy],[[1],[0,1],[0]],[[1],[0],[0]]]
    one=[[[1] if i==j else [0] for j in range(3)] for i in range(3)]
    def mm(A,C):
        return [[sum_poly([poly_mul(A[i][k],C[k][j]) for k in range(3)]) for j in range(3)] for i in range(3)]
    def sum_poly(xs):
        o=[0]
        for v in xs:o=poly_add(o,v)
        return o
    T=one
    for z in range(n):T=mm(T,B)
    p=sum_poly([T[i][i] for i in range(3)])
    return poly_add(p,[0]*n+[q-1])

def poly_even(q,n):
    # Independence polynomial of crown K_{q,q}-M_q
    one=[2*math.comb(q,r) for r in range(q+1)]
    one[0]-=1
    one[2]+=q
    v=[1]
    for _ in range(n//2): v=poly_mul(v,one)
    return v

def brute(q,n):
    adj=mmd_adj(q,n);N=q*n
    counts=[0]*(N+1)
    maxima=[];best=0
    # each independent bitset enumerated explicitly; forbid adjacent chosen vertices
    for mask in range(1<<N):
        t=mask;okay=True
        while t:
            one=t&-t;v=one.bit_length()-1;t^=one
            if adj[v]&t: okay=False;break
        if okay:
            size=mask.bit_count();counts[size]+=1
            if size>best:best=size;maxima=[mask]
            elif size==best:maxima.append(mask)
    return counts,best,maxima,adj

def strong(q,n,S):
    N=q*n
    for u in range(N):
        for v in range(u+1,N):
            d=original_distance(q,n,u,v)
            if not any(original_distance(q,n,s,u)==original_distance(q,n,s,v)+d or original_distance(q,n,s,v)==original_distance(q,n,s,u)+d for s in S):
                return False
    return True

def predicted(q,n):
    if n%2==0: return q*n//2, 2**(n//2), n//2
    if n>=5:return q*(n+1)//2,n,2
    if q==3:return 6,6,3
    return 2*q,3,2

def forcing_of_basis(maxima,N):
    # A basis is complement of a maximum independent set.
    B=(1<<N)-1-maxima[0]
    others=[(1<<N)-1-x for x in maxima[1:]]
    for r in range(N+1):
        for sub in itertools.combinations([i for i in range(N) if B&(1<<i)],r):
            selected=sum(1<<i for i in sub)
            if all((selected&~O)!=0 for O in others):return r
    raise AssertionError

for q,n in [(3,3),(4,3),(5,3),(3,4),(4,4),(3,5),(4,5),(3,6),(3,7)]:
    counts,best,maxima,adj=brute(q,n)
    formula=poly_even(q,n) if n%2==0 else poly_odd(q,n)
    assert counts[:len(formula)]==formula and not any(counts[len(formula):]), (q,n,counts,formula)
    B,Nbases,F=predicted(q,n)
    assert q*n-best==B and len(maxima)==Nbases,(q,n,best,len(maxima),B,Nbases)
    if q*n<=15:
        # Original all-pairs metric definition, not merely the SR graph lemma.
        for mask in range(1<<(q*n)):
            chosen=[v for v in range(q*n) if mask&(1<<v)]
            covers=all(mask&(1<<u) or mask&(1<<v) for u in range(q*n) for v in range(u+1,q*n) if adj[u]&(1<<v))
            assert covers==strong(q,n,chosen),(q,n,mask)
    if q*n<=16:
        assert all(forcing_of_basis([x]+[y for y in maxima if y!=x],q*n)==F for x in maxima),(q,n)
    print('PASS',q,n,'vertices',q*n,'max_independent',best,'bases',len(maxima),'coeffs',len(formula))
print('VERIFY_OK')
