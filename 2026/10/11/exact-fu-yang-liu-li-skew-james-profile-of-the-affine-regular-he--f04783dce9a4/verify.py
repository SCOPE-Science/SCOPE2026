from fractions import Fraction
from math import gcd

def N(v):
    s,u=v
    return max(abs(s),abs(u),abs(s-u))

def Q(v):
    s,u=v
    return (u,u-s)

def R(v):
    s,u=v
    return (s,s-u)

# Isometry checks on an exact integer grid.
for s in range(-5,6):
    for u in range(-5,6):
        v=(Fraction(s),Fraction(u))
        assert N(Q(v))==N(v)
        assert N(R(v))==N(v)

def L(t):
    return (t*t+t+1)/(t+1)

def skew(x,y,t):
    a=N((x[0]+t*y[0],x[1]+t*y[1]))
    b=N((t*x[0]-y[0],t*x[1]-y[1]))
    return min(a,b),a,b

# Exact formulas and inequalities on rational test grids.
ts=[]
for q in range(1,11):
    for p in range(1,q+1):
        if gcd(p,q)==1:
            ts.append(Fraction(p,q))

grid=sorted({Fraction(k,q) for q in range(1,11) for k in range(q+1)})

checked=0
for t in ts:
    target=L(t)

    # Equality family on E1.
    x=(Fraction(1),Fraction(0))
    y=(t/(1+t),Fraction(1))
    val,A,B=skew(x,y,t)
    assert A==target and B==target and val==target

    # Equality family on E2.
    x2=(Fraction(1),Fraction(1)/(1+t))
    y2=(Fraction(0),Fraction(1))
    val,A,B=skew(x2,y2,t)
    assert A==target and B==target and val==target

    for a in grid:
        x=(Fraction(1),a)

        # E0
        for b in grid:
            y=(Fraction(1),b)
            val,A,B=skew(x,y,t)
            assert B<=1
            assert val<=target
            checked+=1

        # E3
        for b in grid:
            y=(Fraction(-1),-b)
            val,A,B=skew(x,y,t)
            assert A<=1
            assert val<=target
            checked+=1

        # E1 and exact formulas.
        for c in grid:
            y=(c,Fraction(1))
            val,A,B=skew(x,y,t)
            A0=max(1+t*c,a+t)
            B0=1-t*a+max(Fraction(0),t-c)
            assert A==A0 and B==B0
            assert val<=target
            checked+=1

        # E2 and exact formulas.
        for b in grid:
            y=(-b,1-b)
            val,A,B=skew(x,y,t)
            A0=-t*b+max(Fraction(1),a+t)
            B0=max(t+b,1+t-t*a)
            assert A==A0 and B==B0
            assert val<=target
            checked+=1

# Reciprocal algebra and sample equality for t>=1.
for t0 in ts:
    t=1/t0
    target=L(t)
    rhs=t*L(1/t)
    assert target==rhs

print(f"VERIFY_OK rational_t={len(ts)} edge_checks={checked} profile=(t^2+t+1)/(t+1)")
