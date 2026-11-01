"""Independent state enumeration for synchronous majority on two cliques joined by one edge.
Public-domain-style finite arithmetic verification; no external dependencies.
"""
from collections import Counter
from math import comb


def expected(m):
    if m == 2:
        return {0: 6, 1: 6, 2: 4, 3: 0, 4: 0}, 1
    if m % 2:
        h = comb(m - 1, (m - 1) // 2)
        t2 = 2 * h * (2**m - h)
        return {0: 4, 1: 4**m - 4 - t2, 2: t2, 3: 0, 4: 0}, 0
    c = comb(m, m // 2)
    u = 2**m - c
    return {0: 4 + c*c//2,
            1: u*u - 4,
            2: c*c//2 + c*u,
            3: c*2**(m-1),
            4: c*(2**(m-1) - c)}, c*c//4


def solve(m):
    nn = 2*m
    full = (1 << nn) - 1
    neigh = []
    for v in range(nn):
        low = 0 if v < m else m
        cmask = (((1 << m) - 1) << low) & ~(1 << v)
        if v == 0: cmask |= 1 << m
        if v == m: cmask |= 1
        neigh.append((cmask, cmask.bit_count()))

    def F(state):
        result = 0
        for v, (mask, deg) in enumerate(neigh):
            n1 = (state & mask).bit_count()
            b = 1 if 2*n1 > deg else 0 if 2*n1 < deg else (state >> v)&1
            result |= b << v
        return result

    counts = Counter()
    period2 = set()
    period2_basin = 0
    for state in range(1 << nn):
        chain = [state]
        for t in range(7):
            if t+2 >= len(chain):
                chain.append(F(chain[-1]))
            if t+2 >= len(chain):
                chain.append(F(chain[-1]))
            if chain[t] == chain[t+2]:
                counts[t] += 1
                if chain[t] != chain[t+1]:
                    if t == 0: period2.add(min(chain[0],chain[1]))
                    else: period2_basin += 1
                break
        else:
            raise AssertionError(('Unexpected long preperiod',m,state))
    return dict(counts),len(period2),period2_basin


if __name__ == '__main__':
    total = 0
    for m in range(2, 10):
        actual, orbits, basin = solve(m)
        pred, number = expected(m)
        assert actual == {k:v for k,v in pred.items() if v},(m,actual,pred)
        assert orbits == number,(m,orbits,number)
        assert basin == 0,(m,basin)
        total += 4**m
        print(f'm={m}: configurations={4**m}, T={actual}, primitive_2_orbits={orbits}, transient_to_2_cycle={basin}')
    for m in range(2,300):
        pred,num=expected(m)
        assert sum(pred.values())==4**m,(m,'sum')
        assert all(x>=0 for x in pred.values())
        assert num>=0
    print('BARBELL_MAJORITY_VERIFY_OK', 'exhaustive_microstates',total,'formula_identity_sizes',298)
