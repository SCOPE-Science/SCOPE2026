#!/usr/bin/env python3
"""Independent finite verification for N(4,5,1)=42."""
from itertools import product
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

WITNESS = """
0000 0011 0022 0033 0044 0120 0213 0340 1043 1100 1111 1122 1133 1144
1231 1302 1401 2014 2032 2200 2211 2222 2233 2244 2412 2430 3041 3124
3300 3311 3322 3333 3344 3423 4024 4134 4321 4400 4411 4422 4433 4444
""".split()

def shadow(w):
    return {w[:i] + w[i+1:] for i in range(4)}

def witness_valid(code):
    used = set()
    for w in code:
        s = shadow(w)
        if used.intersection(s):
            return False
        used.update(s)
    return True

def optimum(q):
    words = ["".join(map(str, x)) for x in product(range(q), repeat=4)]
    outputs = ["".join(map(str, x)) for x in product(range(q), repeat=3)]
    row = {y: i for i, y in enumerate(outputs)}
    A = lil_matrix((len(outputs), len(words)), dtype=float)
    for j, w in enumerate(words):
        for y in shadow(w):
            A[row[y], j] = 1.0
    result = milp(
        c=-np.ones(len(words)),
        integrality=np.ones(len(words)),
        bounds=Bounds(np.zeros(len(words)), np.ones(len(words))),
        constraints=LinearConstraint(
            A.tocsr(),
            -np.inf * np.ones(len(outputs)),
            np.ones(len(outputs)),
        ),
        options={"mip_rel_gap": 0.0},
    )
    assert result.success and result.status == 0
    assert result.mip_gap == 0.0
    return int(round(-result.fun)), result.mip_gap

assert len(WITNESS) == 42
assert witness_valid(WITNESS)
q4, gap4 = optimum(4)
q5, gap5 = optimum(5)
assert q4 == 24 and q5 == 42
print("witness_size=42")
print("witness_valid=true")
print(f"q4_optimum={q4} mip_gap={gap4:.1f}")
print(f"q5_optimum={q5} mip_gap={gap5:.1f}")
print("N(4,5,1)=42")
