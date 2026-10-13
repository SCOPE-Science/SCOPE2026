"""Finite exact-arithmetic checks for weighted coordinate-refresh coupon dynamics.

The asymptotic statements in RESULT.md are proved analytically, not by this
finite checker. Run with Python 3: python CHECKER.py
"""
from fractions import Fraction


def step_probability_tables(n, weights, q, rounds):
    """Independent Markov calculations from all-one state."""
    p = 1-q
    full = (1 << n)-1
    state = {full: Fraction(1)}
    entries = []
    for _ in range(rounds):
        nxt = {}
        entry = Fraction(0)
        for mask, mass in state.items():
            for i, wi in enumerate(weights):
                bit = 1 << i
                for newbit, prob in ((0,p),(1,q)):
                    to = (mask | bit) if newbit else (mask & ~bit)
                    dm = mass*wi*prob
                    nxt[to] = nxt.get(to, Fraction(0))+dm
                    if mask != full and to == full:
                        entry += dm
        entries.append(entry)
        state = nxt
        assert sum(state.values()) == 1
    return entries


def fresh_set_clump_formula(n, weights, q, rounds):
    """Separate calculation using only the set of coordinates visited."""
    p = 1-q
    dist = {0:Fraction(1)}
    answers = []
    for r in range(rounds):
        if r == 0:
            answers.append(Fraction(0))
        else:
            value = Fraction(0)
            for seen, prob in dist.items():
                k = seen.bit_count()
                seen_weight = sum((weights[i] for i in range(n)
                                   if (seen >> i)&1), Fraction(0))
                value += prob*p*(q**k)*seen_weight
            answers.append(value)
        nxt = {}
        for mask, mass in dist.items():
            for i, wi in enumerate(weights):
                to = mask | (1 << i)
                nxt[to] = nxt.get(to, Fraction(0))+mass*wi
        assert sum(nxt.values()) == 1
        dist = nxt
    return answers


def stationary_flux(n, weights, q):
    p = 1-q
    result = Fraction(0)
    for mask in range(1 << n):
        k = mask.bit_count()
        pi = q**k*p**(n-k)
        for i, wi in enumerate(weights):
            bit = 1 << i
            if mask == ((1 << n)-1)^bit:
                result += pi*wi*q
    return result


def main():
    checks = 0
    for n in range(2,8):
        for exponent in (0,1,2):
            raw = [(i+1)**exponent for i in range(n)]
            total = sum(raw)
            weights = [Fraction(v,total) for v in raw]
            for q in (Fraction(1,3), Fraction(1,2), Fraction(3,5)):
                assert sum(weights) == 1
                checks += 1
                flux = stationary_flux(n,weights,q)
                assert flux == (1-q)*q**n
                checks += 1
                rounds = 8
                direct = step_probability_tables(n,weights,q,rounds)
                visited = fresh_set_clump_formula(n,weights,q,rounds)
                for a,b in zip(direct,visited):
                    assert a == b, (n,exponent,q,a,b)
                    checks += 1
    print(f'PASS: {checks} exact rational assertions')

if __name__=='__main__':
    main()
