"""Exact arithmetic checks for a two-coordinate conditional-expectation commutator.

Run with Python 3: python3 conditional_commutator_checker.py
This finite regression test is not a replacement for the general analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

checks = 0


def verify(ok):
    global checks
    checks += 1
    assert ok, f"Exact check {checks} failed"


def matmul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def trial(aw, bw, amask, bmask):
    aw = [F(w, sum(aw)) for w in aw]
    bw = [F(w, sum(bw)) for w in bw]
    A, B = set(amask), set(bmask)
    p = sum((aw[i] for i in A), F(0))
    q = sum((bw[j] for j in B), F(0))
    verify(0 < p < 1 and 0 < q < 1)
    E = [(i,j) for i in range(len(aw)) for j in range(len(bw))
         if not (i in A and j in B)]
    w = [aw[i]*bw[j]/(1-p*q) for i,j in E]
    verify(sum(w) == 1)
    N = len(E)
    P = [[F(0) for _ in E] for _ in E]
    Q = [[F(0) for _ in E] for _ in E]
    for u, (i,j) in enumerate(E):
        pden = sum((bw[v] for x,v in E if x == i), F(0))
        qden = sum((aw[x] for x,v in E if v == j), F(0))
        for t, (x,v) in enumerate(E):
            if i == x:
                P[u][t] = bw[v]/pden
            if j == v:
                Q[u][t] = aw[x]/qden
    PQ, QP = matmul(P, Q), matmul(Q, P)
    C = [[PQ[i][j] - QP[i][j] for j in range(N)] for i in range(N)]
    weights = [(1-p)*(1-q), (1-p)*q, p*(1-q)]
    K = [[F(0), p/(1-p), -q/(1-q)],
         [-p/(1-p), F(0), F(1)],
         [q/(1-q), -F(1), F(0)]]
    def which(i,j):
        return 0 if i not in A and j not in B else (1 if i not in A else 2)
    for u in range(N):
        for v in range(N):
            verify(C[u][v] == K[which(*E[u])][which(*E[v])]*aw[E[v][0]]*bw[E[v][1]])
            verify(w[u]*C[u][v] == -w[v]*C[v][u])
    row_norms = [sum(abs(x) for x in row) for row in C]
    col_norms = [sum((w[i]*abs(C[i][j]) for i in range(N)), F(0))/w[j] for j in range(N)]
    sharp = 2*max(p*q, p*(1-q), (1-p)*q)
    verify(max(row_norms) == sharp)
    verify(max(col_norms) == sharp)
    S = p*q*(1-p*q)
    C2 = matmul(C,C)
    verify(sum(C2[i][i] for i in range(N)) == -2*S)
    C3 = matmul(C2,C)
    for i in range(N):
        for j in range(N):
            verify(C3[i][j] == -S*C[i][j])
    winner = max(range(N), key=lambda u: row_norms[u])
    witness = [(1 if C[winner][j] >= 0 else -1) for j in range(N)]
    verify(sum(C[winner][j]*witness[j] for j in range(N)) == sharp)


def main():
    rng = Random(10071)
    for n in [2,3,4]:
        for m in [2,3,4]:
            for _ in range(9):
                aw = [rng.randint(1,11) for i in range(n)]
                bw = [rng.randint(1,13) for j in range(m)]
                a = rng.sample(range(n), rng.randint(1,n-1))
                b = rng.sample(range(m), rng.randint(1,m-1))
                trial(aw,bw,a,b)
    print(f"PASS: {checks} exact-rational assertions on 81 weighted arrays and deleting nonempty proper rectangles")

if __name__ == '__main__':
    main()
