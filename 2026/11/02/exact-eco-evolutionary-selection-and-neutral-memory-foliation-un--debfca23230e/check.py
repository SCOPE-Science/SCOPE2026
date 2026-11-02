"""Symbolic algebraic and integration checks for a neutral-selection invariant."""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit
r,k,beta,delta,e,ep,x,P,Y=s.symbols('r k beta delta e ep x P Y', real=True, positive=True)
frA = r+e*(1-x)
frB = r-e*x
fpA = delta+ep*(1-x)
fpB = delta-ep*x
assert s.simplify(x*frA+(1-x)*frB-r)==0
assert s.simplify(x*fpA+(1-x)*fpB-delta)==0
assert s.simplify(frA-frB-e)==0
assert s.simplify(fpA-fpB-ep)==0
Pt=P*(r-P/k-delta*Y)
Yt=beta*Y*(-1+delta*P)
Ps=1/delta
Ys=(r-1/(k*delta))/delta
c=e-ep*Ys
Jdot=e-ep*Y-ep/delta*Pt/P-ep/(k*beta*delta**2)*Yt/Y
assert s.simplify(Jdot-c)==0
Vdot=(1-Ps/P)*Pt+(1/beta)*(1-Ys/Y)*Yt
assert s.simplify(Vdot+(P-Ps)**2/k)==0
print('symbolic cancellation, invariant and Lyapunov identities: PASS')

def integrate(ee):
    rr,dd,kk,bb,ee_p=2.,1.,2.,1.,.4
    ps,ys=1./dd,(rr-1./(kk*dd))/dd
    p0,y0,x0=2.,.5,.3
    def f(t,z):
        zz,p,y=z
        return [ee-ee_p*y, p*(rr-p/kk-dd*y),bb*y*(-1+dd*p)]
    sol=solve_ivp(f,(0,120),(np.log(x0/(1-x0)),p0,y0),rtol=2e-12,atol=1e-13,dense_output=True)
    assert sol.success
    tests=np.linspace(0,110,35)
    for t in tests:
        zz,pp,yy=sol.sol(t)
        target=(x0/(1-x0))*(pp/p0)**(ee_p/dd)*(yy/y0)**(ee_p/(kk*bb*dd*dd))*np.exp((ee-ee_p*ys)*t)
        assert abs(zz-np.log(target))<2e-7
    assert abs(sol.y[1,-1]-ps)<1e-9 and abs(sol.y[2,-1]-ys)<1e-9
    if abs(ee-ee_p*ys)<1e-12:
        ratio=(x0/(1-x0))*(ps/p0)**(ee_p/dd)*(ys/y0)**(ee_p/(kk*bb*dd*dd))
        assert abs(expit(sol.y[0,-1])-ratio/(1+ratio))<1e-9
    elif ee>ee_p*ys:
        assert 1-expit(sol.y[0,-1])<1e-9
    else:
        assert expit(sol.y[0,-1])<1e-9
    print('integration: parameter e=',ee,'late x=',expit(sol.y[0,-1]),'expected growth exponent',ee-ee_p*ys)
for ee in [.3,.6,.9]: integrate(ee)
print('all checks: PASS')
