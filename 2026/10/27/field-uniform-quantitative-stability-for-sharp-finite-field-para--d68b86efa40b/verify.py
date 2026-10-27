"""Standalone finite-field checks for the quadratic phase/amplitude stability formulas.

Usage: python verify.py
Only the Python standard library is required. Finite computations do not
substitute for the all-field analytical argument.
"""
import cmath
import math


def finite_field(q):
    if q == 25:
        # F_25 = F_5[w]/(w*w-2); 2 is a nonsquare in F_5.
        def add(x, y):
            return ((x % 5 + y % 5) % 5) + 5 * ((x // 5 + y // 5) % 5)
        def mul(x, y):
            a, b, c, d = x % 5, x // 5, y % 5, y // 5
            return ((a*c + 2*b*d) % 5) + 5*((a*d + b*c) % 5)
        def tr(x):
            return (2 * (x % 5)) % 5
        return range(q), add, mul, lambda z: cmath.exp(2j*math.pi*tr(z)/5)
    p = q
    return range(q), lambda x,y:(x+y)%p, lambda x,y:(x*y)%p, lambda z:cmath.exp(2j*math.pi*z/p)


def check(q):
    F, add, mul, psi = finite_field(q)
    elems = list(F)
    rows = []
    for X in elems:
        for Y in elems:
            row = [psi(add(mul(X, t), mul(Y, mul(t, t))))/q for t in elems]
            rows.append((X, Y, row))
    C = 1+1/q-1/q**2
    F0 = [sum(row) for X,Y,row in rows]
    M0 = sum(abs(x)**6 for x in F0)
    assert abs(M0-C) < 3e-9, (q, M0, C)
    assertions = 1
    for (X,Y,row), a in zip(rows, F0):
        if Y:
            assert abs(abs(a)**2-1/q) < 1e-10
        else:
            assert abs(a-(1 if X == 0 else 0)) < 1e-10
        assertions += 1
    base_r = [((t*7+3) % 11)-5 for t in elems]
    base_i = [((t*3+1) % 7)-3 for t in elems]
    mean_r = sum(base_r)/q
    mean_i = sum(base_i)/q
    directions = [[complex(t-mean_r) for t in base_r],
                  [1j*(t-mean_i) for t in base_i],
                  [complex(t-mean_r,t2-mean_i) for t,t2 in zip(base_r,base_i)]]
    for h in directions:
        N = sum(abs(z)**2 for z in h)/q
        hu = sum(z.real*z.real for z in h)/q
        hv = sum(z.imag*z.imag for z in h)/q
        assert abs(sum(h)) < 1e-9
        H = [sum(w*z for w,z in zip(row,h)) for X,Y,row in rows]
        coeff_M = sum(9*abs(b)**4*abs(a)**2 +
                      6*(abs(b)**2*complex(b).conjugate()**2*a*a).real
                      for b,a in zip(F0,H))
        predicted_M = 9*(q-1)/q**2*N -6/q**2*(sum(z*z for z in h)/q).real
        assert abs(coeff_M-predicted_M) < 2e-8*max(1,N)
        coeff_D = 3*C*N-coeff_M
        predicted_D=(3-6/q+12/q**2)*hu+(3-6/q)*hv
        assert abs(coeff_D-predicted_D) < 2e-8*max(1,N)
        assertions += 3
        if N < 1e-14:
            continue
        small = [(1/128)*z/math.sqrt(N) for z in h]
        f = [1+z for z in small]
        M = sum(abs(sum(w*z for w,z in zip(row,f)))**6 for X,Y,row in rows)
        nf = sum(abs(z)**2 for z in f)/q
        D = C*nf**3-M
        r2 = sum(abs(z)**2 for z in small)/q
        lower = 0.5*(3-6/q)*r2
        assert D >= lower-1e-9, (q,D,lower)
        A,B=elems[1],elems[-1]
        chirped=[z*psi(add(mul(A,t),mul(B,mul(t,t)))) for t,z in zip(elems,f)]
        Mc = sum(abs(sum(w*z for w,z in zip(row,chirped)))**6 for X,Y,row in rows)
        assert abs(Mc-M)<5e-8
        assertions += 2
    print(f'field_order={q} checks={assertions} constant={C:.12g} amplitude_curvature={3-6/q+12/q**2:.12g} phase_curvature={3-6/q:.12g} PASS')
    return assertions

if __name__ == '__main__':
    total=sum(check(q) for q in (5,7,11,13,25))
    print(f'ALL_VERIFIED total_checks={total}. Finite tests are not the universal proof.')
