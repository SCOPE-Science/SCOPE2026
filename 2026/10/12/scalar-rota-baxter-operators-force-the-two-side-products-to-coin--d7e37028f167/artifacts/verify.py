import sympy as sp

lam=sp.symbols("lam")
# General 2D structure constants for dashv, vdash, perp.
L=sp.symbols("l000:8")
Rr=sp.symbols("r000:8")
P=sp.symbols("p000:8")

def mk(vals):
    # vals ordered by (i,j,k), k fastest
    T={}
    q=0
    for i in range(2):
        for j in range(2):
            T[i,j]=sp.Matrix([vals[q],vals[q+1]])
            q+=2
    return T

TL,TR,TP=mk(L),mk(Rr),mk(P)
e=[sp.Matrix([1,0]),sp.Matrix([0,1])]

def mul(T,x,y):
    z=sp.zeros(2,1)
    for i in range(2):
        for j in range(2):
            z += x[i]*y[j]*T[i,j]
    return sp.expand(z)

def S(x):
    return -lam*x

for x in e:
    for y in e:
        # Printed first equation: S(x) vdash S(y) = S(S(x) dashv y + x dashv S(y) + lam x dashv y)
        d1=sp.expand(mul(TR,S(x),S(y))-S(mul(TL,S(x),y)+mul(TL,x,S(y))+lam*mul(TL,x,y)))
        want1=sp.expand(lam**2*(mul(TR,x,y)-mul(TL,x,y)))
        assert sp.simplify(d1-want1)==sp.zeros(2,1)
        # Printed second equation.
        d2=sp.expand(mul(TL,S(x),S(y))-S(mul(TR,S(x),y)+mul(TR,x,S(y))+lam*mul(TR,x,y)))
        want2=sp.expand(lam**2*(mul(TL,x,y)-mul(TR,x,y)))
        assert sp.simplify(d2-want2)==sp.zeros(2,1)
        # Middle operation.
        d3=sp.expand(mul(TP,S(x),S(y))-S(mul(TP,S(x),y)+mul(TP,x,S(y))+lam*mul(TP,x,y)))
        assert sp.simplify(d3)==sp.zeros(2,1)

# Example 2.10: unlisted products are zero.
left={(0,1):sp.Matrix([1,0]),(1,0):sp.Matrix([1,0])}
right={(0,1):sp.Matrix([1,0])}
mid={(0,1):sp.Matrix([1,0]),(1,1):sp.Matrix([1,0])}
Z=sp.zeros(2,1)

def emul(T,x,y):
    z=sp.zeros(2,1)
    for i in range(2):
        for j in range(2):
            z += x[i]*y[j]*T.get((i,j),Z)
    return sp.expand(z)

x=e[1]; y=e[0]
d1=sp.expand(emul(right,S(x),S(y))-S(emul(left,S(x),y)+emul(left,x,S(y))+lam*emul(left,x,y)))
assert d1 == sp.Matrix([-lam**2,0])
assert sp.simplify(d1.subs(lam,0))==Z

# Check every Example 2.10 basis-pair defect vanishes at weight zero.
for x in e:
    for y in e:
        D1=emul(right,S(x),S(y))-S(emul(left,S(x),y)+emul(left,x,S(y))+lam*emul(left,x,y))
        D2=emul(left,S(x),S(y))-S(emul(right,S(x),y)+emul(right,x,S(y))+lam*emul(right,x,y))
        D3=emul(mid,S(x),S(y))-S(emul(mid,S(x),y)+emul(mid,x,S(y))+lam*emul(mid,x,y))
        for D in (D1,D2,D3):
            assert sp.simplify(D.subs(lam,0))==Z

print("VERIFY_OK")
