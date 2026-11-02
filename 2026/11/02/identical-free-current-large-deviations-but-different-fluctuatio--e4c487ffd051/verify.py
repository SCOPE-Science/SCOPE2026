"""Independent finite-matrix and quadrature checks for an Erlang-phase active-particle model.

Requires Python 3, NumPy, and SciPy. This is numerical verification, not a substitute for proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

checks = 0

def close(a, b, tol=3e-8):
    global checks
    checks += 1
    if not math.isfinite(float(a)) or abs(float(a)-float(b)) > tol*(1+abs(float(a))+abs(float(b))):
        raise AssertionError((a,b))

def cycle(rate):
    Q=np.zeros((4,4))
    for i in range(4):
        Q[i,i]=-rate
        Q[i,(i+1)%4]=rate
    return Q

s=np.array([1.,1.,-1.,-1.])
for rate in (0.4,1.,2.3):
    Q=cycle(rate)
    for speed in (0.6, 1.9):
        for w in (-2.5,-0.8,0.,0.7,3.4):
            tilted=Q+w*speed*np.diag(s)
            eig=np.linalg.eigvals(tilted)
            close(max(eig.real),-rate+math.sqrt(rate*rate+(speed*w)**2))
            for z in (-3.1,-0.33,0.7,4.2):
                det=np.linalg.det(z*np.eye(4)-tilted)
                poly=(z*(z+2*rate)-(speed*w)**2)*((z+rate)**2+rate*rate-(speed*w)**2)
                close(det,poly)
        for t in (0.,0.04,0.2,0.9,2.,6.5):
            C=0.25*s@expm(Q*t)@s
            close(C,math.exp(-rate*t)*math.cos(rate*t))
            CE=lambda a:math.exp(-rate*a)*math.cos(rate*a)
            CM=lambda a:math.exp(-2*rate*a)
            var_e=2*speed*speed*quad(lambda a:(t-a)*CE(a),0,t,epsabs=2e-11)[0]
            var_m=2*speed*speed*quad(lambda a:(t-a)*CM(a),0,t,epsabs=2e-11)[0]
            exact_e=speed*speed*(t/rate-math.exp(-rate*t)*math.sin(rate*t)/(rate*rate))
            exact_m=speed*speed*(t/rate-(1-math.exp(-2*rate*t))/(2*rate*rate))
            close(var_e,exact_e)
            close(var_m,exact_m)
            close(var_e-var_m,speed*speed*math.exp(-rate*t)*(math.sinh(rate*t)-math.sin(rate*t))/(rate*rate))
            if t>0 and not var_e>var_m: raise AssertionError('variance strict inequality')
            checks += 1
        for trap in (0.2,1.,4.):
            ve= speed*speed/trap*quad(lambda x: math.exp(-trap*x)*math.exp(-rate*x)*math.cos(rate*x),0,np.inf)[0]
            vm= speed*speed/trap*quad(lambda x: math.exp(-(trap+2*rate)*x),0,np.inf)[0]
            exact_ve=speed*speed*(trap+rate)/(trap*((trap+rate)**2+rate*rate))
            exact_vm=speed*speed/(trap*(trap+2*rate))
            close(ve,exact_ve)
            close(vm,exact_vm)
            close(ve-vm,speed*speed*rate/((trap+2*rate)*((trap+rate)**2+rate*rate)))
            if not ve>vm: raise AssertionError('trapped strict inequality')
            checks+=1
        for y in (-0.85,-0.3,0.,0.4,0.9):
            # Independent numerical Legendre transformation at zero Brownian noise.
            f=lambda k:k*(speed*y)-(-rate+math.sqrt(rate*rate+(speed*k)**2))
            opt=minimize_scalar(lambda k:-f(k),bounds=(-30*rate/speed,30*rate/speed),method='bounded', options={'xatol':1e-12})
            close(-opt.fun,rate*(1-math.sqrt(1-y*y)))
print('PASS',checks,'independent deterministic matrix, quadrature and Legendre checks')
