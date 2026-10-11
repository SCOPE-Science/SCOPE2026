#!/usr/bin/env python3
import cmath
from collections import defaultdict
A=[0,1,3,4,9,10]
fib=defaultdict(list)
for i in range(6):
    for j in range(i+1,6):
        fib[A[i]+A[j]].append((i,j))
coll={s:p for s,p in fib.items() if len(p)==2}
assert coll=={4:[(0,3),(1,2)],10:[(0,5),(1,4)],13:[(2,5),(3,4)]}
rows=[]
for s in [4,10,13]:
    (i,j),(k,l)=coll[s]
    r=[0]*6
    r[i]+=1;r[j]+=1;r[k]-=1;r[l]-=1
    rows.append(r)
assert [rows[0][j]-rows[1][j]+rows[2][j] for j in range(6)]==[0]*6
S=set(A)
for i in range(6):
    for j in range(i+1,6):
        s=A[i]+A[j]
        if s%2==0:
            assert s//2 not in S
w=cmath.exp(2j*cmath.pi/3)
c=[w*w,1,w,1,1,1]
conv=defaultdict(complex)
for i,a in enumerate(A):
    for j,b in enumerate(A):
        conv[a+b]+=c[i]*c[j]
moment=sum(abs(z)**2 for z in conv.values())
assert abs(moment-54)<1e-10
inter=[]
for r in rows:
    z=1+0j
    for j,e in enumerate(r):
        if e==1:z*=c[j]
        elif e==-1:z/=c[j]
    inter.append(z.real)
assert all(abs(x+0.5)<1e-10 for x in inter)
assert abs(66+8*sum(inter)-54)<1e-10
for k in range(10001):
    u=k/10000
    assert 2*(u-0.5)**2-1.5>=-1.5000000000001
print("VERIFY_OK support=6 collisions=3 dependency=1 exact_moment=54")
