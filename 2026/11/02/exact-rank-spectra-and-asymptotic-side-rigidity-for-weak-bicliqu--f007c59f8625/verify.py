from itertools import product
from math import comb

def predicted(a,b):
    d={1:a+b}
    for i in range(1,a+1):
        for j in range(1,b+1):
            if i==j==1: z=2**(a+b-2)
            elif i>=2 and j==1: z=(i+1)**(a-i)
            elif i==1 and j>=2: z=(j+1)**(b-j)
            else: z=i**(a-i)*j**(b-j)
            d[i+j]=d.get(i+j,0)+comb(a,i)*comb(b,j)*z
    return d

def empirical(a,b):
    n=a+b
    d={}
    for f in product(range(n),repeat=n):
        if any(f[f[k]]!=f[k] for k in range(n)): continue
        if any(f[x]!=f[y] and (f[x]<a)==(f[y]<a) for x in range(a) for y in range(a,n)): continue
        rank=len(set(f))
        d[rank]=d.get(rank,0)+1
    return d
for a,b in [(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(1,5),(3,4)]:
    x=predicted(a,b)
    y=empirical(a,b)
    print((a,b),x,y,'OK' if x==y else 'MISMATCH')
    assert x==y

print("VERIFY_OK")
