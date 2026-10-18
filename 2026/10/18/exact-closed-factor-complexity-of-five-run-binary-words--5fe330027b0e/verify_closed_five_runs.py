#!/usr/bin/env python3
"""Independent direct factor enumeration for the five-run closed-factor count."""
from itertools import product, combinations


def predicted(a, b, c, d, e):
    n = a + b + c + d + e
    u, v = min(a, c), min(c, e)
    return n + min(b, d) * (u + v) + (u * v - min(u, v) if b == d else 0)


def factor_closed(s):
    if len(s) == 1:
        return True
    for k in range(1, len(s)):
        border = s[:k]
        if border == s[-k:]:
            occurrences = [i for i in range(len(s)-k+1) if s[i:i+k] == border]
            if occurrences == [0, len(s)-k]:
                return True
    return False


def actual(a, b, c, d, e):
    word = '0'*a+'1'*b+'0'*c+'1'*d+'0'*e
    # Enumerate *distinct* nonempty factors, then independently test each border.
    factors = {word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1)}
    return sum(factor_closed(f) for f in factors)


def run():
    total=0
    max_length=0
    for a,b,c,d,e in product(range(1,5),repeat=5):
        got=actual(a,b,c,d,e)
        want=predicted(a,b,c,d,e)
        assert got==want, ((a,b,c,d,e),got,want)
        total+=1
        max_length=max(max_length,a+b+c+d+e)
    for n in range(5,19):
        for q in combinations(range(1,n),4):
            a,b,c,d,e=q[0],q[1]-q[0],q[2]-q[1],q[3]-q[2],n-q[3]
            assert actual(a,b,c,d,e)==predicted(a,b,c,d,e)
            total+=1
    for t in range(1,11):
        a=c=e=2*t
        b=d=t
        value=predicted(a,b,c,d,e)
        assert value==8*t*t+6*t
        assert value <= 8*t+(8*t)**2/8
    print('ALL_FIVE_RUN_CLOSED_FACTOR_CHECKS_PASSED', 'cases',total,'maximum_cartesian_length',max_length,'sharp_family_parameters',10)


if __name__ == '__main__':
    run()
