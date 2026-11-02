# Exact John and Löwner ellipsoids of Euclidean capsules with a sharp volume-ratio spectrum

## Finding

For every integer \(d\ge2\), radius \(r>0\), and half-length \(a\ge0\), define the full-dimensional Euclidean capsule
\[
K_{r,a}=rB_2^d+[-a,a]e_1\subset\mathbb R^d.
\]
Put \(s=a/r\) and let \(w\) denote the unique solution in \((0,1/\sqrt d]\) of
\[
dw^2+(d-1)sw=1,
\qquad
w=\frac{2}{\sqrt{(d-1)^2s^2+4d}+(d-1)s}.
\]
Write points as \((x,y)\in\mathbb R\times\mathbb R^{d-1}\). The **unique maximum-volume contained ellipsoid** and the **unique minimum-volume covering ellipsoid** are, respectively,
\[
J_{r,a}=\left\{(x,y):\frac{x^2}{(r+a)^2}+\frac{\|y\|^2}{r^2}\le1\right\}
\]
and
\[
L_{r,a}=\left\{(x,y):\frac{x^2}{d r^2(s+w)^2}
+\frac{(d-1)\|y\|^2}{d r^2(1-w^2)}\le1\right\}.
\]
Their volume quotient is exactly
\[
\mathcal R_d(s)
=\frac{d^{d/2}}{(d-1)^{(d-1)/2}}
\frac{1+w}{1+dw}(1-w^2)^{(d-1)/2}.
\]
It is strictly increasing for \(s\ge0\), starting at \(\mathcal R_d(0)=1\), and for every \(s>0\) satisfies the sharp inequalities
\[
1<\mathcal R_d(s)<\frac{d^{d/2}}{(d-1)^{(d-1)/2}}.
\]
The upper endpoint is a strict supremum attained only in the rod-degeneration limit \(s\to\infty\). More precisely,
\[
\mathcal R_d(s)=1+(\sqrt d-1)s+O_d(s^2)\quad(s\downarrow0),
\]
\[
\mathcal R_d(s)=\frac{d^{d/2}}{(d-1)^{(d-1)/2}}
\big(1-s^{-1}+O_d(s^{-2})\big)\quad(s\to\infty).
\]
For \(s>0\), the Löwner contact set consists **exactly** of the two rotationally symmetric \((d-2)\)-spheres
\[
\left\{\big(\pm r(s+w),\,r\sqrt{1-w^2}\,z\big):\ z\in S^{d-2}\right\}.
\]
For \(s=0\) both extremal ellipsoids equal the ball \(rB_2^d\).

## Assumptions and scope

All volumes are ordinary \(d\)-dimensional Lebesgue volumes. The Euclidean ball is closed and centered at the origin. The axis \(e_1\) is a Euclidean unit vector. The inner ellipsoid is the John ellipsoid; the outer one is the Löwner ellipsoid. The family includes a ball when \(a=0\), and no claim is made for a radius-zero, lower-dimensional body. The contact-sphere assertion for \(d=2\) means two copies of \(S^0\), hence four points.

## Proof

**1. Symmetry and the inner ellipsoid.** The capsule is invariant under reflection of its axial coordinate and all orthogonal transformations in the transverse \((d-1)\)-space. Existence and uniqueness of the extremal ellipsoids imply that both are centered at the origin and have one axial and one transverse semiaxis (for \(d=2\), use both coordinate reflections). For a unit direction with axial coordinate of absolute value \(v\in[0,1]\), the support function of the capsule is \(r+av\). The proposed John ellipsoid has support
\[
r\sqrt{1+s(s+2)v^2}\le r(1+sv),
\]
because the squares differ by \(2r^2sv(1-v)\ge0\). Hence \(J_{r,a}\subset K_{r,a}\). Every axially symmetric ellipsoid inside the capsule has axial semiaxis at most \(r+a\) and transverse semiaxis at most \(r\), by comparing coordinate support widths. Our candidate reaches both bounds, so it maximizes volume among the symmetry-forced possibilities, and uniqueness proves the assertion.

**2. Exact containment of the outer ellipsoid.** Divide by \(r\) and set \(r=1\) temporarily. Let
\[
A=\sqrt d(s+w),\qquad B=\sqrt{\frac d{d-1}}\sqrt{1-w^2}.
\]
For \(s>0\), the defining quadratic for \(w\) implies \(0<w<1/\sqrt d\), so \(A>B\). Every point of the translated unit ball centered at \(se_1\) can be written as \((s+v,\sqrt{1-v^2}\,z)\), with \(-1\le v\le1\) and \(\|z\|=1\), including limiting poles. Its ellipsoidal squared norm is
\[
F(v)=\frac{(s+v)^2}{A^2}+\frac{1-v^2}{B^2}.
\]
This is a strictly concave quadratic. The unique stationary maximum occurs at \(v=w\), since
\[
\frac{s+w}{A^2}=\frac w{B^2}
\quad\Longleftrightarrow\quad dw^2+(d-1)sw=1.
\]
At that point, \(F(w)=1/d+(d-1)/d=1\). Thus the entire translated ball lies in the proposed ellipsoid; by axial reflection so does the ball centered at \(-se_1\). Their convex hull is precisely \(K_{1,s}\), proving containment. For \(s=0\), both proposed semiaxes are one.

**3. Global optimality and the contact set.** For \(s>0\), the only end-ball points attaining \(F(v)=1\) have \(v=w\). Strict convexity of the enclosing ellipsoid shows that convex combinations of distinct such points cannot yield additional boundary contacts. Therefore its exact contact set is the two spheres stated above. Under the affine map carrying \(L_{1,s}\) to the unit ball, these points become
\[
Z_{\pm,z}=\left(\pm\frac1{\sqrt d},\sqrt{\frac{d-1}{d}}z\right),\qquad z\in S^{d-2}.
\]
Choose the sign equiprobably and independently choose \(z\) uniformly on \(S^{d-2}\). Then
\[
\mathbb EZ_{\pm,z}=0,\qquad
\mathbb E(Z_{\pm,z}Z_{\pm,z}^{\mathsf T})=\frac1d I_d.
\]
The Löwner contact characterization (dual to the usual John characterization) now proves global minimum volume and uniqueness. This is also verifiable directly for centered competing ellipsoids using the trace–determinant inequality and uniqueness/symmetry to reduce to centered competitors.

**4. Ratio, strict monotonicity, and endpoints.** Ellipsoidal volume is the unit-ball volume times the product of semiaxes, so
\[
\frac{\operatorname{vol}(L_{r,a})}{\operatorname{vol}(J_{r,a})}
=\frac{A B^{d-1}}{s+1}.
\]
The defining equation for \(w\) yields
\[
s=\frac{1-dw^2}{(d-1)w},\quad
s+w=\frac{1-w^2}{(d-1)w},\quad
1+s=\frac{(1-w)(1+dw)}{(d-1)w},
\]
which gives the displayed closed formula. Differentiating its logarithm with respect to \(w\) gives
\[
\frac{d}{dw}\log\mathcal R_d
=\frac{1-d}{(1+w)(1+dw)}-\frac{(d-1)w}{1-w^2}<0.
\]
As \(s\) increases, \(w\) decreases strictly from \(1/\sqrt d\) to zero. This proves the strict monotonicity and sharp range. Expanding the defining equation near these endpoints yields \(w=1/\sqrt d-(d-1)s/(2d)+O_d(s^2)\) at zero and \(w=((d-1)s)^{-1}+O_d(s^{-3})\) at infinity, giving both asymptotic expansions.

## Verification

The accompanying script `verify_capsule.py` evaluates the exact quadratic containment maximum over translated balls, checks normalized contact moments and the defining algebraic identities, tests the John support inequality, and independently minimizes the enclosing ellipsoid log-volume numerically. It checks 42 positive dimension–aspect-ratio pairs for dimensions \(2,3,4,5,8,16\), with maximum algebraic residual \(4.45\times10^{-16}\) and maximum numerical log-volume discrepancy \(3.7\times10^{-10}\) in the execution recorded here. Numerical optimization is not used as a proof of uniqueness or global minimality; those are established analytically above.

## Relationship to prior work

John's 1948 contact theory, as developed in Ball's dated 1990 preprint, supplies the general maximal-inscribed-ellipsoid criterion. Seeger's 1993 Theorem 2.3 gives an exact *family* of circumscribing ellipsoids for Minkowski sums, explicitly allowing rank-one flat summands; applying that theorem to a ball plus a segment supplies a natural family of outer candidates. Its paper does not select a minimum-volume member for this capsule, identify the actual Löwner contact orbit, give the John and Löwner pair together, or establish the strictly monotone sharp volume-ratio spectrum. In particular, the result proved here requires and supplies a separate global Löwner contact certificate. This attribution does not claim novelty for the general ellipsoid-calculus formula or contact theorem.

## Limitations

Historical novelty is assessed against the inspected sources and literature searches, not independently certified. The 1991 Kurzhanski–Valyi working paper referenced by Seeger was not inspected in full and remains a possible historical-priority source. The theorem concerns the exactly isotropic Euclidean ball-plus-segment family (and affine images), not arbitrary Minkowski sums of ellipsoids. Numerical checks are finite; the continuum containment and optimum follow from the analytic proof.

## References

1. K. Ball, *Ellipsoids of maximal volume in convex bodies*, arXiv:math/9201217v1, publicly dated 1990-09-25. https://arxiv.org/pdf/math/9201217
2. A. Seeger, *Calculus rules for combinations of ellipsoids and applications*, Bulletin of the Australian Mathematical Society 47 (1993), 1–12, Theorem 2.3 and §3. DOI:10.1017/S0004972700012211. https://doi.org/10.1017/S0004972700012211
3. A. B. Kurzhanski and I. Valyi, *Ellipsoidal techniques: guaranteed state estimation*, 1991 working paper, referenced by Seeger; full material not inspected.
