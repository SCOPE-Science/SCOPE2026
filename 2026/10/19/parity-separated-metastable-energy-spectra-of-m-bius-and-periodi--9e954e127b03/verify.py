"""Independent finite-graph checks and exact symbolic transfer algebra.
Run with Python 3 and SymPy (tested with SymPy 1.13+).
"""
from itertools import product
from collections import Counter
from math import comb
import sympy as sp

z, t = sp.symbols('z t')
S=list(product((-1,1), repeat=2))
T=sp.zeros(16,16)
Q=sp.zeros(16,16)
for a,b in product(range(4), repeat=2):
    aa=S.index(S[a][::-1]);bb=S.index(S[b][::-1]); Q[4*a+b,4*aa+bb]=1
    for c in range(4):
        prev,middle,nxt=S[a],S[b],S[c]
        aligned0=sum(middle[0]==v for v in (prev[0],nxt[0],middle[1]))
        aligned1=sum(middle[1]==v for v in (prev[1],nxt[1],middle[0]))
        if aligned0<=1 and aligned1<=1:
            k=sum(middle[j]==nxt[j] for j in range(2))+int(middle[0]==middle[1])
            T[4*a+b,4*b+c]=z**k
assert T*Q==Q*T

# Exact characteristic polynomials of the invariant row-swap sectors.
for sign,expected in [(+1,t**6*(t*t-z*z)*(t*t-t-z*z)),
                      (-1,t**4*(t*t+t+z*z))]:
    visited=set(); base=[]
    for i in range(16):
        if i in visited:continue
        j=next(k for k in range(16) if Q[i,k])
        visited.update((i,j))
        if i==j and sign<0:continue
        v=sp.zeros(16,1);v[i]=1
        if i!=j:v[j]=sign
        base.append(v)
    B=sp.Matrix.hstack(*base)
    M=sp.Matrix.hstack(*(B.gauss_jordan_solve(T*v)[0] for v in base))
    assert sp.expand(M.charpoly(t).as_expr()-expected)==0
    print('sector',sign,'dimension',M.rows,'polynomial certified')

def poly(n,twisted):
    # R_n(+z^2) and (-1)^n R_n(-z^2).
    Lp=sum(sp.Rational(n,n-j)*comb(n-j,j)*z**(2*j)
           for j in range(n//2+1))
    Lm=sum(sp.Rational(n,n-j)*comb(n-j,j)*(-z*z)**j
           for j in range(n//2+1))*(-1)**n
    return sp.Poly(sp.expand(Lp+(-1 if twisted else +1)*Lm
                         +(1+(-1)**n)*z**n),z)

def brute(n,twisted):
    edges={(i,(i+1)%(2*n)) for i in range(2*n)}
    edges |= {(i,i+n) for i in range(n)}
    adj=[[] for _ in range(2*n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    assert all(len(x)==3 for x in adj)
    counts=Counter()
    for bits in range(1<<(2*n)):
        # spin equal iff bit equal
        if all(sum(bool((bits>>v)&1)==bool((bits>>w)&1) for w in adj[v])<=1
               for v in range(2*n)):
            defects=sum(((bits>>a)&1)==((bits>>b)&1) for a,b in edges)
            counts[defects]+=1
    return sp.Poly.from_dict({(k,):v for k,v in counts.items()},z)

for n in range(3,10):
    assert poly(n,True)==brute(n,True)
    trace=sp.Poly(sp.expand(sp.trace((T**n)*Q)),z)
    assert trace==poly(n,True)
    # Untwisted prism: graph edges of n-rungs periodic ladder.
    prism_edges=set()
    for i in range(n):
        for row in range(2):
            a=2*i+row; b=2*((i+1)%n)+row
            prism_edges.add(tuple(sorted((a,b))))
        prism_edges.add((2*i,2*i+1))
    p_adj=[[] for _ in range(2*n)]
    for a,b in prism_edges:p_adj[a].append(b);p_adj[b].append(a)
    vals=Counter()
    for bits in range(1<<(2*n)):
        if all(sum(bool((bits>>v)&1)==bool((bits>>w)&1) for w in p_adj[v])<=1
               for v in range(2*n)):
            vals[sum(((bits>>a)&1)==((bits>>b)&1) for a,b in prism_edges)]+=1
    assert sp.Poly.from_dict({(k,):v for k,v in vals.items()},z)==poly(n,False)
    assert sp.Poly(sp.expand(sp.trace(T**n)),z)==poly(n,False)
    print('n',n,'M',str(poly(n,True).as_expr()),'P',str(poly(n,False).as_expr()))
print('Exact symbolic sector determinants and exhaustive spin checks succeeded.')
