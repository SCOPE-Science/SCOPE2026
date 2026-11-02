#!/usr/bin/env python3
"""Finite exact sanity checks for capped-counting semirings and a first-order witness."""
from itertools import product

def add(a,b,M): return min(M,a+b)
def mul(a,b,M): return min(M,a*b)
def val_theta(values,M):
    n=len(values)
    acc=0
    for t in values:
        power=1
        for _ in range(n): power=mul(power,t,M)
        acc=add(acc,power,M)
    return acc

def val_exist(values,M):
    a=0
    for v in values: a=add(a,v,M)
    return a

def run():
    count_axioms=count_ext=count_witness=0
    for M in range(1,8):
        K=range(M+1)
        for a,b,c in product(K,repeat=3):
            assert add(a,add(b,c,M),M)==add(add(a,b,M),c,M)
            assert mul(a,mul(b,c,M),M)==mul(mul(a,b,M),c,M)
            assert mul(a,add(b,c,M),M)==add(mul(a,b,M),mul(a,c,M),M)
            assert add(a,b,M)==add(b,a,M)
            assert mul(a,b,M)==mul(b,a,M)
            count_axioms+=1
        for n in range(1,4):
            for vals in product(K,repeat=n):
                before=val_theta(vals,M)
                for u in K:
                    after=val_theta(vals+(u,),M)
                    assert before<=after, (M,vals,u,before,after)
                    count_ext+=1
        for t in (1,2) if M>=2 else (1,):
            x=val_theta((t,),M)
            y=val_theta((t,0),M)
            assert x==t and y==mul(t,t,M)
            count_witness+=1
        if M<=2:
            for n in range(1,5):
                for vals in product(K,repeat=n):
                    assert val_theta(vals,M)==val_exist(vals,M)
        else:
            assert val_theta((1,),M)==val_theta((1,0),M)==1
            assert val_theta((2,),M)==2
            assert val_theta((2,0),M)==min(M,4)>2
    print(f'ALL_CHECKS_OK axioms={count_axioms} extension_pairs={count_ext} witness_cases={count_witness}')
if __name__=='__main__': run()
