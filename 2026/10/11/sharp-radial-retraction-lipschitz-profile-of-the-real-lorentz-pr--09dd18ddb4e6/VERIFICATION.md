---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the radial Lipschitz theorem

Let \(0<w<1\), \(a=1+w\), \(z=(1,w)\), and let the signed-permuted unit-ball vertices be \((\pm1,\pm w)\) and \((\pm w,\pm1)\). Define the exact norm
\[
N_w(u,v)=\max\left\{|u|,|v|,\frac{|u|+|v|}{a}\right\}.
\]

The supporting functionals incident with \(z\) are \(f_V(u,v)=u\) and \(f_D(u,v)=(u+v)/a\). For the linear functional \(\ell(u,v)=v-wu\), the vertex values in absolute value are precisely
\[
\{0,1-w^2,2w,1+w^2\}.
\]
Because \((1-w)^2\ge0\), its dual norm is \(\|\ell\|_{X_w^*}=1+w^2\), attained at \((-w,1)\). The two endpoint matrices, their images, and norms are
\[
Q_V=I-z\otimes f_V,\quad Q_V(u,v)=(0,v-wu),\quad\|Q_V\|=1+w^2,
\]
\[
Q_D=I-z\otimes f_D,\quad Q_D(u,v)=\frac{wu-v}{a}(1,-1),\quad\|Q_D\|=\frac{2(1+w^2)}{a^2}.
\]
No exhaustive numerical grid is involved: the norm over the unit polygon is attained at its finitely many vertices, and the map \(z\mapsto\|I-z\otimes f\|\) is convex on each facet. The global radial Lipschitz bound follows by integrating derivatives on generic line segments and passing by continuity to arbitrary segments. Sharpness follows by approaching the pertinent facet endpoint from the exterior, using the unit direction \((-w,1)\), not by asserting attainment of a finite-pair supremum.

Independent exact-rational checks evaluated the two operator norms by complete vertex enumeration at weights \(1/10\), \(1/5\), \(1/3\), \(1/2\), \(7/10\), and \(9/10\), and matched both closed expressions. These checks are independent of the analytic proof but finite and do not certify the infinite statement by themselves.

The branch equality requires \((1+w)^2=2\), giving the unique admissible parameter \(w=\sqrt2-1\). The first branch has derivative \(4(w-1)/(1+w)^3<0\); the second has derivative \(2w>0\). Their intersection is the unique global minimum \(4-2\sqrt2\). Scaling establishes radius-independence for all \(r>0\).
