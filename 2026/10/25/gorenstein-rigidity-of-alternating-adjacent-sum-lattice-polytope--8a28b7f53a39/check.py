#!/usr/bin/env python3
"""Exact arithmetic checks for alternating adjacent-sum lattice polytopes.

For d>=2, s>=1: P={x>=0, x_i+x_{i+1}<=s+(i is even)}.
This finite checker corroborates a separate all-parameter facet proof.
"""
from math import comb

def count(d, s, t):
    if t == 0: return 1
    dp = [1] * (s*t+1)
    for e in range(1,d):
        cap = (s + (e%2==0))*t
        partial=[]
        z=0
        for v in dp:
            z+=v
            partial.append(z)
        ndp=[0]*(cap+1)
        for y in range(cap+1):
            k=min(len(dp)-1,cap-y)
            if k>=0: ndp[y]=partial[k]
        dp=ndp
    return sum(dp)

def hstar(d,s):
    L=[count(d,s,t) for t in range(d+1)]
    h=[sum((-1)**j*comb(d+1,j)*L[k-j] for j in range(k+1)) for k in range(d+1)]
    while h and h[-1]==0: h.pop()
    return h

def gorenstein(d,s):
    h=hstar(d,s)
    return h==h[::-1]

def main():
    checks=0
    for d in range(2,11):
      for s in range(1,9):
        actual=gorenstein(d,s)
        expected=(s==1 and d%2==0) or (d==2 and s==3)
        assert actual==expected,(d,s,hstar(d,s))
        checks+=1
    for d,s in [(2,1),(2,3),(3,1),(3,2),(4,1),(4,3),(5,1),(6,1)]:
      print('d=%d s=%d h*=%s'%(d,s,hstar(d,s)))
    print('ALTERNATING_GORENSTEIN_CHECK_OK cases=%d'%checks)
if __name__=='__main__': main()
