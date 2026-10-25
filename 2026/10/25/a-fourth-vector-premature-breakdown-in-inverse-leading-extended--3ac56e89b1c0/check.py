"""Exact fourth-step inverse-leading Krylov residual certificate.

Run with Python 3, SymPy, and NumPy: python check.py
"""
import sympy as s
import numpy as np
A=s.diag(-1,1,2,3)
v=s.Matrix([s.sqrt(3),s.sqrt(56),3,3])/s.sqrt(77)
a=s.simplify((v.T*A.inv()*v)[0]); m=s.simplify((v.T*A*v)[0]); assert (a,m)==(s.Rational(11,14),s.Rational(14,11))
tau2=s.simplify(((A.inv()*v-a*v).T*(A.inv()*v-a*v))[0]);assert tau2==s.Rational(103,539)
tau=s.sqrt(tau2);u=s.simplify((A.inv()*v-a*v)/tau)
P2=s.eye(4)-v*v.T-u*u.T
r2=s.simplify(((P2*A*v).T*(P2*A*v))[0]); assert r2==s.Rational(564,847)
r=s.sqrt(r2);w=s.simplify(P2*A*v/r)
P3=s.eye(4)-v*v.T-u*u.T-w*w.T
rs=s.simplify(P3*A.inv()*u);rm=s.simplify(P3*A.inv()*w)
assert all(s.simplify(t)==0 for t in rm)
assert s.simplify((rs.T*rs)[0])==s.Rational(14112,498623)
assert all(s.simplify(t)==0 for t in P3*A.inv()*w + ((1-a*m)/(tau*r))*P3*A.inv()*u)
assert s.simplify((P2*A*u).norm())!=0
An=np.diag([-1.,1.,2.,3.]);vf=np.array([np.sqrt(3),np.sqrt(56),3,3])/np.sqrt(77)
for eps in [-1e-3,-1e-5,0.,1e-5,1e-3]:
    vt=vf.copy(); vt[0]+=eps; vt/=np.linalg.norm(vt)
    a2=np.dot(vt,np.linalg.solve(An,vt)); z=np.linalg.solve(An,vt)-a2*vt; u2=z/np.linalg.norm(z)
    proj2=np.eye(4)-np.outer(vt,vt)-np.outer(u2,u2)
    rvec=proj2@(An@vt); w2=rvec/np.linalg.norm(rvec)
    proj3=proj2-np.outer(w2,w2)
    sres=proj3@np.linalg.solve(An,u2);mres=proj3@np.linalg.solve(An,w2)
    assert np.linalg.norm(mres + (1-a2*(vt@An@vt))/(np.linalg.norm(z)*np.linalg.norm(rvec))*sres)<1e-11
    assert np.linalg.norm(sres)>0.15
    if eps==0: assert np.linalg.norm(mres)<1e-13
print('VERIFIED: exact fourth-step witness, rational Gram residuals, and neighboring projections')
