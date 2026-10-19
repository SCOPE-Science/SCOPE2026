#!/usr/bin/env python3
"""Independent exact-rational diagnostic for the conductance-capped theta theorem."""
import itertools
import sympy as S

def connected(n,edges):
    seen={0}
    while True:
        add={v for u,v in edges if u in seen}|{u for u,v in edges if v in seen}
        if add<=seen: return len(seen)==n
        seen|=add

def laplacian(n,weighted_edges):
    L=S.zeros(n)
    for i,j,w in weighted_edges:
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    return L

def positive(M):
    return all(x>=0 for x in M)

def update(L,theta,h):
    I=S.eye(L.rows)
    return (I+theta*h*L).inv()*(I-(1-theta)*h*L)

def saturated(n,edges,w):
    d={(min(i,j),max(i,j)):v for i,j,v in edges}
    return any(all(d.get((min(i,j),max(i,j)),0)==w for j in range(n) if j!=i) for i in range(n))

checks=0
for n in [3,4]:
    possible=list(itertools.combinations(range(n),2))
    for mask in range(1,1<<len(possible)):
        es=[e for k,e in enumerate(possible) if (mask>>k)&1]
        if not connected(n,es): continue
        E=[(a,b,S.Integer(1)) for a,b in es]
        L=laplacian(n,E)
        for theta in [S.Rational(0),S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Rational(1)]:
            if theta<S.Rational(n-1,n):
                H=1/(n-1-n*theta)
                assert positive(update(L,theta,H))
                if saturated(n,E,S.Integer(1)):
                    assert not positive(update(L,theta,H+S.Rational(1,20)))
                else:
                    assert positive(update(L,theta,H+S.Rational(1,100000)))
            else:
                for h in [S.Rational(1,3),S.Integer(3),S.Integer(200)]:
                    assert positive(update(L,theta,h))
            checks+=1
for n in [3,4,5]:
    E=[(0,j,S.Integer(1)) for j in range(1,n)]
    for i in range(1,n):
        for j in range(i+1,n):
            if (i+j)%2==0: E.append((i,j,S.Rational(1,2)))
    L=laplacian(n,E)
    for theta in [S.Rational(1,5),S.Rational(1,2)]:
        if theta>=S.Rational(n-1,n): continue
        H=1/(n-1-n*theta)
        assert positive(update(L,theta,H))
        assert not positive(update(L,theta,H+S.Rational(1,20)))
        checks+=1
print('PASS exact-rational configurations:',checks)
