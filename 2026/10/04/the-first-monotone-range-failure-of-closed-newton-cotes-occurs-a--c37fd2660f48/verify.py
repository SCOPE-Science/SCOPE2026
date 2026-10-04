from fractions import Fraction as F

def solve_weights(n):
    # Exact closed Newton-Cotes weights on [0,1]:
    # sum_j w_j (j/n)^r = 1/(r+1), r=0,...,n.
    A = [
        [F(j, n) ** r for j in range(n + 1)] + [F(1, r + 1)]
        for r in range(n + 1)
    ]
    N = n + 1
    for col in range(N):
        pivot = next(i for i in range(col, N) if A[i][col] != 0)
        A[col], A[pivot] = A[pivot], A[col]
        q = A[col][col]
        A[col] = [x / q for x in A[col]]
        for i in range(N):
            if i == col:
                continue
            q = A[i][col]
            if q:
                A[i] = [A[i][j] - q * A[col][j] for j in range(N + 1)]
    return [A[i][-1] for i in range(N)]

expected_min = {
    1: F(1,2),
    2: F(1,6),
    3: F(1,8),
    4: F(7,90),
    5: F(19,288),
    6: F(41,840),
    7: F(751,17280),
    8: F(989,28350),
    9: F(2857,89600),
    10: F(16067,598752),
    11: F(434293,17418240),
    12: F(-147227,750750),
    13: F(8181904909,402361344000),
}

all_weights = {}
for n in range(1,14):
    w = solve_weights(n)
    all_weights[n] = w
    assert sum(w, F(0)) == 1
    assert all(w[j] == w[n-j] for j in range(n+1))
    s = F(0)
    prefixes = []
    for j in range(n):
        s += w[j]
        prefixes.append(s)
    assert min(prefixes) == expected_min[n]

# Negative individual weights occur before the first monotone-range failure.
assert sum(x < 0 for x in all_weights[8]) == 3
assert sum(x < 0 for x in all_weights[10]) == 4
assert sum(x < 0 for x in all_weights[11]) == 4
assert all(expected_min[n] > 0 for n in range(1,12))

# Published 13-point closed Newton-Cotes coefficients.
scaled12 = [
    1364651, 9903168, -7587864, 35725120, -51491295, 87516288,
    -87797136,
    87516288, -51491295, 35725120, -7587864, 9903168, 1364651
]
w12 = all_weights[12]
assert [x * 63063000 for x in w12] == scaled12

prefix = F(0)
prefixes12 = []
for j in range(12):
    prefix += w12[j]
    prefixes12.append(prefix)
assert min(prefixes12) == F(-147227,750750)
assert prefixes12.index(min(prefixes12)) == 6

# Step extremizer y_j=0 for j<6, 1 for j>=6.
ystep = [F(0) if j < 6 else F(1) for j in range(13)]
qstep = sum(w12[j] * ystep[j] for j in range(13))
assert qstep == F(-147227,750750)

# Strictly positive, strictly increasing witness.
eps = F(1,1000)
y = [
    eps * (j + 1) if j < 6 else F(1) - eps * (13 - j)
    for j in range(13)
]
assert all(F(0) < y[j] < y[j+1] < F(1) for j in range(12))
q = sum(w12[j] * y[j] for j in range(13))
assert q == F(-34977643,187687500)
assert q < 0

# Exceptional recovery at n=13 despite six negative weights.
w13 = all_weights[13]
assert sum(x < 0 for x in w13) == 6
s = F(0)
p13 = []
for j in range(13):
    s += w13[j]
    p13.append(s)
assert min(p13) == F(8181904909,402361344000)
assert min(p13) > 0

print("VERIFY_OK")
