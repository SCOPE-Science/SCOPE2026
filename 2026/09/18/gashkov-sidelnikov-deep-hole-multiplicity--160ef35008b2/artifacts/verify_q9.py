from collections import Counter, defaultdict

# F_81 = F_3[w]/(w^4 + 2 w^3 + 2), as in the q=9 example
# of Shi--Li--Xia--Helleseth--Ozbudak. Elements are stored in base 3.
P = 3
DEG = 4


def coeff(a):
    return [(a // (P ** i)) % P for i in range(DEG)]


def enc(c):
    return sum((x % P) * (P ** i) for i, x in enumerate(c))


def add(a, b):
    aa, bb = coeff(a), coeff(b)
    return enc([(aa[i] + bb[i]) % P for i in range(DEG)])


def neg(a):
    return enc([(-x) % P for x in coeff(a)])


def mul(a, b):
    aa, bb = coeff(a), coeff(b)
    tmp = [0] * 7
    for i, x in enumerate(aa):
        for j, y in enumerate(bb):
            tmp[i + j] = (tmp[i + j] + x * y) % P
    # w^4 + 2 w^3 + 2 = 0, hence w^4 = w^3 + 1 over F_3.
    for d in range(6, 3, -1):
        v = tmp[d] % P
        if v:
            tmp[d] = 0
            tmp[d - 4] = (tmp[d - 4] + v) % P
            tmp[d - 1] = (tmp[d - 1] + v) % P
    return enc(tmp[:4])


def fpow(a, e):
    r = 1
    while e:
        if e & 1:
            r = mul(r, a)
        a = mul(a, a)
        e //= 2
    return r


omega = 3
assert fpow(omega, 80) == 1
assert fpow(omega, 40) != 1
assert fpow(omega, 16) != 1

q = 9
beta = fpow(omega, 16)
assert fpow(beta, 5) == 1
columns = [fpow(beta, i) for i in range(5)]

syndromes = defaultdict(list)
for index in range(3 ** 5):
    x = index
    error = []
    for _ in range(5):
        error.append(x % 3)
        x //= 3
    syndrome = 0
    for value, column in zip(error, columns):
        if value == 1:
            syndrome = add(syndrome, column)
        elif value == 2:
            syndrome = add(syndrome, neg(column))
    weight = sum(value != 0 for value in error)
    syndromes[syndrome].append((weight, tuple(error)))

assert len(syndromes) == q * q
layer_counts = Counter()
deep_multiplicities = Counter()
marked_first_summand_counts = Counter()

# Signed columns form the norm-one torus T in this example.
torus = set(columns + [neg(x) for x in columns])
assert len(torus) == q + 1

for syndrome, entries in syndromes.items():
    minimum = min(weight for weight, _ in entries)
    leaders = [error for weight, error in entries if weight == minimum]
    layer_counts[minimum] += 1
    if minimum == 3:
        multiplicity = len(leaders)
        deep_multiplicities[multiplicity] += 1
        valid_first = 0
        for first in torus:
            remainder = add(syndrome, neg(first))
            remainder_entries = syndromes[remainder]
            if min(weight for weight, _ in remainder_entries) == 2:
                valid_first += 1
        marked_first_summand_counts[valid_first] += 1
        assert valid_first == 3 * multiplicity

expected_layers = Counter({0: 1, 1: 10, 2: 40, 3: 30})
assert layer_counts == expected_layers
assert deep_multiplicities == Counter({2: 30})
assert marked_first_summand_counts == Counter({6: 30})

print("q=9")
print("layer_counts=" + repr(dict(sorted(layer_counts.items()))))
print("deep_hole_leader_multiplicities=" + repr(dict(sorted(deep_multiplicities.items()))))
print("valid_first_summand_counts=" + repr(dict(sorted(marked_first_summand_counts.items()))))
print("PASS")
