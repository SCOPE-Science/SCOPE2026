#!/usr/bin/env python3
"""Series check (stdlib only): H(u)/u^8 = E(u)*T(u) with
E(u) = sum_j G_j e^{iju} (even series), T(u) = (2 sin(u/2)/u)^14.
H_k = N_{k+1}: lambda-class relative GW generating coefficients.
"""
import json
from fractions import Fraction
from math import factorial

L = json.load(open("output/artifacts/ledger.json"))
G = {int(k): v for k, v in L["G"].items()}
K = 5
S = [Fraction((-1) ** m, (4 ** m) * factorial(2 * m + 1)) for m in range(K + 1)]
P = [Fraction(1)] + [Fraction(0)] * K
for _ in range(14):
    Q = [Fraction(0)] * (K + 1)
    for i in range(K + 1):
        for j in range(K + 1 - i):
            Q[i + j] += P[i] * S[j]
    P = Q
T = P
E = [Fraction(0)] * (K + 1)
for j, c in G.items():
    for k in range(K + 1):
        E[k] += Fraction(c) * Fraction((-1) ** k) * Fraction(j) ** (2 * k) / factorial(2 * k)
H = [sum(E[i] * T[k - i] for i in range(k + 1)) for k in range(K + 1)]
names = ["N_1", "N_2", "N_3", "N_4", "N_5", "N_6"]
for n, h in zip(names, H):
    print(f"{n} = {h}")
with open("output/artifacts/series.txt", "w") as f:
    for n, h in zip(names, H):
        f.write(f"{n} = {h}\n")
