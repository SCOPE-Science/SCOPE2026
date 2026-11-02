"""Exact checks for a row-sampling spectral-error theorem (standard library only)."""
from fractions import Fraction as F
from math import factorial, comb, ceil, floor, exp
from itertools import product

CHECKS = 0

def check(ok, tag=''):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(f'{tag}: check {CHECKS}')


def compositions(total, d):
    if d == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for rest in compositions(total-i, d-1):
                yield (i,) + rest


def exact_error(d, r, counts):
    # Each of the d^2 rows is sampled with probability 1/d^2.
    # Grouped counts are multinomial(r;1/d,...,1/d).
    strong = abs(F(d*counts[0], r) - 1)
    weak = max(abs(F(d*c, r) - 1) for c in counts[1:])/d**2
    return max(strong, weak)


def binomial_success(d, r, eps):
    low = F(r,d)*(1-eps)
    high = F(r,d)*(1+eps)
    lo = -(-low.numerator // low.denominator)
    hi = high.numerator // high.denominator
    return sum(F(comb(r,k)*(d-1)**(r-k), d**r)
               for k in range(max(lo,0), min(hi,r)+1))


for d in range(2, 7):
    n = d*d
    strong = F(d*d)
    gram_trace = d*d+d-1
    stable_rank = F(gram_trace,d*d)
    check(stable_rank == 1+F(d-1,d*d), 'stable rank')
    # Every row is nonzero, and all rows have left leverage score 1/d.
    for j in range(d):
        for k in range(d):
            leverage = F(1,d)
            check(leverage == F(1,d), 'leverage')
            joint_probability = leverage/d
            check(joint_probability == F(1,n), 'joint probability')
    p_heavy = F(d*d, gram_trace)
    if d >= 3:
        eps = F(1,4)
        check(F(d-1,d*d) <= eps, 'weak coordinate bound')
        # One draw succeeds under squared-row-norm sampling iff heavy block chosen.
        good_heavy = max(F(d-1,d*d),F(1,d*d))
        check(good_heavy<=eps,'norm heavy outcome')
        bad_weak = max(F(1),F(gram_trace-1,d*d))
        check(bad_weak>eps,'norm weak outcome')
        check(p_heavy > 1-F(1,d), 'one-sample high probability')
    for r in range(1, min(8,n)):
        for eps in (F(1,4),F(2,5),F(3,4)):
            if not (eps>F(d-1,d*d)):
                continue
            lhs = F(0)
            total_prob=F(0)
            for counts in compositions(r,d):
                ways = factorial(r)
                for c in counts:
                    ways //= factorial(c)  # unsafe successive truncation? factorial quotient divisible per step
                prob = F(ways,d**r)
                total_prob += prob
                success = exact_error(d,r,counts) <= eps
                # condition only depends on the heavy block count.
                predicted = abs(F(d*counts[0],r)-1)<=eps
                check(success == predicted, 'success equivalence')
                if success:
                    lhs+=prob
            check(total_prob==1,'multinomial normalization')
            check(lhs==binomial_success(d,r,eps),'binomial probability')
            alpha=F(r,d)
            attainable=any(F(k,1+eps)<=alpha<=F(k,1-eps) for k in range(1,r+1))
            check((lhs>0)==attainable,'arithmetic feasible bands')

for d in (10,20,40,80):
    eps=F(1,4)
    r_ok=d
    check(binomial_success(d,r_ok,eps)==F(d-1,d)**(d-1),'first window at r=d')
    if d%5==0:
        r_forbidden=7*d//5
        check(F(4,3)<F(r_forbidden,d)<F(8,5),'gap coordinate')
        check(binomial_success(d,r_forbidden,eps)==0,'reentrant gap')
    check(binomial_success(d,1,eps)==0,'first-sample failure')
    check(F(d*d,d*d+d-1)>F(1,2),'norm sampler success')

print(f'PASS {CHECKS} exact-arithmetic checks; no Monte Carlo proof claims.')
