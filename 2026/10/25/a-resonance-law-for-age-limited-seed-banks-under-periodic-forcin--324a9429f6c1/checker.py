"""Exact rational checks for periodic age-limited seed-bank identities.

Run with Python 3 (standard library only). The analytical all-size proof is
supplied separately; finite tests here independently reproduce examples.
"""
from fractions import Fraction as F
from itertools import permutations
import json


def mat(l, a, b, r):
    out = [[F(0) for _ in range(l)] for _ in range(l)]
    out[0] = [a * r] * l
    for i in range(1, l):
        out[i][i-1] = b
    return out


def mul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def product(l, a, b, sequence):
    result = eye(l)
    for r in sequence:
        result = mul(result, mat(l, a, b, r))
    return result


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def characteristic(a):
    n = len(a)
    q = eye(n)
    c = [F(1)]
    powers = []
    for _ in range(n):
        q = mul(q, a)
        powers.append(trace(q))
    for k in range(1, n + 1):
        c.append(-sum((c[k-j] * powers[j-1] for j in range(1, k+1)), F(0)) / k)
    return tuple(c)


def vecmul(a, v):
    return [sum((x * y for x,y in zip(row, v)), F(0)) for row in a]


def fmt(q):
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'


def main():
    g, s = F(1, 5), F(9, 10)
    a, b = g, s * (1 - g)
    high, low = F(4), F(1, 6)
    clumped = (high, high, low, low)
    alternating = (high, low, high, low)
    p5 = product(5, a, b, clumped)
    q5 = product(5, a, b, alternating)
    vc, va = [F(x) for x in (104,50,2,2,27)], [F(x) for x in (40,2,22,1,11)]
    margins_c = [u-v for u,v in zip(vecmul(p5, vc), vc)]
    margins_a = [v-u for u,v in zip(vecmul(q5, va), va)]
    assert all(x>0 for x in margins_c) and all(x>0 for x in margins_a)

    p2=product(2,a,b,clumped)
    q2=product(2,a,b,alternating)
    observed = trace(q2)-trace(p2)
    theoretical = a*a*b*b*(high-low)**2
    assert observed==theoretical and observed>0
    assert characteristic(p2)[-1] == characteristic(q2)[-1]

    checks=[]
    for m in (3,4):
        seq=tuple(F(i+2,i+5) for i in range(m))
        for length in (m-1,m,2*m-1,2*m):
            if length<2:continue
            chars={characteristic(product(length,a,b,p)) for p in permutations(seq)}
            assert len(chars)==1,(m,length,len(chars))
            checks.append({'period':m,'max_seed_age':length,'permutations':len(set(permutations(seq))),'charpoly_agrees':True})
    data={
      'model': {'germination_fraction':fmt(g),'dormant_survival':fmt(s),'a':fmt(a),'b':fmt(b),
                'high_fecundity':fmt(high),'low_fecundity':fmt(low)},
      'age_two':{'trace_alternating_minus_clumped':fmt(observed),'exact_factor':fmt(theoretical),
                'determinants_equal':True},
      'age_five':{'clumped_witness':list(map(int,vc)),
                  'clumped_positive_margins':list(map(fmt,margins_c)),
                  'alternating_witness':list(map(int,va)),
                  'alternating_positive_shortfall_margins':list(map(fmt,margins_a)),
                  'conclusion':'rho(M_high^2 M_low^2)>1>rho(M_high M_low M_high M_low)'},
      'finite_isospectral_checks':checks,
      'note':'Finite checks do not replace the general algebraic Floquet proof.'
    }
    print(json.dumps(data,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
