from fractions import Fraction
from math import gcd

def N(v):
    s,t=v
    return max(abs(s),abs(t),abs(s-t))

def Q(v):
    s,t=v
    return (t,t-s)

def R(v):
    s,t=v
    return (s,s-t)

# Exact isometry checks.
for s in range(-6,7):
    for t in range(-6,7):
        v=(Fraction(s),Fraction(t))
        assert N(Q(v))==N(v)
        assert N(R(v))==N(v)

# Unit-edge parametrizations and exact classical James formulas.
grid=sorted({Fraction(k,q) for q in range(1,41) for k in range(q+1)})
checks=0
for a in grid:
    x=(Fraction(1),a)
    assert N(x)==1

    for b in grid:
        y=(Fraction(1),b)                  # E0
        assert N(y)==1
        assert N((x[0]-y[0],x[1]-y[1]))==abs(a-b)
        assert min(N((x[0]+y[0],x[1]+y[1])),
                   N((x[0]-y[0],x[1]-y[1]))) <= Fraction(3,2)
        checks += 1

        y=(-Fraction(1),-b)                # E3
        assert N(y)==1
        assert N((x[0]+y[0],x[1]+y[1]))==abs(a-b)
        assert min(N((x[0]+y[0],x[1]+y[1])),
                   N((x[0]-y[0],x[1]-y[1]))) <= Fraction(3,2)
        checks += 1

    for c in grid:
        y=(c,Fraction(1))                  # E1
        assert N(y)==1
        A=N((x[0]+y[0],x[1]+y[1]))
        B=N((x[0]-y[0],x[1]-y[1]))
        assert A==1+max(a,c)
        assert B==2-a-c
        assert min(A,B)<=Fraction(3,2)
        checks += 1

    for b in grid:
        y=(-b,Fraction(1)-b)               # E2
        assert N(y)==1
        A=N((x[0]+y[0],x[1]+y[1]))
        B=N((x[0]-y[0],x[1]-y[1]))
        assert A==1+a-b
        assert B==max(1+b,2-a)
        assert min(A,B)<=Fraction(3,2)
        checks += 1

# Exact James and support-functional witness.
x=(Fraction(1),Fraction(1,2))
y=(Fraction(0),Fraction(1))
assert N(x)==N(y)==1
assert N((x[0]+y[0],x[1]+y[1]))==Fraction(3,2)
assert N((x[0]-y[0],x[1]-y[1]))==Fraction(3,2)

def fplus(v):
    return v[1]

def fminus(v):
    return v[0]-v[1]

assert fplus(y)==1
assert fplus((x[0]+y[0],x[1]+y[1]))==Fraction(3,2)
assert fminus((-y[0],-y[1]))==1
assert fminus((x[0]-y[0],x[1]-y[1]))==Fraction(3,2)

# Weighted witness and claimed profile on all reduced rational weights.
weights=[]
for q in range(2,81):
    for p in range(1,q):
        if gcd(p,q)==1:
            weights.append(Fraction(p,q))

for lam in weights:
    if lam <= Fraction(1,2):
        xx,yy=x,y
    else:
        xx,yy=y,x
    A=(lam*xx[0]+(1-lam)*yy[0], lam*xx[1]+(1-lam)*yy[1])
    B=(lam*xx[0]-(1-lam)*yy[0], lam*xx[1]-(1-lam)*yy[1])
    m=min(lam,1-lam)
    target=1-m/Fraction(2)
    assert N(A)==target
    assert N(B)==target

print(f"VERIFY_OK edge_checks={checks} rational_weights={len(weights)} JH=3/2 profile=1-min(lambda,1-lambda)/2")
