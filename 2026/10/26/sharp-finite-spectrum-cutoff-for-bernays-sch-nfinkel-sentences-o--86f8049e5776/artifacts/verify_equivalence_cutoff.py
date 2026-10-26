"""Finite sanity checks for the sharp BSR cutoff on equivalence structures.

The mathematical proof is in RESULT.md. These bounded enumerations do not
replace its universal quantification over finite structures and parameters.
Run: python artifacts/verify_equivalence_cutoff.py
"""
from itertools import product


def partitions(n, minpart=1):
    if n == 0:
        yield ()
    for p in range(minpart, n + 1):
        for tail in partitions(n - p, p):
            yield (p,) + tail


def labels(shape):
    return tuple(i for i, sz in enumerate(shape) for _ in range(sz))


def atomic_types(classes, witnesses, ell):
    """All equality/E atomic diagrams over fixed witnesses and ell y-slots."""
    n = len(classes)
    out = set()
    for ys in product(range(n), repeat=ell):
        v = tuple(witnesses) + ys
        out.add(tuple((v[i] == v[j], classes[v[i]] == classes[v[j]])
                      for i in range(len(v)) for j in range(i + 1, len(v))))
    return out


def allowed_extensions(classes, witnesses, ell):
    ws = set(witnesses)
    marked = {classes[v] for v in ws}
    all_classes = set(classes)
    out = []
    for c in all_classes:
        extras = sum(a == c and i not in ws for i, a in enumerate(classes))
        if extras >= ell:
            out.append(("clone", classes + (c,)))
    if len(all_classes - marked) >= ell:
        out.append(("new_free_singleton", classes + (max(all_classes) + 1,)))
    return out


def sharp_criterion(classes, witnesses, ell):
    """Exactly the three forbidden ell-tuples in the extremal sentence."""
    k = len(witnesses)
    if len(set(witnesses)) != k:
        return False
    wcl = {classes[i] for i in witnesses}
    if len(wcl) != k:
        return False
    ws = set(witnesses)
    for c in set(classes):
        nonw = sum(a == c and i not in ws for i, a in enumerate(classes))
        if nonw >= ell:
            return False
    return len(set(classes) - wcl) < ell


def run():
    total = 0
    for k, ell in [(0, 2), (0, 3), (1, 2), (1, 3), (2, 2)]:
        bound = k * ell + (ell - 1) ** 2
        local, extremal = 0, False
        # Check pointed shapes above B and sharp-formula witnesses up through B+1.
        for n in range(1, min(bound + 2, 9) + 1):
            for shape in partitions(n):
                E = labels(shape)
                for w in (product(range(n), repeat=k) if k else [()] ):
                    if sharp_criterion(E, w, ell):
                        assert n <= bound, ("sharp bound broken", k, ell, shape, w)
                        extremal |= (n == bound)
                    if n <= bound:
                        continue
                    old = atomic_types(E, w, ell)
                    options = allowed_extensions(E, w, ell)
                    assert options, ("missing pump", k, ell, shape, w)
                    for name, expanded in options:
                        assert atomic_types(expanded, w, ell) <= old, (
                            "new atomic type", k, ell, shape, w, name
                        )
                    local += 1
        # Explicit witness works also when B>enumeration range.
        shape = (ell,) * k + (ell - 1,) * (ell - 1)
        E = labels(shape)
        w = tuple(i * ell for i in range(k))
        assert len(E) == bound and sharp_criterion(E, w, ell)
        total += local
        print(f"CHECK k={k} ell={ell} B={bound} cases={local} sharp=YES")
    print(f"VERIFY_OK pointed_cases={total}")


if __name__ == "__main__":
    run()
