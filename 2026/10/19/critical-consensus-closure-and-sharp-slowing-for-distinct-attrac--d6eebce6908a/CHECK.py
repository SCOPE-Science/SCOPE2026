#!/usr/bin/env python3
"""Exact three-agent calculations and numerical corroboration for the critical tanh network.

Requires Python 3, SymPy, SciPy. Run as: python CHECK.py
"""
from fractions import Fraction
from math import sqrt, log, tanh
import sympy as sp
from scipy.integrate import solve_ivp

A = sp.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
R = sp.Matrix([[1,0,-1],[0,0,0],[-1,0,1]])
H = A - sp.Rational(1,2)*R
WA = sp.Matrix([[0,1,0],[1,0,1],[0,1,0]])
WR = sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])
assert H == sp.Matrix([[sp.Rational(1,2),-1,sp.Rational(1,2)],
                       [-1,2,-1],[sp.Rational(1,2),-1,sp.Rational(1,2)]])
assert H.eigenvals() == {sp.Integer(0):2,sp.Integer(3):1}
assert H*sp.Matrix([1,0,-1]) == sp.zeros(3,1)
assert H*sp.Matrix([1,-2,1]) == 3*sp.Matrix([1,-2,1])
assert (A-sp.Rational(1,2)*R)*sp.Matrix([1,0,-1]) == sp.zeros(3,1)

# Independent four-agent attractive path, repulsive endpoint edge.
L4 = sp.zeros(4)
for edge in range(3):
    L4[edge,edge] += 1
    L4[edge+1,edge+1] += 1
    L4[edge,edge+1] -= 1
    L4[edge+1,edge] -= 1
R4 = sp.zeros(4)
R4[0,0] = R4[3,3] = 1
R4[0,3] = R4[3,0] = -1
v4 = sp.Matrix([3,1,-1,-3])/sp.sqrt(20)
assert (L4-sp.Rational(1,3)*R4)*v4 == sp.zeros(4,1)
assert (L4-sp.Rational(1,3)*R4).eigenvals() == {
    sp.Integer(0):2,sp.Integer(2):1,sp.Rational(10,3):1}
assert sp.simplify(sp.Rational(1,3)**3/(3*4)*(v4[0]-v4[3])**4) == sp.Rational(1,100)

q,p,mu = sp.symbols('q p mu', real=True)
x = sp.Matrix([mu+q+p, mu-2*p, mu-q+p])

def rhs(xv):
    out=[]
    for i in range(3):
        out.append(-sum((WA[i,j]*(xv[i]-xv[j])
              -WR[i,j]*sp.tanh((xv[i]-xv[j])/2)) for j in range(3))/3)
    return sp.Matrix(out)

dx=rhs(x)
qdot=sp.simplify((dx[0]-dx[2])/2)
pdot=sp.simplify((dx[0]+dx[2]-2*dx[1])/6)
assert sp.simplify(qdot+(q-sp.tanh(q))/3)==0
assert sp.simplify(pdot+p)==0

v=sp.Matrix([1,0,-1])/sp.sqrt(2)
alpha=sp.Rational(1,2)
kappa=sp.simplify(alpha**3/(3*3)*((v[0]-v[2])**4))
assert kappa==sp.Rational(1,18)
assert sp.simplify(sp.Rational(1,1)/sp.sqrt(2*kappa)-3)==0

z=sp.symbols('z')
assert sp.series(-(z-sp.tanh(z))/3,z,0,9).removeO()==(
     -z**3/sp.Integer(9)+2*z**5/sp.Integer(45)-17*z**7/sp.Integer(945))
assert sp.series(sp.Rational(2,3)*(z-sp.tanh(z))/z**3,z,0,6).removeO()==(
     sp.Rational(2,9)-sp.Rational(4,45)*z**2+sp.Rational(34,945)*z**4)
# With U = q^(-2), U'=2/9-4/(45U)+O(U^(-2));
# U ~ (2/9)t, so its logarithmic coefficient is (-4/45)/(2/9).
assert -sp.Rational(4,45)/sp.Rational(2,9)==-sp.Rational(2,5)

solution=solve_ivp(lambda t,y:[-(y[0]-tanh(y[0]))/3],(0,100000),[1.0],
                   rtol=2e-11,atol=2e-13,dense_output=True)
assert solution.success
normalized=[]
for t in (1000,10000,100000):
    qval=float(solution.sol(t)[0])
    assert qval>0
    normalized.append(1/qval**2 - 2*t/9 + 2*log(t)/5)
assert max(normalized)-min(normalized)<0.005
assert abs(sqrt(100000)*float(solution.sol(100000)[0])-3/sqrt(2))<0.002
print('PASS: exact matrix, spectrum, scalar equations, cubic coefficient, logarithmic coefficient and numerical trend')
