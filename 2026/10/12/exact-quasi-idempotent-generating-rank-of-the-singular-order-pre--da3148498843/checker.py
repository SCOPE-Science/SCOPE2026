#!/usr/bin/env python3
"""Exact finite verification for the quasi-idempotent rank theorem.

Only the finite max-plus identity is used as an infinite-case proof certificate.
Finite transformation tests are independent small-case cross-checks.
"""
from itertools import combinations

INF = None
STATES = [(a,b) for a in range(4) for b in range(4)]
INDEX = {s:i for i,s in enumerate(STATES)}

def compatible(a,b,c):
    return not ((c&1 and b&1) or (c&2 and b&2) or
                (c&2 and b&1) or (c&1 and a&2))

def tropical_product(A,B):
    size=len(A)
    C=[[None]*size for _ in range(size)]
    for i in range(size):
        for k,v in enumerate(A[i]):
            if v is None:continue
            for j,w in enumerate(B[k]):
                if w is None:continue
                candidate=v+w
                if C[i][j] is None or candidate>C[i][j]:C[i][j]=candidate
    return C

def tropical_power(T,e):
    n=len(T)
    A=[[0 if i==j else None for j in range(n)] for i in range(n)]
    while e:
        if e&1:A=tropical_product(A,T)
        T=tropical_product(T,T)
        e//=2
    return A

def transition_matrix():
    T=[[None]*16 for _ in range(16)]
    for i,(a,b) in enumerate(STATES):
        for c in range(4):
            if compatible(a,b,c):T[i][INDEX[(b,c)]]=(c&1 != 0)+(c&2 != 0)
    return T

def exact_rank(n):
    if n==4:return 4
    if n==5:return 6
    T=transition_matrix()
    P=tropical_power(T,n-4)
    omitted=max((b&1!=0)+(b&2!=0)+P[INDEX[(0,b)]][INDEX[(a,0)]]
                for b in [0,2] for a in [0,1] if P[INDEX[(0,b)]][INDEX[(a,0)]] is not None)
    return 2*(n-2)-omitted

def formula(n):
    return 6*n//5-(n%5==1)

def quasi_edges(n):
    return [('d',i,i,i-1) for i in range(2,n)] + [('m',i,i-1,i+1) for i in range(2,n)]

def conditions(n,choose):
    D={i for t,i,j,k in choose if t=='d'}
    U={i for t,i,j,k in choose if t=='m'}
    N=n-1
    if any((j not in D and j+1 not in U) for j in range(1,n)):return False
    if any((k+1 not in D and k-1 not in U) for k in range(1,n+1)):return False
    if any((t not in U and t+1 not in U) for t in range(1,N)):return False
    if any((t+1 not in D and t+2 not in D) for t in range(1,N)):return False
    return True

def reaches_all_top_pairs(n,choose):
    # Explicitly enumerate all nonzero products in the rank-(n-1) principal factor.
    # Ordered pair (kernel index, omitted-image index).
    elems={(j,k) for _,_,j,k in choose}
    changed=True
    while changed:
        changed=False
        new=set()
        for j,k in elems:
            for t,l in elems:
                if k==t or k==t+1:new.add((j,l))
        if not new<=elems:elems.update(new);changed=True
    return len(elems)==n*(n-1)

def actual_maps(n):
    out=[]
    for _,i,j,k in quasi_edges(n):
        # unique monotone surjection with kernel block j,j+1 and missing image k
        vals=[v for v in range(1,n+1) if v!=k]
        f=tuple(vals[t if t<j else t-1] for t in range(n))
        out.append(f)
        assert len(set(f))==n-1
        assert f[j-1]==f[j]
        assert all(f[t]<f[t+1] for t in range(n-1) if t!=j-1)
        f2=tuple(f[v-1] for v in f)
        f4=tuple(f2[v-1] for v in f2)
        assert f!=f2 and f2==f4
    return out

def main():
    T=transition_matrix()
    P4=tropical_power(T,4);P9=tropical_power(T,9)
    assert all((a is None and b is None) or (a is not None and b==a+4)
               for row4,row9 in zip(P4,P9) for a,b in zip(row4,row9))
    for n in range(4,101):assert exact_rank(n)==formula(n),(n,exact_rank(n),formula(n))
    for n in range(4,10):
        actual_maps(n)
        edges=quasi_edges(n)
        qrank=100
        for mask in range(1<<len(edges)):
            choose=[v for i,v in enumerate(edges) if mask>>i&1]
            cond=conditions(n,choose)
            if n<=8:
                top=reaches_all_top_pairs(n,choose)
                assert cond==top,(n,choose,cond,top)
            if cond:qrank=min(qrank,len(choose))
        assert qrank==formula(n),(n,qrank,formula(n))
    n=9
    example=[('d',2),('d',3),('d',5),('d',6),('d',8),('m',2),('m',3),('m',5),('m',7),('m',8)]
    chosen=[v for v in quasi_edges(n) if v[:2] in example]
    assert len(chosen)==10 and conditions(n,chosen) and reaches_all_top_pairs(n,chosen)
    print('VERIFY_OK; max-plus T^9=T^4+4; exact rank n=4..100; exhaustive generating-subset comparisons n=4..8; explicit n=9 counterexample')

if __name__=='__main__':main()
