#!/usr/bin/env python3
# Exhaustive small-frame check of the common five-element composition table.

P = ("p",)
BOT = ("bot",)

def neg(x):
    return ("not", x)

def disj(x, y):
    return ("or", x, y)

def dia(x):
    return ("dia", x)

def box(x):
    return ("box", x)

def subst_p(phi, replacement):
    tag = phi[0]
    if tag == "p":
        return replacement
    if tag == "bot":
        return phi
    if tag in ("not", "dia", "box"):
        return (tag, subst_p(phi[1], replacement))
    if tag == "or":
        return ("or", subst_p(phi[1], replacement), subst_p(phi[2], replacement))
    raise ValueError(tag)

def tau(alpha, phi):
    tag = phi[0]
    if tag in ("p", "bot"):
        return phi
    if tag == "not":
        return neg(tau(alpha, phi[1]))
    if tag == "or":
        return disj(tau(alpha, phi[1]), tau(alpha, phi[2]))
    if tag == "dia":
        return subst_p(alpha, tau(alpha, phi[1]))
    if tag == "box":
        # Box is translated through its dual definition.
        return neg(subst_p(alpha, neg(tau(alpha, phi[1]))))
    raise ValueError(tag)

def eval_set(phi, n, rows, valuation):
    tag = phi[0]
    full = (1 << n) - 1
    if tag == "p":
        return valuation
    if tag == "bot":
        return 0
    if tag == "not":
        return full ^ eval_set(phi[1], n, rows, valuation)
    if tag == "or":
        return eval_set(phi[1], n, rows, valuation) | eval_set(phi[2], n, rows, valuation)
    if tag == "dia":
        arg = eval_set(phi[1], n, rows, valuation)
        out = 0
        for w, row in enumerate(rows):
            if row & arg:
                out |= 1 << w
        return out
    if tag == "box":
        arg = eval_set(phi[1], n, rows, valuation)
        out = 0
        for w, row in enumerate(rows):
            if row & ~arg == 0:
                out |= 1 << w
        return out
    raise ValueError(tag)

def frames(n, antisymmetric=False):
    diagonal = sum(1 << (i * n + i) for i in range(n))
    rowmask = (1 << n) - 1
    for bits in range(1 << (n * n)):
        if bits & diagonal != diagonal:
            continue
        rows = [(bits >> (i * n)) & rowmask for i in range(n)]
        transitive = True
        for i in range(n):
            for j in range(n):
                if (rows[i] >> j) & 1 and (rows[j] & ~rows[i]):
                    transitive = False
                    break
            if not transitive:
                break
        if not transitive:
            continue
        if antisymmetric:
            bad = any(
                i != j
                and ((rows[i] >> j) & 1)
                and ((rows[j] >> i) & 1)
                for i in range(n)
                for j in range(n)
            )
            if bad:
                continue
        yield rows

names = ["0", "a", "e", "g", "h"]
expected = [
    ["0", "a", "0", "0", "a"],
    ["0", "a", "a", "a", "a"],
    ["0", "a", "e", "g", "h"],
    ["0", "a", "g", "g", "h"],
    ["0", "a", "h", "g", "h"],
]

frame_counts = {}

for logic in ("S4", "Grz"):
    g = dia(box(dia(P))) if logic == "S4" else dia(box(P))
    reps = {
        "0": BOT,
        "a": P,
        "e": dia(P),
        "g": g,
        "h": disj(P, g),
    }
    counts = []
    signatures = {name: [] for name in names}
    for n in range(1, 5):
        count = 0
        for rows in frames(n, antisymmetric=(logic == "Grz")):
            count += 1
            for valuation in range(1 << n):
                values = {
                    name: eval_set(phi, n, rows, valuation)
                    for name, phi in reps.items()
                }
                for name in names:
                    signatures[name].append(values[name])
                for i, alpha_name in enumerate(names):
                    for j, beta_name in enumerate(names):
                        product_formula = tau(reps[alpha_name], reps[beta_name])
                        actual = eval_set(product_formula, n, rows, valuation)
                        wanted = values[expected[i][j]]
                        assert actual == wanted, (
                            logic, n, alpha_name, beta_name, valuation, rows, actual, wanted
                        )
        counts.append(count)

    # The five representatives are genuinely distinct on the checked finite frames.
    assert len({tuple(signatures[name]) for name in names}) == 5
    frame_counts[logic] = counts

assert frame_counts["S4"] == [1, 4, 29, 355]
assert frame_counts["Grz"] == [1, 3, 19, 219]

print("S4_FRAME_COUNTS", frame_counts["S4"])
print("GRZ_FRAME_COUNTS", frame_counts["Grz"])
print("VERIFY_OK")
