from fractions import Fraction
from itertools import product

V=[(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)]
LO=Fraction(0)
HI=Fraction(1,2)

def N(z):
    s,t=z
    return max(abs(s),abs(t),abs(s-t))

def lin_forms(x,y):
    a0,a1=Fraction(y[0]),Fraction(x[0]-y[0])
    b0,b1=Fraction(y[1]),Fraction(x[1]-y[1])
    return [(a0,a1),(b0,b1),(a0-b0,a1-b1)]

def eval_lin(L,m):
    return L[0]+L[1]*m

def roots_abs_equal(A,B):
    out=set()
    for sign in (1,-1):
        c0=A[0]+sign*B[0]
        c1=A[1]+sign*B[1]
        if c1:
            r=-c0/c1
            if LO <= r <= HI:
                out.add(r)
    return out

def square_poly(L):
    a,b=L
    return (a*a,2*a*b,b*b)

def add_poly(P,Q):
    return tuple(a+b for a,b in zip(P,Q))

def objective_poly(L,D2):
    return add_poly(square_poly(L),(Fraction(0),Fraction(D2),Fraction(-D2)))

def peval(P,m):
    return P[0]+P[1]*m+P[2]*m*m

def quad_nonnegative(P,lo=LO,hi=HI):
    vals=[peval(P,lo),peval(P,hi)]
    a,b,c=P
    if c>0:
        v=-b/(2*c)
        if lo <= v <= hi:
            vals.append(peval(P,v))
    return min(vals) >= 0

pieces=set()
records=[]
for x,y in product(V,repeat=2):
    L=lin_forms(x,y)
    breaks={LO,HI}
    for i in range(3):
        for j in range(i+1,3):
            breaks |= roots_abs_equal(L[i],L[j])
    breaks=sorted(breaks)
    D2=N((x[0]-y[0],x[1]-y[1]))**2
    for a,b in zip(breaks,breaks[1:]):
        if a==b:
            continue
        mid=(a+b)/2
        vals=[abs(eval_lin(T,mid)) for T in L]
        k=max(range(3),key=lambda i: vals[i])
        P=objective_poly(L[k],D2)
        pieces.add(P)
        records.append((x,y,a,b,P))

expected={
    (Fraction(1),Fraction(0),Fraction(0)),
    (Fraction(1),Fraction(1),Fraction(-1)),
    (Fraction(1),Fraction(2),Fraction(-3)),
}
assert pieces == expected

top=(Fraction(1),Fraction(2),Fraction(-3))
for P in pieces:
    diff=tuple(a-b for a,b in zip(top,P))
    assert quad_nonnegative(diff)

target=[r for r in records if r[0]==(1,1) and r[1]==(0,-1)]
assert target
for _,_,a,b,P in target:
    assert P == top

assert peval(top,Fraction(0)) == 1
assert peval(top,Fraction(1,3)) == Fraction(4,3)
assert peval(top,Fraction(1,2)) == Fraction(5,4)
assert Fraction(2,6) == Fraction(1,3)

print("VERIFY_OK")
