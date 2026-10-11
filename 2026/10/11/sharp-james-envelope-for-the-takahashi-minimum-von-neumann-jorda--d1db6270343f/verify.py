from fractions import Fraction

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

grid=sorted({Fraction(k,q) for q in range(1,41) for k in range(q+1)})
checks=0

# Four reduced James edge classes.
for a in grid:
    x=(Fraction(1),a)
    assert N(x)==1

    for b in grid:
        y=(Fraction(1),b)
        assert N(y)==1
        assert min(N((x[0]+y[0],x[1]+y[1])), N((x[0]-y[0],x[1]-y[1]))) <= Fraction(3,2)
        checks += 1

        y=(-Fraction(1),-b)
        assert N(y)==1
        assert min(N((x[0]+y[0],x[1]+y[1])), N((x[0]-y[0],x[1]-y[1]))) <= Fraction(3,2)
        checks += 1

    for c in grid:
        y=(c,Fraction(1))
        A=N((x[0]+y[0],x[1]+y[1]))
        B=N((x[0]-y[0],x[1]-y[1]))
        assert A==max(Fraction(1)+c,Fraction(1)+a)
        assert B==Fraction(2)-a-c
        assert min(A,B)<=Fraction(3,2)
        checks += 1

    for b in grid:
        y=(-b,Fraction(1)-b)
        A=N((x[0]+y[0],x[1]+y[1]))
        B=N((x[0]-y[0],x[1]-y[1]))
        assert A==Fraction(1)+a-b
        assert B==max(Fraction(1)+b,Fraction(2)-a)
        assert min(A,B)<=Fraction(3,2)
        checks += 1

# Sharp James pair.
x=(Fraction(1),Fraction(1,2))
u=(Fraction(0),Fraction(1))
assert N(x)==N(u)==1
assert N((x[0]+u[0],x[1]+u[1]))==Fraction(3,2)
assert N((x[0]-u[0],x[1]-u[1]))==Fraction(3,2)

# Sharp unrestricted Takahashi witness.
p=(Fraction(1),Fraction(0))
q=(Fraction(-1,4),Fraction(-1,2))
assert N(p)==1
assert N(q)==Fraction(1,2)
ap=N((p[0]+q[0],p[1]+q[1]))
am=N((p[0]-q[0],p[1]-q[1]))
assert ap==am==Fraction(5,4)
quot=min(ap*ap,am*am)/(N(p)**2+N(q)**2)
assert quot==Fraction(5,4)

# Exact scalar envelope identity samples.
for c in grid:
    for r in grid:
        lhs=(1+c*c)*(1+r*r)-(1+c*r)*(1+c*r)
        assert lhs==(c-r)*(c-r)
        assert (1+c*r)*(1+c*r) <= (1+c*c)*(1+r*r)

print(f"VERIFY_OK edge_checks={checks} rational_grid={len(grid)} James=3/2 Cminusinf=5/4")
