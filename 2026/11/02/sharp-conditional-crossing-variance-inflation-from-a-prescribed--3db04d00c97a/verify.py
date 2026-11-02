"""Exact finite checks of conditional crossing-moment identities in random chord diagrams.

Run with Python 3 standard library: python verify.py. No external files required.
Finite enumeration checks examples, not an infinite proof.
"""
from fractions import Fraction as F
from functools import lru_cache


def all_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for i in range(1, len(vertices)):
        second = vertices[i]
        remaining = vertices[1:i] + vertices[i+1:]
        for rest in all_matchings(remaining):
            yield ((first, second),) + rest


def crossing(p, q):
    a, b = p
    c, d = q
    return (a < c < b < d) or (c < a < d < b)


def total_crossing(pairs):
    return sum(crossing(pairs[i], pairs[j])
               for i in range(len(pairs)) for j in range(i + 1, len(pairs)))


def base_var(m):
    return F(m * (m - 1) * (m + 3), 45)


def base_mean(m):
    return F(m * (m - 1), 6)


def identity(n, a):
    M = 2*n-2
    b = M-a
    mean = base_mean(n-1) + F(a*b, M-1)
    rise = F(a*b*(a-1)*(b-1)*(M+5), 3*(M-3)*(M-1)**2)
    var = base_var(n-1) + rise
    cov = F(a*b*(a-1)*(b-1), 6*(M-3)*(M-1))
    var_y = F(2*a*b*(a-1)*(b-1), (M-3)*(M-1)**2)
    return mean,var,cov,var_y


def verify():
    checks = 0
    cases = 0
    for n in range(3, 8):
        M = 2*n-2
        all_others = list(all_matchings(tuple(range(1, M+1))))
        for a in range(M+1):
            fixed = (0, a+1)
            rest_pts = [i for i in range(2*n) if i not in fixed]
            sample = all_matchings(rest_pts)
            sX = sY = sC = sXX = sYY = sCC = sXY = 0
            count = 0
            for rest in sample:
                X = total_crossing(rest)
                Y = sum(crossing(fixed, q) for q in rest)
                C = X + Y
                sX+=X; sY+=Y; sC+=C
                sXX+=X*X; sYY+=Y*Y; sCC+=C*C; sXY+=X*Y
                count+=1
            exp = count
            assert exp == len(all_others)
            cases += count
            mean = F(sC,count)
            var = F(sCC,count) - mean**2
            cov = F(sXY,count)-F(sX,count)*F(sY,count)
            vY = F(sYY,count)-F(sY,count)**2
            target_mean,target_var,target_cov,target_vY = identity(n,a)
            assert mean == target_mean, (n,a,'mean',mean,target_mean)
            assert var == target_var, (n,a,'var',var,target_var)
            assert cov == target_cov, (n,a,'cov',cov,target_cov)
            assert vY == target_vY, (n,a,'varY',vY,target_vY)
            checks += 4
        # Conditional moment law is a distributional identity for fixed chord.
    for m in range(1,8):
        sum_ = sq = ct = 0
        for pairs in all_matchings(range(2*m)):
            v = total_crossing(pairs)
            sum_ += v
            sq += v*v
            ct += 1
        mu=F(sum_,ct)
        var=F(sq,ct)-mu*mu
        assert mu == base_mean(m), (m,'unconditional mean',mu)
        assert var == base_var(m), (m,'unconditional variance',var)
        checks += 2
        cases += ct
    print(f'PASS: {checks} exact assertions, {cases} enumerated matching instances, n=3..7 conditional, m=1..7 unconditional.')

if __name__ == '__main__':
    verify()
