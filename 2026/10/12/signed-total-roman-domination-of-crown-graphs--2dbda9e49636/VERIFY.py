#!/usr/bin/env python3
from itertools import product
from math import factorial, comb

VALUES = (-1, 1, 2)

def valid_strd(x, y):
    n = len(x)
    X, Y = sum(x), sum(y)
    for i in range(n):
        if Y - y[i] < 1 or X - x[i] < 1:
            return False
    twos_y = {i for i,v in enumerate(y) if v == 2}
    twos_x = {i for i,v in enumerate(x) if v == 2}
    for i,v in enumerate(x):
        if v == -1 and not (twos_y - {i}):
            return False
    for i,v in enumerate(y):
        if v == -1 and not (twos_x - {i}):
            return False
    return True

def direct_min(n):
    by_sum = {}
    for z in product(VALUES, repeat=n):
        by_sum.setdefault(sum(z), []).append(z)
    for w in range(-2*n, 4*n + 1):
        count = 0
        for X, xs in by_sum.items():
            Y = w-X
            ys = by_sum.get(Y)
            if not ys:
                continue
            for x in xs:
                for y in ys:
                    if valid_strd(x,y):
                        count += 1
        if count:
            return w, count
    raise AssertionError("no feasible function")

def abc(n,c):
    num_a = n+c-3
    num_b = n+3-3*c
    if num_a < 0 or num_b < 0 or num_a % 2 or num_b % 2:
        return None
    a, b = num_a//2, num_b//2
    if a+b+c != n:
        return None
    return a,b,c

def Cvals(n):
    return [c for c in range(n+1) if abc(n,c) is not None]

def T(n,c):
    a,b,c = abc(n,c)
    return factorial(n)//(factorial(a)*factorial(b)*factorial(c))

def formula_min_count(n):
    Cs = Cvals(n)
    if n % 2:
        if n == 3:
            return 10
        return sum(T(n,c) for c in Cs if c >= 2)**2
    a1,b1,_ = abc(n,1)
    T1 = T(n,1)
    big = [c for c in Cs if c >= 3]
    S = sum(T(n,c) for c in big)
    Q_num = sum(T(n,c)*(n-abc(n,c)[0]) for c in big)
    assert Q_num % n == 0
    Q = Q_num//n
    both_one = T1*(comb(n-1,a1) + b1*comb(n-2,a1))
    return S*S + 2*T1*Q + both_one

def construction(n):
    if n % 2:
        neg = (n-1)//2
        pos = (n-3)//2
        x = [2,2] + [-1]*neg + [1]*pos
        y = [2,2] + [-1]*neg + [1]*pos
    else:
        neg = (n-2)//2
        pos = n//2
        x = [2] + [-1]*neg + [1]*pos
        y = [2] + [-1]*neg + [1]*pos
    assert len(x)==n and len(y)==n
    return tuple(x),tuple(y)

expected = {3:10,4:84,5:900,6:3280,7:44100,8:189000}
for n in range(3,9):
    w,c = direct_min(n)
    assert w == 6, (n,w,c)
    assert c == expected[n], (n,c,expected[n])
    assert formula_min_count(n) == c, (n,formula_min_count(n),c)
    x,y = construction(n)
    assert valid_strd(x,y) and sum(x)+sum(y)==6

for n in range(3,41):
    x,y = construction(n)
    assert valid_strd(x,y) and sum(x)+sum(y)==6
    assert formula_min_count(n) > 0

print("ALL CHECKS PASSED; exhaustive_orders=[3,4,5,6,7,8]; minimum_counts=[10,84,900,3280,44100,189000]; formula_range=3..40")
