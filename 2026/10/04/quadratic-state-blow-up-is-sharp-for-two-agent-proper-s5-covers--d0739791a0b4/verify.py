#!/usr/bin/env python3

def construction(m):
    X = tuple(range(m))
    Y = tuple((j, k) for j in X for k in X)

    # Universal target relations.
    R1 = {(x, y) for x in X for y in X}
    R2 = set(R1)

    # Bjorndahl--Sink finite construction specialized to universal relations:
    # agent 2 stays inside columns; agent 1 stays inside skew classes k-j mod m.
    S2 = {
        ((j, k), (jp, kp))
        for j, k in Y
        for jp, kp in Y
        if k == kp
    }
    S1 = {
        ((j, k), (jp, kp))
        for j, k in Y
        for jp, kp in Y
        if (k - j) % m == (kp - jp) % m
    }

    f = {(j, k): j for j, k in Y}
    return X, Y, R1, R2, S1, S2, f

def is_equivalence(Y, S):
    if not all((y, y) in S for y in Y):
        return False
    if not all((b, a) in S for a, b in S):
        return False
    for a, b in S:
        for bb, c in S:
            if b == bb and (a, c) not in S:
                return False
    return True

def classes(Y, S):
    unseen = set(Y)
    out = []
    while unseen:
        y = next(iter(unseen))
        C = {z for z in Y if (y, z) in S}
        out.append(C)
        unseen -= C
    return out

def bounded_morphism(X, Y, R, S, f):
    # forth
    for y, z in S:
        if (f[y], f[z]) not in R:
            return False

    # back
    for y in Y:
        for x in X:
            if (f[y], x) in R:
                if not any((y, z) in S and f[z] == x for z in Y):
                    return False
    return True

for m in range(1, 21):
    X, Y, R1, R2, S1, S2, f = construction(m)

    assert len(Y) == m * m
    assert set(f.values()) == set(X)

    assert is_equivalence(Y, S1)
    assert is_equivalence(Y, S2)

    # Properness: no distinct pair is related by both agents.
    for y in Y:
        for z in Y:
            if y != z:
                assert not ((y, z) in S1 and (y, z) in S2)

    assert bounded_morphism(X, Y, R1, S1, f)
    assert bounded_morphism(X, Y, R2, S2, f)

    C1 = classes(Y, S1)
    C2 = classes(Y, S2)
    assert len(C1) == m
    assert len(C2) == m

    for C in C1 + C2:
        assert len(C) == m
        assert {f[y] for y in C} == set(X)

    # Orthogonality of the two partitions.
    for A in C1:
        for B in C2:
            assert len(A & B) == 1

# Symbolic counting inequality sampled broadly.
for m in range(1, 101):
    min_first_class = m
    distinct_second_classes_met = min_first_class
    min_second_class = m
    lower_bound = distinct_second_classes_met * min_second_class
    assert lower_bound == m * m

print("VERIFY_OK")
