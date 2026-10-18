"""Symbolic replay of spherical-triangle surface integrals (requires SymPy).

The underlying proof uses the Laplace--Beltrami boundary identity on each
spherical triangle. The script checks the resulting exact algebraic moments;
its numerical output is supplementary and is not an integration proof.
"""
import sympy as s
V=lambda a:s.Matrix(a)/s.sqrt(sum(x*x for x in a))
a,b,c,d=[V(z) for z in [(1,0,0),(1,1,0),(2,1,1),(1,1,1)]]

def tri(p,q,r):
    assert s.simplify(p.dot(q.cross(r)))>0
    Omega=2*s.atan(s.simplify(p.dot(q.cross(r)))/(1+p.dot(q)+q.dot(r)+r.dot(p)))
    N=s.zeros(3,1); T=s.zeros(3,3)
    for v,w in ((p,q),(q,r),(r,p)):
        h=s.simplify(s.sqrt(v.cross(w).dot(v.cross(w))))
        nu=-v.cross(w)/h
        theta=s.acos(s.simplify(v.dot(w)))
        edge=((1-v.dot(w))/h)*(v+w)
        N+=nu*theta
        T+=nu*edge.T+edge*nu.T
    return s.simplify(Omega),(-N/2).applyfunc(s.simplify),(s.eye(3)*Omega/3-T/6).applyfunc(s.simplify)

OA,va,MA=tri(a,b,c)
OB,vb,MB=tri(b,d,c)
OS,vs,MS=tri(a,b,d)
# The two small triangles triangulate the first-octant order chamber,
# of spherical angle pi/12. The spherical excess formula yields this area.
assert abs(float(s.N(OS-s.pi/12)))<1e-14
assert abs(float(s.N(OA+OB-s.pi/12)))<1e-14
# Mean-width integrals: integral x and integral (x+y) in order chamber.
theta=s.atan(1/s.sqrt(2))
assert s.simplify(vs[0] - s.sqrt(2)*s.acos(s.sqrt(6)/3)/4)==0
assert s.simplify(vs[0]+vs[1]-s.sqrt(2)*s.acos(s.sqrt(3)/3)/4)==0

# Weighted integrals in the two brightness branches.
Co=s.simplify(4*MA[0,0]+2*(MB[0,0]+MB[0,1]+MB[0,2]))
Ct=s.simplify(8*(MA[0,0]+MA[0,1])+4*(MB[0,0]+2*MB[0,1]+MB[0,2]+MB[1,1]+MB[1,2]))
# Substituting the exact spherical triangle area relation OB=pi/12-OA
# gives the closed forms for the two mixed moments.
co_reduced=s.simplify(Co.xreplace({OB/2:s.pi/24-OA/2}))
ct_reduced=s.simplify(Ct.xreplace({OB/2:s.pi/24-OA/2}))
assert s.simplify(co_reduced-(s.pi/18+s.sqrt(2)/3+2*OA/3))==0
assert s.simplify(ct_reduced-(2*s.pi/9+2*s.sqrt(6)/3))==0
print('PASS: spherical area, first moments, both mixed-moment reductions.')
