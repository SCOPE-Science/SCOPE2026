"""Independent finite checks for three-ring polynomial interpolation determinants.

Only mathematical checks; not a substitute for the analytic proof.
"""
import math
import cmath
import numpy as np
from scipy.optimize import differential_evolution


def triangle_product(t, inner, outer):
    a=1.0/t
    return abs(a*cmath.exp(1j*inner)-1)*abs(t*cmath.exp(1j*outer)-1)*abs(t*cmath.exp(1j*outer)-a*cmath.exp(1j*inner))


def optimum(t):
    assert t >= 1
    crit=2+math.sqrt(3)
    c=-(t+1/t)/4
    th=math.acos(c) if t<=crit else math.pi
    L=(3*math.sqrt(3)/4)*(t+1/t)**2 if t<=crit else (t+1)**3*(t-1)/t**2
    return th,L


def direct_gram_det(n,t,r=0.9):
    h=math.log(t)/n
    radii=[r*math.exp(-h),r,r*math.exp(h)]
    th,L=optimum(t)
    angles=[-th/n,0,th/n]
    roots=[radii[i]*cmath.exp(1j*(angles[i]+2*math.pi*j/n)) for i in range(3) for j in range(n)]
    weights=np.array([math.factorial(k)/math.pi**k for k in range(3*n)],dtype=float)
    norms=np.array([sum(abs(z)**(2*k)/weights[k] for k in range(3*n)) for z in roots])
    M=np.array([[z**k/math.sqrt(weights[k]*norms[j]) for k in range(3*n)] for j,z in enumerate(roots)])
    sign,ldet=np.linalg.slogdet(M@M.conj().T)
    predicted=(3*n)*math.log(n)+(3*n*(3*n-1))*math.log(r)+2*n*math.log(L)
    predicted-=sum(math.log(w) for w in weights)
    predicted-=n*sum(math.log(sum(radii[i]**(2*k)/weights[k] for k in range(3*n))) for i in range(3))
    return float(ldet),predicted


def run():
    tests=0
    worst=0.
    for t in [1.,1.04,1.2,2.,3.,2+math.sqrt(3),3.9,4.5,8.,15.]:
        th,L=optimum(t)
        expected=triangle_product(t,-th,th)
        err=abs(expected-L)/max(1,L)
        assert err<2e-13,(t,err)
        worst=max(worst,err)
        tests+=1
        # Full two-variable numerical search independent of the analytic reduction.
        result=differential_evolution(lambda x:-triangle_product(t,x[0],x[1]),
                           [(0,2*math.pi),(0,2*math.pi)],
                           tol=1e-9,polish=True,popsize=16,maxiter=200,seed=371,workers=1)
        assert (-result.fun) <= L*(1+2e-8)
        assert (L-(-result.fun))/L < 8e-6,(t,L,-result.fun)
        tests+=1
        # Independently check the closed resultant/Vandermonde determinant formula.
        for n in [1,2,3,4]:
            ld,pred=direct_gram_det(n,t)
            err=abs(ld-pred)
            assert err<2e-7,(n,t,err)
            worst=max(worst,err)
            tests+=1
        if t>1:
            from math import cos
            # Strict failure of the naive 120 degree phases away from equal radii.
            other=triangle_product(t,-2*math.pi/3,2*math.pi/3)
            assert L>other*(1+1e-10) if t>=1.2 else L>=other-1e-11
            tests+=1
    print('PASS three-ring optimum: tests=',tests,'max_formula_abs_error=',format(worst,'.3g'))
    print('transition t=',format(2+math.sqrt(3),'.15g'),'theta(t=1)=',format(optimum(1.)[0],'.15g'))
    print('continuous and collinear optimizer sides verified numerically')

if __name__=='__main__': run()
