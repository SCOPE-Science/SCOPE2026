#!/usr/bin/env python3
from itertools import product

def is_poset(n, le):
    for i in range(n):
        if (i, i) not in le:
            return False
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) in le and (j, i) in le:
                return False
    for a, b in le:
        for c, d in le:
            if b == c and (a, d) not in le:
                return False
    return True

def posets(n):
    off = [(i, j) for i in range(n) for j in range(n) if i != j]
    for mask in range(1 << len(off)):
        le = {(i, i) for i in range(n)}
        for k, e in enumerate(off):
            if (mask >> k) & 1:
                le.add(e)
        if is_poset(n, le):
            yield le

def minima(n, le):
    return [
        m for m in range(n)
        if all(z == m or (z, m) not in le for z in range(n))
    ]

def downsets(n, le):
    out = []
    for mask in range(1 << n):
        S = {i for i in range(n) if (mask >> i) & 1}
        if all(x not in S or y in S for y, x in le):
            out.append(S)
    return out

def source_conditions(n, le, R):
    # IFC
    for x, y in R:
        for z in range(n):
            if (z, y) in le and z != y:
                return False
    # FC2
    for x, y in R:
        for z in range(n):
            if (z, x) in le:
                if not any((yp, y) in le and (z, yp) in R for yp in range(n)):
                    return False
    return True

def normal_form(n, le, R):
    M = set(minima(n, le))
    if any(y not in M for x, y in R):
        return False
    ds = downsets(n, le)
    for m in M:
        D = {x for x in range(n) if (x, m) in R}
        if D not in ds:
            return False
    return True

def diamond(n, R, U):
    return {
        x for x in range(n)
        if any((x, y) in R and y in U for y in range(n))
    }

def box(n, le, R, U):
    return {
        x for x in range(n)
        if all(
            not ((y, x) in le and (y, z) in R) or z in U
            for y in range(n) for z in range(n)
        )
    }

def upset(n, le, D):
    return {
        x for x in range(n)
        if any((y, x) in le for y in D)
    }

poset_counts = []
for n in range(1, 5):
    pc = 0
    for le in posets(n):
        pc += 1
        ds = downsets(n, le)
        M = minima(n, le)
        predicted = len(ds) ** len(M)

        if n <= 3:
            pairs = [(i, j) for i in range(n) for j in range(n)]
            actual = 0

            for mask in range(1 << len(pairs)):
                R = {e for k, e in enumerate(pairs) if (mask >> k) & 1}
                sc = source_conditions(n, le, R)
                nf = normal_form(n, le, R)
                assert sc == nf
                actual += int(sc)

                if sc:
                    Dm = {
                        m: {x for x in range(n) if (x, m) in R}
                        for m in M
                    }
                    for U in ds:
                        expected_diamond = set()
                        for m in M:
                            if m in U:
                                expected_diamond |= Dm[m]

                        bad = set()
                        for m in M:
                            if m not in U:
                                bad |= upset(n, le, Dm[m])
                        expected_box = set(range(n)) - bad

                        assert diamond(n, R, U) == expected_diamond
                        assert box(n, le, R, U) == expected_box

            assert actual == predicted

        # Extreme examples are covered automatically, but check the formula.
        if all((i, j) in le or (j, i) in le for i in range(n) for j in range(n)):
            # Any labelled total order has one minimum and n+1 downsets.
            assert len(M) == 1
            assert len(ds) == n + 1
            assert predicted == n + 1

        if le == {(i, i) for i in range(n)}:
            assert len(M) == n
            assert len(ds) == 2 ** n
            assert predicted == 2 ** (n * n)

    poset_counts.append(pc)

assert poset_counts == [1, 3, 19, 219]
print("VERIFY_OK")
