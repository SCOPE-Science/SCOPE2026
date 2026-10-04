# Exact Euclidean Banach--Mazur distance for a Lorentz-predual octagonal plane
## Finding
For the real plane \(X_w=d_*(1,w)^2\), \(0<w<1\), with \(\|(x,y)\|_w=\max\{|x|,|y|,(|x|+|y|)/(1+w)\}\), the Euclidean Banach--Mazur distance is \(d_{\mathrm{BM}}(X_w,\ell_2^2)=\sqrt{2(1+w^2)}/(1+w)\) for \(0<w\le \sqrt2-1\), and \(d_{\mathrm{BM}}(X_w,\ell_2^2)=\sqrt{1+w^2}\) for \(\sqrt2-1\le w<1\). It is uniquely minimized at \(w=\sqrt2-1\), where it equals \(\sqrt{4-2\sqrt2}\).

## Assumptions and scope
The scalar field is real and \(0<w<1\). The space is the two-dimensional Lorentz predual with norm
\[
\|(x,y)\|_w=\max\left\{|x|,|y|,\frac{|x|+|y|}{1+w}\right\}.
\]
Its unit ball is
\[
K_w=\{(x,y): |x|\le1,\ |y|\le1,\ |x|+|y|\le1+w\},
\]
a centrally symmetric octagon with vertices \((\pm1,\pm w)\) and \((\pm w,\pm1)\), with signs chosen consistently around the boundary. The Banach--Mazur distance is the infimum of \(\lambda\ge1\) over centered ellipses \(E\) satisfying \(E\subset K_w\subset \lambda E\); this is equivalent to distance from \(X_w\) to the Euclidean plane.

## Proof
Let an arbitrary centered ellipse be
\[
E_Q=\{x\in\mathbb R^2:x^{\mathsf T}Q^{-1}x\le1\},
\]
where \(Q\) is positive definite. The support function of \(E_Q\) in direction \(u\) is \(\sqrt{u^{\mathsf T}Qu}\). Since
\[
|x|+|y|=\max\{|x+y|,|x-y|\},
\]
the inclusion \(E_Q\subset K_w\) is equivalent to
\[
Q_{11}\le1,\qquad Q_{22}\le1,
\]
and
\[
(1,1)Q(1,1)^{\mathsf T}\le(1+w)^2,\qquad
(1,-1)Q(1,-1)^{\mathsf T}\le(1+w)^2.
\]
Adding the first pair and then the second pair gives
\[
\operatorname{tr}Q\le2,
\qquad
2\operatorname{tr}Q\le2(1+w)^2.
\]
Hence
\[
\operatorname{tr}Q\le2q_*,\qquad
q_*:=\min\left\{1,\frac{(1+w)^2}{2}\right\}.
\]

Assume also \(K_w\subset \lambda E_Q\). Every one of the eight vertices \(v\) of \(K_w\) then satisfies
\[
v^{\mathsf T}Q^{-1}v\le\lambda^2.
\]
Averaging their rank-one matrices gives the exact isotropy identity
\[
\frac18\sum_v vv^{\mathsf T}=\frac{1+w^2}{2}I.
\]
Therefore
\[
\lambda^2\ge \frac{1+w^2}{2}\operatorname{tr}(Q^{-1}).
\]
If the eigenvalues of \(Q\) are positive, the arithmetic--harmonic mean inequality yields
\[
\operatorname{tr}(Q^{-1})\ge\frac{4}{\operatorname{tr}Q}.
\]
Consequently
\[
\lambda^2\ge\frac{2(1+w^2)}{\operatorname{tr}Q}
\ge\frac{1+w^2}{q_*}.
\]
This lower bound holds for every ellipse, without any symmetry assumption on the optimizer.

For equality, take the Euclidean circle
\[
E_*=\sqrt{q_*}\,B_2.
\]
The definition of \(q_*\) gives \(E_*\subset K_w\). Every vertex of \(K_w\) has Euclidean norm \(\sqrt{1+w^2}\), so by convexity
\[
K_w\subset \sqrt{\frac{1+w^2}{q_*}}\,E_*.
\]
Thus
\[
d_{\mathrm{BM}}(X_w,\ell_2^2)^2=\frac{1+w^2}{q_*}.
\]
If \(0<w\le\sqrt2-1\), then \(q_*=(1+w)^2/2\), giving
\[
d_{\mathrm{BM}}(X_w,\ell_2^2)=\frac{\sqrt{2(1+w^2)}}{1+w}.
\]
If \(\sqrt2-1\le w<1\), then \(q_*=1\), giving
\[
d_{\mathrm{BM}}(X_w,\ell_2^2)=\sqrt{1+w^2}.
\]
The square of the first branch is \(2(1+w^2)/(1+w)^2\), whose derivative is negative for \(w<1\); the square of the second branch is \(1+w^2\), whose derivative is positive. Hence the unique minimum occurs at their junction \(w=\sqrt2-1\), and its squared value is \(4-2\sqrt2\).

## Verification
The lower bound optimizes over an arbitrary positive-definite quadratic form \(Q\); it does not assume a circular or axis-aligned optimal ellipse. The four support inequalities are exactly equivalent to \(E_Q\subset K_w\), the eight-vertex covariance is computed exactly, and the only matrix inequality used is \(\operatorname{tr}(Q^{-1})\ge4/\operatorname{tr}Q\) in dimension two. The explicit circle \(E_*\) attains the lower bound. Numerical sampling was used only as a sanity check before the symbolic proof and is not part of the proof.

## Relationship to prior work
Kim (2011) studies the exact plane \(d_*(1,w)^2\) and its polynomial unit ball, and gives the norm used here. The inspected full text does not discuss Banach--Mazur distance or Euclidean approximation.

Kim (2013) again uses the same norm and records the octagonal extreme points. Its analysis naturally splits at \(w=\sqrt2-1\), but for a different problem involving spaces of linear operators on symmetric bilinear forms. The inspected article contains no Banach--Mazur computation. The formula proved here gives an affine-geometric meaning to that same parameter: it is exactly the unique member of the family closest to the Euclidean plane.

Kim (2016) studies the geometry of symmetric bilinear forms associated with the same octagonal norm. The inspected full text contains no Banach--Mazur, Euclidean-distance, or distance-to-Hilbert formula for \(d_*(1,w)^2\).

## Limitations
The originality comparison is bounded by searchable and accessible literature. An older convex-geometry source could conceivably encode the same square--diamond intersection under different notation without mentioning Lorentz spaces. Targeted searches for the object, the octagonal norm, Banach--Mazur distance, and the threshold \(\sqrt2-1\) did not reveal such a formula. This residual indexing risk does not affect the proof.

## References
1. S. G. Kim, “The unit ball of \(\mathcal P(^2 d_*(1,w)^2)\),” Mathematical Proceedings of the Royal Irish Academy 111A (2011), 79--94. DOI: 10.3318/PRIA.2011.111.1.9.
2. S. G. Kim, “The Unit Ball of \(L_s(^2 d_*(1,w)^2)\),” Kyungpook Mathematical Journal 53 (2013), 295--306. DOI: 10.5666/KMJ.2013.53.2.295.
3. S. G. Kim, “The Geometry of the Space of Symmetric Bilinear Forms on \(\mathbb R^2\) with Octagonal Norm,” Kyungpook Mathematical Journal 56 (2016), 781--791. DOI: 10.5666/KMJ.2016.56.3.781.
