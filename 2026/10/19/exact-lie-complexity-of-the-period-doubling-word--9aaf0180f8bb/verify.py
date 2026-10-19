#!/usr/bin/env python3
"""Finite checks for period-doubling Lie complexity. Python 3.8+."""

def substituted(k):
    word = '0'
    for _ in range(k):
        word = ''.join('01' if ch == '0' else '00' for ch in word)
    return word

def arithmetic(k):
    out=[]
    for i in range(1, (1 << k)+1):
        v = i & -i
        out.append(str((v.bit_length()-1)&1))
    return ''.join(out)

def classes(word, n):
    factors = {word[i:i+n] for i in range(len(word)-n+1)}
    found = set()
    for f in factors:
        orbit = {f[j:]+f[:j] for j in range(n)}
        if orbit.issubset(factors):
            found.add(min(orbit))
    return found, factors

def expected(n):
    x=n
    while x%2 == 0: x//=2
    return 2 if x in (1,3) else 0

p=substituted(13)
q=arithmetic(14)
assert p == q[:len(p)]
assert '11' not in q and '0000' not in q
for n in range(1,201):
    a,fa = classes(p,n)
    b,fb = classes(q,n)
    assert fa == fb, ('factor stabilization', n)
    assert a == b, ('two prefix constructions',n)
    assert len(a) == expected(n), ('formula',n,a)
    if n>=4 and n%2==0:
        half,_ = classes(p,n//2)
        exp = set()
        for x in half:
            y = ''.join('0'+('1' if c=='0' else '0') for c in x)
            exp.add(min(y[j:]+y[:j] for j in range(n)))
        assert a == exp, ('conjugacy reduction',n,a,exp)
print('PASS: substitution and arithmetic prefixes agree; forbidden factors absent')
print('PASS: complete factor languages stable across lengths 8192 and 16384 for 1<=n<=200')
print('PASS: direct cyclic-conjugacy classification agrees for 1<=n<=200')
print('PASS: exact support formula for all tested n, and halving bijection for 4<=2m<=200')
print('sample',[(n,len(classes(p,n)[0])) for n in (1,2,3,4,5,6,8,12,16,24,48,96,192,200)])
