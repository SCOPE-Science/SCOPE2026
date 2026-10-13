"""Exact-rational checks for isotropic quadratic S-SZD with signed coordinate frames.

The proof's universal-frame statement is algebraic. Finite coordinate-law
checks here verify the specialized transition, moment recurrences and sharp
endpoints; they are not a proof for every frame law.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


def laws(d, ell, mode):
    r = Q(d, ell)
    for subset in combinations(range(d), ell):
        if mode == 'unsigned':
            signs = [(1,) * ell]
        elif mode == 'signed':
            signs = list(product((-1, 1), repeat=ell))
        elif mode == 'globally_biased':
            signs = [(1,) * ell, (-1,) * ell]
        else:
            raise ValueError(mode)
        for sig in signs:
            if mode == 'globally_biased':
                weight = Q(3, 4) if sig[0] == 1 else Q(1, 4)
            else:
                weight = Q(1, len(signs))
            yield subset, sig, weight / comb(d, ell)


def step(y, subset, sig, br):
    out = list(y)
    for i, s in zip(subset, sig):
        out[i] = (1 - br) * out[i] - br * s
    return tuple(out)


def exact_distribution_step(dist, d, ell, beta, mode):
    br = beta * Q(d, ell)
    new = {}
    for y, p in dist.items():
        for subset, sig, weight in laws(d, ell, mode):
            z = step(y, subset, sig, br)
            new[z] = new.get(z, Q(0)) + p * weight
    return new


def moments(dist, d):
    mean = tuple(sum(p * y[i] for y, p in dist.items()) for i in range(d))
    norm2 = sum(p * sum(t * t for t in y) for y, p in dist.items())
    return mean, norm2


def predicted_moments(prev_mean, prev_second, d, ell, beta, mode):
    r = Q(d, ell)
    br = beta * r
    mu = []
    for i in range(d):
        mu.append(sum(wt * sum(s for ii, s in zip(sub, sig) if ii == i)
                      for sub, sig, wt in laws(d, ell, mode)))
    new_mean = tuple((1-beta)*prev_mean[i] - br*mu[i] for i in range(d))
    rho = 1-2*beta+beta*beta*r
    new_second = (rho*prev_second + br*br*ell
                  - 2*br*(1-br)*sum(prev_mean[i]*mu[i] for i in range(d)))
    return new_mean, new_second, sum(t*t for t in mu)*r


def analytic_limit_y(d, ell, beta, q):
    r = Q(d, ell)
    return r*(beta*d + 2*(1-beta*r)*q)/(2-beta*r)


def main():
    tested = 0
    for d in range(1, 5):
        for ell in range(1, d+1):
            r=Q(d, ell)
            for b_ratio in (Q(1, 3), Q(4, 5), Q(1), Q(6, 5), Q(5, 3)):
                beta=b_ratio/r
                assert 0 < beta*r < 2
                for mode in ('unsigned','signed','globally_biased'):
                    if mode == 'globally_biased' and ell>2:
                        continue
                    dist={tuple(Q(1, i+2) for i in range(d)): Q(1)}
                    mean,second=moments(dist,d)
                    for k in range(3 if d<=3 else 2):
                        expect_mean,expect_second,q=predicted_moments(mean,second,d,ell,beta,mode)
                        dist=exact_distribution_step(dist,d,ell,beta,mode)
                        mean,second=moments(dist,d)
                        assert mean == expect_mean, (d,ell,beta,mode,k,'mean')
                        assert second == expect_second, (d,ell,beta,mode,k,'MSE')
                        tested += 1
                    if mode == 'unsigned':
                        assert q == ell
                        assert analytic_limit_y(d,ell,beta,q)==d
                    elif mode == 'signed':
                        assert q == 0
                    elif mode == 'globally_biased':
                        assert q == Q(ell,4)
    # The extremum switch, all rational and including equality at the pivot.
    for d in range(1, 20):
        for ell in range(1,d+1):
            r=Q(d,ell)
            for b_ratio in (Q(1,10),Q(1,2),Q(1),Q(3,2),Q(19,10)):
                beta=b_ratio/r
                low=analytic_limit_y(d,ell,beta,Q(0))
                high=analytic_limit_y(d,ell,beta,Q(ell))
                assert (low < high) == (b_ratio < 1)
                assert (low == high) == (b_ratio == 1)
                assert high == d
                tested+=1
    print('PASS: %d exact-rational transition, moment and endpoint checks' % tested)
    for beta in (Q(1,4), Q(3,4)):
        d,ell=4,2
        r=Q(d,ell)
        signed=analytic_limit_y(d,ell,beta,Q(0))*r/4
        unsigned=analytic_limit_y(d,ell,beta,Q(ell))*r/4
        print('d=4, ell=2, h=1, lambda=1, alpha=%s: signed MSE=%s, unsigned MSE=%s'
              % (beta,signed,unsigned))

if __name__=='__main__':
    main()
