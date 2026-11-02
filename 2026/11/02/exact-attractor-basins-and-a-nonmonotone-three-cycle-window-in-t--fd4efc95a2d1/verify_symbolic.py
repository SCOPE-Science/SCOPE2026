#!/usr/bin/env python3
"""Exact capped-cohort proof for threshold-two cyclic 3-color dynamics on K_(a,b).

Each pair of shores has three labeled initial-color cohorts. A cohort never splits;
classes represented by two vertices when their population is at least two
faithfully determine all threshold decisions, even after mergers.
"""
from collections import Counter
from itertools import product
from math import factorial


def step(x, y):
    nx = tuple((c + 1) % 3 if y.count((c + 1) % 3) >= 2 else c for c in x)
    ny = tuple((c + 1) % 3 if x.count((c + 1) % 3) >= 2 else c for c in y)
    return nx, ny


def attractor(x, y):
    seen = {}
    t = 0
    while (x, y) not in seen:
        seen[x, y] = t
        x, y = step(x, y)
        t += 1
    return seen[x, y], t - seen[x, y]


def all_signatures():
    triples = [x for x in product(range(3), repeat=3) if any(x)]
    for a, b in product(triples, repeat=2):
        x = tuple(c for c, ct in enumerate(a) for _ in range(ct))
        y = tuple(c for c, ct in enumerate(b) for _ in range(ct))
        yield a, b, attractor(x, y)


def W(n, a):
    fact = factorial(n)
    ans = 0
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if tuple(min(2, v) for v in (i, j, k)) == a:
                ans += fact // (factorial(i) * factorial(j) * factorial(k))
    return ans


def J(n):
    return 2**n - 2*n - 2 if n >= 4 else 0


def H(n):
    return sum(factorial(n) // (factorial(i)*factorial(j)*factorial(n-i-j))
               for i in range(2, n-3) for j in range(2, n-i-1)) if n >= 6 else 0


def U(n):
    return (3 if n == 1 else 6 if n in (2,3) else 0)


def K(n):
    return J(n) + n*J(n-1)


def L(n):
    return n*(n-1) if n >= 4 else 0


def claimed(a,b):
    b3 = H(a)*H(b)+H(a)*U(b)+U(a)*H(b)
    b4 = (3*H(a)*K(b)+3*K(a)*H(b)+6*K(a)*K(b)
          +3*K(a)*L(b)+3*L(a)*K(b))
    return {1:3**(a+b)-b3-b4,3:b3,4:b4}


def main():
    sigs = list(all_signatures())
    assert len(sigs) == 26**2 == 676
    histogram = Counter(tp for _, _, tp in sigs)
    expected = {(0,1):145, (0,3):15, (0,4):6,
                (1,1):171, (1,4):36, (2,1):225,
                (2,4):6, (3,1):72}
    assert histogram == expected, (histogram, expected)
    assert all(t <= 3 and p in (1, 3, 4) for _, _, (t,p) in sigs)
    for a in range(2,13):
        for b in range(2,13):
            weights_a={s:W(a,s) for s in [x for x in product(range(3),repeat=3) if any(x)]}
            weights_b={s:W(b,s) for s in weights_a}
            hist = Counter()
            for x,y,(t,p) in sigs:
                hist[(t,p)] += weights_a[x]*weights_b[y]
            actual={p:sum(c for (t,per),c in hist.items() if per==p) for p in (1,3,4)}
            assert actual == claimed(a,b), (a,b,actual,claimed(a,b))
            assert hist[(0,4)] == 6*J(a)*J(b)
            assert hist[(2,4)] == 3*(H(a)*b*J(b-1)+a*J(a-1)*H(b))
            assert sum(hist.values()) == 3**(a+b)
            assert all(hist[(t,3)]==0 for t in range(1,4))
    # Formal equality in Z[X,Y,Z,W]; no finite-size interpolation and no CAS.
    def monom(sig_left, sig_right):
        return (sig_left.count(2), sig_right.count(2),
                sig_left.count(1), sig_right.count(1))
    def count_polynomial(pred):
        ans=Counter()
        for a,b,(t,p) in sigs:
            if pred(t,p):ans[monom(a,b)] += 1
        return ans
    def plus(*polys):
        out=Counter()
        for p in polys:out.update(p)
        return +out
    def times(a,b):
        c=Counter()
        for u,coef in a.items():
            for v,mult in b.items():
                c[tuple(x+y for x,y in zip(u,v))] += coef*mult
        return +c
    def power(a,n):
        out={(0,0,0,0):1}
        for _ in range(n):out=times(out,a)
        return out
    def scale(a,n):return Counter({k:n*v for k,v in a.items()})
    ONE={(0,0,0,0):1}
    X={(1,0,0,0):1};Y={(0,1,0,0):1}
    Z={(0,0,1,0):1};Wr={(0,0,0,1):1}
    X2=power(X,2);X3=power(X,3)
    Y2=power(Y,2);Y3=power(Y,3)
    ZX=plus(ONE,Z);WY=plus(ONE,Wr)
    # Every coefficient is a count of 676 exact capped signatures.
    model3=plus(times(X3,Y3),
                times(X3,plus(scale(Wr,3),scale(power(Wr,2),3),power(Wr,3))),
                times(Y3,plus(scale(Z,3),scale(power(Z,2),3),power(Z,3))))
    model4=plus(scale(times(times(X3,Y2),WY),3),
                scale(times(times(X2,ZX),Y3),3),
                scale(times(times(times(X2,ZX),Y2),WY),6),
                scale(times(times(times(X2,ZX),power(Wr,2)),Y),3),
                scale(times(times(times(power(Z,2),X),Y2),WY),3))
    assert count_polynomial(lambda t,p:p==3)==model3
    assert count_polynomial(lambda t,p:p==4)==model4
    assert count_polynomial(lambda t,p:t==0 and p==4)==scale(times(X2,Y2),6)
    assert count_polynomial(lambda t,p:t==0 and p==3)==model3
    print('PASS: formal exact identity of full 4-variable generating polynomials for all n')
    print('PASS: periodic 4 polynomial 6 X^2Y^2, periodic 3 polynomial equals basin')
    print('PASS: all 676 initial cohort signature pairs classified')
    print('PASS: exact 8-cell (entry time, eventual period) signature histogram', sorted(histogram.items()))
    print('PASS: all 121 size pairs 2<=a,b<=12 match exact symbolic basin formulas')
    print('PASS: periodic 3 and 4 counts and transient layers verified via weighted cohort enumerators')
    print('sample K(4,4):',claimed(4,4),'sample K(6,6):',claimed(6,6))

if __name__ == '__main__':main()
