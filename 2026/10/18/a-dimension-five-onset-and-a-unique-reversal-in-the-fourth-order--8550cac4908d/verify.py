"""Reproduce the rational transform and the dimension-dependent time-asymmetry threshold.
Run: python3 verify.py (requires sympy, scipy, numpy).
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm

s, a, d, h2, h4 = sp.symbols('s a d h2 h4', positive=True)
m2 = h2/(a+1)
m13 = h4/(a+1)
m4 = 3*(2*h4+a*h2*h2)/((a+1)*(a+2)*(a+3))
m31 = m4
m22 = (a+3)*m4/3
R = sp.Matrix([[-3,3,0,0,0,0],
               [0,-2-a,2,0,0,0],
               [0,0,-1-a,1,a*h2,0],
               [0,0,0,-a,0,0],
               [0,0,0,0,-1,1],
               [0,0,0,0,0,-a]])
e = sp.Matrix([m4,m31,m22,m13,m2,m2])
R1 = sp.Matrix([[-1,1],[0,-a]])
e1=sp.Matrix([m4,m31])
# Solve triangular linear systems independently of any closed-form transform.
p6=(s*sp.eye(6)-R).inv()*e
p2=(s*sp.eye(2)-R1).inv()*e1
Q=sp.factor(p6[0]-p2[0]); num=sp.factor(Q.subs({h2:1/d,h4:3/(d*(d+2))}))
expected=12*a*((4-d)*a*a+3*a*(s+3)+3*(d+1)*(s+1))/(d*d*(d+2)*(a+1)*(a+2)*(a+3)*(s+a)*(s+1)*(s+3)*(s+a+1)*(s+a+2))
assert sp.cancel(num-expected)==0
print('PASS rational Laplace expression, any dimension d>=1')
assert sp.factor((4-d)*a*a+3*a*(s+3)+3*(d+1)*(s+1) - (3*(a+d+1)*(s+1)+a*(6-(d-4)*a))) == 0
print('PASS four-fold/five-fold exponential convolution decomposition')
for dim in list(range(1,21))+[30,100]:
    if dim<=4:
        for alpha in [.1,1,2,10]:
            assert alpha*(6-(dim-4)*alpha)>0
    else:
        critical=6/(dim-4) if dim<=10 else None
        if dim>=11:
            critical=(-3*(dim-2)+np.sqrt(9*(dim-2)**2+12*(dim-1)*(dim+1)))/(2*(dim-1))
        for alpha in [critical*.95,critical*1.05]:
            A0=3*(alpha+dim+1)
            B=alpha*(6-(dim-4)*alpha)
            if alpha<=critical:
                assert B>=0 or (alpha<1 and A0+B/(1-alpha)>0)
            else:
                assert B<0 and (alpha>=1 or A0+B/(1-alpha)<0)
print('PASS analytic threshold inequalities across 22 integer dimensions')
# Independent finite-lag checks using the original Markov polynomial generator.
for dim,alpha in [(1,.5),(2,2),(3,2),(4,15),(5,7),(6,4),(9,1.4),(10,1.2),(11,.95),(11,1.4),(20,.8),(20,1.4)]:
    rv=np.asarray(R.subs({a:alpha,h2:1/dim}),dtype=float)
    r1=np.asarray(R1.subs(a,alpha),dtype=float)
    v=np.asarray(e.subs({a:alpha,h2:1/dim,h4:3/(dim*(dim+2))}),dtype=float).flatten()
    w=np.asarray(e1.subs({a:alpha,h2:1/dim,h4:3/(dim*(dim+2))}),dtype=float).flatten()
    def arrow(t):
        return (expm(rv*t)@v)[0]-(expm(r1*t)@w)[0]
    vals=[arrow(t) for t in [0.3,1,3,8,15,30]]
    assert vals[0]>-1e-10
    critical=6/(dim-4) if 5<=dim<=10 else ((-3*(dim-2)+np.sqrt(9*(dim-2)**2+12*(dim-1)*(dim+1)))/(2*(dim-1)) if dim>=11 else 1e100)
    # When the sign reversal is predicted, test at least at moderate or large lags.
    if alpha>critical:
        assert any(z < -1e-13 for z in vals[1:]),(dim,alpha,vals)
    else:
        assert all(z>-1e-10 for z in vals),(dim,alpha,vals)
print('PASS 12 independent finite-lag matrix exponential comparisons')
print('VERIFY_OK')
