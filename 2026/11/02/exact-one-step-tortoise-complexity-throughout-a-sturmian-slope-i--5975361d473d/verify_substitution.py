"""Exact finite checks for factors under the Fibonacci substitution.
Only standard-library Python is required; finite checks do not prove the infinite theorem.
"""
from collections import defaultdict

def morph(word):
    return ''.join('01' if c == '0' else '0' for c in word)

def factors_exact(n):
    a,b='0','1'
    while len(b)<n:
        a,b=morph(a),morph(b)
    f=set()
    # Every pair 00,01,10 occurs, and all substitution blocks have size >= n.
    for x,y in ('00','01','10'):
        s=(a if x=='0' else b)+(a if y=='0' else b)
        f.update(s[i:i+n] for i in range(len(s)-n+1))
    return f

def tortoise(word):
    pieces=word.split('1')
    if len(pieces)==1:
        return word
    return pieces[0]+pieces[1]+''.join('1'+v for v in pieces[2:])+'1'

def prefix(n):
    w='0'
    while len(w)<n: w=morph(w)
    return w[:n]

for n in range(1,181):
    fac=factors_exact(n)
    assert len(fac)==n+1, (n,'factor count',len(fac))
    fibers=defaultdict(list)
    for w in fac: fibers[tortoise(w)].append(w)
    assert len(fibers)==(2 if n<=2 else n-1), (n,len(fibers))
    if n>=4:
        z1=prefix(n-2); z2=prefix(n-3)
        expected={frozenset(('10'+z1,'01'+z1)),frozenset(('001'+z2,'010'+z2))}
        actual={frozenset(v) for v in fibers.values() if len(v)>1}
        assert actual==expected, (n,actual,expected)
        assert sorted(len(v) for v in fibers.values()).count(2)==2
print('PASS: exact substitution-block factor census and all tortoise fibers, n=1..180')
print('complexities n=1..12:',[len({tortoise(w) for w in factors_exact(n)}) for n in range(1,13)])
