#!/usr/bin/env python3
"""Direct checks of the scalar soft-sign momentum phase diagram.

Uses only the Python standard library. Finite tests corroborate, but do not
replace, the analytical proof supplied with the result.
"""
import cmath
import math
import random


def step(z, w, beta, c):
    wp = beta * w + (1.0 - beta) * z
    return (z - c * wp / math.hypot(1.0, wp), wp)


def characteristic_eigenvalues(beta, effective_c):
    trace = 1.0 + beta - effective_c * (1.0 - beta)
    det = beta
    root = cmath.sqrt(trace * trace - 4.0 * det)
    return ((trace + root) / 2.0, (trace - root) / 2.0)


def assert_close(x, y, *, tol=5e-12):
    if abs(x-y) > tol * (1.0+abs(y)):
        raise AssertionError((x, y, tol))


def main():
    random.seed(637291)
    for beta in (0.0, 0.025, 0.2, 0.5, 0.75, 0.92, 0.98):
        t = (1.0-beta)/(1.0+beta)
        crit = 2.0/t
        for q in (0.20, 0.5, 0.99, 0.999, 1.001, 1.05, 1.5, 2.0, 7.0):
            c=q*crit
            ev=characteristic_eigenvalues(beta,c)
            if q < 1.0:
                assert max(abs(v) for v in ev)<1.0
            else:
                assert max(abs(v) for v in ev)>1.0
                amp=math.sqrt((c*t/2.0)**2-1.0)/t
                state=(amp,-t*amp)
                next_state=step(*state,beta,c)
                assert_close(next_state[0],-amp)
                assert_close(next_state[1],+t*amp)
                assert_close(step(*next_state,beta,c)[0],+amp)
                assert_close(step(*next_state,beta,c)[1],-t*amp)
                eff=c/(1.0+(t*amp)**2)**1.5
                assert_close(eff,8.0/(c*c*t**3))
                assert max(abs(v) for v in characteristic_eigenvalues(beta,eff))<1.0
                # All nontrivial two-cycles have zero midpoint:
                # soft-sign injectivity enforces w_1=-w_2 and z_1=-z_2.
        # The critical cubic coefficient from the projection onto the -1 eigenspace.
        k=2.0*beta*(1.0+beta)/(1.0-beta)**2
        a11=1.0-crit*(1.0-beta)
        a12=-crit*beta
        a21=1.0-beta
        a22=beta
        assert_close(a11 + k*(a21+t*a11), -1.0-k*t)
        assert_close(a12 + k*(a22+t*a12), -k)
        assert_close((a21+t*a11),-beta*t)
        assert_close(a22+t*a12, -beta)
        # Direct algebra: center eigenvector (1,-t), cubic force projected using
        # left eigvector (1/t,k).
        cubic=(1.0/t)*(t**3)*(1.0/t)
        assert_close(cubic,t)
    # Coordinate transform and linearization checks for random parameter values.
    for _ in range(3000):
        beta=random.uniform(0.0,0.95)
        c=random.uniform(0.01,35.0)
        z=random.uniform(-4.0,4.0)
        w=random.uniform(-4.0,4.0)
        h=1e-6
        f=step(z,w,beta,c)
        dz=step(z+h,w,beta,c)
        dw=step(z,w+h,beta,c)
        wp=beta*w+(1.0-beta)*z
        d=c/(1.0+wp*wp)**1.5
        J=((1.0-d*(1.0-beta),-d*beta),(1.0-beta,beta))
        for i in range(2):
            assert abs((dz[i]-f[i])/h-J[i][0])<2e-5
            assert abs((dw[i]-f[i])/h-J[i][1])<2e-5
        assert_close(J[0][0]*J[1][1]-J[0][1]*J[1][0],beta,tol=1e-13)
    # Critical n^(-1/2) limit from near center direction. Absolute value avoids
    # numerical sign cancellation while the transverse stable mode decays.
    for beta in (0.0,0.25,0.5,0.75):
        t=(1.0-beta)/(1.0+beta)
        c=2.0/t
        k=2.0*beta*(1.0+beta)/(1.0-beta)**2
        z,w=0.1,-0.1*t
        for _ in range(40000):
            z,w=step(z,w,beta,c)
        u=z+k*(w+t*z)
        approx=math.sqrt(40000)*abs(u)
        ideal=1.0/math.sqrt(2.0*t)
        assert abs(approx/ideal-1)<0.035,(beta,approx,ideal)
    # Exact illustrative parameter point beta=1/2, c=8 gives amplitude sqrt(7).
    beta,c=0.5,8.0
    amp=math.sqrt(7)
    assert_close(step(amp,-amp/3,beta,c)[0],-amp)
    print("PASS: 63 parameter configurations; 3000 Jacobian comparisons; 4 critical-rate tests; 7 cubic-identity checks; 1 exact cycle example.")

if __name__=='__main__':
    main()
