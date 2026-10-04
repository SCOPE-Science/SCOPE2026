from fractions import Fraction as F

# Sparse polynomials in variables (x,y,z,a,b), keyed by exponent 5-tuples.
N = 5
ZERO = {}

def clean(p):
    return {m:c for m,c in p.items() if c}

def add(p,q):
    r = dict(p)
    for m,c in q.items(): r[m] = r.get(m,F(0)) + c
    return clean(r)

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def scale(p,c): return clean({m:c*v for m,v in p.items()})

def mul(p,q):
    r = {}
    for m,c in p.items():
        for n,d in q.items():
            k = tuple(m[i]+n[i] for i in range(N))
            r[k] = r.get(k,F(0)) + c*d
    return clean(r)

def power(p,n):
    r = const(1)
    for _ in range(n): r = mul(r,p)
    return r

def const(c): return {(0,0,0,0,0):F(c)} if c else {}
def var(i):
    m=[0]*N; m[i]=1
    return {tuple(m):F(1)}

def deriv(p,i):
    r={}
    for m,c in p.items():
        if m[i]:
            k=list(m); k[i]-=1; k=tuple(k)
            r[k]=r.get(k,F(0))+c*m[i]
    return clean(r)

def subst(p, vals):
    # vals maps variable index to a sparse polynomial.
    r={}
    for m,c in p.items():
        term=const(c)
        for i,e in enumerate(m):
            if e:
                term=mul(term,power(vals.get(i,var(i)),e))
        r=add(r,term)
    return clean(r)

def assert_poly_equal(p,q,label):
    d=sub(p,q)
    if d:
        raise AssertionError(f'{label}: {d}')

x,y,z,a,b = [var(i) for i in range(5)]
fx = neg(z)
fy = sub(x,y)
fz = add(add(mul(a,x),power(y,2)),mul(b,z))
field=[fx,fy,fz]

def L(p):
    r={}
    for i,fi in enumerate(field): r=add(r,mul(deriv(p,i),fi))
    return clean(r)

w=sub(x,y)
v=L(w)
K=sub(add(z,mul(b,x)),mul(a,y))
assert_poly_equal(L(K),mul(y,add(y,a)),'K identity')

H=add(add(add(mul(w,v), scale(power(w,2),F(1,2))), scale(mul(b,power(w,2)),F(-1,2))),
      add(scale(mul(a,power(y,2)),F(1,2)), scale(power(y,3),F(1,3))))
rhs=sub(power(v,2),mul(sub(a,b),power(w,2)))
assert_poly_equal(L(H),rhs,'H identity')

jerk=add(add(add(add(L(v),v),neg(mul(b,v))),mul(sub(a,b),w)),add(mul(a,y),power(y,2)))
assert_poly_equal(jerk,ZERO,'jerk identity')

# Symbolic equilibrium checks: substitute x=y=z=0 and x=y=-a,z=0.
for name,vals in [
    ('E0',{0:const(0),1:const(0),2:const(0)}),
    ('E1',{0:neg(a),1:neg(a),2:const(0)})
]:
    for j,fi in enumerate(field):
        assert_poly_equal(subst(fi,vals),ZERO,f'{name} field {j}')

print('VERIFY_OK')
