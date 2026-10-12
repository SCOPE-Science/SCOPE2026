#!/usr/bin/env python3
"""Exact finite-dimensional check of the proposed boundary-loss passage-time observable.

No third-party packages, network services, or external files are required.
This program checks finitely many matrices; the general statement requires
and is established by the separate algebraic proof.
"""
from fractions import Fraction as Q

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def scalar(a, r):
    return (r * a[0], r * a[1])

def times_i(a):
    return (-a[1], a[0])

def observable(n, J, kap):
    def upper(i, j):
        # 1-indexed indices, i <= j.
        b = Q(n + 1 - j)
        if (j - i) % 2 == 0:
            return (b*(Q(i)/kap + kap*Q(i-1)/(4*J*J)), Q(0))
        return (Q(0), b/(2*J))
    return [[upper(i+1,j+1) if i<=j else (upper(j+1,i+1)[0], -upper(j+1,i+1)[1])
             for j in range(n)] for i in range(n)]

def test(n,J,kap):
    T = observable(n,J,kap)
    for i in range(n):
        expected = (Q(n-i)*(Q(i+1)/kap + kap*Q(i)/(4*J*J)), Q(0))
        assert T[i][i] == expected
        for j in range(n):
            # K^*T+TK = iJ(AT-TA) - kap/2 {P_1,T}.
            diff = ZERO
            for h in (i-1,i+1):
                if 0<=h<n: diff = add(diff,T[h][j])
            for h in (j-1,j+1):
                if 0<=h<n: diff = sub(diff,T[i][h])
            residue = scalar(times_i(diff), J)
            if i==0: residue = sub(residue, scalar(T[i][j], kap/2))
            if j==0: residue = sub(residue, scalar(T[i][j], kap/2))
            target = (Q(-1),Q(0)) if i==j else ZERO
            assert residue == target, (n,J,kap,i,j,residue,target)
    return n*n

def main():
    count = 0
    for n in range(1,41):
        for J,kap in [(Q(1),Q(1)),(Q(2),Q(3)),(Q(3,2),Q(5,4)),(Q(5,3),Q(7,2))]:
            count += test(n,J,kap)
    print('VERIFY_OK', count, 'exact rational Lyapunov matrix entries')

if __name__=='__main__':main()
