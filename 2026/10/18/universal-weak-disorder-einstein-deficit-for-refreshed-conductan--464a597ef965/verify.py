"""Independent finite-state and integral checks for a weak-disorder response law.

Checks are finite diagnostics; the analytic proof addresses the infinite lattice.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve


def spectral(mu):
    a = lambda x: 1.0 - math.cos(x)
    rho = quad(lambda x: math.sin(x)**2 / (mu+a(x)), -math.pi, math.pi,
               epsabs=1e-12)[0] / (2*math.pi)
    j = quad(lambda x: a(x)*math.sin(x)**2/(mu+a(x))**2,
             -math.pi, math.pi, epsabs=1e-12)[0] / (2*math.pi)
    sig = quad(lambda x: a(x)*(1-a(x))/(mu+a(x))
               - a(x)*math.sin(x)**2/(mu+a(x))**2,
               -math.pi, math.pi, epsabs=1e-12)[0]/(2*math.pi)
    root=math.sqrt(mu*(mu+2))
    assert abs(rho-(mu+1-root))<1e-11
    assert abs(sig+rho)<1e-11
    assert abs((-rho) - (-.5*(1+j)) - .5*math.sqrt(mu/(mu+2)))<1e-11
    return -rho, -0.5*(1+j)


def finite_ring(n,mu,eps,lam):
    """State bit j is a Rademacher edge; no spatial averaging shortcuts."""
    count=1<<n
    q=np.zeros((count,count)); drift=np.zeros(count); jumps=[]
    for s in range(count):
        b=np.array([1 if (s>>j)&1 else -1 for j in range(n)])
        right=math.exp(lam)*(1+eps*b[0])
        left=math.exp(-lam)*(1+eps*b[-1])
        p=right/(right+left)
        drift[s]=2*p-1
        plus=sum(((s>>((j+1)%n))&1)<<j for j in range(n))
        minus=sum(((s>>((j-1)%n))&1)<<j for j in range(n))
        for t,rate in ((plus,p),(minus,1-p)):
            if t!=s:
                q[s,t]+=rate
                q[s,s]-=rate
        for j in range(n):
            t=s^(1<<j)
            q[s,t]+=mu/2
            q[s,s]-=mu/2
        jumps.append((plus,minus,p))
    a=q.T.copy();a[-1,:]=1
    rhs=np.zeros(count);rhs[-1]=1
    pi=solve(a,rhs)
    speed=pi@drift
    if lam!=0:
        return speed
    b=q.copy();b[-1,:]=pi
    rhs=-(drift-speed);rhs[-1]=0
    corrector=solve(b,rhs)
    var=0.0
    for s,(plus,minus,p) in enumerate(jumps):
        term=p*(1+corrector[plus]-corrector[s])**2
        term+=(1-p)*(-1+corrector[minus]-corrector[s])**2
        term+=sum(mu/2*(corrector[s^(1<<j)]-corrector[s])**2
                  for j in range(n))
        var+=pi[s]*term
    return speed,var


def main():
    checks=0
    for mu in (0.5,1.0,4.0,10.0):
        ds,dm=spectral(mu)
        assert abs((ds-dm)-.5*math.sqrt(mu/(mu+2)))<1e-10
        checks+=4
    for mu in (1.0,4.0):
        ds,dm=spectral(mu)
        speed0,var0=finite_ring(7,mu,0.0,0.0)
        assert abs(speed0)<1e-11 and abs(var0-1)<1e-11
        checks+=2
        for eps in (0.04,0.02):
            speed,var=finite_ring(7,mu,eps,0)
            h=2e-5
            mobility=(finite_ring(7,mu,eps,h)-finite_ring(7,mu,eps,-h))/(2*h)
            assert abs(speed)<1e-9
            assert abs((var-1)/eps**2-ds)<0.005
            assert abs((mobility-1)/eps**2-dm)<0.005
            assert var>mobility
            checks+=4
    print(f"PASS: {checks} independent analytic/finite-state consistency checks")

if __name__ == '__main__':
    main()
