"""Exact checks for singleton-symbol counts and run counts in iid words.

Uses only Python's standard library. These finite checks do not substitute
for the induction and conditional-expectation proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def formula(n, p):
    assert n >= 2 and len(p) >= 2 and all(x > 0 for x in p) and sum(p) == 1
    s = sum((x*x for x in p), Q(0))
    ans = Q(0)
    for x in p:
        h = (s - x*x) / (1-x)**2
        ans += x*(1-x)**(n-1)*(n*(s-h)+2*h)
    return (n-1)*ans


def enumerate_directly(n,p):
    eh = er = ehr = Q(0)
    for word in product(range(len(p)), repeat=n):
        prob = Q(1)
        for letter in word:
            prob *= p[letter]
        h = sum(word.count(j) == 1 for j in range(len(p)))
        r = 1 + sum(word[t] != word[t+1] for t in range(n-1))
        eh += prob*h
        er += prob*r
        ehr += prob*h*r
    return ehr-eh*er


def binary_closed(n,a):
    b=1-a
    return 2*(n-1)*(1-n*a*b)*(a*b**(n-1)+b*a**(n-1))


def uniform_closed(n,m):
    return Q((n-1)*(2*m-n)*(m-1)**(n-2),m**n)


def test():
    count=0
    families=[(Q(1,2),Q(1,2)),(Q(1,3),Q(2,3)),
              (Q(1,19),Q(6,19),Q(12,19)),
              (Q(1,2),Q(1,4),Q(1,4)),
              (Q(1,4),Q(1,4),Q(1,4),Q(1,4))]
    for p in families:
        for n in range(2,7):
            assert formula(n,p)==enumerate_directly(n,p)
            count+=1
    for denominator in range(2,13):
        for numerator in range(1,denominator):
            a=Q(numerator,denominator)
            for n in range(2,16):
                assert formula(n,(a,1-a)) == binary_closed(n,a)
                count+=1
    for m in range(2,8):
        for n in range(2,3*m+5):
            assert formula(n,tuple(Q(1,m) for _ in range(m))) == uniform_closed(n,m)
            count+=1
    witness=(Q(1,19),Q(6,19),Q(12,19))
    signs=[1 if formula(n,witness)>0 else -1 for n in (2,8,11,19)]
    assert signs==[1,-1,1,-1]
    count+=1
    assert formula(4,(Q(1,2),Q(1,2))) == 0
    count+=1
    print('PASS',count,'exact assertions; witness signs',signs)

if __name__ == '__main__': test()
