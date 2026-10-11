from itertools import combinations
from mpmath import mp
import sympy as sp

mp.dps = 80
N=7
zeta=mp.e**(2j*mp.pi/N)

def samples(H):
    return [abs(sum(zeta**(h*k) for h in H)) for k in range(N)]

def ratio(H):
    v=samples(H)
    return 2*v[1]/sum(v)

# Complete nonzero subset census.
rows=[]
for m in range(1,N+1):
    for H in combinations(range(N),m):
        rows.append((ratio(H),H))
rows.sort(reverse=True, key=lambda x:x[0])
best=rows[0][0]
maximizers=[H for r,H in rows if abs(r-best)<mp.mpf('1e-60')]
expected=[tuple(sorted(((b+i)%N for i in range(3)))) for b in range(N)]
expected=sorted(set(expected))
assert sorted(maximizers)==expected
assert len(rows)==127 and len(maximizers)==7

# Exact affine orbit census for three-subsets.
def aff(H,a,b):
    return tuple(sorted(((a*x+b)%7 for x in H)))
def orb(H):
    return {aff(H,a,b) for a in range(1,7) for b in range(7)}
Oap=orb((0,1,2)); Ods=orb((0,1,3))
assert len(Oap)==21 and len(Ods)==14 and len(Oap|Ods)==35 and not (Oap&Ods)

x=sp.symbols('x')
c1=sp.cos(2*sp.pi/7); c2=sp.cos(4*sp.pi/7); c3=sp.cos(6*sp.pi/7)
g=sp.simplify(2*(1+2*c1)/(5+4*(c1+c2-c3)))
pg=97*x**3+44*x**2-20*x-8
assert sp.Poly(sp.minpoly(g,x),x).monic()==sp.Poly(pg,x).monic()
assert sp.signsimp(pg.subs(x,sp.Rational(11,25)))<0
assert sp.signsimp(pg.subs(x,sp.Rational(441,1000)))>0
assert sp.Poly(pg,x).count_roots(0,sp.oo)==1

# Exact two-frequency comparison and difference-set comparison.
r2=sp.simplify(2*sp.sin(sp.pi/14)*sp.cos(sp.pi/7))
p2=8*x**3+8*x**2-2*x-1
assert sp.Poly(sp.minpoly(r2,x),x).monic()==sp.Poly(p2,x).monic()
assert sp.Poly(p2,x).count_roots(0,sp.oo)==1
assert sp.signsimp(p2.subs(x,sp.Rational(41,100)))>0
rd=sp.simplify(2*sp.sqrt(2)/(3+6*sp.sqrt(2)))
assert sp.simplify(rd-(8-2*sp.sqrt(2))/21)==0
assert sp.N(rd,50) < sp.Rational(1,4)

# Difference-set Fourier magnitude identity.
D=(0,1,3)
diffs=[(a-b)%7 for a in D for b in D if a!=b]
assert sorted(diffs)==list(range(1,7))
for k in range(1,7):
    v=sum(zeta**(h*k) for h in D)
    assert abs(abs(v)**2-2) < mp.mpf('1e-65')

# Formula agrees with exhaustive maximum.
gnum=mp.mpf(str(sp.N(g,70)))
assert abs(gnum-best)<mp.mpf('1e-60')
print('VERIFY_OK subsets=127 maximizers=7 three_orbits=21+14')
print('gamma=', mp.nstr(best,50))
print('minpoly=97*x^3+44*x^2-20*x-8')
