#!/usr/bin/env python3
import cmath, math

TOL=2e-8
NMAX=300

def coeffs_from_roots(roots):
    r1,r2,r3=roots
    # ascending coefficients of (z-r1)(z-r2)(z-r3)
    return [-r1*r2*r3, r1*r2+r1*r3+r2*r3, -(r1+r2+r3), 1+0j]

def value(c,z):
    return c[0]+c[1]*z+c[2]*z*z+c[3]*z*z*z

def grid_zero_count(c,N):
    return sum(abs(value(c,cmath.exp(2j*math.pi*k/N))) < TOL for k in range(N))

def check_case(N,roots,expected):
    c=coeffs_from_roots(roots)
    err=max(abs(abs(x)-1.0) for x in c)
    if err>1e-10:
        raise AssertionError((N,expected,'coefficient modulus',err,c))
    got=grid_zero_count(c,N)
    if got!=expected:
        raise AssertionError((N,expected,got,roots))
    return err

checks=0
maxerr=0.0
for N in range(4,NMAX+1):
    zeta=cmath.exp(2j*math.pi/N)
    t=cmath.exp(1j*math.sqrt(2.0))
    s=cmath.exp(1j*math.sqrt(3.0))
    # zero sampled roots
    maxerr=max(maxerr,check_case(N,(t,-t,s),0)); checks+=1
    # one sampled root
    maxerr=max(maxerr,check_case(N,(t,-t,1+0j),1)); checks+=1
    if N%2:
        # exactly two: 1 and zeta are sampled, -1 is not
        maxerr=max(maxerr,check_case(N,(1+0j,-1+0j,zeta),2)); checks+=1
    else:
        # exactly two: antipodal sampled pair, third nonsampled
        maxerr=max(maxerr,check_case(N,(1+0j,-1+0j,t),2)); checks+=1
        # exactly three sampled roots
        maxerr=max(maxerr,check_case(N,(1+0j,-1+0j,zeta),3)); checks+=1

# Directly check the algebraic trigonometric identity on a deterministic mesh.
for ia in range(101):
    a=2*math.pi*ia/101
    for ib in range(103):
        b=2*math.pi*ib/103
        lhs=1+math.cos(a)+math.cos(b)+math.cos(a-b)
        s0=(a+b)/2
        d=(a-b)/2
        rhs=2*math.cos(d)*(math.cos(s0)+math.cos(d))
        if abs(lhs-rhs)>2e-12:
            raise AssertionError(('identity',a,b,lhs,rhs))

print(f'VERIFY_OK N_max={NMAX} witness_checks={checks} max_coeff_modulus_error={maxerr:.3e}')
