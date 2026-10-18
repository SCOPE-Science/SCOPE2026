"""Reproduce exact curvature identities for finite undirected independent cascades.
Run: python verify_influence_risk.py (requires sympy)."""
from itertools import combinations
from fractions import Fraction
import sympy as sp

p,t=sp.symbols('p t',positive=True)

def moments(n,edges):
    out={S:[sp.S.Zero,sp.S.Zero] for S in range(1<<n)}
    for pattern in range(1<<len(edges)):
        adj=[set() for _ in range(n)]
        for i,(a,b) in enumerate(edges):
            if pattern>>i&1:adj[a].add(b);adj[b].add(a)
        weight=p**pattern.bit_count()*(1-p)**(len(edges)-pattern.bit_count())
        for S in out:
            reached={v for v in range(n) if S>>v&1}
            queue=list(reached)
            for v in queue:
                for u in adj[v]:
                    if u not in reached:reached.add(u);queue.append(u)
            z=len(reached)
            out[S][0]+=weight*z
            out[S][1]+=weight*z*z
    return {S:sp.factor(b-a*a) for S,(a,b) in out.items()}

def gap(V,S,a,b):
    return sp.factor(V[S|(1<<a)]+V[S|(1<<b)]-V[S]-V[S|(1<<a)|(1<<b)])

# Complete small-network curvature classification.
V2=moments(2,[(0,1)])
assert sp.expand(gap(V2,0,0,1)-2*p*(1-p))==0
Vp=moments(3,[(0,1),(1,2)])
assert sp.expand(gap(Vp,0,0,1)-p*(1-p)*(p+1)*(p+2))==0
assert sp.expand(gap(Vp,0,0,2)-p*p*(1-p)*(p+9))==0
assert gap(Vp,1<<1,0,2)==0
assert sp.expand(gap(Vp,1<<2,0,1)-2*p*(1-p)*(1-3*p))==0
Vt=moments(3,[(0,1),(1,2),(0,2)])
assert sp.expand(gap(Vt,0,0,1)-p*(1-p)**2*(2+17*p-8*p**3))==0
assert sp.expand(gap(Vt,1<<2,0,1)-2*p*(1-p)**2*(1-5*p+2*p**3))==0
assert all(sp.simplify(gap(Vt,0,i,j)-gap(Vt,0,0,1))==0 for i,j in combinations(range(3),2))
assert all(sp.simplify(gap(Vt,1<<(3-i-j),i,j)-gap(Vt,1<<2,0,1))==0 for i,j in combinations(range(3),2))
crit=sp.nroots(2*p**3-5*p+1,maxsteps=100)
assert len([z for z in crit if abs(sp.im(z))<1e-10 and 0<float(sp.re(z))<1])==1

# Independent directed-arc enumeration, rather than bond percolation.
def directed_moments(n,edges,prob):
    arcs=[(a,b) for a,b in edges]+[(b,a) for a,b in edges]
    out={S:[Fraction(0),Fraction(0)] for S in range(1<<n)}
    for pat in range(1<<len(arcs)):
        w=prob**pat.bit_count()*(1-prob)**(len(arcs)-pat.bit_count())
        adj=[set() for _ in range(n)]
        for i,(a,b) in enumerate(arcs):
            if pat>>i&1:adj[a].add(b)
        for S in out:
            seen={i for i in range(n) if S>>i&1};queue=list(seen)
            for a in queue:
                for b in adj[a]:
                    if b not in seen:seen.add(b);queue.append(b)
            z=len(seen)
            out[S][0]+=w*z;out[S][1]+=w*z*z
    return {S:v[1]-v[0]*v[0] for S,v in out.items()}

for n,edges in [(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(0,2)]),(5,[(0,1),(0,2),(0,3),(0,4)])]:
    u=moments(n,edges)
    for rational in [Fraction(1,5),Fraction(1,2)]:
        v=directed_moments(n,edges,rational)
        assert all(sp.Rational(v[S].numerator,v[S].denominator)==u[S].subs(p,sp.Rational(rational.numerator,rational.denominator)) for S in v)

# Star moments: m leaves; k of the leaves seeded, center not seeded.
def star(k,m):
    q=1-(1-p)**k
    return sp.expand(q*(1-q)*(1+(m-k)*p)**2+q*(m-k)*p*(1-p))
for m in range(2,7):
    ed=[(0,i) for i in range(1,m+1)]
    v=moments(m+1,ed)
    for k in range(m+1):
        S=sum(1<<i for i in range(1,k+1))
        assert sp.factor(v[S]-star(k,m))==0

# Exact obstruction from the final pair of unseeded leaves.
D=sp.factor(star(2,2)-2*star(1,2)+star(0,2)) # Not the general m formula; check by substitution below.
for m in range(2,8):
    tt=(1-p)**(m-2)
    formula=p**2*tt*((5+4*p)-(14-4*p-p**2)*tt)
    assert sp.factor(star(m,m)-2*star(m-1,m)+star(m-2,m)-formula)==0
for num,den,m in [(1,10,11),(1,5,6),(1,2,3),(4,5,3)]:
    z=sp.Rational(num,den)
    delta=sp.factor(star(m,m)-2*star(m-1,m)+star(m-2,m)).subs(p,z)
    assert delta>0
print('PASS: 3 connected small-network topologies, symbolic curvature, 3 directed-live-edge cross-checks at 2 p values, star identity m=2..6, global star obstruction and rational witnesses')
print('critical probability:',[str(sp.N(z,16)) for z in crit if abs(sp.im(z))<1e-10 and 0<float(sp.re(z))<1])
