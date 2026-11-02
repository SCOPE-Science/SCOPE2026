"""Symbolic and numerical verification of a two-site coupled-logistic phase chart.

Requires Python 3 and SymPy. Symbolic assertions check identities that are
used in the separate mathematical proof; numerical samples do not prove it.
"""
from __future__ import annotations
import math
import sympy as S

r, s, z = S.symbols('r s z', real=True)
d = 1+s**2
A = (1+s)/d
B = (1-s)/d
x, y = S.symbols('x y', real=True)
F = S.Matrix([r*x*(1-x+s*y), r*y*(1-y-s*x)])
f = r*z*(1-z)
ray = {x:A*z,y:B*z}
assert all(S.simplify(t)==0 for t in F.subs(ray)-S.Matrix([A*f,B*f]))
J = F.jacobian([x,y]).subs(ray)
assert all(S.simplify(t)==0 for t in J*S.Matrix([A,B])-r*(1-2*z)*S.Matrix([A,B]))
assert S.simplify(S.trace(J)-r*(1-2*z)-r*(1-2*z/d)) == 0

zplus, zminus = [(r+1+sgn*S.sqrt((r-3)*(r+1)))/(2*r) for sgn in (1,-1)]
assert S.simplify(zplus+zminus-(r+1)/r)==0
assert S.simplify(zplus*zminus-(r+1)/r**2)==0
parallel = S.factor(r**2*(1-2*zplus)*(1-2*zminus))
perp = S.factor(r**2*(1-2*zplus/d)*(1-2*zminus/d))
assert S.simplify(parallel-(4+2*r-r**2))==0
assert S.simplify(perp-(r*r-2*r*(r+1)/d+4*(r+1)/d**2))==0
assert S.simplify(perp.subs(r,3)-(3-4/d)**2)==0
assert S.simplify((perp-1)*d**2-(d-2)*(r+1)*(d*r-d-2))==0
assert S.simplify(S.diff(perp,r)-2*(d-2)*(d*r-1)/d**2)==0

# Polynomial conditions for loss of transverse hyperbolicity and first clipping.
K = S.expand(d**2*(perp+1))
W = S.factor(1/A)
P = S.expand(r**2*W**2-r*(r+1)*W+r+1)
R = S.expand(r*s*(1-s)*(r*d-(1+s))-(1+s)**2)
assert S.simplify(P*(1+s)**2+R)==0
res = S.factor(S.resultant(K,R,r))
expected = (s-1)**4*d**3*(s**3+s**2+s-1)*(s**3+s**2+3*s-1)
assert S.simplify(res-expected)==0, (res,expected)
subres = S.factor(S.subresultants(K,R,r)[-2])
assert S.simplify(subres-(s-1)**2*d*(r*(s**3-s)+(s**4+s**3+2*s**2-s+1)))==0


# At r_c the signs of the two relevant phase multipliers coincide only at s_3.
rc=1+S.sqrt(6)
assert S.simplify((perp+1).subs(r,rc)*d**2-2*(d-1)*((4+S.sqrt(6))*d-4-2*S.sqrt(6)))==0

def rp(sv):
    dv=1+sv*sv
    return (1+math.sqrt((dv**3+3*dv+2)/(2-dv)))/dv

def rs(sv):
    dv=1+sv*sv
    return (1+sv)/(2*dv)*(1+math.sqrt(1+4*dv/(sv*(1-sv))))

roots=[]
for poly in [s**3+s**2+3*s-1, s**3+s**2+s-1]:
    positive=[float(S.re(q)) for q in S.nroots(poly) if abs(float(S.im(q)))<1e-12 and 0<float(S.re(q))<1]
    assert len(positive)==1
    roots.append(positive[0])
roots.append(math.sqrt((2*math.sqrt(6)-3)/5))
assert 0.295 < roots[0]<0.296 < 0.543 < roots[1]<0.544 < 0.616 < roots[2]<0.617
assert max(abs(rp(v)-rs(v)) for v in roots[:2])<1e-11
assert abs(rp(roots[2])-float(rc))<1e-11
for sample, expected_first in [(1/4,'transverse'),(2/5,'clipping'),(3/5,'transverse'),(4/5,'tangential')]:
    cand={'transverse':rp(sample),'clipping':rs(sample),'tangential':float(rc)}
    first=min(cand,key=cand.get)
    assert first == expected_first,(sample,cand,first)
    r0=3+(cand[first]-3)/2
    za=(r0+1+math.sqrt((r0-3)*(r0+1)))/(2*r0)
    zb=(r0+1-math.sqrt((r0-3)*(r0+1)))/(2*r0)
    aa=(1+sample)/(1+sample*sample)
    bb=(1-sample)/(1+sample*sample)
    assert 0<bb*zb<bb*za<1 and 0<aa*zb<aa*za<1
    for u in [za,zb]:
        X,Y=aa*u,bb*u
        newx=r0*X*(1-X+sample*Y)
        newy=r0*Y*(1-Y-sample*X)
        zp=r0*u*(1-u)
        assert max(abs(newx-aa*zp),abs(newy-bb*zp))<1e-12
    # Both return multipliers are strictly inside the unit circle before first event.
    mp=4+2*r0-r0*r0
    mt=r0*r0-2*r0*(r0+1)/(1+sample*sample)+4*(r0+1)/(1+sample*sample)**2
    assert max(abs(mp),abs(mt))<1
    # Evaluate the full two-by-two period-return Jacobian independently.
    Jnum=lambda u: S.Matrix([[r0*(1-2*aa*u+sample*bb*u),r0*sample*aa*u],
                              [-r0*sample*bb*u,r0*(1-2*bb*u-sample*aa*u)]])
    eigvals=list((Jnum(za)*Jnum(zb)).eigenvals().keys())
    assert len(eigvals)==2
    assert max(abs(a-b) for a,b in zip(sorted([float(v) for v in eigvals]),sorted([mp,mt])))<1e-9
    print(f's={sample:.6f}: transverse={cand["transverse"]:.12f}; clipping={cand["clipping"]:.12f}; tangential={cand["tangential"]:.12f}; first={first}')
print('Critical couplings:',*roots)
print('All exact identities, eliminations, and sample consistency checks passed.')
