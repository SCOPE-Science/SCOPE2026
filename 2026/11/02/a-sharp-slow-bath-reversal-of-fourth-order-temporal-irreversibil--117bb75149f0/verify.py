"""Exact symbolic consistency checks for a partial-reset viscoelastic tracer.
Run with Python 3 and sympy; scipy is optional for finite-time illustrations.
"""
import sympy as S
from math import sqrt

z, t, s = S.symbols('z t s', real=True)
g = (1-z)/(z*(2-z))
# Observables in the generator, with no-reset diffusion and rate-one reset X -> 0.
def action(powers):
    i,j = powers
    d = {}
    def add(key, val): d[key] = d.get(key,0)+val
    add((i,j), -i-j/g-(1 if i else 0))
    if i: add((i-1,j+1),i)
    if j: add((i+1,j-1),j/g)
    if i>=2: add((i-2,j),i*(i-1))
    if j>=2: add((i,j-2),j*(j-1)/g)
    return {key:S.cancel(val) for key,val in d.items()}

def solve_moments(n, lower):
    inds = [(n-k,k) for k in range(n+1)]
    mat = S.zeros(len(inds)); rhs=S.zeros(len(inds),1)
    for row,pow_ in enumerate(inds):
        for q,v in action(pow_).items():
            if q in inds: mat[row,inds.index(q)] += v
            elif q in lower: rhs[row] -= v*lower[q]
            else: raise AssertionError((n,pow_,q))
    out=mat.inv()*rhs
    return {q:S.factor(out[i]) for i,q in enumerate(inds)}

M={(0,0):S.Integer(1)}
M.update(solve_moments(2,M)); M.update(solve_moments(4,M))
assert S.factor(-3*M[2,0]+2*M[1,1]+2)==0
assert S.factor(-5*M[4,0]+4*M[3,1]+12*M[2,0])==0

mon=[(3,0),(2,1),(1,2),(0,3),(1,0),(0,1)]
B=S.zeros(6)
for k,q in enumerate(mon):
    for other,value in action(q).items():
        B[k,mon.index(other)] += value
A=B[4:6,4:6]; C=B[:4,:4]; F=B[:4,4:6]
assert all(S.factor(q)==0 for q in (A-S.Matrix([[-2,1],[1/g,-1/g]])))
assert S.factor((A+z*S.eye(2)).det())==0
w=S.Matrix([1,2-z]); v=S.Matrix([1,g*(2-z)])
assert all(S.factor(q)==0 for q in (A+z*S.eye(2))*w)
assert all(S.factor(q)==0 for q in (v.T*(A+z*S.eye(2))))

# Fourth-order time arrow and its positive short-lag slope.
initial1=S.Matrix([M[i+1,j] for i,j in mon])
initial3=S.Matrix([M[4,0],M[3,1]])
short=S.factor((B*initial1)[0]-(A*initial3)[0])
assert S.factor(short-M[4,0]/2)==0
assert S.factor(M[4,0])!=0

w_c=-(C+z*S.eye(4)).inv()*F*w
L=S.factor((w_c[0]*(v.dot(initial1[4:6,0])) - v.dot(initial3))/(v.dot(w)))
P=12*z**11-26*z**10-323*z**9+1081*z**8+623*z**7-5918*z**6+5548*z**5+3765*z**4-6534*z**3-87*z**2+2204*z-309
S6=6*z**6-z**5-30*z**4+45*z**2+34*z-60
expected=-6*z*P/((z-1)*(z*z-2*z+2)*(z*z+z-3)*(z**3-z*z-9*z+12)*S6)
assert S.factor(L-expected)==0

# The positive-t substitution maps the whole physical interval z in (0,1) to t>0.
Ptrans=S.Poly(S.expand(sum(c*t**i*(1+t)**(11-i) for (i,),c in S.Poly(P,z).terms())),t)
assert Ptrans.all_coeffs()==[36,702,5864,27411,78556,142219,161725,110871,40878,4958,-1195,-309]
# Exactly one sign change in the descending transformed coefficients -> one positive root.
# The signs at the two z-interval endpoints are negative/positive.
assert P.subs(z,0)<0 and P.subs(z,1)>0

# All 4 eigenvalues of the cubic block lie strictly to the left of the slow -z mode.
poly=S.Poly((s*S.eye(4)-(C+z*S.eye(4))).det(),s)
a1,a2,a3,a4=[S.factor(poly.nth(j)) for j in [3,2,1,0]]
h2=S.factor(a1*a2-a3)
h3=S.factor(a1*a2*a3-a3*a3-a1*a1*a4)
cert={
 'a1':[6,17,9],
 'a2':[11,63,124,99,26],
 'a3':[6,52,185,341,334,154,24],
 'a4':[6,46,122,132,48,0],
 'h2':[60,453,1276,1652,969,210],
 'h3':[360,5838,42096,177649,486133,903188,1159251,1025169,610958,233634,51708,5040],
}
for name,q in [('a1',a1),('a2',a2),('a3',a3),('a4',a4),('h2',h2),('h3',h3)]:
    rat=S.cancel(q.subs(z,t/(1+t)))
    num,den=S.fraction(rat)
    nc=S.Poly(num,t).all_coeffs(); dc=S.Poly(den,t).all_coeffs()
    # Sympy normalization can differ by overall positive scalar, hence compare ratios.
    assert all(c>=0 for c in nc) and any(c>0 for c in nc), (name,nc)
    assert all(c>0 for c in dc), (name,dc)
    assert [S.cancel(c/nc[0]) for c in nc]==[S.cancel(c/S.Integer(cert[name][0])) for c in cert[name]], name

# Sign of each factor of the slow-mode residue denominator on z in (0,1).
for q,sign in [(z-1,-1),(z*z-2*z+2,1),(z*z+z-3,-1),
               (z**3-z*z-9*z+12,1),(S6,-1)]:
    degree=S.degree(q,z)
    trans=S.Poly(S.cancel((1+t)**degree*q.subs(z,t/(1+t))),t)
    assert all(c*sign>0 for c in trans.all_coeffs()),(q,trans)

zroot=float(S.nsolve(P,.15,prec=35)); gr=(1-zroot)/(zroot*(2-zroot))
assert .15008<zroot<.15009 and 3.0612<gr<3.0613
for gn,sgn in [(1,1),(2,1),(3,1),(4,-1),(10,-1),(100,-1)]:
    zn=2/((2*gn+1)+sqrt((2*gn+1)**2-4*gn))
    ln=float(L.subs(z,zn));assert ln*sgn>0,(gn,ln)
print('PASS: exact moment equations; short-time arrow; slow-mode residue; spectral Routh-Hurwitz; unique threshold')
print('z_star=',format(zroot,'.15g'),'gamma_star=',format(gr,'.15g'))
