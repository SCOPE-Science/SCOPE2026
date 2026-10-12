#!/usr/bin/env python3
import sys
d=int(sys.argv[1]) if len(sys.argv)>1 else 5
if d<5: raise SystemExit("require d >= 5")
dims=(2,2,d)
supports=[]
for mask in range(8):
    S=tuple(i for i in range(3) if mask&(1<<i))
    w=1
    for i in S: w*=dims[i]
    supports.append((S,w))
allowed=[S for S,w in supports if w<=4]
assert set(allowed)=={(),(0,),(1,),(0,1)}
for A in allowed:
    for B in allowed:
        U=set(A)|set(B); w=1
        for i in U: w*=dims[i]
        assert w<=4
count=1+2*(2**2-1)+(2**2-1)**2
assert count==16
print("VERIFY_OK d=%d allowed_supports=%s error_basis_count=%d"%(d,allowed,count))
