#!/usr/bin/env python3
"""Independent antisquare-factor enumeration and finite parameter checks."""
from itertools import product
from math import comb

def formula(a,b,c,d):
    two_01=max(min(a,b),min(c,d))
    two_10=min(b,c)
    three_010=max(0,min(a,b-1)-max(1,b-c)+1)
    three_101=max(0,min(b,c-1)-max(1,c-d)+1)
    return two_01+two_10+three_010+three_101

def actual(a,b,c,d):
    w='0'*a+'1'*b+'0'*c+'1'*d
    factors=set()
    for i in range(len(w)):
        for h in range(1,(len(w)-i)//2+1):
            x=w[i:i+h]
            y=w[i+h:i+2*h]
            if all(u!=v for u,v in zip(x,y)):
                factors.add(x+y)
    return len(factors)

def equality(a,b,c,d):
    return (a in (b-1,b) and c in (b-1,b) and d<c) or (b in (c-1,c) and d in (c-1,c) and a<b)

def main():
    count=0
    for a,b,c,d in product(range(1,9),repeat=4):
        v=formula(a,b,c,d)
        assert actual(a,b,c,d)==v,(a,b,c,d,'enumeration')
        assert v<=a+b+c+d-1,(a,b,c,d,'bound')
        assert (v==a+b+c+d-1)==equality(a,b,c,d),(a,b,c,d,'equality')
        count+=1
    for n in range(4,81):
        total=0;maxima=0
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    val=formula(a,b,c,d)
                    total+=val
                    maxima=max(maxima,val)
        assert maxima==(n-1 if n>=6 else n-2),(n,maxima)
        if n in [10,20,40,80]:
            print('n=%d mean=%.10f mean_over_n=%.10f'%(n,total/comb(n-1,3),total/comb(n-1,3)/n))
    print('VERIFY_OK exhaustively_enumerated_quadruples=%d exact_bound_equality_and_extrema_n=4..80'%count)
if __name__=='__main__': main()
