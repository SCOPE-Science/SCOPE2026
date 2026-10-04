#!/usr/bin/env python3

def families(q):
    teams = list(range(1 << q))
    for mask in range(1 << len(teams)):
        yield {teams[i] for i in range(len(teams)) if (mask >> i) & 1}

def union_closed(F):
    return all((a | b) in F for a in F for b in F)

def intersection_closed(F):
    return all((a & b) in F for a in F for b in F)

def nonempty_down(P, q):
    teams = range(1 << q)
    return all(
        not (T in P and S != 0 and (S & ~T) == 0) or S in P
        for T in teams for S in teams
    )

def proper_up(P, q):
    teams = range(1 << q)
    full = (1 << q) - 1
    return all(
        not (T in P and S != full and (T & ~S) == 0) or S in P
        for T in teams for S in teams
    )

def nonempty_proper_up(P, q):
    teams = range(1 << q)
    full = (1 << q) - 1
    return all(
        not (T in P and T != 0 and S != full and (T & ~S) == 0) or S in P
        for T in teams for S in teams
    )

def material(P, Q, q, weak=False):
    R = set(range(1 << q)) - P
    R |= Q
    if weak:
        R.add(0)
    return R

# Full quantifier replay for small bases.
for q in range(1, 4):
    fs = list(families(q))
    union_q = [Q for Q in fs if union_closed(Q)]
    inter_q = [Q for Q in fs if intersection_closed(Q)]

    for P in fs:
        strong_union = all(union_closed(material(P, Q, q)) for Q in union_q)
        weak_union = all(union_closed(material(P, Q, q, True)) for Q in union_q)
        strong_inter = all(intersection_closed(material(P, Q, q)) for Q in inter_q)
        weak_inter = all(intersection_closed(material(P, Q, q, True)) for Q in inter_q)

        assert strong_union == nonempty_down(P, q)
        assert weak_union == nonempty_down(P, q)
        assert strong_inter == proper_up(P, q)
        assert weak_inter == nonempty_proper_up(P, q)

# Structural corollaries through four base points.
for q in range(1, 5):
    full = (1 << q) - 1
    fs = list(families(q))

    for P in fs:
        if union_closed(P):
            if not P:
                union_form = True
            else:
                A = 0
                for T in P:
                    A |= T
                ideal = {S for S in range(1 << q) if (S & ~A) == 0}
                punctured = ideal - {0}
                union_form = P == ideal or P == punctured
            assert nonempty_down(P, q) == union_form

        if intersection_closed(P):
            if not P:
                inter_form = True
            else:
                B = full
                for T in P:
                    B &= T
                upset = {S for S in range(1 << q) if (B & ~S) == 0}
                punctured = upset - {full}
                inter_form = P == upset or (B != full and P == punctured)
            assert proper_up(P, q) == inter_form

    if q >= 3:
        strong_safe = sum(nonempty_down(P, q) and proper_up(P, q) for P in fs)
        weak_safe = sum(nonempty_down(P, q) and nonempty_proper_up(P, q) for P in fs)
        assert strong_safe == 5
        assert weak_safe == 6

print("VERIFY_OK")
