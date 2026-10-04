#!/usr/bin/env python3
import cmath, math

TOL=2e-10
checks=0
max_err=0.0

def peak(N,u,v):
    zeta=cmath.exp(2j*math.pi/N)
    return max(abs(1+u*(zeta**k)+v*(zeta**(2*k)))**2 for k in range(N))

for N in range(3,1201):
    if N%2:
        target=1+4*math.cos(math.pi/N)
        c=math.cos(math.pi/N)-1
        alpha=math.acos(max(-1.0,min(1.0,c)))
        u=cmath.exp(1j*alpha)
        v=1+0j
    else:
        target=3+2*math.cos(2*math.pi/N)
        u=cmath.exp(1j*(math.pi/2+math.pi/N))
        v=cmath.exp(2j*math.pi/N)
    got=peak(N,u,v)
    err=abs(got-target)
    max_err=max(max_err,err)
    assert err<TOL,(N,got,target,err)
    checks+=1

    # Deterministic rotations check the endpoint-balancing reduction.
    for frac in (0.0,0.17,0.41,0.73,1.0):
        theta=(math.pi/N)*frac
        vals=[math.cos(theta+2*math.pi*k/N) for k in range(N)]
        p=max(vals); r=-min(vals)
        c=r-p
        red=max(1+4*c*x+4*x*x for x in vals)
        target_red=1+4*p*r
        err=abs(red-target_red)
        max_err=max(max_err,err)
        assert err<TOL,(N,frac,red,target_red,err)
        assert -1-TOL <= c <= 1+TOL
        checks+=1

    # Geometry of the minimizing rotation.
    if N%2:
        theta=0.0
        vals=[math.cos(theta+2*math.pi*k/N) for k in range(N)]
        prod=max(vals)*(-min(vals))
        target_prod=math.cos(math.pi/N)
    else:
        theta=math.pi/N
        vals=[math.cos(theta+2*math.pi*k/N) for k in range(N)]
        prod=max(vals)*(-min(vals))
        target_prod=math.cos(math.pi/N)**2
    err=abs(prod-target_prod)
    max_err=max(max_err,err)
    assert err<TOL,(N,prod,target_prod,err)
    checks+=1

print(f"VERIFY_OK N_max=1200 checks={checks} max_error={max_err:.3e}")
