#!/usr/bin/env python3
"""Independent scalar census; no bit-mask set intersection or imported verifier."""
from math import isqrt
import json


def is_prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))


def scalar_minimum(p):
    squares={i*i%p for i in range(1,(p+1)//2)}
    least=p
    attaining=None
    count_reps=0
    for u in range(2,p):
        for v in range(u+1,p):
            labels=(0,1,u,v)
            freq=[0]*16
            for z in range(p):
                if z in labels:continue
                code=0
                for j,a in enumerate(labels):
                    if (z-a)%p in squares:
                        code|=(1<<j)
                freq[code]+=1
            count_reps+=1
            val=min(freq)
            if val<least:
                least=val
                attaining=[list(labels),freq.index(val),val]
    return [p,least,count_reps,attaining]

if __name__=='__main__':
    tests=[p for p in range(7,212) if p%4==3 and is_prime(p)]
    result=[scalar_minimum(p) for p in tests]
    assert [(r[0],r[1]) for r in result if r[0]>=107 and r[1]<2]==[]
    assert [(r[0],r[1]) for r in result if r[0]<107 and r[1]>=2]==[]
    print(json.dumps({'independent_scalar_census':result,'conclusion':'PASS'},indent=2))
