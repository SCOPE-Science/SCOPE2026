from fractions import Fraction
from itertools import product

# A polynomial is a low-to-high tuple of exact rational coefficients.
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)

def padd(a,b):
    n=max(len(a),len(b))
    return trim(tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)))

def pneg(a): return tuple(-x for x in a)
def psub(a,b): return padd(a,pneg(b))

def pmul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(tuple(out))

def pscale(a,c): return trim(tuple(c*x for x in a))

ZERO=(Fraction(0),)
ONE=(Fraction(1),)
R=(Fraction(0),Fraction(1))
R2=pmul(R,R)
R2P4=padd(R2,(Fraction(4),))

# Quad(A,B) represents A(r)+B(r)S with S^2=r^2+4.
def qadd(x,y): return (padd(x[0],y[0]),padd(x[1],y[1]))
def qneg(x): return (pneg(x[0]),pneg(x[1]))
def qsub(x,y): return qadd(x,qneg(y))
def qscale(x,c): return (pscale(x[0],c),pscale(x[1],c))
def qmul(x,y):
    a,b=x; c,d=y
    return (padd(pmul(a,c),pmul(pmul(b,d),R2P4)), padd(pmul(a,d),pmul(b,c)))
def qpoly(p): return (p,ZERO)

def qeq(x,y): return trim(x[0])==trim(y[0]) and trim(x[1])==trim(y[1])

# E=(2+r^2+rS)/2.
E=(padd(ONE,pscale(R2,Fraction(1,2))), pscale(R,Fraction(1,2)))

V=[(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)]
F=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]

def ev(f,u): return f[0]*u[0]+f[1]*u[1]

types=set()
for u,v in product(V,repeat=2):
    for f,g in product(F,repeat=2):
        fu,fv,gu,gv=ev(f,u),ev(f,v),ev(g,u),ev(g,v)
        types.add((fu*fu,gu*gu,gv*gv,fv*fv,fu*fv-gu*gv))

expected_types={
 (0,0,0,0,0),(0,0,1,1,0),(0,1,0,1,0),(0,1,1,0,-1),(0,1,1,0,1),
 (0,1,1,1,-1),(0,1,1,1,1),(1,0,0,1,-1),(1,0,0,1,1),(1,0,1,0,0),
 (1,0,1,1,-1),(1,0,1,1,1),(1,1,0,0,0),(1,1,0,1,-1),(1,1,0,1,1),
 (1,1,1,0,-1),(1,1,1,0,1),(1,1,1,1,0)
}
assert types == expected_types

# Exact candidate determinant expressions.
SFORM=(ZERO,ONE)
E2=qmul(E,E)
rplusS=qadd(qpoly(R),SFORM)
rminusS=qsub(qpoly(R),SFORM)
certs={
 'zero': qpoly(ZERO),
 'E2': E2,
 'rp': qscale(qmul(qpoly(R),rplusS),Fraction(1,2)),
 'sqm': qscale(qmul(qsub(qsub(qpoly(R2),qmul(qpoly(R),SFORM)),qpoly((Fraction(2),))),
                         qsub(qsub(qpoly(R2),qmul(qpoly(R),SFORM)),qpoly((Fraction(2),)))),Fraction(1,4)),
 'cross': qscale(qmul(qpoly(pmul(pmul(R,psub(R,ONE)),padd(R,ONE))),rminusS),Fraction(1,2)),
 'r2p': qscale(qmul(qpoly(R2),qmul(rplusS,rplusS)),Fraction(1,4)),
 'r2m': qscale(qmul(qpoly(R2),qmul(rminusS,rminusS)),Fraction(1,4)),
}

kind_count={k:0 for k in certs}
for a,b,c,d,k in sorted(types):
    m11=padd((Fraction(a),),pscale(R2,Fraction(b)))
    m22=padd((Fraction(c),),pscale(R2,Fraction(d)))
    off2=pscale(R2,Fraction(k*k))
    det=qsub(qmul(qsub(E,qpoly(m11)),qsub(E,qpoly(m22))),qpoly(off2))
    hits=[name for name,form in certs.items() if qeq(det,form)]
    assert len(hits)==1, ((a,b,c,d,k),hits,det)
    kind_count[hits[0]]+=1

# All seven certificate kinds occur, and their signs on 0<=r<=1 are immediate:
# squares and zero are nonnegative; r(r+S)/2 is nonnegative; for the cross term,
# r>=0, r-1<=0, r+1>0, and r-S<0 because S=sqrt(r^2+4)>r.
assert all(kind_count[k]>0 for k in kind_count)

# Verify E satisfies its characteristic equation E^2-(2+r^2)E+1=0.
char=qadd(qsub(qmul(E,E),qmul(qpoly(padd((Fraction(2),),R2)),E)),qpoly(ONE))
assert qeq(char,qpoly(ZERO))

# tau=(r+S)/2 is the positive top-eigenvector slope: E-1 = r*tau.
tau=qscale(rplusS,Fraction(1,2))
assert qeq(qsub(E,qpoly(ONE)),qmul(qpoly(R),tau))
# tau^2-r*tau-1=0.
assert qeq(qsub(qsub(qmul(tau,tau),qmul(qpoly(R),tau)),qpoly(ONE)),qpoly(ZERO))

# Parameter maximum algebra:
# (2+5r^2)^2 - 9r^2(r^2+4) = 4(2r^2-1)^2.
left=psub(pmul(padd((Fraction(2),),pscale(R2,Fraction(5))),padd((Fraction(2),),pscale(R2,Fraction(5)))),
          pscale(pmul(R2,R2P4),Fraction(9)))
right=pscale(pmul(psub(pscale(R2,Fraction(2)),ONE),psub(pscale(R2,Fraction(2)),ONE)),Fraction(4))
assert trim(left)==trim(right)

print('VERIFY_OK')
