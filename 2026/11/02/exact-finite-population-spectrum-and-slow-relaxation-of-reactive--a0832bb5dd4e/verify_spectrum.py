"""Reproduce exact characteristic identities and numerical finite-ensemble examples.

Run: python verify_spectrum.py
Requires sympy and numpy; no external data.
"""
import sympy as sp
import numpy as np

lam = sp.symbols('lam')
b = sp.Rational(6,5)
g = sp.Rational(3,10)
M = 4
u = [(sp.S.One, sp.S.Zero),(-sp.S.One, sp.S.Zero),
     (sp.Rational(3,5),sp.Rational(4,5)),
     (-sp.Rational(3,5),-sp.Rational(4,5))]
J=sp.zeros(2*M)
for j,(x,y) in enumerate(u):
    local=-2*b*sp.Matrix([[x*x,x*y],[x*y,y*y]])
    for r in range(2):
        for s in range(2):
            J[2*j+r,2*j+s]+=local[r,s]
    for k in range(M):
        J[2*j,2*k+1]-=g
        J[2*j+1,2*k]+=g
Q=sum((x+sp.I*y)**2 for x,y in u)/M
q2=sp.simplify(sp.expand_complex(Q*sp.conjugate(Q)))
assert q2 == sp.Rational(9,25)
h=M*g
d=lam*(lam+2*b)
quartic=sp.expand(d*d+h*h*((lam+b)**2-b*b*q2))
expected=sp.expand(d**(M-2)*quartic)
assert sp.expand(J.charpoly(lam).as_expr()-expected)==0
print('RATIONAL_EIGHT_BY_EIGHT_CHARACTERISTIC_PASS')

q2sym,B,H=sp.symbols('q2 B H', positive=True)
a3=4*B; a2=4*B**2+H**2; a1=2*B*H**2; a0=B**2*H**2*(1-q2sym)
assert sp.simplify(a3*a2-a1 - (16*B**3+2*B*H**2))==0
assert sp.simplify(a3*a2*a1-a1*a1-a3*a3*a0 - (16*B**4*H**2*(1+q2sym)+4*B**2*H**4))==0
assert sp.simplify(-a0.diff(q2sym)/(a1) - B/2)==0
print('ROUTH_HURWITZ_AND_SLOW_ROOT_DERIVATIVE_PASS')

for phases in (np.array([0,2*np.pi/3,4*np.pi/3]),
               np.array([0,np.pi,0.6,np.pi+0.6]),
               2*np.pi*np.arange(5)/5,
               np.array([0,np.pi,0.1,np.pi+0.1,1.3,np.pi+1.3]),
               2*np.pi*np.arange(8)/8):
    n=len(phases)
    v=np.exp(1j*phases)
    assert abs(sum(v))<1e-11
    q=abs(np.mean(v**2))
    beta=1.2; gamma=0.37; h=n*gamma
    A=np.zeros((2*n,2*n))
    for j in range(n):
        w=np.array([v[j].real,v[j].imag]);
        A[2*j:2*j+2,2*j:2*j+2]-=2*beta*np.outer(w,w)
        for k in range(n):
            A[2*j:2*j+2,2*k:2*k+2]+=gamma*np.array([[0,-1],[1,0]])
    ds=np.polynomial.polynomial.polymul([0,2*beta,1],[0,2*beta,1])
    p=np.polynomial.polynomial.polyadd(ds,h*h*np.polynomial.polynomial.polymul([beta,1],[beta,1]))
    p[0]-=h*h*beta*beta*q*q
    target=np.hstack([np.zeros(n-2),np.full(n-2,-2*beta),np.polynomial.polynomial.polyroots(p)])
    obs=np.linalg.eigvals(A)
    from scipy.optimize import linear_sum_assignment
    rows,cols=linear_sum_assignment(np.abs(obs[:,None]-target[None,:]))
    assert max(abs(obs[rows]-target[cols]))<1e-8
print('FINITE_ENSEMBLE_NUMERICAL_REPLAYS_PASS')
