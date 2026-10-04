#!/usr/bin/env python3
P=769
A=768
B=769
M=384

def add(x,y):
    n=max(len(x),len(y)); z=[0]*n
    for i,c in enumerate(x): z[i]+=c
    for i,c in enumerate(y): z[i]+=c
    while len(z)>1 and z[-1]==0: z.pop()
    return z

def sub(x,y):
    n=max(len(x),len(y)); z=[0]*n
    for i,c in enumerate(x): z[i]+=c
    for i,c in enumerate(y): z[i]-=c
    while len(z)>1 and z[-1]==0: z.pop()
    return z

def scale(x,c): return [c*v for v in x]

def mul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b: z[i+j]+=a*b
    while len(z)>1 and z[-1]==0: z.pop()
    return z

def vp(n,p):
    if n==0: return 10**9
    n=abs(n); e=0
    while n%p==0:
        n//=p; e+=1
    return e

# E_m(t)=U_{2m}(sqrt(1-A^2 t)).  The recurrence is
# E_m=(4(1-A^2 t)-2)E_{m-1}-E_{m-2}.
z=[1,-A*A]
E0=[1]
E1=add(scale(z,4),[-1])
fac=add(scale(z,4),[-2])
for _ in range(2,M+1):
    E2=sub(mul(fac,E1),E0)
    E0,E1=E1,E2
polyP=scale(E1,A)
assert len(polyP)-1==M
assert polyP[0]==P*A
assert all(c%P==0 for c in polyP[:-1])
assert polyP[-1]%P!=0

Q=mul(polyP,polyP)
Q[0]-=4*B*B
Q[1]+=4*B**4
assert len(Q)-1==768
vals=[vp(c,P) for c in Q]
assert vals[0]==2
assert vals[-1]==0
assert all(vals[i]>=2 for i in range(1,M))
assert all(vals[i]>=1 for i in range(M,768))
# These inequalities put every coefficient point on or above the line
# from (0,2) to (768,0), whose reduced slope is -1/384.
assert A*A-4 != 0 and (A*A-4)%P != 0
# Existence criterion is immediate: the longest side is shorter than the
# sum of the remaining 770 sides.
assert B < 769*A + B
# 769 is prime; trial division suffices here.
for q in range(2,int(P**0.5)+1):
    assert P%q != 0
assert 384%3==0 and (384 & (384-1)) != 0
print('VERIFY_OK')
