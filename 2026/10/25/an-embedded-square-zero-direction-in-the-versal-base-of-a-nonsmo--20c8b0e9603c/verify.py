"""Exact checks for a specified five-edge polygon and its Minkowski equations."""
from math import comb, gcd

P = [(0, 0), (-2, -1), (-3, -2), (-2, -3), (-1, -2)]
D = [tuple(P[(i + 1) % len(P)][j] - P[i][j] for j in (0, 1)) for i in range(5)]
assert D == [(-2, -1), (-1, -1), (1, -1), (1, 1), (1, 2)]
assert all(gcd(abs(x), abs(y)) == 1 for x, y in D)
assert [sum(d[j] for d in D) for j in (0, 1)] == [0, 0]
area2 = abs(sum(P[i][0] * P[(i+1)%5][1] - P[(i+1)%5][0] * P[i][1] for i in range(5)))
assert area2 == 7

# After eliminating linear equations and diagonal translation,
# edge parameters are u, v, 0, 3u+v, -u.
T = [(1, 0), (0, 1), (0, 0), (3, 1), (-1, 0)]

def equations(k):
    output = [{}, {}]
    for p in (0, 1):
        for (A, B), d in zip(T, D):
            for i in range(k + 1):
                mon = (i, k-i)
                coefficient = d[p] * comb(k, i) * A**i * B**(k-i)
                if coefficient:
                    output[p][mon] = output[p].get(mon, 0) + coefficient
        output[p] = {m: c for m, c in output[p].items() if c}
    return output

assert equations(1) == [{}, {}]
assert equations(2) == [{(2, 0): 8, (1, 1): 6}, {(2, 0): 10, (1, 1): 6}]
for k in range(3, 21):
    assert all(u_power >= 2 or (u_power >= 1 and v_power >= 1)
               for polynomial in equations(k) for (u_power, v_power) in polynomial)
print('VERIFY_OK')
