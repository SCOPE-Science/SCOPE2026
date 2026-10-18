"""Exact finite checks for signed derangement cycle-count covariance.
Run: python verify.py. Only stdlib is needed.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0

def check(condition, message):
    global checks
    checks += 1
    assert condition, message


def a(n):
    return sum((Fraction((-1)**j, factorial(j)) for j in range(n+1)), Fraction(0))


def predicted(n, r, s):
    assert 2 <= r < s <= n
    mean_r = a(n-r) / (r*a(n))
    mean_s = a(n-s) / (s*a(n))
    joint = (a(n-r-s)/(r*s*a(n))) if r+s <= n else Fraction(0)
    return mean_r, mean_s, joint, joint-mean_r*mean_s


def cycle_counts(p):
    n=len(p)
    seen=set()
    counts=[0]*(n+1)
    for i in range(n):
        if i in seen:
            continue
        j=i;k=0
        while j not in seen:
            seen.add(j);k+=1;j=p[j]
        counts[k]+=1
    return counts

# Independent direct enumeration of all derangements through n=8.
for n in range(3,9):
    samples=[cycle_counts(p) for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
    check(len(samples) == factorial(n)*a(n), ('derangement count', n))
    total=len(samples)
    for r in range(2,n):
        for s in range(r+1,n+1):
            if s==n:  # one cycle of size n is permitted
                pass
            er=sum(x[r] for x in samples)
            es=sum(x[s] for x in samples)
            ers=sum(x[r]*x[s] for x in samples)
            direct=(Fraction(er,total), Fraction(es,total), Fraction(ers,total))
            formula=predicted(n,r,s)[:3]
            check(direct==formula, ('independent enumeration',n,r,s,direct,formula))

# Arbitrary length shifts of alternating partial sums, all exact rationals.
for m in range(0,38):
    for r in range(2,13):
        for s in range(2,13):
            n=m+r+s
            B1=sum((Fraction((-1)**(j+1),factorial(m+j)) for j in range(1,s+1)),Fraction(0))
            B2=sum((Fraction((-1)**(j+1),factorial(m+r+j)) for j in range(1,s+1)),Fraction(0))
            delta=a(m)*a(n)-a(m+r)*a(m+s)
            alternate=((-1)**m)*(a(m+r)*B1-((-1)**r)*a(m)*B2)
            check(delta==alternate,('determinant reduction',m,r,s))
            check(((-1)**m)*delta>0,('strict sign',m,r,s))
            check(B1>0 and B2>0,('B positivity',m,r,s))
            check(B1>=Fraction(m+1,factorial(m+2)),('B lower bound',m,r,s))
            check(B2<=Fraction(1,factorial(m+r+1)),('B upper bound',m,r,s))
            if r!=s:
                cov=delta/(r*s*a(n)*a(n))
                check(((-1)**m)*cov>0,('cov sign',m,r,s))

# Explicit examples at the first two sizes for r=2,s=3.
check(predicted(5,2,3)[3]==Fraction(30,121),'n=5 example')
check(predicted(6,2,3)[3]==Fraction(-432,2809),'n=6 example')

# Finite asymptotic consistency, not an infinite-limit proof.
import math
for m in (20,28,36):
    cov=predicted(m+5,2,3)[3]
    scaled=float(cov * Fraction(((-1)**m)*6*factorial(m+1),1))
    check(abs(scaled-math.e) < 0.3, ('asymptotic finite check',m,scaled))

print('PASS:',checks,'checks (27,234 exact and 3 numerical asymptotic consistency checks)')
