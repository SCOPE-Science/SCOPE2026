#!/usr/bin/env python3
"""Independent integer and modular checks for shifted odd-factorial product theorem."""

def nu2(n):
    if n == 0:
        return None
    n = abs(n)
    return (n & -n).bit_length() - 1


def odd_product(e, a, modulus=None):
    p = 1
    step = 1 << e
    for odd in range(1, step, 2):
        p *= step * a + odd
        if modulus is not None:
            p %= modulus
    return p


def test_exact():
    count = 0
    collisions = 0
    power_tests = 0
    for e in range(2, 10):
        vals = {a: odd_product(e, a) for a in range(-8, 9)}
        for a in vals:
            for b in vals:
                d = (a-b) * (a+b+1)
                got = vals[a] - vals[b]
                if d == 0:
                    assert got == 0, ('collision', e, a, b)
                    collisions += 1
                else:
                    expected = 3*e-2 + nu2(d)
                    assert nu2(got) == expected, ('valuation', e, a, b, nu2(got), expected)
                    count += 1
                    if a in (-3, 0, 1, 5) and b in (-4, -1, 2, 7):
                        for j in (1,2):
                            power_d = vals[a]**(1<<j) - vals[b]**(1<<j)
                            assert nu2(power_d) == expected+j, ('power', e, a, b, j)
                            power_tests += 1
    return count, collisions, power_tests


def test_modular():
    pairs=0
    for e in range(10, 14):
        M = 4*e+14
        md = 1<<M
        vals={a:odd_product(e,a,md) for a in range(-6, 7)}
        for a in vals:
            for b in vals:
                d=(a-b)*(a+b+1)
                got=(vals[a]-vals[b])%md
                if d:
                    expected=3*e-2+nu2(d)
                    assert expected<M
                    assert nu2(got)==expected,('modular',e,a,b,expected,nu2(got))
                    pairs+=1
                else:
                    assert got==0
    return pairs


def test_fibers():
    checks=0
    for e in range(2, 10):
        for s in range(1, 8):
            m=1<<(3*e-2+s)
            residues=[odd_product(e,a,m) for a in range(1<<s)]
            assert len(set(residues)) == 1<<(s-1),(e,s,'image')
            for a in range(1<<s):
                fibers=[b for b in range(1<<s) if residues[b]==residues[a]]
                assert fibers==sorted({a,(-a-1)%(1<<s)}),(e,s,a,fibers)
                checks+=1
    return checks

if __name__=='__main__':
    a,b,c=test_exact()
    d=test_modular()
    f=test_fibers()
    print('EXACT_PAIR_VALUATIONS',a)
    print('EXACT_REFLECTION_EQUALITIES',b)
    print('DIRECT_POWER_LIFTS',c)
    print('MODULAR_PAIR_VALUATIONS',d)
    print('MODULAR_FIBER_MEMBERSHIPS',f)
    print('VERIFY_OK')
