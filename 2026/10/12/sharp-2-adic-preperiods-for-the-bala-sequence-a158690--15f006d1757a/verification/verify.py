#!/usr/bin/env python3
"""Exact arithmetic checks for 2-adic periods of OEIS A158690.

Checks finite residue lemmas exhaustively and independent initial terms,
then tests the infinite theorem on many explicitly bounded examples.
Computational tests are not a substitute for the written infinite proof.
"""
from math import comb, factorial


def shifted_product_coefficients(degree):
    # G(y)=1+sum_{m>=1} prod_{i=1}^m(1-(1+y)^-(2i-1)).
    g = [1] + [0] * degree
    product = [1] + [0] * degree
    for i in range(1, degree + 1):
        exponent = 2 * i - 1
        factor = [0] + [(-1) ** (r + 1) * comb(exponent + r - 1, r)
                         for r in range(1, degree + 1)]
        product = [sum(product[j] * factor[k - j] for j in range(k + 1))
                   for k in range(degree + 1)]
        g = [u + v for u, v in zip(g, product)]
    return g


def direct_exponential_coefficients(degree):
    # Independently expand each factor 1-exp(-(2i-1)t) in EGF basis.
    a = [factorial(n) * 0 for n in range(degree + 1)]
    a[0] = 1
    product = [1] + [0] * degree
    for i in range(1, degree + 1):
        d = 2 * i - 1
        factor = [0] + [-(-d) ** r for r in range(1, degree + 1)]
        nxt = [0] * (degree + 1)
        for n in range(degree + 1):
            nxt[n] = sum(comb(n, k) * product[k] * factor[n-k]
                         for k in range(n + 1))
        product = nxt
        a = [u + v for u, v in zip(a, product)]
    return a


def transformed_sequence(g):
    N = len(g) - 1
    out = []
    row = [1]
    for n in range(N+1):
        out.append(sum(g[k] * factorial(k) * row[k]
                       for k in range(n + 1)))
        row = [0] + [k * row[k] + row[k-1] if k < len(row) else row[k-1]
                     for k in range(1, n+2)]
    return out


def cyclic_differences(values, modulus, depth):
    arr = [x % modulus for x in values]
    history = []
    for _ in range(depth+1):
        history.append(arr[:])
        arr = [(arr[(j+1) % len(arr)]-arr[j]) % modulus
               for j in range(len(arr))]
    return history


def spectral_coefficients(e, g):
    modulus = 1 << e
    K = 1
    while factorial(K) % modulus:
        K += 1
    c = [sum((-1) ** (k-j) * comb(k, j) * g[k]
             for k in range(j,K)) % modulus for j in range(K)]
    return K,c


def value_at(c,n,modulus):
    return sum(cj*pow(j,n,modulus) for j,cj in enumerate(c) if j) % modulus


def main():
    g = shifted_product_coefficients(25)
    assert g[:7] == [1,1,2,7,33,197,1419], g[:7]
    a = transformed_sequence(g[:13])
    direct = direct_exponential_coefficients(12)
    expected = [1,1,5,55,1073,32671,1431665,85363615,
                6646603073,654896692351,79656194515025]
    assert a == direct
    assert a[:len(expected)] == expected

    # Each difference identity is an exact finite cyclic calculation.
    h = [int(j % 4 == 2) for j in range(4)]
    dh = cyclic_differences(h,2,4)
    assert dh[4] == [0]*4
    assert [x[0] for x in dh[:4]] == [0,0,1,1]
    b = [int(j % 8 in (3,5)) for j in range(8)]
    db = cyclic_differences(b,2,6)
    assert db[6] == [0]*8
    assert [x[0] for x in db[:6]] == [0,0,0,1,0,1]
    f = [((j*j-1)//8)%4 if j%2 else 0 for j in range(16)]
    df = cyclic_differences(f,4,7)
    assert df[7] == [0]*16
    assert [x[0] for x in df[:7]] == [0,0,0,1,0,1,2]

    tested_positions = 0
    e1 = [x%2 for x in direct]
    assert e1 == [1]*(len(direct))
    print('Exact first coefficients, Stirling transform and independent EGF: PASS')
    print('Finite differences h, b, f on all residues: PASS')
    print('Power-of-two cases:')
    for e in range(2,13):
        mod = 1<<e
        K,c = spectral_coefficients(e,g)
        period = 1<<(max(1,e-3))
        lam = 2 if e==2 else 1<<(e-2)
        onset = value_at(c,e-1+lam,mod)-value_at(c,e-1,mod)
        assert onset %mod == 1<<(e-1),(e,'onset',onset%mod)
        for n in range(e,e+max(2*period+10,35)):
            assert value_at(c,n+period,mod)==value_at(c,n,mod), (e,n,'period')
            tested_positions+=1
        if period>2:
            ne=e if e%2==0 else e+1
            assert (value_at(c,ne+period//2,mod)-value_at(c,ne,mod)) %mod == 1<<(e-1)
        elif e in (2,3,4):
            assert value_at(c,e,mod)!=value_at(c,e+1,mod)
        print(f'  e={e:2d} modulus={mod:5d} K={K:2d} '
              f'preperiod={e:2d} least_period={period:4d} : PASS')
    print(f'PASS: {tested_positions} modular tail position comparisons; '
          '11 onset obstructions; 8 half-period obstructions; 3 short periods')
    print('LIMIT: finite parameter tests only; infinite claim proved in RESULT.md.')


if __name__ == '__main__':
    main()
