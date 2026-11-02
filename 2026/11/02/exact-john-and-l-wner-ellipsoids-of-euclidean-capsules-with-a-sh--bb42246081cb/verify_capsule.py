"""Independent numerical checks for extremal ellipsoids of Euclidean capsules.

Run: python3 verify_capsule.py
No numerical test substitutes for the analytic containment and contact proof.
"""
import math
import random
from scipy.optimize import minimize


def shape(d, t):
    assert d >= 2 and t >= 0
    # Rationalized root avoids loss of significance for large t.
    u = 2 / (math.sqrt((d-1)**2*t*t + 4*d) + (d-1)*t)
    A = math.sqrt(d)*(t+u)
    B = math.sqrt(d/(d-1) * (1-u*u))
    return u,A,B


def full_ellipse_boundary_sup(A,B,t):
    # Exact max for either translated unit sphere when A>=B.
    q=1/A**2 - 1/B**2
    uv = min(1.0, max(-1.0, -(t/A**2)/q)) if abs(q)>1e-15 else 1.0
    return max((t+v)**2/A**2+(1-v*v)/B**2 for v in [-1,uv,1])


def log_vol(z, d):
    return z[0]+(d-1)*z[1]


def constraint(z,d,t):
    return 1 - full_ellipse_boundary_sup(math.exp(z[0]),math.exp(z[1]),t)


def main():
    rng=random.Random(3181990)
    max_eq = 0.0
    max_volume_error=0.0
    tests=0
    for d in (2,3,4,5,8,16):
        for t in (0.001,.025,.2,.7,2.,10.,80.):
            u,A,B=shape(d,t)
            assert 0<u<1/math.sqrt(d)
            residual=max(abs(d*u*u+(d-1)*t*u-1), abs((t+u)**2/A**2-1/d), abs((1-u*u)/B**2-(d-1)/d), abs(full_ellipse_boundary_sup(A,B,t)-1))
            max_eq=max(max_eq,residual)
            assert residual<3e-12,(d,t,residual)
            for j in range(100):
                v=2*rng.random()-1
                F=(t+v)**2/A**2+(1-v*v)/B**2
                assert F<=1+1e-12,(d,t,v,F)
            # John ellipsoid support test: h_J<=h_capsule.
            for j in range(100):
                v=rng.random()
                hJ=math.sqrt(1+(t*t+2*t)*v*v)
                assert hJ<=1+t*v+1e-12
            if t>0:
                out=minimize(log_vol, [math.log(A)*1.02,math.log(B)*1.01], args=(d,),
                   method='SLSQP', constraints={'type':'ineq','fun':lambda z:constraint(z,d,t)},
                   bounds=[(math.log(t+1),math.log(10*(t+1))),(0,math.log(10))],
                   options={'ftol':1e-11,'maxiter':200})
                if out.success:
                    max_volume_error=max(max_volume_error,abs(out.fun-math.log(A)-(d-1)*math.log(B)))
            tests+=1
    print('dimension-parameter cases',tests)
    print('maximum algebra/containment equality residual',max_eq)
    print('max log-volume discrepancy numerical optimizer',max_volume_error)
    assert max_volume_error<1e-5

if __name__=='__main__': main()
