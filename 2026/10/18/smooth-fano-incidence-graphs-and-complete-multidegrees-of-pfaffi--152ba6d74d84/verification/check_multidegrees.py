#!/usr/bin/env python3
"""Exact arithmetic checks for the Pfaffian incidence graph multidegree formula.

Only rational/integer polynomial identities are tested. Generic smoothness,
identification with the graph and ampleness require the separate geometric proof.
"""
from math import comb


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x*y
    return c


def coefficients_via_division(n):
    """Divide (1+t)^(n+1) by 1+2t to precision t^n."""
    rhs = [comb(n+1, j) for j in range(n+2)]
    answer = [1]
    for j in range(1, n):
        answer.append(rhs[j] - 2*answer[-1])
    assert poly_mul([1,2], answer)[:n] == rhs[:n]
    return answer


def coefficients_via_chern_expansion(n):
    """Euler resolution: c(Ω(2))=(1+h)^(n+1)/(1+2h)."""
    return [sum(comb(n+1, i) * (-2)**(j-i) for i in range(j+1))
            for j in range(n)]


def check(n):
    a = coefficients_via_division(n)
    assert a == coefficients_via_chern_expansion(n)
    assert a[0] == 1 and a[1] == n-1
    assert a[2] == (n-1)**2 - (comb(n,2)-1)
    assert a[-1] == (n+1)//2
    assert all(x > 0 for x in a)
    anticanonical_degree = sum(comb(n-1,j) * a[j] for j in range(n))
    return a, anticanonical_degree


def main():
    expected = {
        5: [1,4,7,6,3],
        7: [1,6,16,24,22,12,4],
        9: [1,8,29,62,86,80,50,20,5],
        11: [1,10,46,128,239,314,296,200,95,30,6],
    }
    for n in range(5, 102, 2):
        a, volume = check(n)
        if n in expected:
            assert a == expected[n]
            print(f'n={n}: multidegrees={a}; (-K)^(n-1)={volume}')
    print('PASS: two independent coefficient recurrences and all endpoint/base-degree checks for 49 odd dimensions, n=5,...,101.')
    print('Geometric graph-identification, smoothness, Fano property: PROOF ONLY, not inferred from finite tests.')

if __name__ == '__main__':
    main()
