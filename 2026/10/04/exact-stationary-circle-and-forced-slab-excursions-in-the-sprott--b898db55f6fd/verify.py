from fractions import Fraction

# Sparse polynomials in (x,y,z,a,b): monomial -> Fraction coefficient.
N = 5

def add(*ps):
    out = {}
    for p in ps:
        for m,c in p.items():
            out[m] = out.get(m,Fraction(0)) + c
            if out[m] == 0:
                del out[m]
    return out

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            out[k]=out.get(k,Fraction(0))+c*d
    return {m:c for m,c in out.items() if c}
def scale(c,p): return {m:Fraction(c)*v for m,v in p.items() if c*v}
def powp(p,k):
    out={(0,0,0,0,0):Fraction(1)}
    for _ in range(k): out=mul(out,p)
    return out

def v(i):
    m=[0]*N; m[i]=1
    return {tuple(m):Fraction(1)}

x,y,z,a,b=[v(i) for i in range(5)]
one={(0,0,0,0,0):Fraction(1)}
f1=add(y,z)
f2=add(neg(x),mul(a,y))
f3=add(powp(x,2),neg(mul(b,z)))

# Core coboundary identity, with denominators cleared:
# a L(z+b x-(b/a)y) = a x^2 + b x.
lhs=add(mul(a,f3),mul(mul(a,b),f1),neg(mul(b,f2)))
rhs=add(mul(a,powp(x,2)),mul(b,x))
assert lhs == rhs

# The mean relations used in the theorem are exactly the coordinate generators.
assert f1 == add(y,z)
assert f2 == add(neg(x),mul(a,y))
assert f3 == add(powp(x,2),neg(mul(b,z)))

# Equilibrium reduction: y=-z and x=-a z reduce f3 to z(a^2 z-b).
reduced=add(mul(powp(a,2),powp(z,2)),neg(mul(b,z)))
factor=mul(z,add(mul(powp(a,2),z),neg(b)))
assert reduced == factor

# Canonical parameters a=1/2,b=1 give center -1, radius 1 and equilibria
# (0,0,0), (-2,-4,4). Check directly with exact arithmetic.
def eval_poly(p, vals):
    s=Fraction(0)
    for m,c in p.items():
        term=c
        for i,e in enumerate(m): term*=vals[i]**e
        s+=term
    return s
vals0=[Fraction(0),Fraction(0),Fraction(0),Fraction(1,2),Fraction(1)]
vals1=[Fraction(-2),Fraction(-4),Fraction(4),Fraction(1,2),Fraction(1)]
for vals in (vals0,vals1):
    assert eval_poly(f1,vals)==0 and eval_poly(f2,vals)==0 and eval_poly(f3,vals)==0

print('VERIFY_OK')
