#!/usr/bin/env python3
"""Independent labelled-state verification of majority relaxation on two bridged cliques.
Run with Python 3.9 or newer. No dependencies beyond standard library.
"""
from collections import Counter
from math import comb

def formula(a,b):
    if (a%2,b%2)==(1,1):
        ca=comb(a-1,(a-1)//2)
        cb=comb(b-1,(b-1)//2)
        return 2, 2**b*ca + 2**a*cb-2*ca*cb
    if (a%2,b%2)==(0,0):
        ca=comb(a-1,a//2-1)
        cb=comb(b-1,b//2-1)
        return 4, 2*(ca*(2**(b-2)-cb)+cb*(2**(a-2)-ca))
    if a%2:
        return 5, comb(a-1,(a-1)//2)*comb(b,b//2)
    return 5, comb(b-1,(b-1)//2)*comb(a,a//2)

def test(a,b):
    n=a+b
    masks=[]
    for i in range(n):
        if i<a:
            v=sum(1<<j for j in range(a) if j!=i)
            if i==0:v|=1<<a
        else:
            v=sum(1<<j for j in range(a,n) if j!=i)
            if i==a:v|=1
        masks.append(v)
    f=[0]*(1<<n)
    for x in range(1<<n):
        nxt=0
        for i,nb in enumerate(masks):
            v=(x&nb).bit_count()
            deg=nb.bit_count()
            if v*2>deg or (v*2==deg and (x>>i)&1):
                nxt|=1<<i
        f[x]=nxt
    histogram=Counter()
    for x in range(1<<n):
        y=x
        for t in range(7):
            z=f[y]
            if f[z]==y:
                per=1 if z==y else 2
                histogram[(t,per)]+=1
                break
            y=z
        else:
            raise AssertionError(('long orbit',a,b,x))
    T, expected_last=formula(a,b)
    assert max(t for t,p in histogram)==T,(a,b,histogram)
    assert sum(v for (t,p),v in histogram.items() if t==T)==expected_last,(a,b,histogram,expected_last)
    assert histogram[(0,1)]==4,(a,b,histogram)
    exp_two=(2*comb(a-1,a//2-1)*comb(b-1,b//2-1) if a%2==0 and b%2==0 else 0)
    assert histogram[(0,2)]==exp_two,(a,b,histogram,exp_two)
    assert sum(histogram.values())==(1<<n)
    assert all(per==1 for (t,per) in histogram if t>0), (a,b,histogram)
    return T,expected_last,sum(histogram.values()),sum(1 for k,v in histogram.items() if v)

def main():
    total=0; cases=0; bins=0
    for a in range(3,9):
        for b in range(3,9):
            T,last,states,nonzero=test(a,b)
            print(f'{a}x{b}: sharp_depth={T} depth_population={last} states={states}')
            total+=states;cases+=1;bins+=nonzero
    print(f'BARBELL_MAJORITY_VERIFY_OK cases={cases} labelled_states={total} nonzero_strata={bins}')

if __name__=='__main__':main()
