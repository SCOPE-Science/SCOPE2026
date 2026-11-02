#!/usr/bin/env python3
"""Independent exact enumeration checks for a root--terminal dependence theorem.

Run: python3 verify.py
Requires only Python's standard library. The exhaustive checks are finite
consistency tests and do not substitute for the general proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks = 0
cases = 0

def eq(a, b, what):
    global checks
    assert a == b, (what, a, b)
    checks += 1

for n in range(3, 8):
    possibilities = [tuple(i for i in range(1, n + 1) if i != j)
                     for j in range(2, n + 1)]
    total = (n-1)**(n-1)
    sums_N = sums_L = sums_NN = sums_LL = sums_NL = 0
    marginal_R = [0] * (n+1)
    marginal_L = [0] * (n+1)
    joint_RL = [[0]*(n+1) for _ in range(n+1)]
    joint_LL = [[0]*(n+1) for _ in range(n+1)]
    joint_CL = {}
    seen = 0
    for choices in product(*possibilities):
        seen += 1
        children = [0] * (n+1)
        roots = [0] * (n+1)
        roots[1] = 1
        for j, parent in enumerate(choices, 2):
            if parent < j:
                children[parent] += 1
            else:
                roots[j] = 1
        leaves = [0] + [int(children[i] == 0) for i in range(1, n+1)]
        C, L = sum(roots), sum(leaves)
        sums_N += C
        sums_L += L
        sums_NN += C*C
        sums_LL += L*L
        sums_NL += C*L
        joint_CL[(C,L)] = joint_CL.get((C,L),0) + 1
        for i in range(1, n+1):
            marginal_R[i] += roots[i]
            marginal_L[i] += leaves[i]
            for j in range(1, n+1):
                joint_RL[i][j] += roots[i]*leaves[j]
                joint_LL[i][j] += leaves[i]*leaves[j]
    eq(seen, total, ('sample space', n))
    cases += seen
    q = F(n-2, n-1)
    r = F(n-3, n-1)
    EN = F(n,2)
    VN = F(n*(n-2),6*(n-1))
    EL = (n-1)*(1-q**n)
    cov = (n-2) - F(5*n-8,2)*q**(n-1)
    raw_cov = sum(F(comb(m,2), (n-1)**2)*q**(m-1)
                  for m in range(2,n))
    fac_L = 2*sum(q**(j-i)*r**(n-j)
                  for i in range(1,n+1) for j in range(i+1,n+1))
    VL = fac_L + EL - EL*EL
    eq(raw_cov,cov,('closed covariance',n))
    eq(F(sums_N,total), EN, ('roots mean',n))
    eq(F(sums_NN,total)-F(sums_N,total)**2, VN, ('roots variance',n))
    eq(F(sums_L,total), EL, ('terminals mean',n))
    eq(F(sums_LL,total)-F(sums_L,total)**2, VL, ('terminals variance',n))
    eq(F(sums_NL,total)-F(sums_N,total)*F(sums_L,total), cov,
       ('cross covariance',n))
    for c in range(2,n):
        for ell in range(2,n+1):
            ca = sum(v for (C,L),v in joint_CL.items() if C>=c)
            lb = sum(v for (C,L),v in joint_CL.items() if L>=ell)
            cab = sum(v for (C,L),v in joint_CL.items() if C>=c and L>=ell)
            assert cab*total >= ca*lb, ('upper quadrant association',n,c,ell)
            checks += 1
    for i in range(1,n+1):
        pR = F(n-i,n-1) if i>=2 else F(1)
        pL = q**(n-i)
        eq(F(marginal_R[i],total),pR,('root marginal',n,i))
        eq(F(marginal_L[i],total),pL,('terminal marginal',n,i))
        for j in range(1,n+1):
            if i>j:
                expected_C = F(n-i,(n-1)**2)*q**(n-j-1)
            else:
                expected_C = F(0)
            measured_C = (F(joint_RL[i][j],total)-
                          F(marginal_R[i],total)*F(marginal_L[j],total))
            eq(measured_C,expected_C,('root-terminal kernel',n,i,j))
            if i<j:
                expected_P = q**(j-i)*r**(n-j)
            elif i==j:
                expected_P = q**(n-i)
            else:
                expected_P = q**(i-j)*r**(n-i)
            eq(F(joint_LL[i][j],total),expected_P,
               ('terminal pair joint',n,i,j))
    print(f'n={n}: enumerated={seen}, E(C)={EN}, E(L)={EL}, Cov(C,L)={cov}, Var(L)={VL}')

print(f'PASS: {checks} independent exact-rational identities; {cases} exhaustively enumerated configurations.')
