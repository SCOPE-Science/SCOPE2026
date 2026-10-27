#!/usr/bin/env python3
"""Independent finite-field checks of prescribed additive commutators in radical-square-zero quiver algebras."""
from itertools import product
from collections import Counter

def product_in_algebra(x,y,n,edges,q):
    diag=tuple(x[v]*y[v]%q for v in range(n))
    arr=tuple((x[u]*y[n+j]+x[n+j]*y[v])%q for j,(u,v) in enumerate(edges))
    return diag+arr

def brute(n,edges,q):
    D=n+len(edges)
    A=list(product(range(q),repeat=D))
    count=Counter()
    for a in A:
        for b in A:
            ab=product_in_algebra(a,b,n,edges,q)
            ba=product_in_algebra(b,a,n,edges,q)
            c=tuple((ab[n+j]-ba[n+j])%q for j in range(len(edges)))
            assert all(ab[v]==ba[v] for v in range(n))
            count[c]+=1
    return count

def predicted(n,edges,q,c,t=1):
    if any(u==v and c[j] for j,(u,v) in enumerate(edges)):
        return 0
    total=0
    # Color labels in (F_q)^(2t); number of colorings q^(2tn).
    for colors in product(range(q**(2*t)),repeat=n):
        same=sum(colors[u]==colors[v] for u,v in edges)
        if any(c[j] and colors[u]==colors[v] for j,(u,v) in enumerate(edges)):
            continue
        total+=q**((2*t-1)*len(edges)+same)
    return total

def validate(n,edges,q):
    got=brute(n,edges,q)
    for c in product(range(q),repeat=len(edges)):
        expected=predicted(n,edges,q,c)
        assert got[c]==expected,(n,edges,q,c,got[c],expected)
    assert sum(got.values())==q**(2*(n+len(edges)))
    print('PASS',n,edges,q,'targets',q**len(edges),'pairs',q**(2*(n+len(edges))))

def chromatic_bruteforce(n,edges,K):
    # Edges support only, no loops.
    return any(all(cols[u]!=cols[v] for u,v in edges)
               for cols in product(range(K),repeat=n))

if __name__=='__main__':
    validate(2,[(0,1)],2)
    validate(2,[(0,1),(0,1)],2)
    validate(2,[(0,0),(0,1)],2)
    validate(3,[(0,1),(1,2),(0,2)],2)
    validate(3,[(0,1),(1,2),(0,2)],3)
    K4=[(i,j) for i in range(4) for j in range(i+1,4)]
    K5=[(i,j) for i in range(5) for j in range(i+1,5)]
    assert chromatic_bruteforce(4,K4,4)
    assert not chromatic_bruteforce(5,K5,4)
    assert chromatic_bruteforce(5,K5,16)
    print('PASS K4 one-commutator and K5 two-commutator threshold over F2')
    print('VERIFY_OK_QUIVER_CHROMATIC_COMMUTATOR_WIDTH')
