# Exact Minkowski asymmetry and complete center loci of homothetic frusta

## Finding
For an integer \(m\ge1\), let \(B\subset\mathbb R^m\) be **any** compact convex body with nonempty interior, not necessarily centrally symmetric, smooth, or polyhedral. Put
\[
F_t(B)=\operatorname{conv}(B\times\{0\},\,tB\times\{1\}),\qquad 0\le t\le1.
\]
For a convex body \(C\), define its Minkowski asymmetry and minimizing-center set by
\[
s(C)=\min\{\lambda\ge1:\exists c,\quad (1+\lambda)c-C\subseteq\lambda C\},
\qquad M(C)=\{c:(1+s(C))c-C\subseteq s(C)C\}.
\]
Write \(\sigma=s(B)\). The entire homothetic-frustum family satisfies the **exact additive asymmetry law**
\[
\boxed{s(F_t(B))=\sigma+1-t.}\tag{1}
\]
For every genuine frustum and for the pyramid endpoint, \(0\le t<1\), the **complete set of minimizing Minkowski centers** is
\[
\boxed{M(F_t(B))=
\left\{\left(\frac{\sigma+1}{\sigma+2-t}c,\frac1{\sigma+2-t}\right):c\in M(B)\right\}.}\tag{2}
\]
For the prism endpoint, the complete center locus is instead
\[
\boxed{M(F_1(B))=M(B)\times
\left[\frac1{\sigma+1},\frac\sigma{\sigma+1}\right].}\tag{3}
\]
Thus for \(t<1\) every minimizing center has the same axial coordinate, but it need not be unique horizontally. When \(\sigma>1\), the prism acquires an additional independent axial interval of minimizing centers at \(t=1\), a genuine change of center-locus dimension.

In ambient dimension \(d=m+1\), the bound on base asymmetry yields the **sharp range**
\[
\boxed{2-t\le s(F_t(B))\le d-t.}\tag{4}
\]
The lower equality occurs exactly when \(B\) is centrally symmetric; the upper equality occurs exactly when \(B\) is a simplex in its affine span. In the planar case, every interval base is both, and the two bounds coincide. Formula (1) also reconstructs the taper directly from the asymmetries of the full frustum and its base: \(t=1+\sigma-s(F_t(B))\).

## Assumptions and scope
The base \(B\) has affine dimension \(m\ge1\), and the two parallel sections are related by positive homothety about the coordinate origin, with the limiting apex \(t=0\) admitted. This is a full-dimensional convex body in \(\mathbb R^{m+1}\), regardless of whether the origin lies in \(B\). The height-one parametrization is affine; arbitrary positive height and affine shear preserve the conclusions after transforming centers accordingly. The scalar \(t\) is a nonnegative section homothety ratio, **not** a Euclidean aspect ratio.

For the containment convention above, \(M(B)\) is nonempty and contained in \(B\). The latter follows directly: if \((1+\sigma)c-b\in\sigma B\) for any \(b\in B\), then \((1+\sigma)c\in B+\sigma B=(1+\sigma)B\), hence \(c\in B\). At \(t=1\), the limiting body is the prism \(B\times[0,1]\). The theorem concerns Minkowski **point-reflection** asymmetry, not the optimal overlap volume of a reflected body, nor its Santaló point, John ellipsoid, or reflection in an affine hyperplane.

## Proof
**1. The optimal containment criterion.** For \(\lambda\ge1\), a point \(p=(q,z)\) is a feasible center at factor \(\lambda\) precisely when
\[
(1+\lambda)p-F_t(B)\subseteq\lambda F_t(B).\tag{5}
\]
Let \(k=1-t\). The section of \(\lambda F_t(B)\) at vertical coordinate \(w\in[0,\lambda]\) is
\[
(\lambda-kw)B.\tag{6}
\]
Because the upper generating section of \(F_t(B)\) lies at height \(1\), its reflection under (5) lies at height \((1+\lambda)z-1\), which must be nonnegative. Consequently
\[
z\ge\frac1{1+\lambda}.\tag{7}
\]
The reflected lower generating section lies at height \(w=(1+\lambda)z\). Applying (6) to it gives the *necessary* horizontal containment
\[
(1+\lambda)q-B\subseteq
\bigl[\lambda-k(1+\lambda)z\bigr]B.\tag{8}
\]
By the definition of the base's Minkowski asymmetry, the bracketed factor must be at least \(\sigma\). Combining this with (7) gives
\[
\sigma\le\lambda-k(1+\lambda)z\le\lambda-k,
\qquad\text{so}\quad \lambda\ge\sigma+k.\tag{9}
\]
This lower bound holds for **every** center, including off-axis centers and all nonsmooth or asymmetric bases.

**2. An attaining center.** Choose any \(c\in M(B)\), and set
\[
\lambda=\sigma+k=\sigma+1-t,\qquad
z=\frac1{\lambda+1},\qquad
q=\frac{\sigma+1}{\lambda+1}c.\tag{10}
\]
The defining inclusion for \(c\) is
\[
(1+\sigma)c-B\subseteq\sigma B.\tag{11}
\]
Under the affine reflection in (5), the lower generator \(B\times\{0\}\) maps to the horizontal section at height \(1\), with horizontal set \((1+\sigma)c-B\). By (6), the target section there is \((\lambda-k)B=\sigma B\); hence (11) proves its containment.

The upper generator \(tB\times\{1\}\) maps to height \(0\), where the target section is \(\lambda B\). Since \(c\in B\), the following is a valid Minkowski-sum inclusion:
\[
\begin{aligned}
(1+\sigma)c-tB
&=t\big((1+\sigma)c-B\big)+(1-t)(1+\sigma)c\\
&\subseteq t\sigma B+(1-t)(1+\sigma)B\\
&=\bigl[t\sigma+(1-t)(1+\sigma)\bigr]B
=\lambda B.
\end{aligned}\tag{12}
\]
Here the sum equality uses convexity of \(B\) and nonnegative coefficients; no symmetry is used. The two generating-section inclusions (11)--(12), together with the convexity of \(\lambda F_t(B)\), establish (5) on their entire convex hull. This attains the lower bound (9), proving (1).

**3. Every center when \(0\le t<1\).** Suppose (5) holds at the optimal factor \(\lambda=\sigma+k\). The lower-bound chain (9) must consist entirely of equalities. Because \(k>0\), (7)--(9) force
\[
z=\frac1{\sigma+2-t}.\tag{13}
\]
The lower-section inclusion (8) now reads
\[
(\sigma+2-t)q-B\subseteq\sigma B.\tag{14}
\]
By definition, this is equivalent to \(c=((\sigma+2-t)/(\sigma+1))q\in M(B)\). Every such \(c\) is feasible by Step 2, proving the *entire* locus (2), not merely an example of an optimal center.

**4. The prism endpoint.** For \(t=1\), \(F_1(B)=B\times[0,1]\) is a Cartesian product. The reflected-containment condition (5) at factor \(\lambda\) separates into
\[
(1+\lambda)q-B\subseteq\lambda B,
\qquad 0\le(1+\lambda)z-1,
\qquad (1+\lambda)z\le\lambda.\tag{15}
\]
The first condition forces \(\lambda\ge\sigma\). At \(\lambda=\sigma\), it is precisely \(q\in M(B)\), and the other two are \(1/(\sigma+1)\le z\le\sigma/(\sigma+1)\). This proves (3) without a continuity assumption at \(t=1\).

**5. Rigidity and examples.** The classical sharp bounds \(1\le s(B)\le m\), with central symmetry and simplices as the respective equality cases, inserted into (1) prove (4). For a triangular base, \(\sigma=2\), so in three dimensions \(s(F_t(B))=3-t\); its center is unique. For a centrally symmetric base in any dimension, \(\sigma=1\), so the value is \(2-t\). If \(B\) is a product of a triangle and a symmetric segment, then \(\sigma=2\) but its base Minkowski center set is an interval; (2) transports the full interval to a fixed-height center locus, whereas (3) supplies an extra axial interval at the prism endpoint. These examples verify that the nonuniqueness assertion is real and need not be a limiting convention.

## Verification
The standalone `verify.py` checks the reflection inclusion with **exact rational arithmetic** for an asymmetric triangle base, a centrally symmetric square base, and the product of a triangle and a segment with a non-singleton set of base Minkowski centers. It tests both pyramid/prism endpoints and three interior tapers, including both extreme centers of the latter interval. An *independent unrestricted linear program* minimizes the dilation factor over all ambient center coordinates using every vertex-to-facet inequality of the actual polytope; this independently recovers the theoretical value in fifteen cases. The command `python verify.py` (with SciPy installed) prints `ALL_CHECKS_PASSED` when assertions succeed. These finite checks are diagnostic; Steps 1--5 give the universal proof for all dimensions and bases.

## Relationship to prior work
Brandenberg, von Dichter, and González Merino study Minkowski asymmetry and its relation to symmetrizations and diameter-to-width inequalities. Their definitions and the classical \([1,m]\) asymmetry bounds are used here; their main theorems do **not** supply (1)--(3) for homothetic frusta. A publicly available result on *Santaló and volume-product laws for homothetic frusta* treats exactly the same family of bodies but a different affine invariant. Its shape-independent polar-volume formula does not determine the optimal point-reflection containment factor or its full center locus. Similarly, results on Godbersen mixed-volume profiles of one-vertex simplex truncations concern mixed volumes and a simplex-base subfamily, not arbitrary-base asymmetry or all its centers.

The relationship is therefore one of **different implications**, not merely different names. Even if one knows every frustum's John or Santaló center, neither its Minkowski center nor its sharp reflection factor follows: these centers optimize different geometric functionals. The two-generator, base-asymmetry containment certificate in the proof provides the missing universal link.

## Limitations
Only *homothetic parallel sections with a common homothety origin* are covered. Nonhomothetic convex hulls, unequal unrelated bases, and nonlinear taper profiles are excluded. The formula does not reconstruct the unknown base or determine \(t\) from the frustum asymmetry alone unless \(s(B)\) is known. The proof gives exact ideal-body invariants, not a numerical stability theorem under noisy measurements.

Historical priority of this exact additive identity and full center-locus description is not independently certified; specialized older literature on Minkowski centers of pyramids or truncated prisms may contain an equivalent formula. The triangle and simplex endpoint implications of general Minkowski-asymmetry theory are credited rather than claimed as independent discoveries. An independent mathematical audit has not been performed.

## References
1. R. Brandenberg, K. von Dichter, and B. González Merino, *From inequalities relating symmetrizations of convex bodies to the diameter-width ratio for complete and pseudo-complete convex sets*, arXiv:2306.11460v1, first public 20 June 2023; especially §1 on Minkowski asymmetry and Theorems 1.1--1.3.
2. *Universal Santaló and volume-product laws for homothetic frusta*, publicly available research result dated 11 October 2026; its polar-section, Santaló-center, and volume-product formulas concern the identical body family but a different invariant.
3. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, publicly available research result dated 11 October 2026; a simplex-based truncation family and mixed-volume functional rather than the Minkowski asymmetry.
4. D. Pavlov and S. Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955v1, 29 February 2024, for the distinct Santaló-center and rational polar-volume framework.
