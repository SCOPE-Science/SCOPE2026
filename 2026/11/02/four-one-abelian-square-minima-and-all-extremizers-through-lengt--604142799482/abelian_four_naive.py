#!/usr/bin/env python3
"""Independent direct substring checker: brute-force word/substrings; finite lengths <= 18."""
from itertools import combinations
from collections import defaultdict

def direct(word):
    n=len(word)
    found=set()
    for s in range(n):
        for half in range(1,(n-s)//2+1):
            left=word[s:s+half];right=word[s+half:s+2*half]
            if left.count('1')==right.count('1'):
                found.add(word[s:s+2*half])
    return len(found)

def formula(word):
    positions=[i for i,x in enumerate(word) if x=='1']
    assert len(positions)==4
    a,b,c,d=positions
    r=[a,b-a-1,c-b-1,d-c-1,len(word)-1-d]
    count=max(r)//2
    for g in set(r[1:4]):
        rect=[(r[i],r[i+2]) for i in (0,1,2) if r[i+1]==g]
        for u in range(max(L for L,_ in rect)+1):
            rr=max((R for L,R in rect if u<=L),default=-1)
            for v in range(rr+1):
                if abs(u-v)<=g and (u-v-g)%2==0:count+=1
    for u in range(r[0]+1):
        for v in range(r[4]+1):
            if r[1]-r[2]-r[3] <= v-u <= r[1]+r[2]-r[3] and (u+v+r[1]+r[2]+r[3])%2==0:
                count+=1
    return count

def verify(top=18):
    for n in range(4,top+1):
        mn=n; cnt=0; tot=0
        for p in combinations(range(n),4):
            w=['0']*n
            for x in p:w[x]='1'
            s=''.join(w)
            f=formula(s);v=direct(s)
            if f!=v: raise AssertionError((n,p,f,v))
            tot+=1
            if v<mn:mn=v;cnt=1
            elif v==mn:cnt+=1
        print(n,mn,cnt,tot,flush=True)
if __name__=='__main__':verify()
