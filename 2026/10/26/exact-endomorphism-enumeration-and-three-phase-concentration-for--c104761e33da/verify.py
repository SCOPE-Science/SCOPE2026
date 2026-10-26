"""Independent finite checks of the outward-star monoid endomorphism count.
Standard library only; no external services or files needed.
"""
from itertools import combinations, product
from math import comb

RULES = (("cc", "c"), ("ll", "l"), ("clc", "cl"), ("lcl", "cl"))

def normal_form(word):
    while True:
        for lhs, rhs in RULES:
            pos = word.find(lhs)
            if pos >= 0:
                word = word[:pos] + rhs + word[pos + len(lhs):]
                break
        else:
            return word or "1"

ELEMENTS = ("1", "c", "l", "cl", "lc")
def m1(x, y):
    result = normal_form(("" if x == "1" else x) + ("" if y == "1" else y))
    assert result in ELEMENTS, (x, y, result)
    return result

# Check that the canonical five-state multiplication is associative, has unit,
# that its generators satisfy the one-arrow presentation, and that lc is not an idempotent.
for x, y, z in product(ELEMENTS, repeat=3):
    assert m1(m1(x, y), z) == m1(x, m1(y, z))
for x in ELEMENTS:
    assert m1("1", x) == m1(x, "1") == x
assert m1("c", "c") == "c" and m1("l", "l") == "l"
assert m1(m1("c", "l"), "c") == "cl"
assert m1(m1("l", "c"), "l") == "cl"
assert m1("lc", "lc") == "cl" != "lc"

def idempotent_image(b, support, r):
    # One coordinate for each edge c -> l_i; c is the diagonal c-generator.
    return tuple(("cl" if (support >> j) & 1 else "c") if b
                 else ("l" if (support >> j) & 1 else "1") for j in range(r))

def multiply(a, b):
    return tuple(m1(x, y) for x, y in zip(a, b))

def satisfies_star_relations(center, leaf_images):
    if any(multiply(x, x) != x for x in (center, *leaf_images)):
        return False
    for a, b in combinations(leaf_images, 2):
        if multiply(a, b) != multiply(b, a):
            return False
    for leaf in leaf_images:
        base = multiply(center, leaf)
        if multiply(base, center) != base or multiply(multiply(leaf, center), leaf) != base:
            return False
    return True

def formula(r):
    return sum(comb(r, s) * (
        2**r * (2**s + 2**(r-s) - 1)**r
        + (2**(s+1) + 2**(r-s) - 1)**r
    ) for s in range(r+1))

expected = {1:15, 2:339, 3:22233, 4:4780047}
for r in range(1, 4):
    images = [idempotent_image(b, x, r) for b in (0,1) for x in range(1<<r)]
    assert len(set(images)) == 2**(r+1)
    assert all(multiply(e, e) == e for e in images)
    count = 0
    regimes = [0,0,0]
    for center in images:
        for leaves in product(images, repeat=r):
            if not satisfies_star_relations(center, leaves):
                continue
            count += 1
            center_type = 1 if all(z in ("c", "cl") for z in center) else 0
            types = [1 if all(z in ("c", "cl") for z in leaf) else 0 for leaf in leaves]
            if center_type and all(types):
                regimes[0]+=1
            if center_type and not any(types):
                regimes[1]+=1
            if not center_type and not any(types):
                regimes[2]+=1
    assert count == formula(r) == expected[r], (r, count, formula(r))
    assert regimes == [2**(r*(r+1))]*3, (r, regimes)
    print(f"r={r}: exhaustive_count={count}, three_regimes={regimes}")
for r in range(4, 13):
    f = formula(r)
    if r in expected:
        assert f == expected[r]
    ratio = f / 2**(r*(r+1))
    print(f"r={r}: exact_formula={f}, normalized={ratio:.10f}")
# Leading expansion is a theorem, not an inference from these finite checks.
print("VERIFY_OK")
