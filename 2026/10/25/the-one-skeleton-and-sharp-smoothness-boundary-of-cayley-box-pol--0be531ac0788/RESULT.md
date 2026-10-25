# The one-skeleton and sharp smoothness boundary of Cayley box polytopes

## Finding
Let \(d,n\geq 1\) and let \(A=(a_{ij})\) be a nonnegative integer matrix with \(n\) rows indexed by \(i=1,\ldots,n\) and \(d+1\) columns indexed by \(j=0,\ldots,d\). Assume that every row has a positive entry. Write \(S_j=\{i:a_{ij}>0\}\). The associated Cayley box polytope is
\[
\mathcal C(A)=\left\{(x,\lambda):\lambda\in\Delta_d,\quad 0\leq x_i\leq\sum_{j=0}^d a_{ij}\lambda_j\ (1\leq i\leq n)\right\},
\]
where \(\Delta_d=\{\lambda_j\geq0:\sum_{j=0}^d\lambda_j=1\}\). Its ambient lattice uses the \(n\) fiber coordinates and \(d\) independent barycentric coordinates. It has dimension \(n+d\).

**Complete graph theorem.** Every vertex lies over a base vertex \(e_j\) and is specified by a binary lower/upper choice on \(S_j\). Two vertices in the same layer are adjacent exactly when they differ in one such choice. Vertices in distinct layers \(j\) and \(\ell\) are adjacent exactly when their binary choices agree on \(S_j\cap S_\ell\). Thus the graph depends only on the zero pattern of \(A\), not on its positive entries. In particular,
\[
\deg(v)=|S_j|+\sum_{\ell\ne j}2^{|S_\ell\setminus S_j|}
\quad\text{for every vertex over }e_j,
\]
and
\[
 f_1(\mathcal C(A))=
 \sum_{j=0}^d |S_j|2^{|S_j|-1}
 +\sum_{0\leq j<\ell\leq d}2^{|S_j\cup S_\ell|}.
\]

**Sharp simplicity and smoothness theorem.** The polytope \(\mathcal C(A)\) is simple if and only if every row of \(A\) is either positive in *all* columns or positive in *exactly one* column, and no two single-support rows use the same column. If these conditions hold and \(t\) is the number of single-support rows, then \(\mathcal C(A)\) is combinatorially isomorphic to
\[
 \Delta_{d+t}\times[0,1]^{n-t}.
\]
It is smooth (Delzant in its ambient lattice) if and only if it is simple **and every positive entry in a single-support row equals \(1\)**. Positive values in the full-support rows are unrestricted.

For each \(j\), let \(Z_j=\{1,\ldots,n\}\setminus S_j\) and \(r_{j\ell}=|Z_j\cap S_\ell|\). Every vertex over \(e_j\) is nonsimple if and only if
\[
\sum_{\ell\ne j}(2^{r_{j\ell}}-1)>|Z_j|.
\]
Hence the exact number of nonsimple vertices is the sum of \(2^{|S_j|}\) over the columns satisfying this strict inequality.

**Consequence for the motivating counterexample family.** For Ferroni's matrix \(A_{\alpha,\beta}=[\alpha\mathbf 1_d\mid\beta I_d]\), with \(d\geq2\) and positive \(\alpha,\beta\), there are exactly \(2^d\) simple vertices over column \(0\) and exactly \(2d\) nonsimple vertices over the other columns. Every nonsimple vertex has degree \(2^{d-1}+2d-1\), while every simple vertex has degree \(2d\). Hence the original high-dimensional examples have a small exceptional set of vertices with exponentially large degree.

## Assumptions and scope
All dimensions \(d,n\) are positive integers. Matrix entries are nonnegative integers and no row is identically zero. Zero-length coordinate fibers are allowed on boundary layers; the full polytope is still \((n+d)\)-dimensional. The graph theorem, simplicity criterion, and combinatorial product description remain valid for nonnegative **real** entries with the same zero pattern. Smoothness requires integral coordinates in the standard lattice and refers to the primitive edge generators at *every* vertex. No claim is made for signed coefficients or non-box fibers.

## Proof
**1. Vertices.** For fixed \(\lambda\), the fiber is a product of intervals. At a base vertex \(e_j\), its vertices have \(x_i\in\{0,a_{ij}\}\), with coincident choices when \(a_{ij}=0\). Conversely, any vertex of the Cayley sum projects to a base vertex because the polytope is the convex hull of these fibers. The number of vertices over \(e_j\) is \(2^{|S_j|}\). Each row is nonzero, so at an interior base point all fibers have positive length; this proves the dimension assertion.

**2. Exact tangent cone.** Fix a vertex \(v\) over \(e_j\). For each \(i\in S_j\), precisely one of the lower and upper fiber inequalities is active. By an integral unimodular shear in the fiber coordinate, its inward slack becomes an independent nonnegative variable \(u_i\). Put \(Z_j=S_j^{\mathrm c}\) and write \(z_\ell=\delta\lambda_\ell\) for \(\ell\ne j\). Then the tangent cone at \(v\) is unimodularly linearly equivalent to the direct product of \(\mathbb R_{\geq0}^{|S_j|}\) with
\[
 T_j=\left\{(z,w):z_\ell\geq0,\quad
 0\leq w_i\leq\sum_{\ell\ne j}a_{i\ell}z_\ell
 \ (i\in Z_j)\right\}.
\]
This is the homogenization of a Cayley sum of boxes over the simplex on the \(d\) columns other than \(j\). Its extreme rays have \(z=e_\ell\), and each coordinate \(w_i\) independently equal to \(0\) or \(a_{i\ell}\). For fixed \(\ell\), precisely \(2^{r_{j\ell}}\) distinct rays arise. No mixed-base ray is extreme, since any point of \(T_j\) is a conic combination of these box vertices. All rays are extreme because each is a vertex of its cube in the exposed base layer.

The orthant rays flip exactly one positive fiber coordinate at fixed base layer. A ray of \(T_j\) leads to a vertex over \(e_\ell\); for every \(i\in S_j\cap S_\ell\), its upper/lower choice must remain the one active at \(v\), while each \(i\in S_\ell\setminus S_j\) may choose freely. These are **all** edge rays, proving the graph criterion and the per-layer degree. A cube with \(|S_j|\) active coordinates has \(|S_j|2^{|S_j|-1}\) edges. Across distinct layers \(j,\ell\), each binary assignment on \(S_j\cup S_\ell\) gives exactly one edge. This proves the edge formula.

**3. Simplicity.** The tangent cone at a vertex over \(e_j\) has
\[
 |S_j|+\sum_{\ell\ne j}2^{r_{j\ell}}
\]
extreme rays in dimension \(|S_j|+|Z_j|+d\). The number of rays minus the dimension is
\[
\sum_{\ell\ne j}(2^{r_{j\ell}}-1)-|Z_j|.
\]
Every row in \(Z_j\) is positive in at least one of the other columns, so \(\sum_{\ell\ne j}r_{j\ell}\geq|Z_j|\). Since \(2^r-1\geq r\) for integral \(r\geq0\), with equality precisely at \(r\in\{0,1\}\), the deficit vanishes exactly when each zero row has one positive column elsewhere and those positive columns are pairwise different. Requiring this at every \(j\) yields the global support-pattern criterion. A pointed full-dimensional polyhedral cone is simplicial exactly when it has as many extreme rays as its dimension; thus the criterion is necessary and sufficient for simplicity. The displayed nonsimple-vertex count follows because all vertices over a given layer have equal degree.

**4. Combinatorial type.** Remove the \(n-t\) full-support rows temporarily. Each remaining row is supported at one column, with distinct supports. The resulting Cayley polytope has \(d+t\) dimensions but exactly \(d+1+t\) vertices (one extra vertex for each single-support row), hence is a simplex. Restore the full-support rows one at a time. Their upper affine fiber lengths are strictly positive throughout the base polytope; each restoration is a strict interval bundle with the face incidences of a product with a segment. Thus the stated simplex–cube product is its complete combinatorial type.

**5. Smoothness.** Under the simplicity conditions, the tangent cone above splits, by integral unit-determinant shears, into independent one-dimensional orthants and blocks indexed by columns \(\ell\ne j\). A block without a single-support row has primitive generator \((1)\). A block with a single-support row of positive entry \(m\) has the two primitive generators \((1,0)\) and \((1,m)\) in the coordinate lattice spanned by its base displacement and its fiber coordinate. Its determinant has absolute value \(m\). Thus the absolute determinant of the full set of primitive edge directions at a vertex over \(e_j\) is the product of the single-support entries in columns other than \(j\). Because \(d\geq1\), each such column is other than at least one base layer. Consequently all vertex cones are unimodular if and only if every single-support entry equals one. This proves the exact smoothness characterization.

## Verification
The standalone `verify.py` uses only the Python 3 standard library. It builds the vertices from fiber endpoint choices, independently derives every active linear inequality, tests adjacency via the exact rational rank of the common active-normal matrix, and computes determinants of primitive incident edge directions. It compares independently obtained adjacency, edge totals, degrees, simplicity, and smoothness with the formulas above. The test covers every no-zero-row matrix with entries in \(\{0,1,2\}\) for \((n,d)=(1,1),(1,2),(2,1),(2,2),(3,1)\), plus 400 seeded random matrices in four larger parameter regimes. Execution produces:

`EXACT_OK matrices=1686 graph_edge_count_simplicity_smoothness=verified sparse_family_d=2..50`

These are finite regression checks; the all-dimensional assertion is proved by the tangent-cone argument, not by enumeration.

## Relationship to prior work
Ferroni's 2026 work introduces this particular Cayley construction, supplies its complete vertex description, establishes regular unimodular flag triangulations, and shows smoothness when all matrix entries are positive (Propositions 2.1–2.3). The present statement retains that known sufficient case but adds an exact one-skeleton for arbitrary zero patterns, necessary and sufficient simplicity and smoothness conditions, and a classification of every resulting simple combinatorial type. The source does not state these graph or zero-pattern criteria.

Curtis, Le, and Lowen (2026) give general structural and Minkowski-summand theorems for smooth polytopes combinatorially equivalent to products of simplices and for Nakajima polytopes. Those general results provide broader context but do not state the matrix-support graph and equivalence criteria above. Tsuchiya's Cayley-sum work addresses IDP and Minkowski sums, rather than the present adjacency and smoothness question. The criteria here are proved directly and do not claim novelty for the previously established IDP or regular triangulation properties.

## Limitations
The statement concerns this concrete coordinate-box Cayley realization rather than every Nakajima polytope or Cayley sum. Graph combinatorics alone cannot detect the lattice determinant: changing a positive singleton coefficient preserves the graph and simplicity but can destroy smoothness. The criterion is independent of positive magnitudes only for the graph and simplicity, not for smoothness. Historical priority for a possible equivalent zero-pattern characterization in older toric literature has not been conclusively ruled out. No independent external validation has occurred.

## References
1. L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513v1 (first publicly posted 2026-09-09), especially Propositions 2.1–2.3, https://arxiv.org/html/2609.10513v1.
2. J. Curtis, T. Le, C. Lowen, *On Smooth Combinatorial Products of Simplices*, arXiv:2609.25181 (first publicly posted 2026-09-21), especially Theorems 1.1–1.3, https://arxiv.org/abs/2609.25181.
3. A. Tsuchiya, *Cayley sums and Minkowski sums of lattice polytopes*, arXiv:1804.10538, https://arxiv.org/html/1804.10538v4.
