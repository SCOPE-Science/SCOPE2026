"""Exact Hermite-moment and temporal-Fourier check for the stated odd Strichartz formulas.
Requires Python 3 and SymPy. Does not sample any infinite function class.
"""
from collections import defaultdict
from itertools import product
from functools import lru_cache
import sympy as sp

x, s, eps = sp.symbols('x s eps', real=True)
lam, ell = sp.symbols('lam ell')
PI = sp.pi
H = {n:sp.hermite(n,x)/sp.sqrt(2**n*sp.factorial(n))/PI**sp.Rational(1,4) for n in [1,3,5]}

@lru_cache(None)
def moment(indices):
    """Integral of a product of four normalized Hermite functions."""
    poly=sp.Poly(sp.expand(sp.prod(H[n] for n in indices)),x)
    total=0
    for (degree,),coeff in poly.terms():
        if degree%2: continue
        m=degree//2
        total+=coeff*sp.sqrt(PI/2)*sp.factorial2(2*m-1)/4**m if m else coeff*sp.sqrt(PI/2)
    return sp.simplify(total)

M={(1,1,1,1):3*sp.sqrt(2)/(8*sp.sqrt(PI)),
   (3,3,3,3):147*sp.sqrt(2)/(512*sp.sqrt(PI)),
   (1,1,3,3):11*sp.sqrt(2)/(64*sp.sqrt(PI)),
   (1,1,1,3):-sp.sqrt(3)/(16*sp.sqrt(PI)),
   (1,3,3,3):3*sp.sqrt(3)/(128*sp.sqrt(PI))}
for inds,target in M.items():
    assert sp.simplify(moment(inds)-target)==0, inds

# For h1 + eps*h3 + lam*eps^2*h5 (complex lam), record epsilon degree
# and harmonic e^{2 i theta}. Only the zero harmonic survives time average.
terms=[(0,0,sp.Integer(1),1),(1,1,sp.Integer(1),3),(2,2,lam,5)]
I=defaultdict(lambda:sp.Integer(0))
for ids in product(range(3),repeat=4):
    n=sum(terms[i][0] for i in ids)
    if n>8: continue
    k=terms[ids[0]][1]+terms[ids[1]][1]-terms[ids[2]][1]-terms[ids[3]][1]
    coefficient=(sp.prod(terms[i][2] for i in ids[:2])
                 *sp.prod(terms[i][2].subs(lam,ell) for i in ids[2:]))
    I[n,k]+=coefficient*moment(tuple(sorted(terms[i][3] for i in ids)))
J=defaultdict(lambda:sp.Integer(0))
for (n,k),a in I.items():
    for (m,l),b in I.items():
        if k+l==0 and n+m<=8: J[n+m]+=a*b
N=1+eps**2+lam*ell*eps**4
T=sp.pi/2*sum(sp.expand(v)*eps**n for n,v in J.items())
# Do not use the normalization in the pre-factor of I: N is the squared L2 norm.
S=sp.series(T/N**4,eps,0,9).removeO().expand()
assert sp.simplify(S.coeff(eps,0)-sp.Rational(9,64))==0
assert sp.simplify(S.coeff(eps,2))==0
assert sp.simplify(S.coeff(eps,4)+sp.Rational(81,512)*(lam-sp.sqrt(30)/6)*(ell-sp.sqrt(30)/6))==0
assert sp.simplify(S.coeff(eps,6).subs({lam:sp.sqrt(30)/6,ell:sp.sqrt(30)/6})+sp.Rational(525,4096))==0
assert sp.simplify(S.coeff(eps,8).subs({lam:sp.sqrt(30)/6,ell:sp.sqrt(30)/6})-sp.Rational(105,1048576))==0

# Exact two-mode norm, with s=|b|^2/(|a|^2+|b|^2).
A=M[(1,1,1,1)];B=M[(3,3,3,3)];C=M[(1,1,3,3)]
D=M[(1,1,1,3)];E=M[(1,3,3,3)]
U=(1-s)**2*A+s**2*B+4*s*(1-s)*C
V2=16*s*(1-s)*((1-s)*D+s*E)**2
W2=4*s**2*(1-s)**2*C**2
S2=sp.factor(sp.pi/2*(U**2+(V2+W2)/2))
claim=sp.Rational(3,262144)*(12288-11520*s**2+8960*s**3-2525*s**4)
assert sp.simplify(S2-claim)==0
# Positivity over [0,1] proven analytically by monotonic quadratic factors.
assert sp.factor(sp.diff(claim,s))==-15*s*(505*s**2-1344*s+1152)/65536
assert sp.simplify(claim.subs(s,0)-sp.Rational(9,64))==0
assert sp.simplify((sp.Rational(9,64)-claim).subs(s,1)-sp.Rational(15255,262144))==0
print('PASS: five exact fourth-power Gaussian moments, sharp two-mode polynomial, fourth and sixth-order three-mode normal form')
