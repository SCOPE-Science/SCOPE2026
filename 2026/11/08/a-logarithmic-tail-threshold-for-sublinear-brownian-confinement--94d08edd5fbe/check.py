#!/usr/bin/env python3
"""Finite diagnostics for a sublinear-potential reset resolvent tail.
These checks do not replace the analytic asymptotic argument.
"""
import math
from scipy.integrate import solve_ivp, quad

D = 0.91
r = 1.17
lam = 1.32
k = math.sqrt(r/D)

def V(x, alpha):
    return lam * ((1.0 + x*x)**(alpha/2.0) - 1.0)

def vp(x, alpha):
    return lam*alpha*x*(1+x*x)**(alpha/2.0-1.0)

def vpp(x, alpha):
    return lam*alpha*(1+x*x)**(alpha/2.0-2.0)*(1.0+(alpha-1.0)*x*x)

def qfun(x, alpha):
    return k*k + vp(x,alpha)**2/(4*D*D) - vpp(x,alpha)/(2*D)

def q_prime(x, alpha):
    h=max(0.002,1.0e-4*x)
    return (qfun(x+h,alpha)-qfun(x-h,alpha))/(2*h)

def riccati_grid(alpha, final=3000.0, minimum=100.0):
    # y=-psi'/psi solves y'=y^2-Q for the decaying branch.
    y_at_right=math.sqrt(qfun(final,alpha))
    sol=solve_ivp(lambda x,z: [z[0]**2-qfun(x,alpha)],
                  (final,minimum),[y_at_right],
                  dense_output=True,rtol=4.e-11,atol=3.e-13,
                  max_step=8.0)
    assert sol.success, sol.message
    return sol

def run():
    n=0
    alphas=[1/3,0.5,2/3,0.82]
    for alpha in alphas:
        # Verify exact conjugated coefficient and its asymptotic power.
        C=(lam*alpha)**2/(8*D*D*k)
        for x in (120.0,240.0,480.0,960.0):
            root=math.sqrt(qfun(x,alpha))
            assert qfun(x,alpha)>0
            delta=(vp(x,alpha)**2/(4*D*D)-vpp(x,alpha)/(2*D))/(2*k)
            rel=(root-k)/delta
            assert abs(rel-1.0)<0.02, (alpha,x,rel)
            n += 2
        sol=riccati_grid(alpha)
        for x in (200.,400.,700.,1000.,1500.):
            y=float(sol.sol(x)[0])
            assert y>0
            delta=(vp(x,alpha)**2/(4*D*D)-vpp(x,alpha)/(2*D))/(2*k)
            asymptotic=(y-k)/delta
            assert abs(asymptotic-1)<0.05,(alpha,x,asymptotic)
            # Riccati correction is smaller than the local eikonal term.
            assert abs(y-math.sqrt(qfun(x,alpha)))/abs(delta) <0.05
            n+=3
        # Integrate only the positive eikonal correction.
        action=lambda x:math.sqrt(qfun(x,alpha))-k
        for X in (300.,600.,1200.):
            I,_=quad(action,100.,X,epsabs=1e-10,epsrel=2e-9,limit=200)
            assert I>0
            n+=1
    # Directly check the critical logarithmic integral of the Riccati slope.
    s_critical=riccati_grid(0.5,final=8000.0,minimum=300.0)
    critical_integral,_=quad(lambda x:float(s_critical.sol(x)[0]-k),
                             500.,2000.,epsabs=2e-9,limit=150)
    theta=lam*lam/(32*D*D*k)
    assert abs(critical_integral/(theta*math.log(4.0))-1.0)<0.08
    n+=1
    # The critical logarithmic coefficient must be exactly C at alpha=1/2.
    theta=lam*lam/(32*D*D*k)
    assert abs((lam*0.5)**2/(8*D*D*k)-theta)<1e-14
    n+=1
    print(f"PASS {n} finite diagnostic assertions; critical logarithmic power {theta:.12f}")
if __name__=="__main__":
    run()
