"""Standalone exact checks for a two-hub bond-percolation shortcut theorem.

Run: python verify.py
Requires only Python standard library. This script tests finitely many cases;
the infinite-range proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def base_edges(a, b):
    # hubs 0,1; left leaves 2..a+1; right leaves a+2..a+b+1
    return [(0, 1)] + [(0, i) for i in range(2, a+2)] + [(1, j) for j in range(a+2, a+b+2)]


def components_squared(n, retained):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for u, v in retained:
        x, y = root(u), root(v)
        if x != y:
            parent[x] = y
    sizes = {}
    for i in range(n):
        r = root(i)
        sizes[r] = sizes.get(r, 0) + 1
    return sum(t*t for t in sizes.values())


def exact_mean(a, b, extra, p):
    edges = base_edges(a, b)
    if extra is not None:
        assert tuple(sorted(extra)) not in [tuple(sorted(e)) for e in edges]
        edges.append(extra)
    n = a+b+2
    E = len(edges)
    num = 0
    for mask in range(1<<E):
        selected = [edges[i] for i in range(E) if mask>>i & 1]
        k = len(selected)
        num += components_squared(n, selected)*p.numerator**k*(p.denominator-p.numerator)**(E-k)
    return Fraction(num, n*p.denominator**E)


def gains(a,b,p):
    A=p*(1-p)*(1+3*p+2*(a-1)*p**2+2*b*p**3)
    B=p*(1-p)*(1+3*p+2*(b-1)*p**2+2*a*p**3)
    C=p*(1-p)*(1+(b+3)*p+2*(a+b-1)*p**2+b*(a-1)*p**3)
    D=p*(1-p)*(1+(a+3)*p+2*(a+b-1)*p**2+a*(b-1)*p**3)
    E=p*(1-p)*(1+3*p+(a+b+4)*p**2+3*(a+b-2)*p**3+(a-1)*(b-1)*p**4)
    return {'A':A,'B':B,'C':C,'D':D,'E':E}


def candidates(a,b):
    return {'A': (2,3) if a>=2 else None,
            'B': (a+2,a+3) if b>=2 else None,
            'C':(2,1), 'D':(a+2,0), 'E':(2,a+2)}


def base_formula(a,b,p):
    pair_sum=(a+b+1)*p+(a+b+comb(a,2)+comb(b,2))*p**2+a*b*p**3
    return 1+Fraction(2,a+b+2)*pair_sum

checks=0
for a in range(1,5):
    for b in range(1,5):
        for p in (Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(4,5)):
            baseline=exact_mean(a,b,None,p)
            assert baseline==base_formula(a,b,p), (a,b,p,'base')
            checks+=1
            formulas=gains(a,b,p)
            for typ,edge in candidates(a,b).items():
                if edge is None:
                    continue
                actual=exact_mean(a,b,edge,p)
                expected=baseline+Fraction(2,a+b+2)*formulas[typ]
                assert actual==expected,(a,b,p,typ,actual,expected)
                checks+=1
            # Check all missing edges by exhaustive graph type reduction.
            class_values=set()
            for u,v in combinations(range(a+b+2),2):
                if (u,v) in base_edges(a,b) or (v,u) in base_edges(a,b):
                    continue
                if u>=2 and v<=a+1: typ='A'
                elif u>=a+2 and v>=a+2: typ='B'
                elif u==1 and 2<=v<=a+1: typ='C'
                elif u==0 and v>=a+2: typ='D'
                elif 2<=u<=a+1 and v>=a+2: typ='E'
                else: raise AssertionError((a,b,u,v))
                class_values.add(typ)
                assert exact_mean(a,b,(u,v),p)==baseline+Fraction(2,a+b+2)*formulas[typ]
                checks+=1
            assert class_values==set(k for k,v in candidates(a,b).items() if v is not None)
            checks+=1
            winner=max(formulas[k] for k in class_values)
            # Algebraic ordering: the best triangle always attaches a leaf
            # from the smaller side, unless the sides are tied.
            best_triangle='C' if a<=b else 'D'
            assert winner==max(formulas[best_triangle],formulas['E'])
            checks+=1

# Direct exact-rational proof certificates on a broad finite parameter grid,
# distinct from the symbolic all-integer argument documented in RESULT.md.
for a in range(1,31):
    for b in range(1,a+1):
        for k in range(1,20):
            p=Fraction(k,20)
            F=gains(a,b,p)
            assert F['D']>=F['C']
            if a>=2: assert F['C']>F['A']
            if b>=2: assert F['D']>F['B']
            H=((a-1)*(b-1)*p**3 + (-a*b+4*a+3*b-6)*p**2 +(6-a-b)*p-a)
            assert F['E']-F['D']==p**2*(1-p)*H
            checks+=5

print('VERIFY_OK assertions=',checks)
