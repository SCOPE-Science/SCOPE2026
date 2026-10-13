#!/usr/bin/env python3
# Exact checks in Q(omega), omega^2+omega+1=0.

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    a,b=x; c,d=y
    # (a+bw)(c+dw) = ac-bd + (ad+bc-bd)w
    return (a*c-b*d, a*d+b*c-b*d)
def smul(k,x): return (k*x[0],k*x[1])
ZERO=(0,0); ONE=(1,0); W=(0,1); W2=(-1,-1)
assert mul(W,W)==W2 and mul(W2,W)==ONE

def matvec(A,v):
    out=[]
    for row in A:
        z=ZERO
        for a,x in zip(row,v): z=add(z,smul(a,x))
        out.append(z)
    return out

# Directed 3-cycle E12+E23+E31.
C3=[[0,1,0],[0,0,1],[1,0,0]]
v3=[ONE,W,W2]
assert matvec(C3,v3)==[mul(W,x) for x in v3]
assert add(add(v3[0],v3[1]),v3[2])==ZERO

# Balanced n=4, m=8 witness.
C4=[[1,1,1,1],[1,0,1,0],[0,0,0,1],[0,1,0,0]]
v4=[ZERO,W2,W,ONE]
assert sum(sum(row) for row in C4)==8
assert matvec(C4,v4)==[mul(W2,x) for x in v4]
z=ZERO
for x in v4: z=add(z,x)
assert z==ZERO

# Finite-range cross-check of the symbolic packing inequality.
for n in range(5,501):
    assert (n*n)//2 - 3 <= n*(n-3)
print('CHECK_OK')
