# Parity-exceptional John and Löwner contact structures of diagonal halfcubes

## Finding

For each integer \(d\ge 2\), bisect the Euclidean cube through its center by the hyperplane orthogonal to the main diagonal:
\[
K_d=[-1,1]^d\cap\{x\in\mathbb R^d:\sum_{i=1}^d x_i\ge0\}.
\]
Let \(e=(1,\ldots,1)^\mathsf T\), \(H=ee^\mathsf T/d\), and \(P=I-H\). Define an ellipsoid by
\[
E(t,u,v)=\{x:(x-te)^\mathsf T(uH+vP)^{-1}(x-te)\le1\},\quad u,v>0.
\]
Then the **unique maximum-volume contained ellipsoid** (John ellipsoid) is
\[
E_J=E\left(\frac1{d+1},\frac{d}{(d+1)^2},\frac d{d+1}\right).
\]
Its contact facets are precisely the cutting facet \(e^\mathsf T x=0\) and the \(d\) upper coordinate facets \(x_i=1\); no lower coordinate facet is tangent.

The **unique minimum-volume containing ellipsoid** (Löwner ellipsoid) is \(E_L=E(t_d,u_d,v_d)\), with the following complete exact formulas:
\[
(t_d,u_d,v_d)=
\begin{cases}
\left(\frac1{d+1},\frac{d^3}{(d+1)^2},\frac{d^3}{d^2-1}\right),&d\text{ even};\\[3pt]
\left(\frac{d+1}{4d},\frac{(3d-1)^2}{16d},\frac{(3d-1)^2}{8d}\right),&d\in\{3,5\};\\[3pt]
\left(\frac2{d+1},\frac{d(d-1)^2}{(d+1)^2},d\right),&d\ge7\text{ odd}.
\end{cases}
\]
The **entire set of Löwner-contact vertices** consists of the positive pole \(e\), together with the following orbits:

- For even \(d\): the cube vertices with \(d/2\) positive and \(d/2\) negative entries.
- For odd \(d\ge7\): the cube vertices with \((d+1)/2\) positive entries and \((d-1)/2\) negative entries.
- For \(d=3,5\): the preceding odd cube-vertex orbit *and* all cut-edge midpoint vertices having one zero coordinate and equal counts of \(+1\) and \(-1\) among the others.

Consequently the total Löwner-contact vertex count is
\[
N_d=\begin{cases}
1+\binom d{d/2},&d\text{ even},\\
1+\binom d{(d+1)/2}+d\binom{d-1}{(d-1)/2},&d\in\{3,5\},\\
1+\binom d{(d+1)/2},&d\ge7\text{ odd}.
\end{cases}
\]
In particular, \(N_3=10\) (all vertices of \(K_3\) contact), \(N_5=41\), while the cut-edge midpoints cease contacting for all odd \(d\ge7\).

## Assumptions and scope

The cube has exact coordinate bounds \(-1\le x_i\le1\) and the cutting halfspace includes its boundary. The Euclidean inner product and ambient \(d\)-volume are the standard ones. The ellipsoid shape matrix is the squared-semiaxis matrix, not its inverse: \(u\) is the squared semiaxis in the \(e\)-direction and \(v\) is the repeated squared semiaxis perpendicular to \(e\). The theorem includes \(d=2\) and every higher integer dimension, not arbitrary off-center hyperplane cuts or unequal orthotopes. All formulas are exact.

## Proof

**1. Coordinate-permutation reduction.** Both extremal ellipsoids are unique for a full-dimensional convex body. Each coordinate permutation preserves \(K_d\), so the center of either ellipsoid equals \(te\) and its shape matrix equals \(uH+vP\). Thus it suffices to verify optimality of the stated \((t,u,v)\), rather than optimize over general nonsymmetric ellipsoids.

**2. Maximum inscribed ellipsoid.** Let \(S_d=\{x:x_i\le1\ (1\le i\le d),\ e^\mathsf T x\ge0\}\). This is a simplex with vertices \(e\) and \(e-de_i\) for \(1\le i\le d\), and \(K_d\subset S_d\). The John ellipsoid of any simplex is its centroid-based affine image of the inscribed ball of a regular simplex. Its center is the mean of these \(d+1\) vertices, \(e/(d+1)\); its shape matrix is the uniform vertex covariance divided by \(d\). Directly computing this covariance gives \(u_J=d/(d+1)^2\) and \(v_J=d/(d+1)\). Its \(i\)th coordinate has extreme values \(1\) and \((1-d)/(d+1)>-1\), since \(u_J/d+(d-1)v_J/d=d^2/(d+1)^2\). Thus this simplex John ellipsoid is actually contained in \(K_d\). Since \(K_d\subset S_d\), the same ellipsoid is John for \(K_d\), by optimality in the containing simplex. The coordinate maxima and the minimum of \(e^\mathsf T x\) are attained, giving exactly the stated tangencies.

**3. Every vertex of the cut body.** The original cube vertices with coordinate sum \(s\ge0\) remain vertices. Additional cut vertices can only be intersections of the hyperplane \(s=0\) with original cube edges. For even \(d\), every cube-vertex sum is even, and sums on the endpoints of an edge differ by two, so such intersections are pre-existing cube vertices; no new vertices occur. For odd \(d\), the intersected edges have endpoint sums \(-1\) and \(+1\), producing exactly all vectors with one zero coordinate and equal counts of \(+1\) and \(-1\) elsewhere. This describes every vertex.

**4. Exhaustive containing-ellipsoid inequalities.** For a vertex of squared norm \(q\) and sum \(s=e^\mathsf T x\), its squared ellipsoid norm is
\[
F_d(s,q)=\frac{(s-dt)^2}{du}+\frac{q-s^2/d}{v}.
\]
At a \(\pm1\) cube vertex, \(q=d\) and \(s\) ranges over \(0,2,\ldots,d\) (even \(d\)) or \(1,3,\ldots,d\) (odd \(d\)). In all three asserted regimes \(0<u<v\), so \(F_d(s,d)\) is a strictly convex quadratic in \(s\). The formulas give equality \(F_d(0,d)=F_d(d,d)=1\) for even \(d\), and \(F_d(1,d)=F_d(d,d)=1\) for odd \(d\). Strict convexity makes all intermediate cube orbits strictly interior. For odd \(d\), every new cut-edge vertex has \(s=0,q=d-1\); substitution gives \(F_d(0,d-1)=1\) for \(d\in\{3,5\}\), and for odd \(d\ge7\) gives
\[
F_d(0,d-1)=\frac4{(d-1)^2}+\frac{d-1}{d}<1,
\]
using \((d-1)^2>4d\). Hence each proposed ellipsoid contains *all* vertices and therefore all of \(K_d\), and the stated contact orbits are complete.

**5. Exact Löwner optimality certificates.** We use the standard Löwner contact criterion: if a containing ellipsoid with center \(c\) and shape \(Q\) has a probability distribution on boundary contact points \(X\) satisfying \(\mathbb E[X]=c\) and \(\mathbb E[(X-c)(X-c)^\mathsf T]=Q/d\), then that ellipsoid is the unique minimum-volume enclosing ellipsoid. Every orbit below is endowed with its uniform permutation-invariant distribution. Write \(p\) for the pole orbit, \(b\) for the balanced cube orbit (sum zero, even case), \(a\) for the odd cube orbit (sum one), and \(m\) for the odd cut-edge midpoint orbit (sum zero). Assign probability masses as follows:
\[
\begin{array}{c|c|c|c|c}
\text{dimension}&w_p&w_b&w_a&w_m\\\hline
 d\text{ even}&\frac1{d+1}&\frac d{d+1}&0&0\\[3pt]
 d\ge7\text{ odd}&\frac1{d+1}&0&\frac d{d+1}&0\\[3pt]
 d\in\{3,5\}&\frac{d^2+8d-1}{16d^2}&0&\frac{3d^2-4d+1}{16d}&\frac{-3d^3+19d^2-9d+1}{16d^2}
\end{array}
\]
Each row consists of nonnegative masses summing to one, and every displayed nonzero mass is positive in its stipulated domain; for \(d=3\) the masses are \((w_p,w_a,w_m)=(2/9,1/3,4/9)\), and for \(d=5\) they are \((4/25,7/10,7/50)\). For an orbit with coordinate sum \(s\) and squared norm \(q\), its mean is \((s/d)e\), its axis second moment is \(s^2/d\), and its perpendicular squared-norm expectation is \(q-s^2/d\). Substitution verifies the three scalar identities
\[
\sum w s=dt,\qquad \sum w(s-dt)^2=u,\qquad \frac d{d-1}\sum w(q-s^2/d)=v,
\]
with \((t,u,v)\) from the theorem. Permutation symmetry makes the covariance precisely \((uH+vP)/d\). All supporting points have ellipsoid norm one by Step 4, so the criterion proves global Löwner optimality and uniqueness. Contact classification follows from Step 4.

**6. The parity and exceptional boundary.** The even case's lowest cube-vertex orbit has sum zero, whereas the odd case's lowest sum is one and a new midpoint orbit appears. The odd high-dimensional two-orbit certificate is feasible at the midpoint orbit precisely when \((d-1)^2\ge4d\). For odd \(d\ge3\) this first occurs at \(d=7\). The middle orbit must therefore enter the exact optimality certificate in dimensions three and five, producing the stated exceptional contact geometry. No asymptotic or numerical argument is used in this conclusion.

## Verification

The supplied standalone standard-library program `verify.py` uses rational arithmetic. It checks all three coefficient regimes, strict shape positivity, exact ellipsoid contact equalities, all vertex-type containments, and the contact-moment certificates for every dimension \(2\le d\le70\). It separately enumerates all cube corners and newly created cut-edge vertices through dimension nine and compares their contact counts to the closed formulas. It prints `VERIFY_OK exact_Loewner_certificates_dimensions=2..70 exhaustive_vertices_dimensions=2..9 John_support=yes parity_and_exceptions=yes`. These computations check transcription and small cases; the preceding argument, not finite experiments, establishes all dimensions.

## Relationship to prior work

Ambrus (2021/2022) studies critical *central section volumes* of cubes, including diagonal sections, and Bartha–Fodor–González Merino (2020/2021) prove monotonicity of the diagonal-section volume. They do not determine minimum-volume ellipsoids containing the resulting **half-bodies**, or maximum-volume ellipsoids inside them. Glover–Tkocz–Wyczesany (2023) prove stability of *complex-polydisc slicing*; it supplies different section-volume bounds, not the present ellipsoid coefficients. Sun–Freund (2004) give a general MVEE algorithm, not a closed contact-orbit classification for diagonal halfcubes. A publicly indexed orthotope-division result concerns maximizing the lesser **Euclidean inradius** under two-piece cuts and identifies diagonal bisectors in the cube; a scalar Euclidean inradius does not determine the affine-optimal Löwner and John ellipsoids, nor their complete vertex-contact distribution. None of the inspected statements entails the parity-exceptional formulas here.

## Limitations

The result is for the central, diagonal, **one-sided half** of an axis-aligned Euclidean cube; it is not about alternated/demicube vertices, arbitrary diagonally truncated cubes, arbitrary cutting offsets, weighted coordinate normal vectors, or non-Euclidean ellipsoid volume. Historical general-purpose ellipsoid algorithms and unindexed literature could in principle contain equivalent specialized computations; the literature search cannot certify global uniqueness. The proof gives an all-dimensional exact result but makes no claim about generic halfspace-truncated orthotopes. The independent audit has not been performed.

## References

1. G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (public version of 30 July 2021), https://arxiv.org/html/2107.14778v3. Primary MSC2020 52A40.
2. F. A. Bartha, F. Fodor, B. González Merino, *Central diagonal sections of the n-cube*, arXiv:2005.08292 (17 May 2020), https://arxiv.org/html/2005.08292v2.
3. N. Glover, T. Tkocz, K. Wyczesany, *Stability of polydisc slicing*, Mathematika 69 (2023), 1165–1182, https://doi.org/10.1112/mtk.12225.
4. P. Sun and R. M. Freund, *Computation of Minimum-Volume Covering Ellipsoids*, Operations Research 52 (2004), 690–706, https://doi.org/10.1287/opre.1040.0115.
5. *Exact max-min inradius divisions of orthotopes*, publicly indexed published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-max-min-inradius-divisions-of-orthotopes--f1ec4eeb67b7.
