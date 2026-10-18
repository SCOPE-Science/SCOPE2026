#!/usr/bin/env python3
"""Check finite consequences of a uniform palindrome difference theorem."""

def pal(n,b):
    digits=[]
    while n:
        digits.append(n%b); n//=b
    return bool(digits) and digits==digits[::-1]

def gap(b): return b**3-(b-1)**2

def witnesses(b):
    J=lambda a:a*(b+1)
    P=lambda a,c:a*(b*b+1)+c*b
    U=b*b+b+1; V=b**3+b*b+b+1
    out={2-1}
    for a in range(1,b):
        for t in range(1,b):
            assert pal(J(a),b) and pal(t,b)
            out.add(J(a)-t)
    for a in range(1,b-1):
        assert pal(J(a+1),b) and pal(J(1),b)
        assert pal(U,b) and pal(J(b-a),b)
        out.update((J(a+1)-J(1),U-J(b-a)))
    for a in range(1,b):
        for c in range(b):
            for t in range(1,b):
                out.add(P(a,c)-t)
            if a<b-1:
                assert pal(P(b-1,c),b) and pal(P(b-1-a,0),b)
                out.add(P(b-1,c)-P(b-1-a,0))
    assert pal(V,b) and pal(P(2,0),b)
    out.add(V-P(2,0))
    for a in range(1,b-1):
        assert pal(P(b-a,1),b)
        out.add(V-P(b-a,1))
    return out

def run():
    for b in range(5,21):
        T=gap(b)
        assert set(range(1,T)).issubset(witnesses(b)),b
        if b<=10:
            small=[n for n in range(1,b**5) if pal(n,b)]
            assert all(not pal(n+T,b) for n in small),b
        print('base',b,'first excluded',T,'checks passed')
    print('PASS')
if __name__=='__main__': run()
