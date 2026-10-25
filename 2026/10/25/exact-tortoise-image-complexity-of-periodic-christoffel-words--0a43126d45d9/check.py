#!/usr/bin/env python3
"""Exact checks for tortoise-image counts of periodic mechanical words.
Uses only Python 3 standard library and integer arithmetic.
"""
from math import gcd

def tortoise(w):
    i = w.find('1')
    return w if i < 0 else w[:i] + w[i+1:] + '1'

def mechanical_period(p, q):
    return ''.join(str((i+1)*p//q - i*p//q) for i in range(q))

def expected(p, q, n):
    a=(q-1)//p
    return n+1-min(n-1,a) if n < q else min(q,n-a)

def check():
    cases=lengths=0
    for q in range(2,51):
        for p in range(1,q):
            if gcd(p,q) != 1: continue
            period=mechanical_period(p,q)
            assert len(period)==q and period.count('1')==p
            text=period*4
            for n in range(1,2*q+2):
                factors={text[i:i+n] for i in range(q)}
                obs=len({tortoise(f) for f in factors})
                pred=expected(p,q,n)
                assert obs==pred,(p,q,n,obs,pred)
                assert len(factors)==(min(n+1,q) if n<q else q)
                lengths+=1
            cases+=1
    print('PASS: %d coprime pairs, %d exact factor-image enumerations' %(cases,lengths))
    # An independent boundary sample verifies the claimed transient drop.
    for p,q in [(1,9),(2,5),(2,11),(3,8),(6,11)]:
        per=mechanical_period(p,q)
        seq=per*4
        obs=[len({tortoise(seq[i:i+n]) for i in range(q)}) for n in range(q-1,q+(q-1)//p+2)]
        pred=[expected(p,q,n) for n in range(q-1,q+(q-1)//p+2)]
        assert obs==pred
    print('PASS: rational boundary and stabilization checks')
if __name__ == '__main__':check()
