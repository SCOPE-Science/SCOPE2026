"""Stand-alone exact-arithmetic checks for the quadratic random-map correlation theorem.

Run: python3 verify.py.  All arithmetic is rational; numerical experiments are not
used as evidence for the infinite-parameter uniqueness and optimization proof.
"""
from fractions import Fraction as F


def add(a, b):
    n = max(len(a), len(b))
    return [ (a[i] if i < len(a) else F(0)) +
             (b[i] if i < len(b) else F(0)) for i in range(n)]


def neg(a):
    return [-x for x in a]


def mul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def scale(a, c):
    return [c*x for x in a]


def integ(a, lo, hi):
    return sum((c * (hi**(i+1)-lo**(i+1)) / F(i+1)
                for i, c in enumerate(a)), F(0))


def ev(a, x):
    return sum((c*x**i for i, c in enumerate(a)), F(0))


def checks_for_parameters(b1, b2):
    assert 0 < b1 < 2 < b2 < 4
    k1 = (b2-F(2)) / (2*(b2-b1))
    k2 = (F(2)-b1) / (2*(b2-b1))
    f1 = [F(0), b1, F(4)-2*b1]
    f2 = [F(0), b2, F(4)-2*b2]
    r1 = [b1, 2*(F(4)-2*b1)]
    r2 = [b2, 2*(F(4)-2*b2)]
    S = scale(r1, 2*k1)
    assert add(scale(r1,k1),scale(r2,k2)) == [F(1),F(0)]
    assert k1+k2 == F(1,2)
    assert ev(f1,F(0)) == ev(f2,F(0)) == 0
    assert ev(f1,F(1,2)) == ev(f2,F(1,2)) == 1
    assert 0 < ev(S,F(0)) < 2 and 0 < ev(S,F(1,2)) < 2
    for u in (F(1,17),F(1,9),F(2,7),F(3,7)):
        assert 0 < u < F(1,2)
        assert ev(f2,u) > ev(f1,u)
        assert ev(S,u)/ev(r1,u) == 2*k1
        assert (2-ev(S,u))/ev(r2,u) == 2*k2
    return f1,f2,S,k1,k2


def canonical_bounds():
    b1,b2 = F(1,2),F(7,2)
    f1,f2,S,k1,k2 = checks_for_parameters(b1,b2)
    assert S == [F(1,4),F(3)]
    fdelta = add(f2,neg(f1))
    b = add(mul([F(1,2),F(2)],f2),
            neg(mul([F(0),F(1)],mul(S,fdelta))))
    # For the lower bound, h is as large as allowed; for the upper bound,
    # h is as small as allowed.  h means p(u+1/2).
    q = F(1,4)
    hmin_left, hmin_right = [F(0)], add(S,[F(-1)])
    hmax_left, hmax_right = S, [F(1)]
    term = scale(fdelta,F(-1,2))
    def cov(hleft,hright):
        return (integ(b,F(0),F(1,2))+
                integ(mul(term,hleft),F(0),q)+
                integ(mul(term,hright),q,F(1,2)) -F(1,4))
    lower = cov(hmax_left,hmax_right)
    upper = cov(hmin_left,hmin_right)
    assert lower == F(223,15360), (lower,'expected 223/15360')
    assert upper == F(913,15360), (upper,'expected 913/15360')
    assert upper-lower == F(23,512)
    symmetric = cov(scale(S,F(1,2)),scale(S,F(1,2)))
    assert symmetric == F(71,1920)
    for v in (lower,symmetric,upper):
        assert v > 0
    # Bounds really are feasible pointwise on both half-intervals.
    for u in [F(i,100) for i in range(1,50)]:
        s=ev(S,u)
        for h in (max(F(0),s-1), min(F(1),s)):
            assert F(0)<=h<=F(1) and F(0)<=s-h<=F(1)
    return lower,upper


def main():
    for a,b in ((F(1,2),F(7,2)), (F(1),F(3)),
                (F(3,2),F(5,2)), (F(1,4),F(9,4)),
                (F(19,10),F(21,10)), (F(1,10),F(39,10))):
        checks_for_parameters(a,b)
    lower,upper=canonical_bounds()
    print('SHARP_COVARIANCE_INTERVAL',str(lower),str(upper))
    print('VERIFY_OK')


if __name__=='__main__':
    main()
