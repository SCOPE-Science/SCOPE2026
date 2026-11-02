"""Independent finite checks of online EF1 value-alphabet frontier.
Scientific limits: finite checks are not the proofs for arbitrary n.
"""
from itertools import product


def ef1(values, assignment, n):
    for i in range(n):
        own = sum(values[t][i] for t, a in enumerate(assignment) if a == i)
        for j in range(n):
            if i == j:
                continue
            other = [values[t][i] for t, a in enumerate(assignment) if a == j]
            if other and own < sum(other) - max(other):
                return False
    return True


def binary_allocation(values):
    n = len(values[0])
    bundles = [-1]*len(values)
    remaining = list(range(n))
    pivot = None
    for t in range(n):
        hi = [i for i in remaining if values[t][i] == 2]
        i = hi[0] if hi else remaining[0]
        bundles[t] = i
        remaining.remove(i)
        if pivot is None and values[t][i] == 1:
            pivot = i
    bundles[-1] = pivot if pivot is not None else 0
    return bundles


def ternary_allocation(v):
    a, b, c = 1, 2, 3
    if c in v[0]:
        i = v[0].index(c)
        return [i, 1-i, 1-i]
    if a in v[0]:
        j = v[0].index(a)
        i = 1-j
        return [i, j, i]
    assert v[0] == (b,b)
    i, j = 0,1
    if v[1][j] == a:
        return [i, i, j]
    return [i,j,i]


def four_tier_witness(first_recipient, second_recipient):
    i = first_recipient
    j = 1-i
    assert second_recipient in (i, j)
    v = [None,None,None]
    v[0] = (3,3)
    v[1] = (4,2) if i == 0 else (2,4)
    if second_recipient == i:
        v[2] = (1,1)
    else:
        v[2] = (4,3) if i == 0 else (3,4)
    for last_recipient in (i,j):
        assert not ef1(v,[i,second_recipient,last_recipient],2), (v,i,second_recipient,last_recipient)
    return True


def run():
    for n in (2,3,4):
        total = 0
        for v0 in product((1,2),repeat=n*(n+1)):
            v = tuple(tuple(v0[t*n:(t+1)*n]) for t in range(n+1))
            allocation = binary_allocation(v)
            assert ef1(v,allocation,n), (n,v,allocation)
            total += 1
        print('binary', n, total)
    total = 0
    for v0 in product((1,2,3),repeat=6):
        v = tuple(tuple(v0[t*2:t*2+2]) for t in range(3))
        allocation = ternary_allocation(v)
        assert ef1(v,allocation,2), (v,allocation)
        total += 1
    print('ternary', 2, total)
    assert sum(four_tier_witness(i,j) for i in (0,1) for j in (0,1)) == 4
    print('four-tier adaptive witness', '4 branches each with 2 final responses checked')

if __name__ == '__main__':
    run()
