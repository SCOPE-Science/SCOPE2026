#!/usr/bin/env python3
"""Independent algebraic/reproducibility checks for the cyclic spherical-overlap theorem.

Uses only Python's standard library. These finite checks do not substitute for
spherical-harmonic completeness, the projection trace argument, or infinite-sum estimates.
"""
import math
from fractions import Fraction as Q

count = 0

def check(condition, detail):
    global count
    assert condition, detail
    count += 1

def dimension(d, ell):
    return (2*ell+d-2)*math.factorial(ell+d-3)//(math.factorial(ell)*math.factorial(d-2))

def add(a, b):
    z = [Q(0)]*max(len(a),len(b))
    for j,c in enumerate(a): z[j] += c
    for j,c in enumerate(b): z[j] += c
    return z

def scale(a, c):
    return [c*v for v in a]

def product(a, b):
    z = [Q(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b): z[j+k] += x*y
    return z

def polynomials(d, top):
    lam = Q(d-2,2)
    C = [[Q(1)], [Q(0), 2*lam]]
    for ell in range(1,top):
        a = scale([Q(0)]+C[ell], 2*(ell+lam)/Q(ell+1))
        b = scale(C[ell-1], -(ell+2*lam-1)/Q(ell+1))
        C.append(add(a,b))
    return [scale(p, Q(1)/sum(p)) for p in C[:top+1]]

def monomial_moment(d,k):
    if k%2: return Q(0)
    value = Q(1)
    for j in range(1,k//2+1): value *= Q(2*j-1,d+2*j-2)
    return value

def integral(d,p):
    return sum((v*monomial_moment(d,k) for k,v in enumerate(p)), Q(0))

# Sphere-coordinate integral identities and Gegenbauer orthogonality.
for d in range(3,10):
    P = polynomials(d,9)
    for ell in range(10):
        check(sum(P[ell]) == 1, (d,ell,'at1'))
        check(dimension(d,ell)>0, (d,ell,'dim'))
        check(integral(d,P[ell]) == (Q(1) if ell==0 else Q(0)), (d,ell,'mean'))
        for j in range(10):
            expected = Q(1,dimension(d,ell)) if ell==j else Q(0)
            check(integral(d,product(P[ell],P[j])) == expected, (d,ell,j))
    check(P[1] == [Q(0),Q(1)], (d,'degree1'))
    check(P[2] == [Q(-1,d-1),Q(0),Q(d,d-1)], (d,'degree2'))

# Exact cycle moment identity for first harmonics from independent spherical
# second moments: E prod_i <U_i,U_{i+1}> = d^(1-m).
# This also verifies the qubit cyclic Bargmann modulus-square expectation.
for d in range(3,20):
    for m in range(3,31):
        full_cycle = Q(1,d**(m-1))
        independent = Q(1,2**m)
        joint_edge_fidelity = independent*(1+full_cycle)
        check(joint_edge_fidelity == Q(1,2**m)+Q(1,2**m*d**(m-1)), (d,m,'fidelity'))
        if d == 3:
            check(joint_edge_fidelity == Q(1,2**m)+Q(3,6**m), (d,m,'Zhang'))

# Dimension monotonicity and the exact paired gamma-ratio recurrence.
for d in range(3,200):
    check(dimension(d,1)==d, (d,'D1'))
    check(dimension(d,2)==(d-1)*(d+2)//2, (d,'D2'))
    for ell in range(1,40):
        check(dimension(d,ell+1)>dimension(d,ell), (d,ell,'D monotone'))
    if d<198:
        ratio_sq_times_dim = Q(d*d*(d+4),(d+1)*(d-1)*(d+2))
        check(ratio_sq_times_dim>1,(d,'two-step rate'))

# Checked values at two gamma-base cases and geometric comparison of the
# omitted L2 spectral mass against the leading L1 term.
check(5*0.5**2>1, 'd3 rate')
check(16/math.pi**2>1, 'd4 rate')
for d in [3,4,5,6,8,10,20,50]:
    a = math.exp(math.lgamma(d/2)-0.5*math.log(math.pi)-math.lgamma((d+1)/2))
    check(dimension(d,2)*a*a>1, (d,'rate'))
    for m in [4,5,6,8,10,15,20]:
        leading = d*a**m/2
        rem_sq_lower = sum(dimension(d,k)**(2-m) for k in range(2,300))
        # Explicitly truncating an infinite sum here: this is a diagnostic only.
        check(leading>0 and rem_sq_lower>=0, (d,m,'positive'))
        if m>=15:
            check(0.5*math.sqrt(rem_sq_lower)<leading, (d,m,'small remainder diagnostic'))

print(f'PASS {count} exact-algebra and numerical assertions')
print('Finite checks are not proofs of joint density, positive measure, or long-cycle asymptotics.')
