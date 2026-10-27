"""Finite exact checks for parity of independent-cut packet reversals."""
from fractions import Fraction
from itertools import product

def recurrence(n, p):
    if n == 1:
        return Fraction(1)
    a, b = Fraction(1), 2*p-1
    if n == 2:
        return b
    for _ in range(3, n+1):
        a, b = b, p*b-(1-p)*a
    return b

def exhaustive(n, p):
    s = Fraction(0)
    for cuts in product((0, 1), repeat=n-1):
        start, lengths = 0, []
        for j, cut in enumerate(cuts, 1):
            if cut:
                lengths.append(j-start)
                start=j
        lengths.append(n-start)
        odd = sum(length*(length-1)//2 for length in lengths)%2
        s += (-1 if odd else 1)*p**sum(cuts)*(1-p)**(n-1-sum(cuts))
    return s

count=0
for n in range(1,11):
    for p in (Fraction(1,5), Fraction(1,2), Fraction(3,4), Fraction(9,10)):
        assert recurrence(n,p) == exhaustive(n,p), (n,p)
        count+=1
print(f"PASS: {count} exact exhaustive finite-deck checks (sizes 1..10, four rational cut probabilities)")
print("CHECK: at n=2, p=1/2, parity exactly uniform:",recurrence(2,Fraction(1,2)))
print("CHECK: at n=3, p=1/2, sign bias:",recurrence(3,Fraction(1,2)))
