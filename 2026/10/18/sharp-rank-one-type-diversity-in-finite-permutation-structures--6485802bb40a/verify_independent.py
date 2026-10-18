from itertools import permutations
from collections import Counter

counts=Counter(); n=10
for p in permutations(range(1,n+1)):
    lmin=[11]*n; lmax=[0]*n
    rmin=[11]*n; rmax=[0]*n
    mi=11;ma=0
    for i,x in enumerate(p):
        lmin[i],lmax[i]=mi,ma
        mi=min(mi,x);ma=max(ma,x)
    mi=11;ma=0
    for i in range(n-1,-1,-1):
        x=p[i];rmin[i],rmax[i]=mi,ma
        mi=min(mi,x);ma=max(ma,x)
    s=0
    for i,x in enumerate(p):
        m=(lmin[i]<x)+2*(lmax[i]>x)+4*(rmin[i]<x)+8*(rmax[i]>x)
        s|=1<<m
    if s.bit_count()==10:counts[s]+=1
assert counts == {65192:164,64744:164},counts
print('independent signature counts:',dict(counts),'total:',sum(counts.values()))
