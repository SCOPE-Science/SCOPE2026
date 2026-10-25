# Exact first Euclidean-distance transition for arbitrary simplices

## Finding
Let \(d\ge3\), and let \(T\subset\mathbb R^d\) be any nondegenerate Euclidean \(d\)-simplex of volume \(V\). For independent uniform points \(X,Y\in T\), set \(F(r)=\Pr(\|X-Y\|\le r)\). The following theorem specifies exactly where its initial polynomial law ends, the *entire first nonpolynomial branch*, and its sharp singular exponent.

Write \(\lambda_0,\ldots,\lambda_d\) for the affine barycentric coordinates of \(T\), and \(g_i=\nabla\lambda_i\). For each nonempty proper subset \(S\subset\{0,\ldots,d\}\), put \(L_S=\sum_{i\in S}g_i\), and let \(\mathcal L\) be the set of these vectors. Define
\[
q(z)=\sum_{i=0}^d(g_i\cdot z)_+=\max_{L\in\mathcal L}L\cdot z,\quad
 t=\max_{L\in\mathcal L}\|L\|,\quad a=t^{-1},\quad
 M=\{L\in\mathcal L:\|L\|=t\},\quad m=|M|.
\]
Here \((s)_+=\max(s,0)\). The number \(m\) is positive and even. With \(d\sigma\) denoting the usual (unnormalized) area measure on \(S^{d-1}\), set
\[
P(r)=\frac1V\sum_{k=0}^{d}(-1)^k\binom dk
\frac{r^{d+k}}{d+k}\int_{S^{d-1}}q(u)^k\,d\sigma(u).
\]
This is a finite polynomial with explicitly specified coefficients. **Exactly** \(F(r)=P(r)\) for \(0\le r\le a\); equality fails strictly for every \(r>a\) sufficiently close to \(a\). The number \(a\) is the Euclidean inradius of the difference body \(T-T\), centered at the origin.

For an explicit full interval of validity, let \(t'<t\) be the largest norm \(\|L\|\) among \(L\in\mathcal L\setminus M\), if such a vector exists, and set \(b=1/t'\), otherwise \(b=+\infty\). Let \(\vartheta\in(0,\pi]\) be the minimum angle between distinct directions \(L/t\), \(L'/t\) with \(L,L'\in M\). Set \(c=a/\cos(\vartheta/2)\) if \(\vartheta<\pi\), otherwise \(c=+\infty\); finally put \(r_1=\min(b,c)>a\). Let \(\omega_{d-1}=\pi^{(d-1)/2}/\Gamma((d+1)/2)\), and define
\[
C_d(r,a)=\frac{\omega_{d-1}}{a^d}
\int_a^r(s-a)^d(r^2-s^2)^{(d-1)/2}\,ds.
\]
Then on the **whole first interval** \(a\le r<r_1\),
\[
\boxed{F(r)=P(r)+(-1)^{d+1}\frac{m}{V}C_d(r,a).}
\]
In particular, as \(\delta\downarrow0\),
\[
\boxed{F(a+\delta)-P(a+\delta)\sim(-1)^{d+1}\frac{m\omega_{d-1}2^{(d-1)/2}\mathrm B(d+1,(d+1)/2)}{Va^{(d+1)/2}}\,\delta^{(3d+1)/2}.}
\]
Here \(\mathrm B\) is Euler's beta function. This nonzero coefficient gives the exact singular exponent; the initial polynomial cannot persist beyond \(a\).

For **every tetrahedron** (\(d=3\)), the entire first branch simplifies to
\[
\boxed{F(r)=P(r)+\frac{m\pi(r-a)^5(a+5r)}{60Va^3},\qquad a\le r<r_1,}
\]
so \(F(a+\delta)-P(a+\delta)\sim m\pi\delta^5/(10Va^2)\). The first radius \(a\) is the least of the four vertex-to-opposite-face altitudes and three distances between supporting lines of opposite edge pairs. For the unit-coordinate right tetrahedron, \(a=1/\sqrt3\) and \(m=2\); for the regular unit-edge tetrahedron, \(a=1/\sqrt2\) and \(m=6\).

## Assumptions and scope
The simplex is full-dimensional in Euclidean \(\mathbb R^d\), \(d\ge3\), with uniform and independent sampling of the two points and ordinary Euclidean distance. Its shape is unrestricted: no regularity, orthogonality, or generic-position condition is imposed. The angles and multiplicity in the theorem are computed from **distinct** subset-sum vectors, not a list with repetitions. When there is no submaximal norm or the only maximizing directions are antipodal, the stated infinite-threshold conventions apply. The statements cover ties among largest norms and all finite degeneracies of the directional arrangement compatible with a full-dimensional simplex.

## Proof
**1. Exact simplex covariogram.** Because each affine barycentric coordinate is nonnegative precisely on \(T\), the intersection \(T\cap(T+z)\) is characterized by
\[
\lambda_i(x)\ge\max(0,g_i\cdot z)\qquad(0\le i\le d).
\]
The lower bounds sum to \(q(z)\), and \(\sum_i\lambda_i(x)=1\). For \(q(z)\le1\), translating and rescaling the barycentric simplex therefore gives
\[
\operatorname{vol}_d(T\cap(T+z))=V(1-q(z))^d;
\]
for \(q(z)>1\), the intersection is empty. This establishes, without a smoothness assumption,
\[
\frac{\operatorname{vol}_d(T\cap(T+z))}{V}=(1-q(z))_+^d.
\]
For fixed \(z\), the sum of positive quantities \(g_i\cdot z\) is the largest sum over a nonempty proper index subset: since \(\sum_i g_i=0\), taking the complement changes the sign. Thus \(q(z)=\max_{L\in\mathcal L}L\cdot z\), and \(\mathcal L=-\mathcal L\). The vectors are distinct because any \(d\) barycentric gradients are linearly independent; hence maximizing directions form a finite set with positive minimum mutual angle and even cardinality.

**2. Euclidean distance and the initial polynomial.** The density of \(X-Y\) at \(z\) is the covariogram divided by \(V^2\). Therefore
\[
F(r)=\frac1V\int_{\|z\|\le r}(1-q(z))_+^d\,dz.
\]
By homogeneity and Cauchy–Schwarz, \(\max_{\|z\|\le r}q(z)=rt\). Thus \(q(z)\le1\) everywhere in the radius-\(r\) ball if and only if \(r\le a\). In this range the positive-part operation can be dropped. Expanding \((1-q)^d\), using spherical coordinates, and integrating \(\rho^{d+k-1}\) exactly proves the formula for \(P(r)\). The set \(\{z:q(z)\le1\}\) is precisely \(T-T\), so its largest centered ball has radius \(a\).

**3. Disjoint cap decomposition.** At radii \(r<b\), no submaximal vector can satisfy \(L\cdot z>1\) inside the radius-\(r\) ball. For a maximizing vector \(L\in M\), the inequality \(L\cdot z>1\) cuts out the cap \(\{\|z\|\le r:(L/t)\cdot z>a\}\). If two unit normals have angle \(\phi\), the least norm of a point satisfying both corresponding strict inequalities is \(a/\cos(\phi/2)\) when \(\phi<\pi\), and simultaneous satisfaction is impossible for antipodal normals. Hence all maximizing caps are pairwise disjoint for \(r<c\). On one such cap \(q(z)=L\cdot z\), since every other linear form is at most \(1\) there and \(L\cdot z>1\).

Consequently, the difference between the actual positive-part integral and the polynomial integral is exactly the sum of \(m\) congruent cap integrals of \((-1)^{d+1}(L\cdot z-1)^d/V\). Integrate in the coordinate \(s=(L/t)\cdot z\): the perpendicular \((d-1)\)-ball has volume \(\omega_{d-1}(r^2-s^2)^{(d-1)/2}\), and \(L\cdot z-1=(s-a)/a\). This proves the exact first-branch formula.

**4. Sharp asymptotic.** Put \(r=a+\delta\) and \(s=a+\delta u\) in the cap integral. Then
\[
r^2-s^2=\delta(1-u)\bigl(2a+\delta(1+u)\bigr),\qquad 0\le u\le1.
\]
Divide by \(\delta^{(3d+1)/2}\), and use dominated convergence to obtain
\[
\frac{\omega_{d-1}2^{(d-1)/2}}{a^{(d+1)/2}}
\int_0^1u^d(1-u)^{(d-1)/2}\,du.
\]
The integral is \(\mathrm B(d+1,(d+1)/2)\). It is strictly positive, so the sign is \((-1)^{d+1}\) and \(a\) is the genuine first transition.

**5. Specialization to tetrahedra.** For \(d=3\), \(\omega_2=\pi\) and direct integration yields
\[
C_3(r,a)=\frac{\pi(r-a)^5(a+5r)}{60a^3}.
\]
A one-index barycentric-gradient subset represents a vertex-to-opposite-face altitude, and a two-index subset represents the common perpendicular between its two opposite-edge supporting lines. Complementary subsets reverse the same normal. These are all nontrivial subsets of four indices, proving the stated seven-distance characterization. Direct barycentric gradients give the two worked examples.

## Verification
The reproducible standalone file `simplex_distance_checker.py` independently enumerates the facet inequalities of the original and translated simplices, intersects their hyperplanes, and computes volumes by convex hulls; these results are compared with the closed covariogram formula. A separate quasi-Monte-Carlo spherical integration checks the tetrahedral correction without using the cap-decomposition integration formula, for both an orthogonal-coordinate tetrahedron and a regular tetrahedron. A planar triangle is included only as a consistency control, not a newly claimed result. The program also checks cap-integral asymptotics directly. Run `OPENBLAS_NUM_THREADS=1 python simplex_distance_checker.py` with NumPy and SciPy installed. Finite tests do not establish the infinite-dimensional quantifiers; the preceding proof does.

## Relationship to prior work
The simplex-intersection homothety and general identity between the covariogram and random-pair distances are established parts of convex/integral geometry; neither is asserted as new. Wang's October 2026 work develops general concavity and variational theory for pair distributions, but the statements inspected there do not specify the simplex Euclidean first breakpoint, its disjoint-cap branch, or a singular coefficient. Beck’s 2023 exact moment method covers all natural distance moments in polyhedra, including tetrahedra, but does not itself state a Euclidean distance-CDF clipping threshold or its first branch. Published triangle and polygon distance distributions are two-dimensional and do not imply the present claim restricted to \(d\ge3\). An accessible result about a simplex's **difference-body gauge** pair distance does not determine its **Euclidean** distance law, because the two radial level sets differ. The earlier polyhedral first-threshold result for parallelotopes concerns a different covariogram and body class. The formulas here are not a general complete distance law beyond the first cap-overlap/submaximal threshold.

## Limitations
For the interval after \(r_1\), caps can overlap or additional linear forms can become active, and this result does **not** specify subsequent pieces of \(F\). The polynomial's spherical moments are finite explicit integrals, not claimed elementary for every dimension or shape. This is an analytical proof of correctness, not a claim of historical-priority certification. Older stereology literature not available in the inspected sources could contain an equivalent formulation. An independent scientific audit has not been performed.

## References
1. S. Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1, first public October 1, 2026, https://arxiv.org/abs/2610.01916.
2. V. K. Ohanyan and V. H. Khalatyan, *Relation between the covariogram and distribution function of the distance between two uniform and independent points*, Proceedings of the YSU A 56(1), 33–42 (2022), https://doi.org/10.46991/PYSU:A/2022.56.1.033.
3. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles*, arXiv:1312.2498, 2013, https://arxiv.org/abs/1312.2498.
4. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons*, arXiv:1602.03407, 2016, https://arxiv.org/abs/1602.03407.
5. D. Beck, *Mean distance in polyhedra*, arXiv:2309.13177v1 (2023), https://arxiv.org/abs/2309.13177.
6. V. Soltan, *A Characterization of Homothetic Simplices*, Discrete & Computational Geometry (1999), https://doi.org/10.1007/PL00009454.
