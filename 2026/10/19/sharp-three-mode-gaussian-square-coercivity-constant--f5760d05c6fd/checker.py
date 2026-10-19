"""Reproduce finite algebra and independent Gaussian quadrature checks.
Requires Python 3 with NumPy and SymPy. Run: python checker.py
"""
import math
import cmath
import random
import numpy as np
import sympy as sp

x,y=sp.symbols('x y',real=True)
N=(4+8*y**2)*x**2-8*x*y+2+24*y**2+24*y**4
D=(2+4*y**2)*x**2-8*x*y+1+20*y**2+20*y**4
Q=2*x**2-8*x*y**3-8*x*y-2*y**2-1
H=(4*x**3*y**2-2*x**3+16*x**2*y**5+16*x**2*y**3+8*x**2*y+
   12*x*y**4+4*x*y**2-x+8*y**3+4*y)
assert sp.expand(sp.diff(N,x)*D-N*sp.diff(D,x)+8*y*(2*y*y+1)*Q)==0
assert sp.expand(sp.diff(N,y)*D-N*sp.diff(D,y)+8*H)==0
factor=16*(2*y*y+1)*(8*y**6+16*y**4+10*y*y+1)*(96*y**6+96*y**4+6*y*y-1)
assert sp.expand(sp.resultant(Q,H,x)-factor)==0
assert sp.expand(N-2*D-8*y*(x-2*y*(1+y*y)))==0
print('PASS: 4 exact symbolic identities (two derivatives, resultant, ratio deficit)')

q=float(sp.nroots(96*sp.Symbol('q')**3+96*sp.Symbol('q')**2+6*sp.Symbol('q')-1)[2])
yo=math.sqrt(q)
xo=2*yo*(1+yo*yo)+math.sqrt(4*yo*yo*(1+yo*yo)**2+yo*yo+0.5)
Rstar=float((N/D).subs({x:xo,y:yo}))
assert abs(Rstar-2.444087335815063)<1e-12
assert abs(float(Q.subs({x:xo,y:yo})))<1e-10
assert abs(float(H.subs({x:xo,y:yo})))<1e-10
print(f'PASS: algebraic root and stationarity; x={xo:.14f}, y={yo:.14f}, R={Rstar:.14f}')

rng=random.Random(20261014)
from numpy.polynomial.laguerre import laggauss
rho,w=laggauss(18)
theta=2*np.pi*np.arange(24)/24
nodes=(np.sqrt(rho)[:,None])*np.exp(1j*theta[None,:])
weights=w[:,None]/24
checks=0
for _ in range(250):
    aa=complex(rng.uniform(-2,2),rng.uniform(-2,2))
    bb=complex(rng.uniform(-2,2),rng.uniform(-2,2))
    cc=complex(rng.uniform(-2,2),rng.uniform(-2,2))
    E2=abs(aa)**2+abs(bb)**2+2*abs(cc)**2
    E4=(abs(aa)**4+4*abs(aa*bb)**2+2*abs(bb)**4+
        8*abs(aa*cc)**2+8*(bb**2*(aa*cc).conjugate()).real+
        24*abs(bb*cc)**2+24*abs(cc)**4)
    F=aa+bb*nodes+cc*nodes**2
    e4_quadrature=float(np.sum(weights*np.abs(F)**4))
    e2_quadrature=float(np.sum(weights*np.abs(F)**2))
    assert abs(e4_quadrature-E4)<1e-10*max(1,E4)
    assert abs(e2_quadrature-E2)<1e-10*max(1,E2)
    assert E4-E2*E2>0
    R=(E4-abs(aa)**4)/(E4-E2*E2)
    assert R<=Rstar+1e-10
    checks+=1
print(f'PASS: {checks} independent complex-polynomial moment quadratures and sharp inequality tests')

for t in [0.1,1,4]:
    for phi in [0,0.5,2]:
        aa=xo*t
        bb=t*cmath.exp(1j*phi)
        cc=-yo*t*cmath.exp(2j*phi)
        E2=abs(aa)**2+abs(bb)**2+2*abs(cc)**2
        E4=(abs(aa)**4+4*abs(aa*bb)**2+2*abs(bb)**4+8*abs(aa*cc)**2+
            8*(bb**2*(aa*cc).conjugate()).real+24*abs(bb*cc)**2+24*abs(cc)**4)
        assert abs((E4-abs(aa)**4)/(E4-E2**2)-Rstar)<2e-12
print('PASS: 9 exact-orbit equality configurations')
