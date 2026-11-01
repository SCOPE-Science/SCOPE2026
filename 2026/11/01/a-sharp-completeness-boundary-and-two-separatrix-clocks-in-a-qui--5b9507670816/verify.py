"""Standalone reproducibility checks for the stated polynomial vector field.
Finite quadrature is a diagnostic; the theorem uses the analytic proof.
"""
import math
import sympy as S
from scipy.integrate import quad
x,y,a,b,z=S.symbols('x y a b z', real=True)
w=S.exp(-a*x**4/2)
vx=S.exp(-a*x**4/2)*x*(1+b*x**4)
hx=-a*x**3*w*y**3+w*y*(-x-b*x**5+a*x**3*y**2)+vx*y
assert S.simplify(hx)==0
# Time-preserving coordinate and conservative force to order five.
zz=x-a*x**5/S.Integer(20)
f=(1-a*x**4/S.Integer(4))*(x+b*x**5)
assert S.expand(f.subs(x,z+a*z**5/S.Integer(20))).coeff(z,5).expand()==b-a/S.Integer(5)
ceiling=S.integrate(S.exp(-a*x**4/2)*(x+b*x**5),(x,0,S.oo),conds='none')
assert S.simplify(ceiling-S.sqrt(S.pi)/(2*S.sqrt(2*a))*(1+b/a))==0
# Stable finite-amplitude quadrature: v_A(x)^2 = integral_0^(A²-x²)
#    [1+beta(x²+u)²] exp[-alpha(x²u+u²/2)] du.
def speed_sq(xvalue,A,alpha,beta):
    upper=A*A-xvalue*xvalue
    if upper <= 0: return 0.0
    return quad(lambda u:(1+beta*(xvalue*xvalue+u)**2)*math.exp(-alpha*(xvalue*xvalue*u+u*u/2)),0,upper,epsabs=1e-9,epsrel=1e-9)[0]
def period(A,alpha,beta):
    def integrand(theta):
        if theta==0: return 0
        t=A*math.cos(theta)
        return A*math.sin(theta)/math.sqrt(speed_sq(t,A,alpha,beta))
    return 4*quad(integrand,0,math.pi/2,epsabs=1e-6,epsrel=1e-6,limit=140)[0]
for beta in [0.,.2,1.]:
    values=[period(A,1.,beta) for A in (2.,3.,4.,5.)]
    assert all(v>0 for v in values)
    assert all(values[j+1]>values[j] for j in range(3))
    ratios=[v/(2*A*A if beta==0 else 4/math.sqrt(beta)*math.log(A)) for A,v in zip((2.,3.,4.,5.),values)]
    assert abs(ratios[-1]-1)<abs(ratios[0]-1)
    print('beta',beta,'periods',values,'asymptotic-ratios',ratios)
print('CHECK_OK')
