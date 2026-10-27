from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from math import prod

PREC = 80
PRIMES = (2, 3, 5, 7, 11, 13, 17)
N_BOUND = 52_000_000_000
N0 = 367_567_200
A0 = (5, 3, 2, 1, 1, 1, 1)
GAMMA_BRACKET_LO = Decimal('0.5772156648')
GAMMA_BRACKET_HI = Decimal('0.5772156650')
D_LO = Decimal('0.1690')
D_CUT = Decimal('0.1691')

def next_down(x):
    with localcontext() as c:
        c.prec = PREC
        return x.next_minus(c)

def next_up(x):
    with localcontext() as c:
        c.prec = PREC
        return x.next_plus(c)

def ln_lo(x):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_HALF_EVEN
        y = x.ln()
        return y.next_minus(c)

def ln_hi(x):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_HALF_EVEN
        y = x.ln()
        return y.next_plus(c)

def exp_lo(x):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_HALF_EVEN
        y = x.exp()
        return y.next_minus(c)

def exp_hi(x):
    with localcontext() as c:
        c.prec = PREC
        c.rounding = ROUND_HALF_EVEN
        y = x.exp()
        return y.next_plus(c)

def triple_log_bounds(n):
    # Monotone interval evaluation of ln(ln(ln(n))).
    x = Decimal(n)
    l1 = (ln_lo(x), ln_hi(x))
    l2 = (ln_lo(l1[0]), ln_hi(l1[1]))
    l3 = (ln_lo(l2[0]), ln_hi(l2[1]))
    assert l3[0] > 0
    return l3

def p7_bound(x, rounding):
    # P_7(x) = sum_{j=0}^7 x^j/j!, with positive x.
    with localcontext() as c:
        c.prec = PREC
        c.rounding = rounding
        total = Decimal(1)
        term = Decimal(1)
        for j in range(1, 8):
            term = (term * x) / Decimal(j)
            total = total + term
        return total

def gamma_bounds():
    # Euler--Maclaurin: H_N-ln(N)-1/(2N)+1/(12N^2)-1/(120N^4) < gamma
    # < H_N-ln(N)-1/(2N)+1/(12N^2), for N=10000.
    N = 10_000
    hlo = Decimal(0); hhi = Decimal(0)
    for k in range(1, N + 1):
        with localcontext() as c:
            c.prec = PREC; c.rounding = ROUND_FLOOR
            hlo = hlo + (Decimal(1) / Decimal(k))
        with localcontext() as c:
            c.prec = PREC; c.rounding = ROUND_CEILING
            hhi = hhi + (Decimal(1) / Decimal(k))
    llo, lhi = ln_lo(Decimal(N)), ln_hi(Decimal(N))
    r1lo, r1hi = frac_bounds(Fraction(1, 2*N))
    r2lo, r2hi = frac_bounds(Fraction(1, 12*N*N))
    r4lo, r4hi = frac_bounds(Fraction(1, 120*N**4))
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_FLOOR
        glo = hlo - lhi - r1hi + r2lo - r4hi
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_CEILING
        ghi = hhi - llo - r1lo + r2hi
    assert glo > GAMMA_BRACKET_LO and ghi < GAMMA_BRACKET_HI
    return glo, ghi

def e_gamma_bounds():
    glo, ghi = gamma_bounds()
    return exp_lo(glo), exp_hi(ghi)


def c_bounds(n):
    tlo, thi = triple_log_bounds(n)
    plo = p7_bound(tlo, ROUND_FLOOR)
    phi = p7_bound(thi, ROUND_CEILING)
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_FLOOR
        lo = EG_LO * plo
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_CEILING
        hi = EG_HI * phi
    return lo, hi

def sigma_ratio(exps):
    r = Fraction(1, 1)
    for p, a in zip(PRIMES, exps):
        r *= Fraction(p**(a+1)-1, p**a*(p-1))
    return r

def frac_bounds(r):
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_FLOOR
        lo = Decimal(r.numerator) / Decimal(r.denominator)
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_CEILING
        hi = Decimal(r.numerator) / Decimal(r.denominator)
    return lo, hi

EG_LO, EG_HI = e_gamma_bounds()

def gap_bounds(n, exps):
    clo, chi = c_bounds(n)
    rlo, rhi = frac_bounds(sigma_ratio(exps))
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_FLOOR
        lo = clo - rhi
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_CEILING
        hi = chi - rlo
    return lo, hi

def enumerate_tuples():
    out = []
    def rec(i, n, exps):
        if i == len(PRIMES):
            out.append((n, tuple(exps)))
            return
        p = PRIMES[i]
        v, a = p, 1
        while n * v <= N_BOUND:
            rec(i+1, n*v, exps+[a])
            v *= p; a += 1
    rec(0, 1, [])
    return out

def main():
    tuples = enumerate_tuples()
    assert len(tuples) == 2596
    n0 = prod(p**a for p, a in zip(PRIMES, A0))
    assert n0 == N0
    # Candidate margin is rigorously enclosed in (0.1690, 0.1691).
    lo0, hi0 = gap_bounds(N0, A0)
    assert lo0 > D_LO and hi0 < D_CUT, (lo0, hi0)
    # The cutoff beats the universal divisor-ratio bound by a positive margin.
    r7 = Fraction(1, 1)
    for p in PRIMES:
        r7 *= Fraction(p, p-1)
    _, r7_hi = frac_bounds(r7)
    cb_lo, _ = c_bounds(N_BOUND)
    with localcontext() as c:
        c.prec = PREC; c.rounding = ROUND_CEILING
        target = r7_hi + D_CUT
    assert cb_lo > target, (cb_lo, target)
    # Every other first-seven-prime exponent tuple below the cutoff has larger gap.
    checked = 0
    for n, exps in tuples:
        if n == N0 and exps == A0:
            continue
        lo, hi = gap_bounds(n, exps)
        if not lo > D_CUT:
            raise AssertionError((n, exps, lo, hi))
        checked += 1
    print('PASS')
    print('tuples=', len(tuples), 'nonminimizers=', checked)
    print('candidate=', N0, 'exponents=', A0)
    print('sigma_ratio_n0=', sigma_ratio(A0))
    print('gamma_interval=', gamma_bounds())
    print('gap_interval=', lo0, hi0)
    print('cutoff_C_lower=', cb_lo)
    print('cutoff_target_upper=', target)
    print('R7=', r7)

if __name__ == '__main__':
    main()
