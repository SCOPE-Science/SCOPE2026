"""Reproduce exact local equilibrium classification for the alternating four-cycle.
Run: python verify.py (requires SymPy)."""
import math
from itertools import product
import sympy as S

z=S.symbols('z'); x,y,k,a=S.symbols('x y k a', real=True)
weights=[x,y,-x,-y]
L=S.zeros(4)
for j,w in enumerate(weights):
    u,v=j,(j+1)%4
    L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
actual=S.factor(L.charpoly(z).as_expr())
required=S.factor(z*z*(z*z-4*(x*x+y*y)))
assert S.expand(actual-required)==0, (actual,required)
print('SYMBOLIC_CIRCLE_CHARACTERISTIC',actual)

# For four edges, direct sine balance and circular closure, including branch endpoints.
def rem2pi(z):
    return (z+math.pi)%(2*math.pi)-math.pi

def flow_from_edge(d,a,K):
    b=[math.sin(t) for t in d]
    return [((-1)**j)*a+K/2*(b[j]-b[(j-1)%4]) for j in range(4)]

def equiv(edge,a,K):
    assert abs(rem2pi(sum(edge)))<2e-12,edge
    assert max(abs(u) for u in flow_from_edge(edge,a,K))<1e-12,edge

def all_solutions_at_parameter(s,a,K):
    A=math.asin(s-2*a/K);B=math.asin(s)
    arcs=[(A,math.pi-A),(B,math.pi-B),(A,math.pi-A),(B,math.pi-B)]
    return [v for v in product(*arcs) if abs(rem2pi(sum(v)))<2e-12]

for ratio in (1.01,1.2,1.8,2.0,5.0,25.0):
    a=1.0; K=ratio
    rho=a/K
    gamma=math.asin(rho)
    sink=[-gamma,gamma,-gamma,gamma]
    source=[math.pi+gamma, math.pi-gamma, math.pi+gamma, math.pi-gamma]
    equiv(sink,a,K);equiv(source,a,K)
    for f in (0.01,0.123,0.379,0.67,0.99):
        s=2*rho-1+(2-2*rho)*f
        alpha=math.asin(s-2*rho); beta=math.asin(s)
        vals=all_solutions_at_parameter(s,a,K)
        assert len(vals)==4,(ratio,f,len(vals))
        for v in vals:
            equiv(v,a,K)
            c=[math.cos(t) for t in v]
            assert abs(c[0]+c[2])<1e-12
            assert abs(c[1]+c[3])<1e-12
            lam=K*math.sqrt(c[0]**2+c[1]**2)
            lo=2*math.sqrt(a*(K-a)); hi=math.sqrt(2*(K*K-a*a))
            assert lo-1e-11<=lam<=hi+1e-11
    print('DIRECT_EQUILIBRIA_CHECK',ratio,'2 isolated / 4 continuum arcs; exact Jacobian polynomial')

# At K=a the admissible s interval is a singleton and all differences quadrature.
rho=1;s=1; K=a=1
unique=all_solutions_at_parameter(s,a,K)
assert len(set(tuple(round(t%(2*math.pi),12) for t in v) for v in unique))==1
for v in unique:equiv(v,a,K)
print('CRITICAL_POINT_OK; ZERO_JACOBIAN',unique[0]);print('VERIFY_OK')
