"""Exact finite spot checks for the antipodal quartic-force classification.

The proof, not the finite checks, establishes the theorem for all dimensions.
"""
from sympy import Matrix, Rational, sqrt, simplify, beta, N
from itertools import product


def dot(x,y):
    return (x.T*y)[0]


def force_at(index, entries):
    x, _ = entries[index]
    out = Matrix.zeros(x.rows,1)
    for j,(y,m) in enumerate(entries):
        if j == index:
            continue
        z=y-x
        out += m*z*dot(z,z)
    return out.applyfunc(simplify)


def inspect(pairs):
    d=pairs[0][0].rows
    entries=[]
    for v,mu in pairs:
        entries += [(v,mu),(-v,mu)]
    total_mass=2*sum(mu for _,mu in pairs)
    S=Matrix.zeros(d,d)
    for v,mu in pairs:
        S+=2*mu*(v*v.T)
    S=S.applyfunc(simplify)
    I=simplify(S.trace())
    cs=[]
    for v,mu in pairs:
        F=force_at(2*len(cs),entries)
        assert (F+I*v+total_mass*dot(v,v)*v+2*S*v).applyfunc(simplify)==Matrix.zeros(d,1)
        cs.append((v,F))
    lam=simplify(-dot(cs[0][0],cs[0][1])/dot(cs[0][0],cs[0][0]))
    for v,F in cs:
        assert (F+lam*v).applyfunc(simplify)==Matrix.zeros(d,1), (v,F,lam)
    return lam,S


def crosspoly(masses):
    d=len(masses)
    M=2*sum(masses)
    C=Rational(3,2)
    pairs=[]
    for i,mu in enumerate(masses):
        v=Matrix.zeros(d,1)
        v[i]=sqrt(C/(M+4*mu))
        pairs.append((v,mu))
    lam,S=inspect(pairs)
    assert simplify(lam-(S.trace()+C))==0


cases=0
for d in range(2,6):
    for masses in product((1,2,4),repeat=d):
        if cases>200:break
        crosspoly(masses)
        cases+=1
print('Exact cross-polytope force cases:',cases)

# Two orthogonal weighted-frame blocks: a planar equilateral trine and a normal pair.
M=Rational(10); C=Rational(1)
R1=sqrt(C/(M+6)); R2=sqrt(C/(M+8))
pairs=[
    (Matrix([R1,0,0]),Rational(1)),
    (Matrix([-R1/2,sqrt(3)*R1/2,0]),Rational(1)),
    (Matrix([-R1/2,-sqrt(3)*R1/2,0]),Rational(1)),
    (Matrix([0,0,R2]),Rational(2)),
]
lam,S=inspect(pairs)
assert simplify(lam-S.trace()-C)==0
assert S[0,0]==S[1,1] and S[2,2]!=S[1,1]
print('Exact unequal-radius two-block tight-frame case: PASS',S.diagonal())

# The oscillator's time from a=1 to a=0 and back to 1 has full labeled period 4Q.
import mpmath as mp
mp.mp.dps=40
L=mp.mpf(52)/35
Q=mp.sqrt(2/L)*mp.beta(mp.mpf(1)/4,mp.mpf(1)/2)/4
# Independent numerical integration of the smooth oscillator to its first zero.
from scipy.integrate import solve_ivp
import numpy as np
def crossing(t,y): return y[0]
crossing.terminal=True;crossing.direction=-1
sol=solve_ivp(lambda t,y:(y[1],-float(L)*y[0]**3),(0,10),[1.0,0.0],events=crossing,rtol=1e-12,atol=1e-13,max_step=0.005)
assert len(sol.t_events[0])==1
assert abs(sol.t_events[0][0]-float(Q))<1e-9
print('Quartic oscillator beta-integral identity: PASS')
