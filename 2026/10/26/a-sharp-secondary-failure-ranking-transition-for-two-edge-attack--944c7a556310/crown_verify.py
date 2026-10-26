"""Exact, self-contained checks for two-edge Kirchhoff sensitivity of crown graphs.
Run: python crown_verify.py (requires sympy)."""
from itertools import combinations
from sympy import Matrix, Rational, symbols, factor, simplify, expand

z=symbols('z', integer=True, positive=True)
TYPES={'incident': ((0,1),(0,2)), 'reciprocal':((0,1),(1,0)),
       'linked':((0,1),(1,2)), 'independent':((0,1),(2,3))}

def kernel(a,b,k,n):
    i,j=a; p,q=b
    delta=lambda x,y: int(x==y)
    s=delta(i,p)-delta(i,q)-delta(j,p)+delta(j,q)
    h=delta(i,p)+delta(i,q)+delta(j,p)+delta(j,q)
    return Rational(s,2)/n**k+(Rational(h,2)-(Rational(2,1)/n))/(n-2)**k+(Rational(2,1)/n)/(2*(n-1))**k

def damage(n,pair):
    a,b=pair
    R=kernel(a,a,1,n); Q=kernel(a,a,2,n)
    r=kernel(a,b,1,n); q=kernel(a,b,2,n)
    return factor(4*n*((1-R)*Q+r*q)/((1-R)**2-r**2))

EXPECTED={
'incident':2*(4*z**4-21*z**3+38*z**2-32*z+12)/((z-3)*(z-2)*(z-1)*(z**2-3*z+1)),
'reciprocal':2*(4*z-3)/((z-3)*(z-1)),
'linked':2*(4*z**5-31*z**4+89*z**3-116*z**2+68*z-12)/((z-3)*(z-2)*(z-1)*(z**3-5*z**2+7*z-1)),
'independent':2*(4*z**6-35*z**5+120*z**4-202*z**3+184*z**2-88*z+16)/((z-2)*(z-1)*(z**2-4*z+2)*(z**3-5*z**2+8*z-2))}
for k,v in TYPES.items():
    assert simplify(damage(z,v)-EXPECTED[k])==0,k

# An exhaustive (not randomized) check of all deletion pairs at representative sizes.
# The theorem for all orders follows from the symbolic differences + positivity proof.
for n in range(4,8):
    N=2*n
    lap=Matrix.zeros(N)
    edges=[]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            u,v=i,n+j;edges.append((i,j))
            lap[u,u]+=1;lap[v,v]+=1;lap[u,v]-=1;lap[v,u]-=1
    original=N*sum(Rational(1,t) for t in [2*(n-1)]+[n]*(n-1)+[n-2]*(n-1))
    vals={k:damage(n,v) for k,v in TYPES.items()}
    for a,b in combinations(edges,2):
        if a[0]==b[0] or a[1]==b[1]: typ='incident'
        elif a[0]==b[1] and a[1]==b[0]: typ='reciprocal'
        elif a[0]==b[1] or a[1]==b[0]: typ='linked'
        else: typ='independent'
        L=lap.copy()
        for i,j in [a,b]:
            u,v=i,n+j;L[u,u]-=1;L[v,v]-=1;L[u,v]+=1;L[v,u]+=1
        # Ground last vertex, Kirchoff index equals N*trace(green)-sum(green)
        # where green is inverse of a reduced Laplacian; this identity is exact.
        G=L[:-1,:-1].inv()
        Kf=N*sum(G[i,i] for i in range(N-1))-sum(G)
        assert simplify(Kf-original-vals[typ])==0,(n,a,b,typ)
    print('EXHAUSTIVE_OK',n,len(edges)*(len(edges)-1)//2)

# Independent exact polynomial positivity certificates: coefficients of shifts z=t+4.
positive_polys=[2*z**5-17*z**4+49*z**3-60*z**2+34*z-4,
                2*z**4-11*z**3+19*z**2-8*z-6,
                2*z**2-3*z-6,
                5*z**2-15*z+6,
                3*z**4-8*z**3-13*z**2+40*z-14]
t=symbols('t', nonnegative=True)
for f in positive_polys:
    assert all(c>0 for c in __import__('sympy').Poly(expand(f.subs(z,t+4)),t).all_coeffs())
# The only change of order among the four cases occurs between n=11 and n=12.
p=z**3-14*z**2+34*z-12
assert all(p.subs(z,n)<0 for n in range(4,12))
assert all(c>0 for c in __import__('sympy').Poly(expand(p.subs(z,t+12)),t).all_coeffs())
print('VERIFY_OK: symbolic formulas, positivity certificates, exact all-pair inversions for n=4..7, threshold n=12')
