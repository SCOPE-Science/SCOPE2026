"""Standalone checks for the explicit C-approximate Birkhoff asymmetry witnesses.

Numerical experiments support but do not establish the infinite-dimensional proof.
"""
from fractions import Fraction
from math import sqrt, log, isclose

count = 0
exact_ps = [4,9,16,25,36]
for p in exact_ps:
    k = int(sqrt(p))
    assert k*k == p
    t = Fraction(k-1,k)
    # Coordinates of the unnormalized pair (1,t),(-t^(p-1),1).
    # The primal support numerator cancels exactly.
    forward = -t**(p-1)+t**(p-1)
    assert forward == 0
    # Both normalized vectors have p-th norm power 1.
    Ap_p = 1+t**p
    Bp_p = 1+t**(p*(p-1))
    assert Ap_p > 1 and Bp_p > 1
    # Exact p-th power of the reversed normalized support evaluation.
    numerator = (t-t**((p-1)**2))**p
    denominator = Ap_p*(Bp_p**(p-1))
    assert 0 < numerator < denominator
    ratio_pth = numerator/denominator
    rr = float(ratio_pth)**(1/p)
    assert 0 < rr < 1
    # Compare against independently evaluated norming-functional coordinates.
    tt=float(t)
    A=float(Ap_p)**(1/p)
    B=float(Bp_p)**(1/p)
    v_r = (tt - tt**((p-1)**2))/(A*B**(p-1))
    assert isclose(rr,v_r,rel_tol=5e-13,abs_tol=5e-13)
    # Check Birkhoff annihilation in both the primal and dual orientations.
    ju = (A**(1-p), tt**(p-1)*A**(1-p))
    jv = (-tt**((p-1)**2)*B**(1-p), B**(1-p))
    u = (1/A,tt/A)
    v = (-tt**(p-1)/B,1/B)
    assert isclose(ju[0]*v[0]+ju[1]*v[1],0,abs_tol=1e-11)
    assert isclose(jv[0]*u[0]+jv[1]*u[1],v_r,rel_tol=1e-12)
    count+=1

asymptotic_ps = [9,25,100,400,1600,6400]
for p in asymptotic_ps:
    t = 1-1/sqrt(p)
    a = (1+t**p)**(1/p)
    bpower = (1+t**(p*(p-1)))**((p-1)/p)
    r = (t-t**((p-1)**2))/(a*bpower)
    assert 0 < r < 1
    assert abs(r-t) < 0.02
    count+=1
    if p>=1600:
        assert abs(sqrt(p)*(1-r)-1)<0.00001

# Two-coordinate primal and dual norms admit uniform Hilbert comparison.
for p in [3,4,5,8,20,100]:
    for x in [(-2,1),(1,1),(0,1),(2,3),(-1,-4)]:
        normp=(abs(x[0])**p+abs(x[1])**p)**(1/p)
        norm2=(x[0]*x[0]+x[1]*x[1])**0.5
        assert normp <= norm2+1e-10
        assert norm2 <= sqrt(2)*normp+1e-10
        count+=1
print(f'VERIFY_OK exact_witnesses={len(exact_ps)} asymptotic_witnesses={len(asymptotic_ps)} total_checks={count} duality=analytic')
