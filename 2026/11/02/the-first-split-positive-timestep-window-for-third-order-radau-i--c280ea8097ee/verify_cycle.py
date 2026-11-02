#!/usr/bin/env python3
"""Exact proof checks for positivity windows of third-order Radau IIA on directed cycles.

Requires SymPy 1.12 or later. All algebraic comparisons use integer/rational arithmetic.
"""
import sympy as sp

h = sp.symbols('h')
checks = 0

def require(condition, detail):
    global checks
    assert condition, detail
    checks += 1

# Encode a+b*i*sqrt(2) with pairs of exact polynomials (a,b).
def plus(a,b):
    return sp.expand(a[0]+b[0]), sp.expand(a[1]+b[1])

def times(a,b):
    return sp.expand(a[0]*b[0]-2*a[1]*b[1]), sp.expand(a[0]*b[1]+a[1]*b[0])

def power(a,n):
    out=(sp.Integer(1),sp.Integer(0))
    for _ in range(n): out=times(out,a)
    return out

def cyclic_coefficients(n):
    p=(h+2,sp.Integer(1)); q=(h+2,sp.Integer(-1))
    aa=(sp.Integer(1),-sp.Rational(5,2)); bb=(sp.Integer(1),sp.Rational(5,2))
    pn,qn=power(p,n),power(q,n)
    d=times(plus(pn,(-h**n,0)),plus(qn,(-h**n,0)))[0]
    ff=[]
    for j in range(n):
        u=times(times(aa,power(p,n-j-1)),plus(qn,(-h**n,0)))
        v=times(times(bb,power(q,n-j-1)),plus(pn,(-h**n,0)))
        ff.append(sp.factor(-plus(u,v)[0]))
    return sp.factor(d), ff

def all_coefficients_positive(f):
    c=sp.Poly(f,h).all_coeffs()
    return all(x>=0 for x in c) and c[-1]>0 and c[0]>0

def sign_at(f,x):
    return sp.sign(sp.Poly(f,h).eval(x))

def sturm_positive_root_count(f):
    seq=sp.sturm(f,h)
    def variations(s):
        s=[v for v in s if v!=0]
        return sum(s[i]!=s[i+1] for i in range(len(s)-1))
    signs_zero=[sp.sign(sp.limit(z,h,0,dir='+')) for z in seq]
    signs_infty=[sp.sign(sp.LC(sp.Poly(z,h))) for z in seq]
    return variations(signs_zero)-variations(signs_infty), variations(signs_zero), variations(signs_infty)

def bracket_single_positive_root(f,left,right):
    require(sign_at(f,left)<0,('left',f,left))
    require(sign_at(f,right)>0,('right',f,right))
    require(sturm_positive_root_count(f)[0]==1,('unique root',f))

def direct_first_row(n,x):
    I=sp.eye(n); S=sp.zeros(n)
    for i in range(n): S[i,(i+1)%n]=1
    Q=S-I
    P=(6*I-4*x*Q+x*x*Q*Q).inv()*(6*I+2*x*Q)
    return [sp.factor(P[0,j]) for j in range(n)]

polys={}
for n in range(2,9):
    d, ff=cyclic_coefficients(n)
    polys[n]=(d,ff)
    require(sp.Poly(d,h).eval(0)>0,('D at zero',n))
    require(sp.expand(sum(h**j*ff[j] for j in range(n))-d)==0,('mass',n))
    for x in [sp.Rational(1,8),sp.Rational(3,2),sp.Rational(7,2),sp.Integer(8)]:
        row=direct_first_row(n,x)
        for j in range(n):
            require(sp.cancel(row[j]-x**j*ff[j].subs(h,x)/d.subs(h,x))==0,
                    ('direct inverse mismatch',n,j,x))
    if n<=5:
        require(all(all_coefficients_positive(f) for f in ff),('unconditional',n))

# In dimensions six and seven only the furthest-distance coefficient limits
# positivity, once positivity of c_0 is certified by a full Sturm count.
for n in (6,7):
    d, ff=polys[n]
    require(all(all_coefficients_positive(ff[j]) for j in range(1,5)),('internal',n))
    require(sturm_positive_root_count(ff[0])==(0,4,4),('diagonal',n))
    bracket_single_positive_root(ff[5],sp.Rational(208,1000),sp.Rational(209,1000))

f7=polys[7][1]
bracket_single_positive_root(f7[6],sp.Rational(663,1000),sp.Rational(664,1000))

# For the eight-cycle, c_0 loses positivity on one bounded open interval.
f8=polys[8][1]
require(all(all_coefficients_positive(f8[j]) for j in range(1,5)),'eight internal')
for j,lo,hi in [(5,208,209),(6,663,664),(7,1106,1107)]:
    bracket_single_positive_root(f8[j],sp.Rational(lo,1000),sp.Rational(hi,1000))
require(sturm_positive_root_count(f8[0])==(2,6,4),'two positive roots of diagonal')
require(sign_at(f8[0],0)>0,'diagonal at zero')
require(sign_at(f8[0],sp.Rational(3297,1000))>0,'diagonal before first zero')
require(sign_at(f8[0],sp.Rational(3298,1000))<0,'diagonal after first zero')
require(sign_at(f8[0],sp.Rational(7042,1000))<0,'diagonal before second zero')
require(sign_at(f8[0],sp.Rational(7043,1000))>0,'diagonal after second zero')
require(sp.LC(sp.Poly(f8[0],h))>0,'diagonal at infinity')

# For every positive h, D_n(h)=|p^n-h^n|^2>0, since |p|>h.
# Thus exact numerator signs and the disjoint root brackets are sufficient.
print('VERIFY_OK',checks,'exact assertions; dimensions 2..8; root intervals certified')
for j in (0,5,6,7):
    print('P8_'+str(j)+'=',sp.expand(f8[j]/48))
print('Sturm (n,j) (positive roots, V0, Vinf):',
      [(n,j,sturm_positive_root_count(polys[n][1][j]))
       for n,j in ((6,0),(7,0),(8,0))])
