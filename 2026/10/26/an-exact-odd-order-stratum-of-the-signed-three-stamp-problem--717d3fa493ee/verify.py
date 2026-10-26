#!/usr/bin/env python3
"""Exact integer checks of signed three-denomination interval-basis formulas."""
from math import gcd

def coverage(h, triple):
    a,b,c=triple
    visited={x*a+y*b+(h-x-y)*c for x in range(h+1) for y in range(h+1-x)}
    m=0
    while m in visited: m+=1
    return m-1

def best(h):
    best_value=-1
    extremizers=[]
    for a in range(1-h,0):
        for y in range(2,h+2):
            for x in range(1,y):
                if gcd(x,y)!=1:continue
                A=(a,a+x,a+y)
                got=coverage(h,A)
                if got>best_value:
                    best_value=got;extremizers=[A]
                elif got==best_value:extremizers.append(A)
    return best_value,extremizers

def main():
    tested=0
    for t in range(2,62,2):
        h=6*t-3; A=(-t,t,2*t+1)
        target=9*t*t-3
        assert coverage(h,A)==target,(t,h,A)
        tested+=1
    for h in [9,21,33]:
        t=(h+3)//6
        value,bases=best(h)
        assert value==9*t*t-3,(h,value)
        assert (-t,t,2*t+1) in bases
    print(f'CERTIFICATE_OK exact_constructions={tested} exhaustive_small_h=9,21,33')

if __name__=='__main__':main()
