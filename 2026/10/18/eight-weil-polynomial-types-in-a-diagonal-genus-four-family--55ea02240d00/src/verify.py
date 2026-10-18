#!/usr/bin/env python3
"""Exact point-count checks for the diagonal genus-four family.

No computer algebra packages are required.  The proof for arbitrary primes
uses the sextic Fermat quotient and the tame character decomposition;
these finite computations are independent consistency tests, not its proof.
"""
import json
from collections import Counter
from pathlib import Path

PAIRS = ((2,1), (1,1), (1,2), (1,3), (1,5), (2,5), (2,4), (2,3))


def character_exponents(r, s):
    return sorted((2*s*i-r*j) % 6 for i,j in PAIRS)


def cyclotomic_trace(exponents, power=1):
    counts = Counter((e*power)%6 for e in exponents)
    assert counts[1] == counts[5] and counts[2] == counts[4]
    return counts[0]-counts[3]+counts[1]-counts[2]


def factor_signature(exponents):
    c = Counter(exponents)
    assert c[1] == c[5] and c[2] == c[4]
    return [c[0], c[3], c[1], c[2]]


def field(p, nonresidue):
    """Arithmetic on F_p[u]/(u*u-nonresidue), encoded as a*p+b."""
    q = p*p
    one = p
    def add(x,y):
        a,b = divmod(x,p)
        c,d = divmod(y,p)
        return ((a+c)%p)*p+(b+d)%p
    def mul(x,y):
        a,b = divmod(x,p)
        c,d = divmod(y,p)
        return ((a*c+nonresidue*b*d)%p)*p+(a*d+b*c)%p
    def power(x,n):
        v = one
        while n:
            if n & 1:
                v = mul(v,x)
            x = mul(x,x)
            n //= 2
        return v
    def neg(x):
        a,b = divmod(x,p)
        return ((-a)%p)*p+((-b)%p)
    generator = next(x for x in range(1,q)
                     if len({power(x,j) for j in range(q-1)}) == q-1)
    log = {power(generator,j):j for j in range(q-1)}
    return q,one,add,mul,power,neg,generator,log


def count_over_quadratic(p, d):
    q,one,add,mul,power,neg,g,log = field(p,d)
    cubes = Counter(power(t,3) for t in range(q))
    sixths = [power(t,6) for t in range(q)]
    out = []
    for r in range(6):
        for s in range(3):
            B = power(g,s)
            A = power(g,r+s)
            n = sum(cubes[neg(add(mul(A,t6),B))] for t6 in sixths)
            n += 3 if log[A] % 3 == 0 else 0
            exp = character_exponents(r,s)
            theoretical = q+1+p*cyclotomic_trace(exp)
            assert n == theoretical, (p,r,s,n,theoretical)
            out.append([r,s,n,theoretical])
    return out


def count_over_fourth_for_p5():
    p,d = 5,2
    q,one,add,mul,power,neg,g,log = field(p,d)
    squares = {power(x,2) for x in range(q)}
    nonsquare = next(x for x in range(1,q) if x not in squares)
    def add4(x,y):
        a,b = divmod(x,q)
        c,e = divmod(y,q)
        return add(a,c)*q+add(b,e)
    def mul4(x,y):
        a,b = divmod(x,q)
        c,e = divmod(y,q)
        return add(mul(a,c),mul(nonsquare,mul(b,e)))*q+add(mul(a,e),mul(b,c))
    def pow4(x,n):
        v=one*q
        while n:
            if n&1:v=mul4(v,x)
            x=mul4(x,x)
            n//=2
        return v
    def neg4(x):
        a,b = divmod(x,q)
        return neg(a)*q+neg(b)
    cube_counts = Counter(pow4(x,3) for x in range(q*q))
    sixths = [pow4(x,6) for x in range(q*q)]
    out=[]
    for r in range(6):
        for s in range(3):
            A=power(g,r+s)*q
            B=power(g,s)*q
            n=sum(cube_counts[neg4(add4(mul4(A,h),B))] for h in sixths)
            n += 3 if (r+s) % 3 == 0 else 0
            theory=q*q+1-p*p*cyclotomic_trace(character_exponents(r,s),2)
            assert n == theory,(r,s,n,theory)
            out.append([r,s,n,theory])
    return out


def main():
    types={}
    for r in range(6):
        for s in range(3):
            sig=factor_signature(character_exponents(r,s))
            types.setdefault(tuple(sig),[]).append([r,s])
    spectrum=[{"signature":list(k),"parameters":v} for k,v in types.items()]
    out={"distinct_weil_types":len(types),
         "spectrum":spectrum,
         "F25":count_over_quadratic(5,2),
         "F121":count_over_quadratic(11,2),
         "F289":count_over_quadratic(17,3),
         "F625":count_over_fourth_for_p5()}
    expected=json.loads((Path(__file__).resolve().parent.parent / 'data' / 'expected.json').read_text())
    assert out==expected, 'Output differs from the checked table'
    print('PASS: all 18 twists over F25, F121, F289 and F625; eight distinct Weil types')

if __name__=='__main__':
    main()
