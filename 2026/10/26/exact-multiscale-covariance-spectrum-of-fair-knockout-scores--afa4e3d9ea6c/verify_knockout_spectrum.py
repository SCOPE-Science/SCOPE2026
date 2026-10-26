#!/usr/bin/env python3
"""Reproducible exact tests for covariance spectra of fair knockout brackets.
Only Python's standard library is required. Finite checks do not replace the proof.
"""
from fractions import Fraction as F
from math import exp, log


def fair_scores(n, bits):
    """Resolve every node of an n-leaf balanced bracket with prescribed coin bits."""
    winners = list(range(n))
    scores = [0] * n
    bit_index = 0
    while len(winners) > 1:
        nxt = []
        for j in range(0, len(winners), 2):
            chosen = winners[j + (bits[bit_index] & 1)]
            scores[chosen] += 1
            nxt.append(chosen)
            bit_index += 1
        winners = nxt
    assert bit_index == n - 1
    return scores


def common_round(i, j):
    assert i != j
    return (i ^ j).bit_length()


def formulas(ell):
    n = 1 << ell
    s = F(1, n)
    mu = 1 - s
    var = F(2) - (2 * ell + 1) * s - s*s
    cov = [[var if i == j else -(F(1, 1 << (common_round(i,j)-1)) - s)**2 for j in range(n)] for i in range(n)]
    eig = [F(6,1 << d) - F(2 * (ell-d)+5,n) for d in range(1,ell+1)]
    return mu, cov, eig


def verify():
    checks = 0
    for ell in range(1,5):
        n = 1 << ell
        cases = 1 << (n - 1)
        one = [0] * n
        two = [[0] * n for _ in range(n)]
        for b in range(cases):
            bits = [(b >> j) & 1 for j in range(n - 1)]
            score = fair_scores(n, bits)
            assert sum(score) == n-1
            for i in range(n):
                one[i] += score[i]
            for i in range(n):
                for j in range(n):
                    two[i][j] += score[i]*score[j]
        mu, cov, eig = formulas(ell)
        for i in range(n):
            assert F(one[i], cases) == mu
            checks += 1
            for j in range(n):
                assert F(two[i][j],cases) - F(one[i]*one[j],cases*cases) == cov[i][j]
                checks += 1
            assert sum(cov[i]) == 0
            checks += 1
        for d in range(1,ell+1):
            for root in range(0,n,1 << d):
                h = [0]*n
                for k in range(root,root+(1 << (d-1))): h[k] = 1
                for k in range(root+(1 << (d-1)),root+(1 << d)): h[k] = -1
                for i in range(n):
                    got = sum(cov[i][j]*h[j] for j in range(n))
                    assert got == eig[d-1]*h[i], (n,d,root,i,got,eig[d-1]*h[i])
                    checks += 1
        assert all(eig[d] > eig[d+1] for d in range(ell-1))
        checks += 1
        assert eig[-1] == F(1,n)
        checks += 1
        assert eig[0] == 3 - F(2*ell+3,n)
        checks += 1
        assert eig[0] / eig[-1] == 3*n - 2*ell - 3
        checks += 1
        # Distinct covariance values reveal the first meeting round.
        for d in range(1,ell+1):
            target = -(F(1,1 << (d-1)) - F(1,n))**2
            for i in range(n):
                for j in range(n):
                    if i!=j and common_round(i,j)==d:
                        assert cov[i][j]==target
                        checks += 1
        print(f'ell={ell} n={n} enumerated={cases} score-vectors; mu={mu}; eigenvalues={eig}')
    # Closed-form eigenspectra and the generalized-variance limit are analytic;
    # these finite checks provide additional falsifiable diagnostics.
    for ell in range(5,21):
        n = 1 << ell
        vals = [F(6,1 << d) - F(2*(ell-d)+5,n) for d in range(1,ell+1)]
        v = F(2) - F(2*ell+1,n) - F(1,n*n)
        assert sum(F(n,1 << d)*vals[d-1] for d in range(1,ell+1)) == n*v
        checks += 1
        assert vals[-1]==F(1,n) and vals[0]==3-F(2*ell+3,n)
        checks += 1
        assert all(F(1,1 << d) <= vals[d-1] <= F(6,1 << d) for d in range(1,ell+1))
        checks += 1
        log_fixed = sum((1.0/(1 << d))*log(float(vals[d-1])) for d in range(1,ell+1))
        random_eigen = F(n,n-1)*v
        log_random = (1.0 - 1.0/n)*log(float(random_eigen))
        ratio = exp(log_fixed-log_random)
        if ell in (5,10,15,20):
            print(f'ell={ell} n={n} generalized-variance root ratio={ratio:.12f}, limit=0.75')
        if ell==20:
            assert abs(ratio-0.75) < 0.0002
            checks += 1
    print(f'PASS: {checks} exact rational assertions plus finite floating-point limit diagnostics')


if __name__ == '__main__':
    verify()
