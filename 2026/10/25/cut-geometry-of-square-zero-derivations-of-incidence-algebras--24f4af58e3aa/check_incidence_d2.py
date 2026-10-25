#!/usr/bin/env python3
"""Independent finite verification of square-zero incidence-algebra derivations.

Every candidate is independently squared by applying the inner derivation
on every incidence basis vector, not by assuming the cut criterion.
No external dependencies.
"""
from itertools import product


def field(q):
    if q in (2, 3):
        return (lambda a, b: (a+b) % q), (lambda a, b: a*b % q)
    if q == 4:
        def mul(a, b):
            z = 0
            for i in range(2):
                for j in range(2):
                    if (a >> i) & (b >> j) & 1:
                        z ^= 1 << (i+j)
            if z & 8:
                z ^= 8 | 2 | 1
            if z & 4:
                z ^= 4 | 2 | 1
            return z
        return (lambda a, b: a ^ b), mul
    raise ValueError(q)


def model(le, q):
    add, mul = field(q)
    n = len(le)
    basis = [(i,j) for i in range(n) for j in range(n) if le[i][j]]
    radical = [(i,j) for i,j in basis if i < j]
    def plus(a,b):
        return {t:z for t in a.keys()|b.keys() if (z:=add(a.get(t,0),b.get(t,0))) !=0}
    def neg(a):
        return {t:mul(q-1, z) if q!=4 else z for t,z in a.items()}
    def prod(a,b):
        r = {}
        for (i,j),v in a.items():
            for (k,l),w in b.items():
                if j == k:
                    t = (i,l)
                    r[t] = add(r.get(t,0), mul(v,w))
        return {t:v for t,v in r.items() if v}
    def comm(a,b):
        return plus(prod(a,b),neg(prod(b,a)))
    def square_zero_derivation(u):
        for t in basis:
            e = {t:1}
            if comm(u,comm(u,e)):
                return False
        return True
    ideals=[]
    for mask in range(1<<n):
        S={i for i in range(n) if mask & (1<<i)}
        if all(not (j in S and le[i][j]) or i in S for i in range(n) for j in range(n)):
            ideals.append(S)
    def cut(u):
        return any(all(i in S and j not in S for (i,j) in u) for S in ideals)
    counts={'square_zero':0,'cut':0,'overlap':0,'bad_char_odd':0,'char2_outside_cut':0}
    outside_examples=[]
    for vals in product(range(q),repeat=len(radical)):
        u={pair:v for pair,v in zip(radical,vals) if v}
        sq=square_zero_derivation(u)
        cu=cut(u)
        counts['square_zero']+=sq
        counts['cut']+=cu
        counts['overlap']+=sq and cu
        if q%2 and sq != cu:
            counts['bad_char_odd']+=1
            outside_examples.append(u)
        if q%2==0 and sq and not cu:
            counts['char2_outside_cut']+=1
            if len(outside_examples)<2:outside_examples.append(u)
    return len(basis),len(radical),counts,outside_examples


def chain(n):
    return [[int(i<=j) for j in range(n)] for i in range(n)]


def diamond():
    return [[1,1,1,1],[0,1,0,1],[0,0,1,1],[0,0,0,1]]


def fork():
    return [[1,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


def chain_formula(n,q):
    return q**(n-1)+sum(q**(r*(n-r))-q**((r-1)*(n-r)) for r in range(2,n))


def run():
    count=0
    for n,q in [(2,2),(2,3),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,2)]:
        d,m,c,outs = model(chain(n),q)
        if q%2:
            assert c['square_zero']==c['cut']==chain_formula(n,q), (n,q,c)
        else:
            assert c['cut']==chain_formula(n,q),(n,q,c)
            if n<=3: assert c['square_zero']==c['cut'],(n,q,c)
            if n==4: assert c['square_zero']==2*q**4-q**2,(n,q,c)
        assert c['bad_char_odd']==0,(n,q,c,outs)
        print('chain n=%d q=%d basis=%d radical=%d counts=%r extra_examples=%r'%(n,q,d,m,c,outs))
        count+=1
    for name,le in [('diamond',diamond()),('fork',fork())]:
        for q in (2,3,4):
            d,m,c,outs = model(le,q)
            if q%2: assert c['square_zero']==c['cut'],(name,q,c,outs)
            print('%s q=%d basis=%d radical=%d counts=%r extra_examples=%r'%(name,q,d,m,c,outs))
            count+=1
    print('INCIDENCE_SQUARE_ZERO_CUT_OK %d finite exhaustive parameter cases' % count)

if __name__=='__main__':run()
