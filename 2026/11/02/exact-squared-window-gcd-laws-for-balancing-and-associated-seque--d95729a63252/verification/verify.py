#!/usr/bin/env python3
"""Exact integer checks for squared-window GCD formulas of balancing sequences."""
from math import gcd


def seq(a, b, coeff, length):
    x = [a, b]
    for _ in range(2, length):
        x.append(coeff*x[-1]-x[-2])
    return x


def check():
    kmax, nmax = 128, 40
    B = seq(0, 1, 6, 3*kmax+nmax+2)
    C = seq(1, 3, 6, 3*kmax+nmax+2)
    c = seq(-1, 1, 6, 3*kmax+nmax+2)
    P = [0, 1]
    Q = [1, 1]
    for _ in range(2, 4*(kmax+nmax)+16):
        P.append(2*P[-1]+P[-2]); Q.append(2*Q[-1]+Q[-2])
    count_window = 0
    count_expression = 0
    for k in range(1, kmax+1):
        target = gcd(k, B[k])
        desired = {'B': target if k % 2 else target//2,
                   'C': target,
                   'c': target*(3 if k % 6 == 3 else 1)}
        assert target % (2 if k % 2 == 0 else 1) == 0
        for label, X in [('B', B), ('C', C), ('c', c)]:
            running = sum(X[i]**2 for i in range(1, k+1))
            d = 0
            for n in range(nmax+1):
                if n: running += X[n+k]**2-X[n]**2
                d = gcd(d, running)
                if label == 'B': formula = (B[k]*Q[4*n+2*k+2]-k)//16
                elif label == 'C': formula = (B[k]*Q[4*n+2*k+2]+k)//2
                else: formula = (B[k]*Q[4*n+2*k]-k)//2
                assert running == formula, (label,k,n,running,formula)
                count_expression += 1
            assert d == desired[label], (label,k,d,desired[label])
            count_window += 1
    for m in range(1, kmax+1):
        assert B[2*m] == 2*B[m]*C[m]
        assert B[3*m] == B[m]*(4*C[m]**2-1)
        assert C[m] == Q[2*m]
        assert c[m] == Q[2*m-1]
        assert B[m] == P[2*m]//2
    for m in range(0, 4*kmax+8):
        assert Q[m+4]-Q[m] == 8*P[m+2]
    print(f'PASS: {count_window} window-GCD comparisons; '
          f'{count_expression} exact window-expression comparisons; '
          f'{kmax} tests each of doubling, tripling, and Pell representations; '
          f'{4*kmax+8} Pell difference checks.')

if __name__ == '__main__':
    check()
