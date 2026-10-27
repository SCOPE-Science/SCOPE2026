#!/usr/bin/env python3
"""Finite reproducibility checks of period-doubling Lie-complexity formula.
The general theorem is proved symbolically, not by this bounded experiment.
"""

def phi_word(w):
    return b''.join(b'01' if c == 48 else b'00' for c in w)

def rot(w, k=1):
    return w[k:] + w[:k]

def classes(factors, n):
    checked = set()
    good = []
    for w in factors:
        if w in checked:
            continue
        orb = {rot(w, k) for k in range(n)}
        checked.update(orb)
        if orb <= factors:
            good.append(min(orb))
    return set(good)

def expected(n):
    m=n
    while not m & 1:
        m//=2
    return 2 if m in (1,3) else 0

def main():
    d=b'0'
    for _ in range(14):
        d=phi_word(d)
    longer=phi_word(d)
    assert d==longer[:len(d)]
    assert b'11' not in longer and b'0000' not in longer
    facs={}
    for n in range(1,193):
        fac={d[i:i+n] for i in range(len(d)-n+1)}
        fac2={longer[i:i+n] for i in range(len(longer)-n+1)}
        assert fac==fac2, ('unstable factor census',n)
        facs[n]=fac
        observed=classes(fac,n)
        assert len(observed)==expected(n), ('wrong Lie census', n, observed)
        if n<=6:
            print('n=',n,'classes=',sorted(x.decode() for x in observed))
        if n%2==0:
            m=n//2
            imgs={phi_word(w) for w in facs[m]}
            imgs|={rot(phi_word(w)) for w in facs[m]}
            assert imgs==fac, ('factor renormalization',n)
            lifted={min(rot(phi_word(v),k) for k in range(n)) for v in classes(facs[m],m)}
            assert lifted==observed, ('orbit renormalization',n)
    print('PERIOD_DOUBLING_LIE_PASS n=1..192 exact=2 iff odd_part_in={1,3} substitution_factor_and_orbit_bijections=96')

if __name__=='__main__':
    main()
