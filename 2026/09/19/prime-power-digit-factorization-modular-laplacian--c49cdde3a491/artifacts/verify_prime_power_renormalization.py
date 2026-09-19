from collections import defaultdict


def mul(a, b, modulus):
    out = defaultdict(int)
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            out[(i + k, j + l)] = (out[(i + k, j + l)] + x * y) % modulus
    return {e: c for e, c in out.items() if c % modulus}


def power(a, n, modulus):
    result = {(0, 0): 1}
    base = {e: c % modulus for e, c in a.items() if c % modulus}
    while n:
        if n & 1:
            result = mul(result, base, modulus)
        n //= 2
        if n:
            base = mul(base, base, modulus)
    return result


def dilate(a, q):
    return {(q * i, q * j): c for (i, j), c in a.items()}


def digit_factorization(p_symbol, p, r, t):
    modulus = p ** r
    low_block = p ** (r - 1)
    low = t % low_block
    high = t // low_block
    kernel = power(p_symbol, low_block, modulus)
    result = power(p_symbol, low, modulus)
    j = 0
    while high:
        digit = high % p
        if digit:
            factor = power(dilate(kernel, p ** j), digit, modulus)
            result = mul(result, factor, modulus)
        high //= p
        j += 1
    return result


def apply(operator, seed, modulus):
    return mul(operator, seed, modulus)


masks = {
    "von_neumann": {
        (1, 0): 1,
        (-1, 0): 1,
        (0, 1): 1,
        (0, -1): 1,
        (0, 0): -4,
    },
    "diagonal_neumann": {
        (1, 1): 1,
        (1, -1): 1,
        (-1, 1): 1,
        (-1, -1): 1,
        (0, 0): -4,
    },
    "asymmetric": {
        (1, 0): 1,
        (0, 1): 1,
        (-1, 0): 1,
        (2, 1): 1,
        (-1, -2): 1,
        (0, 0): -5,
    },
}

seed = {(0, 0): 1, (1, 0): 2, (0, 2): 3}
all_ok = True

print("SPECIAL-TIME RENORMALIZATION")
for name, symbol in masks.items():
    for p, r, exponents in [
        (2, 2, range(1, 5)),
        (2, 3, range(2, 5)),
        (3, 2, range(1, 4)),
    ]:
        modulus = p ** r
        kernel = power(symbol, p ** (r - 1), modulus)
        for n in exponents:
            q = p ** (n - r + 1)
            lhs = power(symbol, p ** n, modulus)
            rhs = dilate(kernel, q)
            ok = lhs == rhs
            all_ok &= ok
            print(name, "p=", p, "r=", r, "n=", n, "q=", q, "ok=", ok)

print("\nARBITRARY-TIME DIGIT FACTORIZATION")
for name, symbol in masks.items():
    for p, r in [(2, 2), (2, 3), (3, 2)]:
        modulus = p ** r
        local_ok = True
        for t in [0, 1, 2, 3, 5, 7, 11, 19, 37]:
            lhs = power(symbol, t, modulus)
            rhs = digit_factorization(symbol, p, r, t)
            local_ok &= lhs == rhs
        all_ok &= local_ok
        print(name, "p=", p, "r=", r, "ok=", local_ok)

print("\nFULL-EPOCH IDENTITY")
for name, symbol, p, r, n, s in [
    ("von_neumann", masks["von_neumann"], 2, 2, 4, 5),
    ("diagonal_neumann", masks["diagonal_neumann"], 2, 3, 4, 7),
    ("asymmetric", masks["asymmetric"], 3, 2, 3, 4),
]:
    modulus = p ** r
    q = p ** (n - r + 1)
    kernel = power(symbol, p ** (r - 1), modulus)
    lhs = apply(power(symbol, p ** n + s, modulus), seed, modulus)
    rhs = apply(dilate(kernel, q), apply(power(symbol, s, modulus), seed, modulus), modulus)
    ok = lhs == rhs
    all_ok &= ok
    print(name, "p=", p, "r=", r, "n=", n, "s=", s, "q=", q,
          "support=", len(lhs), "ok=", ok)

print("\nALL_CHECKS_PASSED=", all_ok)
if not all_ok:
    raise SystemExit(1)
