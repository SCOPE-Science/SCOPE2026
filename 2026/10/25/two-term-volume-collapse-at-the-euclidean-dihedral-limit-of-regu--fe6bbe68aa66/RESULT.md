# Two-term volume collapse at the Euclidean dihedral limit of regular hyperbolic simplices

## Finding

For every integer \(d\ge 2\), let \(S_d(\alpha)\subset\mathbb H^d\) be the regular compact hyperbolic \(d\)-simplex, in sectional curvature \(-1\), whose interior dihedral angles are all \(\alpha\). Put \(\beta_d=\arccos(1/d)\). As \(\alpha\uparrow\beta_d\), define \(t=\beta_d-\alpha\). Its hyperbolic volume obeys the **sharp two-term law**

\[
\operatorname{Vol}_d(S_d(\alpha))
=C_d t^{d/2}\bigl(1+B_dt+O_d(t^2)\bigr),
\]

\[
C_d=\frac{\sqrt{d+1}\,d^{d/2}(d^2-1)^{d/4}}{d!},\qquad
B_d=\frac{d^2(d^2-2)}{2(d+1)(d+2)}\frac{\sqrt{d^2-1}}d
-\frac{d}{4\sqrt{d^2-1}}.
\]

In dimension four this becomes the especially simple exact expression

\[
\boxed{\operatorname{Vol}_4(S_4(\alpha))
=10\sqrt5\,t^2\bigl(1+\frac{13\sqrt{15}}{15}t+O(t^2)\bigr),\quad
 t=\arccos(1/4)-\alpha\downarrow0.}
\]

Consequently, subject to the classification of minimizing equiangular hyperbolic four-polytopes established by Egorov [1], the minimum-volume branch approaching \(\arccos(1/4)\) from below dies quadratically with the stated sharp coefficient, whereas at the endpoint the minimum is the strictly positive volume of the regular hyperbolic four-cube. Thus the minimum-volume function has a positive upward jump at this combinatorial switch. The quantitative coefficients, rather than the qualitative degeneration or the classification of minimizers, are the claim established here.

## Assumptions and scope

Work in real simply connected hyperbolic space with constant curvature \(-1\) and its Klein unit-ball model. A regular compact \(d\)-simplex is unique up to isometry whenever its common dihedral angle is sufficiently close to and less than \(\beta_d\). Every asymptotic statement is for fixed integer \(d\), with \(t>0\) tending to zero. Landau constants can depend on \(d\). Volume uses the ordinary hyperbolic Riemannian volume form, not Euclidean coordinate volume. The four-polytope minimum statement invokes [1] and is conditional on that cited classification, whose argument is not reproduced.

## Proof

**1. Dihedral angle and Klein circumradius.** Let \(w_0,\dots,w_d\in\mathbb R^d\) be the vertices of the Euclidean regular simplex centered at zero and inscribed in the Euclidean unit sphere, so that \(\langle w_i,w_j\rangle=-1/d\) for \(i\ne j\). In the Klein model place the hyperbolic vertices at \(Rw_i\), where \(0<R<1\).

Their hyperboloid lifts have mutual hyperbolic cosine

\[
q=\cosh\ell=\frac{1+R^2/d}{1-R^2},
\]

where \(\ell\) is the hyperbolic edge length. The Lorentzian Gram matrix of the \(d+1\) lifts has diagonal \(-1\) and off-diagonal \(-q\), i.e., \((q-1)I-qJ\). Its inverse has diagonal proportional to \(1+(d-1)q\) and off-diagonal proportional to \(-q\). After the standard normalization of outward facet normals, their off-diagonal Lorentzian pairing is \(-\cos\alpha\); therefore

\[
\cos\alpha=\frac{q}{1+(d-1)q}
=\frac{d+R^2}{d^2-R^2}.
\]

In particular,

\[
R^2=\frac{d(d\cos\alpha-1)}{1+\cos\alpha}.
\]

This tends to zero exactly when \(\alpha\) tends upward to \(\beta_d\) through the compact regular-simplex family. No non-Euclidean length scale is suppressed.

**2. Exact integral and Euclidean moment.** Let \(T_d=\operatorname{conv}\{w_0,\dots,w_d\}\). The Klein metric has volume density \((1-\lVert x\rVert^2)^{-(d+1)/2}\), so the hyperbolic volume is exactly

\[
V_d(R)=R^d\int_{T_d}(1-R^2\lVert y\rVert^2)^{-(d+1)/2}\,dy.
\]

The Euclidean volume and normalized second radial moment of \(T_d\) are

\[
|T_d|=\frac{(d+1)^{(d+1)/2}}{d!\,d^{d/2}},\qquad
\frac1{|T_d|}\int_{T_d}\lVert y\rVert^2\,dy=\frac1{d+2}.
\]

For the moment formula, express a uniform point as \(y=\sum_{i=0}^d\lambda_iw_i\), where \((\lambda_i)\) is uniform on the barycentric simplex. Then

\[
\lVert y\rVert^2=\frac{(d+1)\sum_i\lambda_i^2-1}{d},\qquad
\mathbb E\sum_i\lambda_i^2=\frac2{d+2}.
\]

Because \(\lVert y\rVert\le1\), Taylor's expansion of the density is uniform for sufficiently small \(R\), and hence

\[
V_d(R)=|T_d|R^d\left(1+\frac{d+1}{2(d+2)}R^2+O_d(R^4)\right).
\]

**3. Two-term dihedral expansion.** Put \(\delta=\cos\alpha-1/d\). Direct algebra from step 1 yields

\[
R^2=\frac{d^3}{d+1}\,\delta\left(1-\frac{d}{d+1}\delta+O_d(\delta^2)\right).
\]

Substitution in the preceding volume expansion simplifies to

\[
V_d(\alpha)=\frac{d^d\sqrt{d+1}}{d!}\,
\delta^{d/2}\left[1+
\frac{d^2(d^2-2)}{2(d+1)(d+2)}\delta+O_d(\delta^2)\right].
\]

Finally,

\[
\delta=\frac{\sqrt{d^2-1}}d\,t-\frac1{2d}t^2+O_d(t^3).
\]

Collecting the coefficients of \(t^{d/2}\) and \(t^{d/2+1}\) proves the displayed formulas for \(C_d\) and \(B_d\). In dimension four these reduce, exactly, to \(C_4=10\sqrt5\) and \(B_4=13\sqrt{15}/15\). Both constants are positive; in particular the leading exponent and coefficient are sharp. For \(d=2\) the formula gives \(C_2=3\), \(B_2=0\), in agreement with the exact Gauss–Bonnet area \(3(\beta_2-\alpha)\) of a regular hyperbolic triangle.

**4. The four-dimensional minimizer switch.** Egorov [1] classifies the minimum among all finite-volume equiangular hyperbolic four-polytopes: the regular four-simplex minimizes for \(\arccos(1/3)\le\alpha<\beta_4\), while the regular hyperbolic four-cube minimizes for \(\beta_4\le\alpha<\pi/2\). The four-cube at \(\beta_4\) is nondegenerate, hence has strictly positive hyperbolic volume. Applying the newly calculated asymptotic on the simplex branch proves the specified quadratic one-sided collapse and the upward jump. No formula for the four-cube's positive endpoint volume is asserted.

## Verification

The accompanying `verify.py` reconstructs the symbolic coefficients independently and evaluates the exact Klein integral by product Gauss–Legendre quadrature in barycentric coordinates. At \(d=4\), its residual after subtracting the two-term model decreases at the predicted relative quadratic rate for several values of \(t\). At \(d=2\), it verifies the Gauss–Bonnet identity numerically. These checks are finite numerical corroboration; the all-dimensional proof is the analytic expansion above. To reproduce, install dependencies in `requirements.txt`, then run `python verify.py`.

## Relationship to prior work

Egorov [1] establishes the hyperbolic four-polytope extremal classification and explicitly notes the regular simplex's Euclidean degeneration at \(\beta_4\). This work does **not** claim to reprove or supersede that classification. The new target is the dimension-dependent two-term quantitative law with precise coefficients, including its four-dimensional minimizer-branch coefficient. Classical descriptions of regular hyperbolic simplices and their hyperbolic Gram matrices provide basic geometric machinery [2]. The indexed Lassak-thickness result [3] concerns distances between supporting hyperplanes, not hyperbolic volume expansions in the common dihedral angle. An exhaustive priority claim cannot be made: the complete text of [1] was not accessible during the comparison, and a full historical search of small-simplex volume expansions remains outstanding.

## Limitations

The expansion concerns the unique regular simplex at each angle, not the volume of arbitrary equiangular hyperbolic polytopes or their stability near a minimizer. The discontinuity of the four-dimensional minimum relies on the published classification [1]. The displayed remainder is \(O_d(t^{d/2+2})\), with constants depending on fixed dimension; no uniform-in-dimension remainder is claimed. A plausible primary full-text source [1] could contain additional asymptotic details not visible in its accessible abstract. No external independent mathematical audit has been performed.

## References

[1] A. Egorov, *Minimal-Volume Equiangular Hyperbolic 4-Polytopes*, arXiv:2609.04258, first posted 2026-09-01. https://arxiv.org/abs/2609.04258

[2] N. Peyerimhoff, *Simplices of Maximal Volume or Minimal Total Edge Length in Hyperbolic Space*, Journal of the London Mathematical Society 66 (2002), 753–768. https://doi.org/10.1112/S0024610702003629

[3] *Exact Lassak thickness of every regular hyperbolic simplex*, published mathematical finding, 2026-10-04. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-lassak-thickness-of-every-regular-hyperbolic-simplex--e2d5415eae12
