#!/usr/bin/env python3
"""Reproducible checks of a convex-body acute-triangle thin-limit theorem.

Requires NumPy and SciPy. Finite quasi-Monte-Carlo checks are diagnostic,
not proofs of a limit. The polynomial fiber calculation and elementary
moment integrations are exact symbolic-rational calculations below.
"""
from fractions import Fraction as F
from math import log
import numpy as np
from scipy.stats import qmc

# Exact: integral over [0,1]^2 of u min(u,v) = 5/24.
# For fixed u: integral_0^u (u v) dv + integral_u^1 u^2 dv
# = u^3/2 + u^2(1-u) = u^2-u^3/2.
J=F(1,3)-F(1,8)
assert J==F(5,24)
# Two middle-extreme arrangements, each integrating the height r^4.
FIBER=2*J/F(5)
assert FIBER==F(1,12)

# Vertical chord w(x) on [0,1], corresponding areas and fifth moments.
AREAS={"rectangle":F(1),"triangle":F(1,2),"trapezoid":F(3,2)}
MOM5={"rectangle":F(1),"triangle":F(1,6),"trapezoid":F(21,2)}
COEFF={name:MOM5[name]/AREAS[name]**3 for name in AREAS}
assert COEFF=={"rectangle":F(1),"triangle":F(4,3),"trapezoid":F(28,9)}
for name in COEFF:
    A=AREAS[name]
    assert A*A<=COEFF[name]<=F(16,3)*A*A
assert COEFF["rectangle"]==AREAS["rectangle"]**2
assert COEFF["triangle"]==F(16,3)*AREAS["triangle"]**2

# Gap-conditioned unbiased integration within s<t and factor 2 for t<s.
# For t=delta exp(u log(1/delta)), z uniform in [0,Z],
# s=eps^2*z/t; integrate x, independent y fibers and exact angle tests.
# Z must cover the maximal ordinate-difference product, hence Z=4
# for trapezoids of height up to 2, not Z=1.
def approx(shape,eps,n=1<<18):
    seed=7049+int(abs(np.log10(eps))*100)
    U=qmc.Sobol(6,scramble=True,seed=seed).random_base2(int(np.log2(n)))
    delta=eps/10.
    logwindow=np.log(1/delta)
    t=delta*np.exp(U[:,0]*logwindow)
    zmax=4 if shape=="trapezoid" else 1
    z=zmax*U[:,1]
    s=eps*eps*z/t
    remaining=1-s-t
    possible=(s<t)&(remaining>0)
    x=np.maximum(remaining,0.)*U[:,2]
    x1,x2,x3=x,x+s,x+s+t
    if shape=="rectangle":
        w1=np.ones(n);w2=np.ones(n);w3=np.ones(n)
    elif shape=="triangle":
        w1=np.maximum(1-x1,0.);w2=np.maximum(1-x2,0.);w3=np.maximum(1-x3,0.)
    else:
        w1=1+x1;w2=1+x2;w3=1+x3
    y1=U[:,3]*w1;y2=U[:,4]*w2;y3=U[:,5]*w3
    alpha=y2-y1;beta=y3-y2
    acute=(s*(s+t)+eps*eps*alpha*(alpha+beta)>0) & \
          (-s*t-eps*eps*alpha*beta>0) & \
          (t*(s+t)+eps*eps*beta*(alpha+beta)>0)
    hit=possible&acute
    # Sorted x order has multiplicity 6 and the symmetric lobe factor 2.
    P=(12./float(AREAS[shape])**3)*eps*eps*logwindow*zmax*np.mean(
        np.maximum(remaining,0)*w1*w2*w3*hit)
    return P/(eps*eps*log(1/eps)),int(np.count_nonzero(hit))

results=[]
for shape in ("rectangle","triangle","trapezoid"):
    target=float(COEFF[shape])
    estimates=[]
    for eps in (1e-3,1e-7):
        estimate,hits=approx(shape,eps)
        assert np.isfinite(estimate) and hits>=1000
        estimates.append(estimate)
        results.append((shape,eps,round(estimate,6),hits))
    # Increasing logarithmic depth significantly reduces relative error.
    assert abs(estimates[-1]/target-1)<0.11, (shape,estimates,target)
    assert abs(estimates[-1]/target-1)<abs(estimates[0]/target-1)+0.025
print("ACUTE_CHORD_CHECK_OK fiber=1/12 coefficients="+str(COEFF))
for x in results: print("shape,eps,ratio,count",x)
