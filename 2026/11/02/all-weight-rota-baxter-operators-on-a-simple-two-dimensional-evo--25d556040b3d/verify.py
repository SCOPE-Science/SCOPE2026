#!/usr/bin/env python3
"""Independent finite-field check of the complete Rota--Baxter classification."""
from itertools import product


def field(q):
    if q in (4, 8):
        modulus = {4: 0b111, 8: 0b1011}[q]
        degree = {4: 2, 8: 3}[q]
        def add(x,y): return x ^ y
        def mul(x,y):
            z=0
            while y:
                if y & 1: z ^= x
                y >>= 1
                x <<= 1
                if x & (1 << degree): x ^= modulus
            return z
    else:
        def add(x,y): return (x+y)%q
        def mul(x,y): return (x*y)%q
    neg=lambda x: next(y for y in range(q) if add(x,y)==0)
    return add,mul,neg


def all_solutions(q, weight):
    add,mul,neg=field(q)
    sq=lambda x:mul(x,x)
    solutions=[]
    for a,b,c,d in product(range(q),repeat=4):
        cd=mul(c,d)
        if cd != add(add(mul(a,c),mul(b,c)),sq(b)): continue
        if mul(a,b) != add(sq(c),mul(b,d)): continue
        twice_a=add(a,a)
        twice_d=add(d,d)
        if sq(c) != mul(add(twice_a,weight),b): continue
        if add(sq(a),sq(c)) != mul(add(twice_a,weight),d):continue
        if sq(d) != mul(add(twice_d,weight),add(a,b)):continue
        if add(sq(d),sq(b)) != mul(add(twice_d,weight),add(c,d)):continue
        solutions.append((a,b,c,d))
    return set(solutions)


def expected_solutions(q, weight):
    add,mul,neg=field(q)
    roots=[t for t in range(q) if mul(t,mul(t,t))==add(mul(t,t),1)]
    ans={(0,0,0,0)}
    if weight:
        ans.add((neg(weight),0,0,neg(weight)))
        for u in roots:
            for v in roots:
                if u==v:continue
                diff=add(u,neg(v))
                inv=next(z for z in range(1,q) if mul(diff,z)==1)
                # Project onto K(1,u) along K(1,v): [[-v, 1],[-uv,u]]/(u-v).
                s=mul(neg(weight),inv)
                ans.add((mul(s,neg(v)),s,mul(s,neg(mul(u,v))),mul(s,u)))
    elif q==31:
        t=11
        for scalar in range(q):
            ans.add((mul(scalar,neg(t)),scalar,
                     mul(scalar,neg(mul(t,t))),mul(scalar,t)))
    return ans,len(roots)


def main():
    for q in (2,3,4,5,7,8,11,13,31):
        for weight in (0,1):
            actual=all_solutions(q,weight)
            expected, m=expected_solutions(q,weight)
            if actual != expected:
                raise AssertionError((q,weight,len(actual),len(expected),
                    list(actual-expected)[:5],list(expected-actual)[:5]))
            print(f'GF({q}) weight={weight}: roots={m}, operators={len(actual)} OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
