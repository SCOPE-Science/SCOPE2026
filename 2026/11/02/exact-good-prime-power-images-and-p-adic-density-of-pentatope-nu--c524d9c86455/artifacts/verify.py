#!/usr/bin/env python3
"""Independent finite-depth checks of the pentatope image classification.

The program independently enumerates polynomial values and compares them with
sets built from the theorem's residue-ball and square-coset descriptions.
No third-party modules or downloaded data are needed.
"""
from math import isqrt


def legendre(a, p):
    a %= p
    if not a:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def poly(x, modulus):
    return (x * (x - 1) * (x - 2) * (x - 3) * pow(24, -1, modulus)) % modulus


def square_count(p, m):
    if m == 0:
        return 1
    return 1 + ((p - 1) // 2) * sum(
        p ** (m - 2*j - 1) for j in range((m + 1) // 2)
    )


def image_count_formula(p, k):
    t = (3*p + 4 + legendre(-1,p) + 2*legendre(5,p) - 2*legendre(10,p)) // 8
    e = int(legendre(5,p) == 1) + int(legendre(10,p) == -1)
    return t if k == 1 else (t-e)*p**(k-1) + e*square_count(p,k-2)


def predicted_values(p, k):
    mod=p**k
    first={poly(x,p) for x in range(p)}
    if k == 1:
        return first
    exceptions=[]
    if legendre(10,p) == -1:
        exceptions.append((3 * pow(128,-1,mod) %mod, -5 * pow(48,-1,mod) %mod))
    if legendre(5,p) == 1:
        exceptions.append((-pow(24,-1,mod) % mod, pow(24,-1,mod)))
    critical_residues={c%p for c,a in exceptions}
    out={(r+p*j)%mod for r in first if r not in critical_residues for j in range(mod//p)}
    if k == 2:
        out.update(c for c,a in exceptions)
    else:
        squares={x*x % p**(k-2) for x in range(p**(k-2))}
        out.update((c+a*p*p*s)%mod for c,a in exceptions for s in squares)
    return out


def test():
    cases=0
    tested_residues=0
    for p in [7,11,13,17,19,23,29,31,37,41]:
        for k in (1,2,3,4):
            modulus=p**k
            if modulus > 120_000:
                continue
            actual={poly(x,modulus) for x in range(modulus)}
            predicted=predicted_values(p,k)
            total=image_count_formula(p,k)
            assert len(actual)==len(predicted)==total, (p,k,len(actual),len(predicted),total)
            assert actual==predicted, (p,k,sorted(actual^predicted)[:8])
            print('LEVEL_OK p={} k={} modulus={} image={}'.format(p,k,modulus,total))
            cases+=1
            tested_residues+=modulus
    print('VERIFY_OK cases={} fully_enumerated_inputs={} complete_set_matches'.format(cases,tested_residues))

if __name__=='__main__':
    test()
