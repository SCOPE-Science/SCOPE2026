from math import factorial
from itertools import product
P=(2,3,5,7,11,13)

def vals(n):
    out=[]
    for p in P:
        e=0
        while n%p==0:
            n//=p;e+=1
        out.append(e)
    assert n==1
    return tuple(out)

def coords(e):
    e2,e3,e5,e7,e11,e13=e
    return (e2-e3-2*e5-e13,
            e3-e5-e7-e11-e13,
            e5-e7-e11,
            e7-e11,
            e11-e13,
            e13)

def criterion(c):
    c1,c2,c3,c4,c5,c6=c
    r0=max(0,-c3)
    m=min(c4,c6)
    rhs=max(0,-c2,r0,(3*r0-c1+1)//2)
    return c5>=0 and m>=rhs

def brute(c):
    c1,c2,c3,c4,c5,c6=c
    if c5<0: return False
    for r in range(max(0,-c3), max(0,min(c4,c6))+1):
        for s in range(0,max(0,min(c4,c6)-r)+1):
            t=r+s
            a=(c1-r+2*s,c2+t,c3+r,c4-t,c5,c6-t)
            if min(a)>=0:return True
    return False
basis=[vals(factorial(p)) for p in P]
# columns should be unimodular triangular; check coordinates of basis are standard units
for j,b in enumerate(basis):
    cc=coords(b)
    assert cc==tuple(1 if i==j else 0 for i in range(6)),(j,b,cc)
expected={
2:(1,0,0,0,0,0),3:(0,1,0,0,0,0),4:(2,1,0,0,0,0),5:(0,0,1,0,0,0),6:(0,1,1,0,0,0),7:(0,0,0,1,0,0),8:(3,0,0,1,0,0),9:(1,2,0,1,0,0),10:(0,1,1,1,0,0),11:(0,0,0,0,1,0),12:(1,1,0,0,1,0),13:(0,0,0,0,0,1),14:(1,-1,-1,1,0,1),15:(-2,-1,0,1,0,1),16:(2,-1,0,1,0,1)}
for k,c in expected.items():
    got=coords(vals(factorial(k)))
    assert got==c,(k,got,c)
assert tuple(expected[15][i]+4*(i==0) for i in range(6))==expected[16]
# exact equivalence on a substantial rectangular box
checks=0
for c1 in range(-8,13):
 for c2 in range(-6,11):
  for c3 in range(-5,9):
   for c4 in range(-2,8):
    for c5 in range(-2,6):
     for c6 in range(0,8):
      c=(c1,c2,c3,c4,c5,c6);checks+=1
      assert criterion(c)==brute(c),c
# verify canonical witnesses for generated tuples r,s,a small
canon=0
u=expected[14];v=expected[15]
for r in range(5):
 for s in range(5):
  for a in product(range(3), repeat=6):
    c=tuple(a[i]+r*u[i]+s*v[i] for i in range(6))
    assert criterion(c)
    c1,c2,c3,c4,c5,c6=c
    rr=max(0,-c3);m=min(c4,c6);ss=m-rr
    aa=(c1+2*m-3*rr,c2+m,c3+rr,c4-m,c5,c6-m)
    assert min(aa)>=0 and ss>=0
    rec=tuple(aa[i]+rr*u[i]+ss*v[i] for i in range(6))
    assert rec==c
    canon+=1
print('VERIFY_OK')
print('factorials_checked=2..16')
print('box_equivalence_checks='+str(checks))
print('generated_canonical_checks='+str(canon))
print('u14='+str(u))
print('v15='+str(v))
