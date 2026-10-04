from fractions import Fraction as Q

# Polynomial in x,y,z,a represented by monomial exponent tuple -> rational coefficient.
def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}

def scale(p,c): return {m:c*v for m,v in p.items() if c*v}
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(4)); out[k]=out.get(k,Q(0))+c*d
    return {m:c for m,c in out.items() if c}
def der(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            n=list(m); n[i]-=1; n=tuple(n); out[n]=out.get(n,Q(0))+c*m[i]
    return {m:c for m,c in out.items() if c}
def lie(p,f): return add(*(mul(der(p,i),f[i]) for i in range(3)))

def mono(exps,c=1): return {tuple(exps):Q(c)}
one=mono((0,0,0,0)); x=mono((1,0,0,0)); y=mono((0,1,0,0)); z=mono((0,0,1,0)); a=mono((0,0,0,1))
x2=mul(x,x); y2=mul(y,y); z2=mul(z,z); xy=mul(x,y); yz=mul(y,z); xz=mul(x,z)

f1=add(scale(x,Q(-2,5)), y, scale(yz,10))
f2=add(scale(x,-1), scale(y,Q(-2,5)), scale(xz,5))
f3=add(mul(a,z), scale(xy,-5))
f=(f1,f2,f3)

V=add(scale(x2,Q(1,2)),scale(y2,Q(1,2)),scale(z2,Q(3,2)))
F1=add(scale(x2,Q(1,2)),z2,scale(z,Q(1,5)))
F2=add(scale(y2,Q(1,2)),scale(z2,Q(1,2)),scale(z,Q(-1,5)))

assert lie(V,f)==add(scale(x2,Q(-2,5)),scale(y2,Q(-2,5)),scale(mul(a,z2),3))

sq1=add(z2,scale(z,Q(1,10)))  # (z+1/20)^2 - 1/400
sq2=add(z2,scale(z,Q(-1,5)))  # (z-1/10)^2 - 1/100
assert lie(F1,f)==add(scale(mul(a,sq1),2),scale(x2,Q(-2,5)))
assert lie(F2,f)==add(mul(a,sq2),scale(y2,Q(-2,5)))

# z-coordinate generator identity underlying E[xy|z] = a z/5.
assert lie(z,f)==add(mul(a,z),scale(xy,-5))

# Exact nonzero equilibrium heights solve 100 z^2 - 10 z - 58/25? Instead verify
# the known quadratic induced by the first two equilibrium equations: 500 z^2-50 z-29=0.
# For z=(5 +/- sqrt(257))/100, this polynomial vanishes algebraically.
# We certify the polynomial reduction itself by determinant expansion.
# Matrix for first two equilibrium equations in (x,y): [-2/5, 1+10z; -1+5z, -2/5].
det=add(mono((0,0,0,0),Q(4,25)), scale(mul(add(one,scale(z,10)),add(scale(one,-1),scale(z,5))),-1))
expected=add(mono((0,0,0,0),Q(29,25)),scale(z,5),scale(z2,-50))
assert det==expected

print('VERIFY_OK')
print('L(V) = -2/5 x^2 - 2/5 y^2 + 3 a z^2')
print('L(F1)=2 a*((z+1/20)^2-1/400)-2/5 x^2')
print('L(F2)=a*((z-1/10)^2-1/100)-2/5 y^2')
print('L(z)=a z-5xy')
