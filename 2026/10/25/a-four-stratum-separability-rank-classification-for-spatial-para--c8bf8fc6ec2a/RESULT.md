# A four-stratum separability-rank classification for spatial parallel sections

## Finding

For a convex body \(K\subset\mathbb R^3\) containing the origin in its interior, define its parallel-section-area function by
\[
S_K(u,t)=\mathcal H^2\bigl(K\cap\{x\in\mathbb R^3:u\cdot x=t\}\bigr),\qquad u\in S^2.
\]
Its **local separation rank** \(r(K)\) is the least positive integer \(r\) for which functions \(a_j:S^2\to\mathbb R\), \(b_j:(-\delta,\delta)\to\mathbb R\), and a common \(\delta>0\) satisfy
\[
S_K(u,t)=\sum_{j=1}^r a_j(u)b_j(t)
\quad(u\in S^2,\ |t|<\delta).
\]
The functions need not satisfy extra regularity assumptions. If no finite representation exists, set \(r(K)=\infty\).

**Classification.** The only finite values are \(1,2,3\). Write any origin-containing ellipsoid as
\[
K=c+A^{1/2}B_2^3,\qquad A=A^\top\succ0,\quad c^\top A^{-1}c<1,
\qquad B=A-cc^\top.
\]
Here \(B_2^3\) is the Euclidean unit ball, and \(B\succ0\). The complete alternatives are:

1. \(r(K)=1\) exactly for Euclidean balls centered at the origin (\(c=0\), \(A=\sigma I\)).
2. \(r(K)=2\) exactly for (a) origin-centered nonspherical ellipsoids (\(c=0\), \(A\) nonscalar), and (b) noncentered prolate spheroids having the origin as one Euclidean focus (\(c\ne0\), \(B=\sigma I\)).
3. \(r(K)=3\) exactly for noncentered ellipsoids for which \(B\) is nonscalar.
4. \(r(K)=\infty\) for every nonellipsoidal convex body.

Every case is attained. The exclusion of nonellipsoidal finite-rank bodies uses the published geometric rigidity theorem of Fish–Ryabogin–Sun–Yaskin [1, Theorem 4.2]. The contribution beyond that theorem is the exact minimum number of separated terms, in particular the exceptional off-center focal stratum.

## Assumptions and scope

The ambient space is Euclidean \(\mathbb R^3\); area is ordinary Euclidean two-dimensional measure, and \(u\) ranges over all unit normals, including both signs. The offset interval is required to be independent of \(u\) and to contain zero. The body is compact, convex, and full-dimensional, with \(0\in\operatorname{int}K\). Ellipsoid matrices are symmetric positive definite, and the representation of an ellipsoid by its center \(c\) and positive-definite squared-semiaxis matrix \(A\) is unique. A scalar matrix means \(\sigma I\) with \(\sigma>0\).

## Proof

**Step 1: exact affine section-area expression.** For an ellipsoid \(K=c+A^{1/2}B_2^3\), let \(q(u)=u^\top Au\) and \(v(u)=c\cdot u\). Passing to Euclidean ball coordinates shows that the corresponding section of \(B_2^3\) is a disk of squared radius \(1-(t-v)^2/q\), and the area Jacobian of \(A^{1/2}\) restricted to this plane is \(\sqrt{\det A}/\sqrt q\). Therefore, whenever the section has interior,
\[
S_K(u,t)=\frac{\pi\sqrt{\det A}}{q(u)^{3/2}}
  \bigl(q(u)-(t-v(u))^2\bigr).
\]
As the origin lies in the interior of \(K\), a uniform \(\delta>0\) makes every such section nonempty for \(|t|<\delta\). Set \(B=A-cc^\top\), which is positive definite by \(c^\top A^{-1}c<1\). Then
\[
S_K(u,t)=\frac{\pi\sqrt{\det A}}{q(u)^{3/2}}
  \left(u^\top Bu+2t(c\cdot u)-t^2\right).\tag{1}
\]

**Step 2: rank of a quadratic in the offset.** The scalar multiplier in front of the parentheses is nonzero for all \(u\), so it does not affect separation rank. For any three distinct numbers \(t_0,t_1,t_2\in(-\delta,\delta)\), the Vandermonde matrix \((1,t_i,t_i^2)\) is invertible. Consequently the linear span of all direction-dependent sections \(u\mapsto S_K(u,t)\) as \(t\) varies is precisely the span of the three coefficient functions
\[
u\longmapsto u^\top Bu,\quad u\longmapsto c\cdot u,\quad u\longmapsto 1,
\]
with the identically zero coefficient omitted. A separated representation with \(r\) terms gives a span of dimension at most \(r\), and any basis of the coefficient span gives a representation with exactly that many terms. Thus the separation rank equals this coefficient-space dimension.

**Step 3: the independence test.** If \(c=0\), the odd linear function vanishes and \(B=A\); the remaining even functions \(u^\top Au\) and \(1\) are dependent exactly when \(A\) is scalar, by the Rayleigh quotient/eigenvector criterion. This yields ranks one and two. If \(c\ne0\), the odd function \(u\mapsto c\cdot u\) is nonzero and linearly independent of all even functions by comparing \(u\) and \(-u\). The two even functions are dependent exactly when \(B\) is scalar. This yields ranks two and three, with no hidden cancellations. The matrix \(B\) is automatically positive definite by the ellipsoid's interior condition.

**Step 4: geometry of the exceptional rank-two case.** If \(c\ne0\) and \(B=\sigma I\), then \(A=\sigma I+cc^\top\). Thus the principal semiaxes are \(\sqrt{\sigma+\|c\|^2}\) in the direction of \(c\), and \(\sqrt\sigma\) in either transverse direction. This is a prolate spheroid whose focal separation from its center is \(\sqrt{\sigma+\|c\|^2-\sigma}=\|c\|\). Its two foci are \(c\pm c\), one being the origin. Conversely a prolate spheroid with a focus at the origin has exactly this covariance form, hence rank two. In particular, this exception is **not** restricted to origin-centered bodies.

**Step 5: no further finite ranks.** Fish–Ryabogin–Sun–Yaskin [1, Theorem 4.2] prove that any convex body in odd Euclidean dimension with locally separable parallel section function near the origin is an ellipsoid; the theorem assumes no boundary smoothness. Apply it in dimension three. Therefore every nonellipsoidal convex body has infinite rank. Combining this external rigidity theorem with Steps 1–4 completes the four-stratum classification.

**Step 6: attainability.** A ball centered at the origin realizes rank one; any nonspherical centered ellipsoid realizes rank two; a translated ball with nonzero displacement smaller than its radius realizes rank three; any cube containing the origin strictly realizes infinite rank. The additional focal subclass of rank two is realized by \(c=(2,0,0)\), \(A=\operatorname{diag}(5,1,1)\).

## Verification

The standalone file `verification/verify_section_rank.py` uses only the Python standard library. Invoke `python3 verification/verify_section_rank.py`. For five explicitly stated ellipsoids it computes coefficient ranks by exact rational Gaussian elimination on twelve rational points of \(S^2\). Separately, it derives planar areas by completing the square in the induced two-dimensional quadratic form, and compares those values with (1) for 180 parameter combinations. It also exactly checks \(u^\top(A-cc^\top)u=1\) in twelve rational directions for the focal example. All checks passed. The finite tests corroborate the exact computations; the infinite classification is proved analytically conditional on [1, Theorem 4.2].

## Relationship to prior work

Reference [1] introduces local separability of section functions and proves the central geometric rigidity implication used in Step 5. Its Theorem 4.2 distinguishes ellipsoids from other convex bodies but does not determine the **minimal number** of separated terms, distinguish the three finite rank strata, or identify the origin-at-focus exception. Reference [2] classifies separably integrable origin-symmetric convex bodies for a related isotropic-volume functional; its symmetry restriction excludes the exceptional displaced focal class. Reference [3, Remark 1.3] gives an explicit standard centered-ellipsoid section formula and studies polynomial/algebraic section functions; the centered formula is compatible with the rank-one and rank-two cases, but neither the complete rank stratification nor the focal exception is asserted there. These known formulas and results are used as background, not claimed as discoveries.

## Limitations

The classification fixes dimension three and a Euclidean reference origin and requires a common interval of offsets for all normals. It does not classify local separation rank in higher odd dimensions, nonconvex sets, or arbitrary restricted normal families. The nonellipsoid implication relies on an external published theorem [1] and is not independently reproved. A search of accessible literature did not reveal the same rank-minimality/focal classification; this is not a guarantee of priority, and older specialized tomographic or finite-rank literature could contain an equivalent statement. No independent external audit has been performed.

## References

[1] Alexander Fish, Dmitry Ryabogin, Wen Rui Sun, Vladyslav Yaskin, *On determination of convex bodies by their section functions*, 2026, arXiv:2610.10229, especially §1 and Theorem 4.2, https://arxiv.org/abs/2610.10229 (first public 2026-10-07).

[2] Vladyslav Yaskin and Bartłomiej Zawalski, *On separably integrable symmetric convex bodies*, arXiv:2306.17127, https://arxiv.org/abs/2306.17127 (first public 2023-06-29).

[3] Mark Agranovsky, *Convex bodies with algebraic section volume functions*, arXiv:2409.19373, https://arxiv.org/abs/2409.19373 (first public 2024-09-28).
