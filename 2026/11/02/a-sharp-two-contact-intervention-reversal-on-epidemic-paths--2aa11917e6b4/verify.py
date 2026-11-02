#!/usr/bin/env python3
"""Exact checks for two-edge transmission-reduction placement on short paths.

Runs with Python 3 and its standard library. This checks symbolic polynomial
identities and uses a separate bond-state enumeration as an independent finite
model test. The positivity arguments for the infinite parameter domain are in
RESULT.md; grid enumeration is not used as an infinite-domain proof.
"""
from fractions import Fraction
from itertools import combinations, product

CHECKS = 0

def check(condition, label="assertion"):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def const(c):
    return {} if c == 0 else {(0, 0): int(c)}


def add(*args):
    out = {}
    for a in args:
        for m, c in a.items():
            out[m] = out.get(m, 0) + c
            if not out[m]:
                del out[m]
    return out


def neg(a):
    return {m: -c for m, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(*args):
    out = const(1)
    for a in args:
        new = {}
        for (i, j), c in out.items():
            for (k, l), d in a.items():
                m = (i + k, j + l)
                new[m] = new.get(m, 0) + c * d
        out = {m: c for m, c in new.items() if c != 0}
    return out


def scale(c, a):
    return {} if c == 0 else {m: c * z for m, z in a.items()}


P, Q, ONE = {(1, 0): 1}, {(0, 1): 1}, const(1)
PMQ = sub(P, Q)

def ef(n, protected):
    """Polynomial n*E[X] with protected edge indices numbered from one."""
    edge = [Q if i in protected else P for i in range(1, n)]
    total = const(n)
    for i in range(n):
        path = ONE
        for j in range(i + 1, n):
            path = mul(path, edge[j - 1])
            total = add(total, scale(2, path))
    return total


def exact_outbreak_enumeration(n, protected, p, q):
    """Directly sum every bond configuration and every uniformly chosen seed."""
    probs = [q if i in protected else p for i in range(1, n)]
    result = Fraction(0, 1)
    for bonds in product((0, 1), repeat=n-1):
        mass = Fraction(1, 1)
        for b, x in zip(bonds, probs):
            mass *= x if b else 1-x
        if not mass:
            continue
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for i, b in enumerate(bonds):
            if b:
                parent[root(i)] = root(i+1)
        sizes = [sum(root(u)==root(v) for v in range(n)) for u in range(n)]
        result += mass * Fraction(sum(sizes),n)
    return result


def peval(a,p,q):
    return sum((Fraction(c)*p**i*q**j for (i,j),c in a.items()),Fraction(0))


def verify_all():
    # Every polynomial identity is checked coefficient by coefficient.
    formulas4 = {
        (1,2):const(0), (2,3):const(0),
        (1,3):scale(2,mul(Q,PMQ)),
    }
    for S, target in formulas4.items():
        check(sub(ef(4,S),ef(4,(1,2)))==target, f"n=4:{S}")
    formulas5 = {
        (2,3):const(0),
        (1,2):scale(2,mul(P,PMQ,add(Q,ONE))),
        (3,4):scale(2,mul(P,PMQ,add(Q,ONE))),
        (1,3):scale(2,mul(Q,PMQ,add(P,ONE))),
        (2,4):scale(2,mul(Q,PMQ,add(P,ONE))),
        (1,4):scale(2,mul(PMQ,add(scale(2,mul(P,Q)),P,Q))),
    }
    for S,target in formulas5.items():
        check(sub(ef(5,S),ef(5,(2,3)))==target,f"n=5:{S}")
    check(len(list(combinations(range(1,3),2)))==1,"n=3:unique")
    formulas6 = {
        (2,4):const(0),
        (2,3):scale(-2,mul(PMQ,add(mul(P,Q),neg(P),Q))),
        (3,4):scale(-2,mul(PMQ,add(mul(P,Q),neg(P),Q))),
        (1,2):scale(2,mul(PMQ,add(mul(P,P,Q),mul(P,P),scale(2,P),neg(Q)))),
        (4,5):scale(2,mul(PMQ,add(mul(P,P,Q),mul(P,P),scale(2,P),neg(Q)))),
        (1,3):scale(2,mul(P,PMQ,add(mul(P,Q),ONE))),
        (3,5):scale(2,mul(P,PMQ,add(mul(P,Q),ONE))),
        (1,4):scale(2,mul(P,PMQ,add(mul(P,Q),Q,ONE))),
        (2,5):scale(2,mul(P,PMQ,add(mul(P,Q),Q,ONE))),
        (1,5):scale(2,mul(P,PMQ,add(scale(2,mul(P,Q)),P,Q,const(2)))),
    }
    check(len(formulas6)==10,"all n=6 choices")
    for S,target in formulas6.items():
        check(sub(ef(6,S),ef(6,(2,4)))==target,f"n=6:{S}")
    check(sub(ef(6,(2,4)),ef(6,(2,3)))==scale(2,mul(PMQ,add(mul(P,Q),Q,neg(P)))),"threshold")
    # General two-edge attenuation identity: for all n and 1 <= i < j < n,
    # with r = p-q, n*E_{i,j} is quadratic in r, with explicit linear
    # central-edge sensitivities and the unique cross-path correction.
    def geometric(length):
        result=const(0)
        term=ONE
        for z in range(length):
            result=add(result,term)
            term=mul(term,P)
        return result
    for n in range(3,13):
        base = add(const(n),scale(2,add(*[scale(n-d,mul(*([P]*d))) for d in range(1,n)])))
        for i,j in combinations(range(1,n),2):
            sensitivity=add(mul(geometric(i),geometric(n-i)),
                            mul(geometric(j),geometric(n-j)))
            coupling=mul(geometric(i),*([P]*(j-i-1)),geometric(n-j))
            candidate=add(base,scale(-2,mul(PMQ,sensitivity)),
                          scale(2,mul(PMQ,PMQ,coupling)))
            check(ef(n,(i,j))==candidate,f"general exact 2-edge formula {n=} {i=} {j=}")
    # Independent rational bond-state reconstruction, including tie surfaces.
    for p in (Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
        for q in sorted({p*Fraction(a,12) for a in (1,3,6,9,11)} | {p/(1+p)}):
            for n in (3,4,5,6):
                for S in combinations(range(1,n),2):
                    direct=exact_outbreak_enumeration(n,S,p,q)
                    check(direct==peval(ef(n,S),p,q)/n,f"bond-state {n=} {S=} {p=} {q=}")
                vals={S:peval(ef(n,S),p,q)/n for S in combinations(range(1,n),2)}
                vmin=min(vals.values())
                winners={S for S in vals if vals[S]==vmin}
                if n==3: expected={(1,2)}
                elif n==4: expected={(1,2),(2,3)}
                elif n==5: expected={(2,3)}
                else:
                    t=p/(1+p)
                    expected={(2,4)} if q<t else ({(2,3),(3,4)} if q>t else {(2,3),(2,4),(3,4)})
                check(winners==expected,f"optimizer {n=} {p=} {q=}")
    print(f"PASS {CHECKS} exact symbolic and rational assertions")

if __name__=='__main__': verify_all()
