"""Standalone checks for expected distinct unbordered scattered subsequences."""
from fractions import Fraction as F
from itertools import product
from math import isclose


def unbordered(word):
    return bool(word) and all(word[:k] != word[-k:] for k in range(1, len(word)))


def convolution(a, b, n):
    out = [F(0)] * (n + 1)
    for i, ai in enumerate(a[:n+1]):
        if ai:
            for j, bj in enumerate(b[:n+1-i]):
                if bj: out[i+j] += ai*bj
    return out


def unbordered_series(alphabet_series, n):
    """Series U(x)=sum_{nonempty unbordered v}prod_i x_{v_i}, truncated."""
    total = [sum(a[k] for a in alphabet_series) for k in range(n+1)]
    if not any(total[1:]):
        return [F(0)] * (n+1)
    squared = [convolution(a,a,n) for a in alphabet_series]
    correction = unbordered_series(squared,n)
    # (1-total)*answer = total-correction; coefficient division by 1-total
    assert total[0] == 0
    ans = [F(0)] * (n+1)
    for k in range(1,n+1):
        ans[k] = total[k]-correction[k] + sum(total[j]*ans[k-j] for j in range(1,k+1))
    return ans


def expectation_gf(prob,n):
    g = [[F(0)]+[p*(1-p)**(k-1) for k in range(1,n+1)] for p in prob]
    a = unbordered_series(g,n)
    return [sum(a[:k+1]) for k in range(n+1)],g,a


def exhaustive_expected(prob,n):
    q=len(prob)
    sums=[F(0)]*(n+1)
    count=0
    for length in range(n+1):
        for letters in product(range(q), repeat=length):
            weight=F(1)
            seen={()}
            for c in letters:
                weight*=prob[c]
                seen|={s+(c,) for s in tuple(seen)}
            cnt=sum(unbordered(s) for s in seen)
            sums[length] += weight*cnt
            count += 1
    return sums,count


def direct_pattern_gf(g,n):
    q=len(g)
    ans=[F(0)]*(n+1)
    for k in range(1,n+1):
        for pattern in product(range(q),repeat=k):
            if unbordered(pattern):
                poly=[F(1)]+[F(0)]*n
                for a in pattern:
                    poly=convolution(poly,g[a],n)
                for j in range(1,n+1):ans[j]+=poly[j]
    return ans


def density(prob,depth=12):
    """Recursively evaluate A(v_1^2,...,v_q^2) with rigorous tail bound."""
    # A(x)=(s-A(x squared))/(1-s), x_i are nonnegative constants, s<1.
    x=[p*p for p in prob]
    levels=[]
    for _ in range(depth):
        s=sum(x)
        levels.append(s)
        x=[y*y for y in x]
    ans=F(0)
    for s in reversed(levels):
        ans=(s-ans)/(1-s)
    # Actual tail error uses sum x^{2^depth}/(1-s), extraordinarily small here.
    return float(1-ans)


def run():
    cases=[([F(1,2),F(1,2)],10),([F(1,3),F(2,3)],10),
           ([F(1,10),F(9,10)],9),([F(1,3)]*3,8),
           ([F(1,2),F(1,3),F(1,6)],8),
           ([F(1,2),F(1,4),F(1,8),F(1,8)],6)]
    total=0
    for p,n in cases:
        gf,g,a=expectation_gf(p,n)
        brute,words=exhaustive_expected(p,n)
        assert gf==brute,('word expectation mismatch',p,n,gf,brute)
        direct=direct_pattern_gf(g,n)
        assert direct==a,('weighted border recurrence mismatch',p,n)
        total+=words
    th=density([F(1,2),F(1,2)],depth=13)
    assert abs(th-0.26778684021788911238)<1e-14,th
    th3=density([F(1,3)]*3,depth=13)
    assert 0.55<th3<0.56
    print(f'VERIFY_OK exact_source_words={total} rational_sources={len(cases)} full_weighted_pattern_check=TRUE fair_binary_unbordered_limit={th:.16f} fair_ternary_limit={th3:.12f}')


if __name__=='__main__':run()
