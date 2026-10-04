#!/usr/bin/env python3
import cmath
import math

TOL = 1e-9

def rank_complex(cols, tol=TOL):
    # cols: list of equal-length complex column vectors
    if not cols:
        return 0
    A = [[complex(cols[j][i]) for j in range(len(cols))] for i in range(len(cols[0]))]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = max(range(r, m), key=lambda i: abs(A[i][c]), default=r)
        if abs(A[pivot][c]) <= tol:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = A[r][c]
        for j in range(c, n):
            A[r][j] /= z
        for i in range(m):
            if i == r:
                continue
            z = A[i][c]
            if abs(z) > tol:
                for j in range(c, n):
                    A[i][j] -= z*A[r][j]
        r += 1
        if r == m:
            break
    return r

def project(v):
    a,b=v
    return [a*a.conjugate(), a*b.conjugate(),
            b*a.conjugate(), b*b.conjugate()]

def orbit_projectors(n,k,a,b):
    zeta=cmath.exp(2j*math.pi/n)
    out=[]
    for j in range(n):
        u=(a*zeta**(k*j), b*zeta**(-k*j))
        v=(b*zeta**(-k*j), a*zeta**(k*j))
        out.append(project(u))
        out.append(project(v))
    return out

def irrep_ks(n):
    # Complex two-dimensional irreducibles of D_{2n}, one from each pair k,n-k.
    return range(1,(n-1)//2+1)

passed=0
special=0
for n in range(3,81):
    for k in irrep_ks(n):
        m=n//math.gcd(n,2*k)
        if m < 2:
            raise AssertionError((n,k,m))
        if m > 2:
            good=(1.0,2.0)
            bad_zero=(1.0,0.0)
            bad_equal=(1.0,1.0)
            if rank_complex(orbit_projectors(n,k,*good)) != 4:
                raise AssertionError(("good",n,k,m))
            if rank_complex(orbit_projectors(n,k,*bad_zero)) >= 4:
                raise AssertionError(("bad_zero",n,k,m))
            if rank_complex(orbit_projectors(n,k,*bad_equal)) >= 4:
                raise AssertionError(("bad_equal",n,k,m))
        else:
            special += 1
            good=(1.0,2.0*cmath.exp(1j*math.pi/8))
            bad_real=(1.0,2.0)
            bad_equal=(1.0,cmath.exp(1j*math.pi/8))
            if rank_complex(orbit_projectors(n,k,*good)) != 4:
                raise AssertionError(("good_m2",n,k,m))
            if rank_complex(orbit_projectors(n,k,*bad_real)) >= 4:
                raise AssertionError(("bad_real",n,k,m))
            if rank_complex(orbit_projectors(n,k,*bad_equal)) >= 4:
                raise AssertionError(("bad_equal_m2",n,k,m))
        passed += 1

print(f"VERIFY_OK irreps={passed} m2_cases={special} n_range=3..80")
