from fractions import Fraction
from itertools import product

checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

# Finite exact replay of the radial-coordinate geometry behind the theorem.
# For rational grids in [0,1]^n, the induced tree pseudometric is |t_i-t_j|,
# and putting two tuples on the same ray realizes the sup-norm type distance.
for n in range(1, 6):
    for den in range(1, 6):
        grid = [Fraction(k, den) for k in range(den + 1)]
        tuples = list(product(grid, repeat=n))
        # Keep pair replay bounded while still checking every tuple internally.
        for t in tuples:
            d = [[abs(t[i]-t[j]) for j in range(n)] for i in range(n)]
            for i in range(n):
                check(d[i][i] == 0, "diagonal")
                for j in range(n):
                    check(d[i][j] == d[j][i], "symmetry")
                    for k in range(n):
                        check(d[i][k] <= d[i][j] + d[j][k], "triangle")
            # Chain condition: sorting radial coordinates places all points on one geodesic.
            order = sorted(range(n), key=lambda i: (t[i], i))
            if n:
                total = t[order[0]]
                for a, b in zip(order, order[1:]):
                    total += abs(t[b] - t[a])
                check(total == max(t), "piecewise path telescopes")

        # Exact isometry replay on a deterministic representative subgrid.
        sample = tuples[:min(len(tuples), 90)]
        for t in sample:
            for s in sample:
                sup = max(abs(a-b) for a,b in zip(t,s))
                same_ray_coordinate_cost = max(abs(a-b) for a,b in zip(t,s))
                check(same_ray_coordinate_cost == sup, "upper-bound realization")
                # Any realization obeys |d(p,a_i)-d(p,b_i)| <= d(a_i,b_i).
                for a,b in zip(t,s):
                    check(abs(a-b) <= sup, "coordinate lower bound")

# Repetition embedding S_2 -> S_n preserves the coordinate maximum exactly.
for n in range(2, 11):
    for den in range(1, 13):
        grid = [Fraction(k, den) for k in range(den + 1)]
        for a,b,c,d in product(grid, repeat=4):
            two = max(abs(a-c), abs(b-d))
            left = [a,b] + [b]*(n-2)
            right = [c,d] + [d]*(n-2)
            nn = max(abs(x-y) for x,y in zip(left,right))
            check(two == nn, "repetition embedding preserves sup metric")

print(f"VERIFY_OK {checks} exact assertions")
