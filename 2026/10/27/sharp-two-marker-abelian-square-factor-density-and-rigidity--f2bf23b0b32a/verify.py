#!/usr/bin/env python3
"""Reproduce finite checks for the sparse Abelian-square factor formula.
This checks examples, not the asymptotic theorem; see the written proof.
"""
from itertools import product
from hashlib import sha256


def H(z: int) -> int:
    return max(z, 0) ** 2 // 4


def predicted(a: int, b: int, c: int) -> int:
    ea = int(a % 2 == 0)
    ec = int(c % 2 == 0)
    all_parity = ((a + 1)*(c + 1) + (1 if b % 2 == 0 else -1)*ea*ec)//2
    two_one = (all_parity - H(a-b) - H(c-b)
               + H(a-b-c-1) + H(c-b-a-1))
    return max(a,b,c)//2 + two_one


def direct(a: int, b: int, c: int) -> int:
    w = '0'*a + '1' + '0'*b + '1' + '0'*c
    F = set()
    for i in range(len(w)):
        for h in range(1, (len(w)-i)//2 + 1):
            left = w[i:i+h]
            right = w[i+h:i+2*h]
            if left.count('1') == right.count('1'):
                F.add(left+right)
    return len(F)


def main():
    tested = 0
    for a,b,c in product(range(11),repeat=3):
        formula=predicted(a,b,c)
        brute=direct(a,b,c)
        assert formula == brute,(a,b,c,formula,brute)
        tested += 1
    print(f'EXACT FORMULA VERIFIED on {tested} gap triples [0,10]^3')
    record=[]
    for n in range(2,37):
        maxval=-1
        examples=[]
        for a in range(n-1):
            for b in range(n-1-a):
                c=n-2-a-b
                v=predicted(a,b,c)
                if v>maxval:
                    maxval=v;examples=[(a,b,c)]
                elif v==maxval:examples.append((a,b,c))
        record.append((n,maxval,examples))
    print('FINITE MAXIMA n=2..36:',[(n,v) for n,v,_ in record])
    # This checks attainability of the stated family; it does not prove global optimality.
    for t in range(1,10):
        a,b,c=3*t,2*t,3*t
        actual=predicted(a,b,c)
        proposed=4*t*t+3*t+1+(3*t)//2
        assert actual==proposed,(t,actual,proposed)
    print('EXPLICIT FAMILY IDENTITY VERIFIED at t=1..9')
    print('SUCCESS')

if __name__ == '__main__':
    main()
