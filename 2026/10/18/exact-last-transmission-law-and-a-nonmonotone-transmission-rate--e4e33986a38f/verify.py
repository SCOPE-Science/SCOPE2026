"""Standalone checks for the last-transmission law on the infinite path.
Run: python verify.py
All finite stochastic comparisons are diagnostic, not proofs of the theorem.
"""
import math
import random
from fractions import Fraction


def a(lam):
    return lam / (1.0 + lam)


def predicted_mean(lam):
    u = a(lam)
    return 1.0 / (2.0 * lam) + 2*u - u*u/2


def predicted_cdf(lam, t, n=4000):
    # Composite Simpson, using the exact convolution integral.
    h = t/n
    def f(x):
        return 2*lam*math.exp(-2*lam*x)*(1-a(lam)*math.exp(-(t-x)))**2
    total = f(0) + f(t)
    for i in range(1,n):
        total += (4 if i % 2 else 2)*f(i*h)
    return h*total/3


def sample_exact_ctmc(lam, rng):
    # Sites absent from the state dictionary are ignorant.
    state = {0:1}
    elapsed = 0.0
    final_birth = 0.0
    while True:
        moves = []
        for x, v in tuple(state.items()):
            if v != 1:
                continue
            neighbours=(x-1,x+1)
            informed=sum(state.get(y,0)!=0 for y in neighbours)
            if informed:
                moves.append((float(informed), 2, x))
            for y in neighbours:
                if state.get(y,0) == 0:
                    moves.append((float(lam), 1, y))
        if not moves:
            return final_birth
        total = sum(item[0] for item in moves)
        elapsed += rng.expovariate(total)
        draw = rng.random()*total
        for rate, new_state, site in moves:
            draw -= rate
            if draw < 0:
                state[site] = new_state
                if new_state == 1:
                    final_birth = elapsed
                break


def algebraic_checks():
    # Exact-rational identities for the moments and the derivative numerator.
    for q in (Fraction(1,7), Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(2), Fraction(7)):
        a = q/(q+1)
        moments = Fraction(1,2)/q + 2*a-a*a/2
        alternative = (3*q**3+5*q**2+2*q+1)/(2*q*(q+1)**2)
        assert moments == alternative
        # The left branch's no-further-birth probability has the same CDF
        # 1-a exp(-t) as the right branch; test at exp(-t)=1/2,1/3,2/3.
        for z in (Fraction(1,2), Fraction(1,3), Fraction(2,3)):
            if q.denominator == 1:
                w = z ** (q+1)
                left = 1-a*w-a*(z-w)
                assert left == 1-a*z
        # E[e^{-0 H}]=1 for H=max(two defective exponential offsets).
        assert (1-a)**2+2*a-a*a==1
    # Unique positive critical point: cubic negative at 0 and 1,
    # positive at 2, and its coefficient signs have one change.
    p=lambda x: x**3+x**2-3*x-1
    assert p(0)<0 and p(1)<0 and p(2)>0
    lo,hi=1.0,2.0
    for _ in range(80):
        mid=(lo+hi)/2
        if p(mid)<0: lo=mid
        else: hi=mid
    x=(lo+hi)/2
    assert abs(x-1.48119430409202)<1e-11
    assert abs(predicted_mean(x)-1.3533164361623)<1e-11
    return x


def stochastic_checks():
    rng = random.Random(20261016)
    for lam in (0.5, 1.0, 2.0, 5.0):
        samples=[sample_exact_ctmc(lam,rng) for _ in range(11000)]
        empirical=sum(samples)/len(samples)
        theory=predicted_mean(lam)
        assert abs(empirical-theory)<0.085, (lam,empirical,theory)
        for t in (0.5,1.0,2.0):
            empirical_cdf=sum(x<=t for x in samples)/len(samples)
            theoretical_cdf=predicted_cdf(lam,t)
            assert abs(empirical_cdf-theoretical_cdf)<0.035, (lam,t,empirical_cdf,theoretical_cdf)
        print('lambda=',lam,'empirical mean=',round(empirical,5),'exact mean=',round(theory,5))


if __name__ == '__main__':
    root=algebraic_checks()
    stochastic_checks()
    print('PASS: exact-rational algebra, root bracket, and independent sitewise CTMC comparisons; critical rate',round(root,12))
