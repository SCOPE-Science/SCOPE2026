#!/usr/bin/env python3
"""Independent F4 root-test census of F2-lines of smooth cubic threefold representatives.
Evaluation on all five P1(F4) points proves that the restricted cubic vanishes identically.
"""
from collections import Counter
import re
from pathlib import Path

REPS=[1118480,1118482,1118484,1118485,1118486,1118616,1118680,1118744,1118745,1122448,1122450,1122451,1122820]
# GF(4)=GF(2)[t]/(t^2+t+1), represented by two bit integers.
def mul(a,b):
    p=0
    for i in range(2):
        if (b>>i)&1: p^=a<<i
    for i in (2,):
        if (p>>i)&1: p ^= 0b111<<(i-2)
    return p

def cubic_on(a,v):
    out=0
    for i in range(5):
        for j in range(5):
            if (a>>(i*5+j))&1:
                out ^= mul(mul(v[i],v[i]),v[j])
    return out

def span_vector(u,v,lambda4):
    return [(1 if (u>>i)&1 else 0) ^ (lambda4 if (v>>i)&1 else 0) for i in range(5)]

def main():
    print('Independent GF4 geometric line verification (5 projective parameter values).')
    for a in REPS:
        pts=[u for u in range(1,32) if cubic_on(a,[(u>>i)&1 for i in range(5)])==0]
        lines=[]
        for u in range(1,32):
            for v in range(u+1,32):
                if v>=u^v: continue
                # P1(F4) = [1:0],[0:1],[1:lambda] for lambda in F4.
                if cubic_on(a,[(v>>i)&1 for i in range(5)])!=0: continue
                if any(cubic_on(a,span_vector(u,v,l))!=0 for l in range(4)): continue
                lines.append((u,v,u^v))
        c=Counter(p for line in lines for p in line)
        prof=Counter(c.get(p,0) for p in pts)
        assert sum(n for _,n in prof.items())==len(pts)
        assert sum(k*n for k,n in prof.items())==3*len(lines)
        print(f'rep={a} points={len(pts)} rational_lines={len(lines)} incidence='+','.join(f'{k}:{prof[k]}' for k in sorted(prof)))
if __name__=='__main__':main()
