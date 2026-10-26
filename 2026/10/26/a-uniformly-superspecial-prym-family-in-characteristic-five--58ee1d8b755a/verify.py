"""Exact polynomial-ring and finite-field checks for the superspecial Prym family.

Python 3 standard library only. Arithmetic polynomial identities hold in F_5[a,x],
not merely for a finite list of parameter values.
"""
P=5

def add(*ps):
    v={}
    for p in ps:
        for mon,c in p.items(): v[mon]=(v.get(mon,0)+c)%P
    return {mon:c for mon,c in v.items() if c}

def mul(p,q):
    v={}
    for (i,j),c in p.items():
        for (u,w),d in q.items():
            mon=(i+u,j+w)
            v[mon]=(v.get(mon,0)+c*d)%P
    return {mon:c for mon,c in v.items() if c}

def scalar(p,c): return {mon:(v*c)%P for mon,v in p.items() if v*c%P}
def pw(p,n):
    z={(0,0):1}
    for _ in range(n): z=mul(z,p)
    return z

def xcoeff(p,n):
    return {j:c for (i,j),c in p.items() if i==n}

X={(1,0):1}; A={(0,1):1}; ONE={(0,0):1}
f=add(pw(X,5), mul(A,pw(X,3)), X)
f3=pw(f,3)
assert xcoeff(f3,4)=={}
assert xcoeff(f3,9)=={3:1,1:1}
assert xcoeff(f3,14)=={}
assert xcoeff(f,4)=={}
assert xcoeff(mul(f,X),4)=={1:1}
assert xcoeff(mul(f,pw(X,2)),4)=={}
h=add(pw(X,6), scalar(mul(A,pw(X,3)),-2), pw(A,2),scalar(ONE,-4))
h2=pw(h,2)
assert xcoeff(h2,4)=={} and xcoeff(h2,8)=={}
assert xcoeff(h2,3)=={3:1,1:1}  # a(a^2-4) modulo 5
assert xcoeff(h2,9)=={1:1}

# GF(25) = GF(5)[u]/(u^2-2): u^5=-u.
def fm(z,t):
    a,b=z; c,d=t
    return ((a*c+2*b*d)%5,(a*d+b*c)%5)
def cube(z): return fm(fm(z,z),z)
field=[(a,b) for a in range(5) for b in range(5)]
counts={}
for z in field:
    v=cube(z)
    counts[v]=counts.get(v,0)+1
# For a=0, y^3=x^5+x = (2*x_0,0) in this representation.
n_affine=sum(counts.get(((2*x[0])%5,0),0) for x in field)
assert n_affine+1==66
print('VERIFY_OK: identities in F5[a,x] for all parameters, Cartier matrices of both curves, genus-four point count 66 over F25 at a=0')
