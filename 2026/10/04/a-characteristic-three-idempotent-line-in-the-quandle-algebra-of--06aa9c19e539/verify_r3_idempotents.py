#!/usr/bin/env python3
"""Exact finite-field consistency checks for the R3 quandle-algebra idempotent classification."""

def mul_vec(x, y, add, mul, zero):
    out=[zero,zero,zero]
    for i,xi in enumerate(x):
        for j,yj in enumerate(y):
            k=(2*j-i)%3
            out[k]=add(out[k],mul(xi,yj))
    return tuple(out)

def prime_check(p):
    add=lambda a,b:(a+b)%p
    mul=lambda a,b:(a*b)%p
    elems=list(range(p))
    ids=[]
    for a in elems:
      for b in elems:
       for c in elems:
        x=(a,b,c)
        if mul_vec(x,x,add,mul,0)==x:
          ids.append(x)
    inv3=pow(3,-1,p) if p!=3 else None
    if p!=3:
      w=(inv3,inv3,inv3)
      pred={(0,0,0),(1,0,0),(0,1,0),(0,0,1),w}
      for i in range(3):
        v=[(-inv3)%p]*3
        v[i]=(1-inv3)%p
        pred.add(tuple(v))
      assert set(ids)==pred, (p,ids,pred)
      assert len(ids)==8
    else:
      inv2=pow(2,-1,p)
      pred={(0,0,0)}
      for u in elems:
        pred.add(((u*u+u)*inv2%p,(u*u-u)*inv2%p,(1-u*u)%p))
      assert set(ids)==pred
      assert len(ids)==p+1
    print(f'F_{p}: {len(ids)} idempotents OK')

# GF(9)=F3[t]/(t^2+1), represented by a+bt.
def gf9_add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def gf9_neg(x): return ((-x[0])%3,(-x[1])%3)
def gf9_mul(x,y):
    a,b=x; c,d=y
    return ((a*c-b*d)%3,(a*d+b*c)%3)
def gf9_eq(x,y): return x==y

def gf9_check():
    E=[(a,b) for a in range(3) for b in range(3)]
    Z=(0,0); O=(1,0); inv2=(2,0)
    ids=[]
    for a in E:
      for b in E:
       for c in E:
        x=(a,b,c)
        if mul_vec(x,x,gf9_add,gf9_mul,Z)==x:
          ids.append(x)
    pred={(Z,Z,Z)}
    for u in E:
      u2=gf9_mul(u,u)
      a=gf9_mul(inv2,gf9_add(u2,u))
      b=gf9_mul(inv2,gf9_add(u2,gf9_neg(u)))
      c=gf9_add(O,gf9_neg(u2))
      pred.add((a,b,c))
    assert set(ids)==pred
    assert len(ids)==10
    print('F_9: 10 idempotents (affine-line family plus zero) OK')

for p in (2,3,5,7,11): prime_check(p)
gf9_check()
print('CHECK_OK')
