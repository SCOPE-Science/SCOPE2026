#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction

PERMS = [
    (1, 2, 3), (1, 3, 2), (2, 1, 3),
    (2, 3, 1), (3, 1, 2), (3, 2, 1),
]

def finite_torus_check(n):
    # U,V are uniform on Z/nZ and X3=U+V mod n.
    # Every ordered pair among X1,X2,X3 is exactly uniform on (Z/nZ)^2.
    pair_counts = {(i,j): Counter() for i in range(3) for j in range(i+1,3)}
    order = Counter()
    ties = 0
    for u in range(n):
        for v in range(n):
            x = (u, v, (u + v) % n)
            for i,j in pair_counts:
                pair_counts[(i,j)][(x[i],x[j])] += 1
            if len(set(x)) < 3:
                ties += 1
            else:
                p = tuple(sorted((1,2,3), key=lambda k: x[k-1]))
                order[p] += 1
    assert all(len(c) == n*n and set(c.values()) == {1} for c in pair_counts.values())
    total = n*n
    return {
        "n": n,
        "tie_fraction": Fraction(ties,total),
        "strict_order_probabilities": {p: Fraction(order[p],total) for p in PERMS},
    }

def ordering_law(q1,q2,q3):
    q1,q2,q3 = map(Fraction,(q1,q2,q3))
    assert q1+q2+q3 == 1
    assert all(Fraction(1,4) <= q <= Fraction(1,2) for q in (q1,q2,q3))
    # pi_abc = P(X_a < X_b < X_c)
    law = {
        (1,2,3): Fraction(1,2)-q2,
        (1,3,2): Fraction(1,2)-q3,
        (2,1,3): Fraction(1,2)-q1,
        (2,3,1): Fraction(1,2)-q3,
        (3,1,2): Fraction(1,2)-q1,
        (3,2,1): Fraction(1,2)-q2,
    }
    assert sum(law.values()) == 1
    assert all(p >= 0 for p in law.values())
    lambdas = tuple(4*q-1 for q in (q1,q2,q3))
    assert sum(lambdas) == 1 and all(x >= 0 for x in lambdas)
    return law, lambdas

def worst_discrete_conformal_cdf(alpha):
    alpha = Fraction(alpha)
    if alpha < Fraction(1,3):
        return Fraction(0)
    if alpha < Fraction(2,3):
        return Fraction(1,2)
    if alpha < 1:
        return Fraction(3,4)
    return Fraction(1)

def worst_jittered_cdf(alpha):
    a = Fraction(alpha)
    if a <= Fraction(1,3):
        return Fraction(3,2)*a
    if a <= Fraction(1,2):
        return Fraction(1,2)
    if a <= Fraction(2,3):
        return Fraction(3,2)*a-Fraction(1,4)
    if a <= 1:
        return Fraction(1,4)+Fraction(3,4)*a
    return Fraction(1)

if __name__ == "__main__":
    for n in (32,64,128,256):
        out=finite_torus_check(n)
        print("N",n,"tie",float(out["tie_fraction"]))
        print("orders", " ".join(f"{p}:{float(out['strict_order_probabilities'][p]):.8f}" for p in PERMS))
    tests = [
        (Fraction(1,2),Fraction(1,4),Fraction(1,4)),
        (Fraction(1,4),Fraction(1,2),Fraction(1,4)),
        (Fraction(1,4),Fraction(1,4),Fraction(1,2)),
        (Fraction(1,3),Fraction(1,3),Fraction(1,3)),
        (Fraction(3,8),Fraction(5,16),Fraction(5,16)),
    ]
    for q in tests:
        law,lam=ordering_law(*q)
        print("q",q,"lambda",lam,"law",law)
    for a in (Fraction(1,20),Fraction(1,3),Fraction(2,5),Fraction(1,2),
              Fraction(3,5),Fraction(2,3),Fraction(9,10)):
        print("alpha",a,"disc",worst_discrete_conformal_cdf(a),
              "jitter",worst_jittered_cdf(a))
