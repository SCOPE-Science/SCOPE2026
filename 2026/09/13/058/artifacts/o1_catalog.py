"""Austenite-start check: is F0 closer to well 1.25I? |F0-1|²=3(.139)²=.0577, |F0-1.25I|²=3(.111)²=.0371.
Yes: W(F0) uses well alpha. Fine.

Bigger question first: order-1 laminate enumeration must consider ALL rank-one directions from F0,
not just axis diag. General rank-one D=u⊗n from F0=lam I: M±=lam I ± s D. W(M) via singular values.
Our deep_hunt random search (3000 o1 + 3000 o2 full-matrix) found nothing below E*. Strengthen: dense
deterministic scan over canonical rank-one directions (axis shears, stretches, mixed) with exact 1D
line optimization. For each D (unit): E1*(D) = min over (t,s1,s2): tW(F0+(1-t)s D)+(1-t)W(F0-tsD)...
parametrize q: M1=F0+(1-t)qD, M2=F0-tqD. Scan (t,q) finely for each D in a direction catalog.
If min over catalog = E* (attained at axis stretch), strong evidence E* is the o1-optimum.
Also consider: leaves with det<0 (reflections)? W allows; include large q.
"""
import random, math

alpha = 1.25
lam = ((1 + alpha**3) / 2) ** (1/3)
Estar = 0.030120427271912907

def Wfull(M):
    A = [[sum(M[i][k]*M[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    for _ in range(250):
        (pp, rr, mx) = (0, 1, abs(A[0][1]))
        if abs(A[0][2]) > mx: (pp, rr, mx) = (0, 2, abs(A[0][2]))
        if abs(A[1][2]) > mx: (pp, rr, mx) = (1, 2, abs(A[1][2]))
        if mx < 1e-14: break
        app, aqq, apq = A[pp][pp], A[rr][rr], A[pp][rr]
        th = 0.5*math.atan2(2*apq, aqq-app)
        co, si = math.cos(th), math.sin(th)
        for k in range(3):
            akp, akq = A[k][pp], A[k][rr]
            A[k][pp] = co*akp-si*akq; A[k][rr] = si*akp+co*akq
        for k in range(3):
            apk, aqk = A[pp][k], A[rr][k]
            A[pp][k] = co*apk-si*aqk; A[rr][k] = si*apk+co*aqk
    ev = [A[0][0], A[1][1], A[2][2]]
    nu = [math.sqrt(max(e, 0.0)) for e in ev]
    return min(sum((v-1)**2 for v in nu), sum((v-alpha)**2 for v in nu))

F0 = [[lam if i == j else 0 for j in range(3)] for i in range(3)]

def best_o1(D, qs=160, ts=41, qmax=1.0):
    best = (Wfull(F0), (0.0, 0.5))
    for iq in range(qs+1):
        q = qmax*iq/qs
        for it in range(ts+1):
            t = 0.05+0.9*it/ts
            M1 = [[F0[i][j]+(1-t)*q*D[i][j] for j in range(3)] for i in range(3)]
            M2 = [[F0[i][j]-t*q*D[i][j] for j in range(3)] for i in range(3)]
            e = t*Wfull(M1)+(1-t)*Wfull(M2)
            if e < best[0]:
                best = (e, (q, t))
    return best

import itertools
dirs = {}
e1 = [1, 0, 0]; e2 = [0, 1, 0]; e3 = [0, 0, 1]
sq = 1/math.sqrt(2); sq3 = 1/math.sqrt(3)
v = {"e1": e1, "e2": e2, "e3": e3, "d12": [sq, sq, 0], "d123": [sq3, sq3, sq3],
     "m12": [sq, -sq, 0]}
for (un, u) in v.items():
    for (nn, n) in v.items():
        D = [[u[i]*n[j] for j in range(3)] for i in range(3)]
        nm = math.sqrt(sum(D[i][j]**2 for i in range(3) for j in range(3)))
        D = [[x/nm for x in row] for row in D]
        (e, prm) = best_o1(D)
        print("u=%s n=%s E=%.8f prm(q,t)=" % (un, nn, e), prm)
print("Estar=%.8f W0=%.8f" % (Estar, Wfull(F0)))
