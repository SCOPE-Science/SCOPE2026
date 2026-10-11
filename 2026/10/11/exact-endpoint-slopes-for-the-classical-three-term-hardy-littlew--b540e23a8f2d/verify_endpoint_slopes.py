from fractions import Fraction as F
from decimal import Decimal, getcontext

# Exact finite certificate for the two endpoint slopes.

def poly_a(x): return x*x*x + x - 1          # a^3+a-1

def poly_b(x): return x*x*x + x*x - 1        # b^3+b^2-1

def isolate(poly, lo=F(0), hi=F(1), steps=160):
    assert poly(lo) < 0 < poly(hi)
    for _ in range(steps):
        m=(lo+hi)/2
        if poly(m) < 0: lo=m
        else: hi=m
    return lo,hi

aL,aU=isolate(poly_a)
bL,bU=isolate(poly_b)
assert F(0)<aL<aU<bL<bU<F(1)

# Convolution coefficients of G_±=|1+z±z^3|^2 and their squares.
def conv(A,B):
    C={}
    for i,x in A.items():
        for j,y in B.items(): C[i+j]=C.get(i+j,0)+x*y
    return C
Gplus={0:3,1:1,-1:1,2:1,-2:1,3:1,-3:1}
Gminus={0:3,1:1,-1:1,2:-1,-2:-1,3:-1,-3:-1}
assert conv(Gplus,Gplus)=={-6:1,-5:2,-4:3,-3:8,-2:9,-1:10,0:15,1:10,2:9,3:8,4:3,5:2,6:1}
assert conv(Gminus,Gminus)=={-6:1,-5:2,-4:-1,-3:-8,-2:-7,-1:6,0:15,1:6,2:-7,3:-8,4:-1,5:2,6:1}

# Power sums of the roots reflected into the open unit disk.  Each entry is
# (quadratic coefficient, linear coefficient, constant) after reduction by
# a^3=1-a or b^3=1-b^2.
Sa={
1:(1,-1,0), 2:(0,-1,0), 3:(1,2,-3),
4:(-3,0,2), 5:(2,1,-1), 6:(-3,-5,5)}
Sb={
1:(-1,0,0), 2:(1,-1,1), 3:(-2,-1,3),
4:(0,-1,0), 5:(-1,-3,4), 6:(-3,-2,3)}

def add_expr(X,Y): return tuple(x+y for x,y in zip(X,Y))
def scale_expr(c,X): return tuple(c*x for x in X)
def sum_weighted(coeffs,S,nmax):
    out=(F(0),F(0),F(0))
    for n in range(1,nmax+1): out=add_expr(out,scale_expr(F(coeffs[n],n),S[n]))
    return out

cp1={1:1,2:1,3:1}; cm1={1:1,2:-1,3:-1}
cp2={1:10,2:9,3:8,4:3,5:2,6:1}
cm2={1:6,2:-7,3:-8,4:-1,5:2,6:1}
# These are the exact Fourier sums \sum c_n S_n/n.
assert sum_weighted(cp1,Sa,3)==(F(4,3),F(-5,6),F(-1))
assert sum_weighted(cm1,Sb,3)==(F(-5,6),F(5,6),F(-3,2))
assert sum_weighted(cp2,Sa,6)==(F(643,60),F(-48,5),F(-91,15))
assert sum_weighted(cm2,Sb,6)==(F(-76,15),F(293,60),F(-47,5))

# Interval arithmetic for the closed forms.
def sq(I):
    lo,hi=I; assert lo>=0
    return lo*lo,hi*hi

def lincomb(terms, const=F(0)):
    lo=hi=const
    for c,(xL,xU) in terms:
        if c>=0: lo += c*xL; hi += c*xU
        else: lo += c*xU; hi += c*xL
    return lo,hi

# u=(b-a)/(b+a), so log(b/a)=2 artanh(u).
numL,numU=bL-aU,bU-aL
denL,denU=bL+aL,bU+aU
uL,uU=numL/denU,numU/denL
assert F(0)<uL<uU<F(1)

def log_ratio_bounds(uL,uU,N=18):
    low=F(0); high=F(0)
    for j in range(N):
        d=2*j+1
        low += 2*uL**d/d
        high += 2*uU**d/d
    d=2*N+1
    high += 2*uU**d/(d*(1-uU*uU))
    return low,high

logBA_L,logBA_U=log_ratio_bounds(uL,uU)
# log(a/b) is the negative interval.
logAB=(-logBA_U,-logBA_L)
a2=sq((aL,aU)); b2=sq((bL,bU))
P2=lincomb([(F(8),a2),(F(-5),(aL,aU)),(F(5),b2),(F(-5),(bL,bU))],F(3))
P2=(P2[0]/6,P2[1]/6)
P4=lincomb([(F(643),a2),(F(-576),(aL,aU)),(F(304),b2),(F(-293),(bL,bU))],F(200))
P4=(P4[0]/60,P4[1]/60)
c2=(3*logAB[0]+P2[0],3*logAB[1]+P2[1])
c4=(15*logAB[0]+P4[0],15*logAB[1]+P4[1])
assert c2[0] > 0
assert c4[1] < 0

getcontext().prec=35
def dec(q): return Decimal(q.numerator)/Decimal(q.denominator)
print('VERIFY_OK')
print('a_interval', dec(aL), dec(aU))
print('b_interval', dec(bL), dec(bU))
print('Delta_prime_2_interval', dec(c2[0]), dec(c2[1]))
print('Delta_prime_4_interval', dec(c4[0]), dec(c4[1]))
