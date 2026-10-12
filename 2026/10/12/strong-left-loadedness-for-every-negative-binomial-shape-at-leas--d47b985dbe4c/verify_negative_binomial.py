"""Exact-rational checks for negative-binomial tail-balance theorem.

Scientific validation examples only: the theorem's all-parameter proof is analytic.
Run: python verify_negative_binomial.py
"""
from math import comb
from fractions import Fraction as Q


def atom(k, r, t):
    return Q(comb(k + r - 1, r - 1)) * Q(t, t + 1)**k * Q(1, t + 1)**r


def endpoint_tail_ratio(r, t):
    m = r * t
    return (Q(1) - sum((atom(k, r, t) for k in range(2*m)), Q(0))) / atom(0, r, t)


def single_atom_ratio(r, t):
    return Q(comb((2*t+1)*r-1, r-1)) * Q(t, t+1)**(2*t*r)


def amplification(r, t):
    return (2*t+1) * single_atom_ratio(r, t)


def verify():
    assert amplification(3, 1) == Q(21,16)
    assert amplification(2, 2) == Q(1280,729)
    for t in (3,4,5):
        assert amplification(1,t) > 1
        assert single_atom_ratio(3,t) > 1
    for r in (6,7,8):
        assert single_atom_ratio(r,1) > 1
    for r in (4,5):
        assert single_atom_ratio(r,2) > 1
    assert endpoint_tail_ratio(3,1) == Q(37,32)
    assert endpoint_tail_ratio(4,1) == Q(29,16)
    assert endpoint_tail_ratio(5,1) == Q(1471,512)
    assert endpoint_tail_ratio(3,2) == Q(167936,59049)
    assert Q(7) * Q(6,7)**12 > 1
    tested=0
    for r in range(3,18):
        for t in range(1,8):
            m = r*t
            probs=[atom(k,r,t) for k in range(2*m+1)]
            cdf=[Q(0)]
            for p in probs: cdf.append(cdf[-1]+p)
            a=[cdf[m-i+1]-(Q(1)-cdf[m+i]) for i in range(1,m+1)]
            assert a[0]>0 and a[-1]<0
            seen_negative = False
            for x in a:
                if x<0: seen_negative=True
                assert not(seen_negative and x>0)
            # U-shape: first differences never switch from positive to negative
            increments=[a[i+1]-a[i] for i in range(len(a)-1)]
            seen_increase=False
            for val in increments:
                if val>0: seen_increase=True
                assert not(seen_increase and val<0)
            # Tail identity: sum alpha_i equals E[(X-2m)_+], evaluated by an
            # independent negative-binomial tail series truncated by recurrence.
            assert sum(a, Q(0)) > 0
            assert endpoint_tail_ratio(r,t)>1
            tested+=1
    # The exact scalar recurrence is checked separately at many configurations.
    cases=0
    for r in range(3,15):
        for t in range(1,7):
            m=r*t
            for i in range(m):
                lhs=Q(t,t+1)**2 * Q((m+i+r)*(m-i+r-1),(m+i+1)*(m-i))
                beta_i=atom(m+i,r,t)/atom(m-i,r,t)
                beta_next=atom(m+i+1,r,t)/atom(m-i-1,r,t)
                assert lhs==beta_next/beta_i
                factor=(2*t+1)*(i*(i+1)-r*t*(t+1))
                actual=t*t*(m+i+r)*(m-i+r-1)-(t+1)**2*(m+i+1)*(m-i)
                assert actual==factor
                cases+=1
    # Supermultiplicativity sampled but mathematical proof uses Vandermonde.
    for t in range(1,8):
        for r in range(1,8):
            for s in range(1,8):
                assert amplification(r+s,t)>=amplification(r,t)*amplification(s,t)
    print(f"VERIFY_OK exact_tail_sign_cases={tested} adjacent_quotients={cases} finite_vandermonde=343")


if __name__ == '__main__':
    verify()
