#!/usr/bin/env python3
"""Finite exact checks for binary semicircle observation and backward-state maps."""
from itertools import product


def step(M,k,z,s):
    return s//2+(M//2)*(z ^ int(s>=k))


def backward(M,k,word,s):
    for z in reversed(word):
        s=step(M,k,z,s)
    return s


def outputs(bits,r,k):
    m=r-1
    M=1<<m
    result=[]
    for n in range(len(bits)-m):
        s=0
        for b in bits[n+1:n+1+m]:
            s=2*s+b
        result.append(bits[n] ^ int(s>=k))
    return tuple(result)


checks=0
for r in range(2,11):
    m=r-1
    M=1<<m
    w=(0,)*m+(1,)+(0,)*m
    for k in range(M):
        v={backward(M,k,w,s) for s in range(M)}
        if k==M//2:
            assert len(v)==2, (r,k,v)
        else:
            assert len(v)==1, (r,k,v)
            assert v==({M-1} if k<M//2 else {0})
        checks+=1
        if r<=6:
            for n in range(1,6):
                L=n+m
                counts={}
                for bits in product((0,1),repeat=L):
                    z=outputs(bits,r,k)
                    counts[z]=counts.get(z,0)+1
                    # Compare against direct dyadic position at every observation time.
                    if r<=4:
                        for j in range(n):
                            cell=sum(b<<(r-1-i) for i,b in enumerate(bits[j:j+r]))
                            assert z[j]==int(k<=cell<k+M)
                assert len(counts)==2**n
                assert set(counts.values())=={M}
                checks+=1
        if k==M//2 and r<=6:
            for bits in product((0,1),repeat=r+3):
                z=outputs(bits,r,k)
                assert all(t==(bits[i]^bits[i+1]) for i,t in enumerate(z))
                checks+=1
print(f'VERIFY_OK: {checks} exact reset, word-distribution, and XOR comparisons; r=2..10')
