from itertools import product
from collections import Counter
from math import comb

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):c[i+j]+=ai*bj
    return c

def poly_add(*arrs):
    q=[0]*max(map(len,arrs))
    for arr in arrs:
        for i,x in enumerate(arr):q[i]+=x
    return q

def poly_pow(a,n):
    q=[1]
    for _ in range(n):q=poly_mul(q,a)
    return q

def formula(ms):
    A=[poly_pow([1,1,1],m) for m in ms]
    def B(m,typ):
        z=poly_pow([1,1,1],m);z[0]-=1
        if typ==0 and m>=2:z[1]-=m
        return z
    pa=[1];p1=[1];p0=[1]
    for m,a in zip(ms,A):
        pa=poly_mul(pa,a);p1=poly_mul(p1,B(m,1));p0=poly_mul(p0,B(m,0))
    return poly_add([0,0]+pa,[0]+p1,p0)

def enum(ms):
    sizes=[1]+list(ms);block=[0]
    for i,m in enumerate(ms,1):block.extend([i]*m)
    n=len(block);out=Counter()
    for vals in product(range(3),repeat=n):
        valid=True
        for v in range(n):
            if vals[v]:continue
            s=0
            for u in range(n):
                if u!=v and (block[u]==0 or block[v]==0 or block[u]==block[v]):s+=vals[u]
            if s<2:valid=False;break
        if valid:out[sum(vals)]+=1
    return [out[k] for k in range(2*n+1)]

count=0;assignments=0
for r in range(2,5):
    for ms in product(range(1,4),repeat=r):
        if sum(ms)>10:continue
        f=formula(ms);e=enum(ms)
        assert f==e,(ms,f,e)
        count+=1;assignments+=3**(1+sum(ms))
print('VERIFY_OK',count,'clique bouquets',assignments,'label assignments')
for ms in ((1,1),(2,2),(2,3,3),(3,3,3),(1,1,2),(1,2,3)):
    print(ms,formula(ms))
