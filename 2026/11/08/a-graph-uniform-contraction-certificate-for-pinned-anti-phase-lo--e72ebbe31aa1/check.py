"""Reproduce exact algebra and finite-graph tests for a pinned logistic two-cycle.
Requires Python 3, sympy and numpy. The analytic all-graph proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
import sympy as s
import numpy as np

T = s.symbols('t', real=True)
mu = (4*T+2)/(4*T+1-4*T**2)
eps = (4*T**2-2*T-1)/(4*T**2-1)
f = lambda x: mu*x*(1-x)
v = s.factor(eps*mu*(2*T-1))
w = s.factor((1-eps)*mu*(2*T-1))
checks = [
    s.factor((1-eps)*f(T)+eps*f(s.Rational(1,2))-s.Rational(1,2)),
    s.factor(eps*f(T)+(1-eps)*f(s.Rational(1,2))-T),
    s.factor(w-v-2),
    s.factor(s.diff(v,T)-4*(4*T**2+1)/(4*T**2-4*T-1)**2),
    s.factor((eps*mu*(2*T-1))**2-v**2),
    s.factor(mu-(T+s.Rational(1,2))/(T*(1-T)+s.Rational(1,4))),
]
assert all(x==0 for x in checks), checks
left=(1+s.sqrt(5))/4
right=(3+s.sqrt(17))/8
vmax=s.simplify(v.subs(T,right))
assert s.simplify(vmax-(s.sqrt(17)-3)/2)==0
max4=s.simplify(vmax**3*(vmax+2))
assert s.simplify(max4-(71-17*s.sqrt(17))/2)==0
assert float(max4)<0.5
assert s.simplify(mu.subs(T,right))==4
assert s.simplify(eps.subs(T,left))==0
assert s.simplify(mu.subs(T,left))==1+s.sqrt(5)
assert s.simplify(eps.subs(T,right)-(7-s.sqrt(17))/16)==0

mu0=Q(88,23); e0=Q(5,33); t0=Q(7,8); half=Q(1,2)
assert f(T).subs(T,s.Rational(7,8))==s.Rational(77,184)
assert mu.subs(T,s.Rational(7,8))==s.Rational(88,23)
assert eps.subs(T,s.Rational(7,8))==s.Rational(5,33)
assert (v**2).subs(T,s.Rational(7,8))==s.Rational(100,529)

def cycle(n):
    assert n>=4 and n%2==0
    return [[(i-1)%n,(i+1)%n] for i in range(n)], [i%2 for i in range(n)]

def complete(k):
    return [[k+j for j in range(k)] for _ in range(k)] + [[j for j in range(k)] for _ in range(k)], [0]*k+[1]*k

def cube(k):
    return [[i^(1<<j) for j in range(k)] for i in range(2**k)], [i.bit_count()%2 for i in range(2**k)]

def torus(L):
    assert L>=4 and L%2==0
    return [[((i-1)%L)*L+j,((i+1)%L)*L+j,i*L+(j-1)%L,i*L+(j+1)%L]
            for i in range(L) for j in range(L)], [(i+j)%2 for i in range(L) for j in range(L)]

def next_state(a, nb, mu0=mu0, eps=e0):
    d=len(nb[0]); ff=[mu0*x*(1-x) for x in a]
    return [(1-eps)*ff[i]+eps*sum(ff[j] for j in nb[i])/d for i in range(len(a))]

families = [cycle(4),cycle(6),cycle(12),complete(2),complete(3),complete(4),cube(3),cube(4),torus(4),torus(6)]
mode_checks=0
for nb,parts in families:
    n=len(nb); d=len(nb[0]); assert len(parts)==n
    assert all(len(adj)==d and all(parts[v]!=parts[j] for j in adj) for v,adj in enumerate(nb))
    a=[t0 if parts[i]==0 else half for i in range(n)]
    b=[half if parts[i]==0 else t0 for i in range(n)]
    assert next_state(a,nb)==b and next_state(b,nb)==a
    C=np.zeros((n,n),float)
    for i,adj in enumerate(nb):
        C[i,i]=float(1-e0)
        for j in adj:C[i,j]+=float(e0)/d
    Ja=C @ np.diag([float(mu0*(1-2*x)) for x in a])
    Jb=C @ np.diag([float(mu0*(1-2*x)) for x in b])
    B=Jb@Ja
    eigen=np.linalg.eigvals(B)
    assert abs(max(abs(eigen))-100/529)<1e-10,(n,eigen)
    B4=B@B
    infnorm=max(np.sum(abs(B4),axis=1))
    expected=Q(10,23)**3*Q(56,23)
    assert abs(infnorm-float(expected))<1e-10,(n,infnorm)
    mode_checks+=n
print(f'VERIFY_OK symbolic_identities={len(checks)} endpoint_checks=5 graph_families={len(families)} vertices={mode_checks} rational_orbits={len(families)} full_Floquet_matrices={len(families)} uniform_four_step_bound={max4} explicit_rational_multiplier=100/529')
