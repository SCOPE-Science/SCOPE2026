"""Finite consistency checks for two-periodic Cesaro singular asymptotics."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import svdvals
from scipy.special import ellipk


def coeff(t, a, b):
    r = t*t
    def f(th):
        R = math.sqrt((1-r)**2 + 2*r*(1-math.cos(th)))
        return math.sqrt((a*a+b*b)*(1+r)+2*a*b*R)/R
    return quad(f, 0, math.pi, epsabs=2e-10, epsrel=2e-10)[0]/(2*math.pi)


def finite_part(a, b):
    beta = a*a+b*b
    P = math.sqrt(2*beta)
    k = 2*a*b/beta
    integral = quad(lambda u: k/(math.sqrt(1+k*math.sin(u))+1), 0, math.pi)[0]
    return P*integral/(4*math.pi)


def direct_symbol(t, a, b, th):
    U = np.array([[0, np.exp(-1j*th)], [1,0]], dtype=complex)
    B = np.diag([a, b]) @ np.linalg.inv(np.eye(2)-t*U)
    return sum(svdvals(B))


def formula_symbol(t, a, b, th):
    R = abs(1-t*t*np.exp(1j*th))
    return math.sqrt((a*a+b*b)*(1+t*t)+2*a*b*R)/R


checks = 0
for t in (0., .2, .5, .82):
    for a,b in ((1.,1.),(1.5,.5),(2.,0.),(.2,3.)):
        for theta in np.linspace(0, 2*math.pi, 41):
            lhs = direct_symbol(t,a,b,theta)
            rhs = formula_symbol(t,a,b,theta)
            assert abs(lhs-rhs) < 3e-12*max(1,rhs), (t,a,b,theta,lhs,rhs)
            checks += 1

for t in (0.,.25,.5,.85):
    for a,b in ((1.,1.),(1.5,.5),(2.,0.)):
        c = coeff(t,a,b)
        assert c > 0
        if t > 0:
            assert coeff(t,1,1) < coeff(t,1.5,.5) < coeff(t,2,0)
        checks += 1
    s = 2
    low = s/(math.pi*(1+t))*ellipk((2*math.sqrt(t)/(1+t))**2)
    high = s/(math.pi*math.sqrt(1+t*t))*ellipk((2*t/(1+t*t))**2)
    assert abs(low-coeff(t,1,1)) < 2e-10
    assert abs(high-coeff(t,2,0)) < 2e-10
    checks += 2

for a,b in ((1.,1.),(1.5,.5),(2.,0.)):
    P = math.sqrt(2*(a*a+b*b))
    F = finite_part(a,b)
    for t in (.99,.999,.9999):
        baseline = P/(2*math.pi)*math.log(8/(1-t*t))+F
        error = abs(coeff(t,a,b)-baseline)
        assert error < .025, (a,b,t,error)
        checks += 1

for t,a,b in ((.5,1.5,.5),(.6,2.,0.)):
    N = 360
    rows = np.arange(N)
    gap = rows[:,None]-rows[None,:]
    A = (np.where(rows%2==0,a,b)/(rows+1))[:,None] * np.where(gap>=0, t**np.maximum(gap,0),0.)
    singular = svdvals(A)
    target = coeff(t,a,b)
    for k in (30,50,70):
        assert abs(k*singular[k-1]-target)<.07*target, (t,a,b,k,k*singular[k-1],target)
        checks+=1

print(f"PASS {checks} finite assertions; analytic proof is independent of these checks")
