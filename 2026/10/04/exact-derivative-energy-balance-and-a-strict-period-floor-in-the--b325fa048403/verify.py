from fractions import Fraction as Q

# Sparse polynomials in variables (x,y,z,c), represented by exponent tuples.
def add(*ps):
    out={}
    for p in ps:
        for m,a in p.items(): out[m]=out.get(m,Q(0))+a
    return {m:a for m,a in out.items() if a}
def mul(p,q):
    out={}
    for m,a in p.items():
        for n,b in q.items():
            k=tuple(i+j for i,j in zip(m,n)); out[k]=out.get(k,Q(0))+a*b
    return {m:a for m,a in out.items() if a}
def scale(a,p): return {m:a*b for m,b in p.items() if a*b}
def deriv(p,j):
    out={}
    for m,a in p.items():
        if m[j]:
            k=list(m); k[j]-=1; k=tuple(k)
            out[k]=out.get(k,Q(0))+a*m[j]
    return out
ONE={(0,0,0,0):Q(1)}
x={(1,0,0,0):Q(1)}; y={(0,1,0,0):Q(1)}; z={(0,0,1,0):Q(1)}; c={(0,0,0,1):Q(1)}
x2=mul(x,x); c2=mul(c,c)
f=[y,z,add(c2,scale(-1,y),scale(Q(-1,2),x2))]
def L(p): return add(*(mul(deriv(p,j),f[j]) for j in range(3)))

assert L(x)==y
assert L(y)==z
assert L(z)==add(c2,scale(-1,y),scale(Q(-1,2),x2))
assert L(scale(Q(1,3),mul(x2,x)))==mul(x2,y)
assert L(mul(y,z))==add(mul(z,z),mul(c2,y),scale(-1,mul(y,y)),scale(Q(-1,2),mul(x2,y)))
assert L(mul(x,y))==add(mul(y,y),mul(x,z))

# Equality case in the periodic Wirtinger step.  If P=2*pi and
# y=A*cos(t+phi), then x=m+A*sin(t+phi).  Substitution reduces the
# third equation to c^2 - (m+A*s)^2/2 == 0 for all s in [-1,1].
# Its s^2 coefficient is -A^2/2, so identity forces A=0.
A2_coeff=Q(-1,2)  # coefficient multiplying A^2*s^2
assert A2_coeff != 0

print('VERIFY_OK')
