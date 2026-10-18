# Shortest-vector rank from the extreme nearest-site margin of a Euclidean lattice

## Finding
Let \(d\ge2\), let \(\Lambda\subset\mathbb R^d\) be a full-rank Euclidean lattice, and let \(V\) be its closed Voronoi cell centered at the origin. Sample \(X\) uniformly by volume in \(V\). Let \(D_1(X)\le D_2(X)\) be the two smallest **squared** Euclidean distances from \(X\) to distinct lattice points, with ties counted with their lattice-point multiplicity. Define the squared nearest-site margin \(G=D_2(X)-D_1(X)\).

Let \(\lambda=\min_{v\in\Lambda\setminus\{0\}}\|v\|^2\), and let \(S=\{s\in\Lambda:\|s\|^2=\lambda\}\) be the nonzero shortest-vector set. Put \(E=\operatorname{span}_{\mathbb R}S\) and \(r=\dim E\). Define two bounded, origin-symmetric convex polytopes in their indicated Euclidean subspaces:
\[
K=\bigl\{z\in E:|\langle z,s\rangle|\le\tfrac12\ \text{for all }s\in S\bigr\},
\]
\[
H=\bigl\{y\in E^\perp:|\langle y,v\rangle|\le\tfrac12(\|v\|^2-\lambda)\ \text{for all }v\in\Lambda\setminus(S\cup\{0\})\bigr\}.
\]
When \(r=d\), use the convention \(\operatorname{vol}_0(H)=1\). Each polytope has nonempty relative interior and strictly positive intrinsic volume. Then, as \(\varepsilon\downarrow0\),
\[
\boxed{\mathbb P\{G>\lambda-\varepsilon\}=C_\Lambda\varepsilon^r+O_\Lambda(\varepsilon^{r+1}),\qquad
C_\Lambda=\frac{\operatorname{vol}_r(K)\operatorname{vol}_{d-r}(H)}{\det\Lambda}>0.}
\]
More precisely, for some \(\varepsilon_0>0\) the survival function on \(0<\varepsilon<\varepsilon_0\) is **exactly a polynomial of degree at most \(d\)** in \(\varepsilon\), with its first nonzero coefficient in degree \(r\). If \(r=d\), it is exactly \(C_\Lambda\varepsilon^d\) in that entire interval.

In particular the distribution of the scalar statistic \(G\) detects the dimension of the shortest-vector span:
\[
\boxed{r=\lim_{\varepsilon\downarrow0}\frac{\log\mathbb P\{G>\lambda-\varepsilon\}}{\log\varepsilon}.}
\]
Thus \(\Lambda\) is well-rounded (its shortest vectors span \(\mathbb R^d\)) if and only if its upper-tail exponent equals \(d\).

## Assumptions and scope
Distances are ordinary Euclidean squared distances and the lattice has full rank, not a random choice of lattice. The point is uniform in the origin-centered Voronoi cell, equivalently a uniformly random point modulo lattice translations. Ties occur on sets of zero volume and do not change the probability formula. The upper endpoint \(\lambda\) and the exponent are taken in the squared-distance normalization; the theorem is not a statement about the unsquared first-versus-second distance gap. The symbol \(\det\Lambda\) denotes the positive fundamental covolume, not the determinant of a Gram matrix.

The constraints describing \(H\) can be reduced to finitely many **Voronoi-relevant lattice vectors**; the displayed all-vector version makes the invariant definition basis-free. A finite exact enumeration of the facets of the Voronoi cell therefore suffices to calculate the coefficient \(C_\Lambda\) by convex-polytope volume computations. No claim is made that the coefficient is universally elementary in arbitrary dimension.

## Proof
**1. Gap reduction and endpoint.** In the interior of \(V\), the origin is the unique nearest lattice site, whence
\[
G(x)=\min_{v\in\Lambda\setminus\{0\}}\bigl(\|v\|^2-2\langle x,v\rangle\bigr).
\]
For any \(s\in S\), both \(s\) and \(-s\) appear in this minimum, so
\[
G(x)\le\lambda-2|\langle x,s\rangle|\le\lambda.
\]
At \(x=0\), equality holds. Hence the exact essential upper endpoint is \(\lambda\). For \(0<\varepsilon<\lambda\), define
\[
P_\varepsilon=\{x\in\mathbb R^d:2\langle x,v\rangle\le\|v\|^2-\lambda+\varepsilon\ \text{for every }v\in\Lambda\setminus\{0\}\}.
\]
Because these inequalities are stronger than the ordinary Voronoi inequalities, \(P_\varepsilon\subset V\). Up to boundary-null sets,
\[
\mathbb P\{G>\lambda-\varepsilon\}=\frac{\operatorname{vol}_d(P_\varepsilon)}{\det\Lambda}.
\]

**2. Why the infinite family is finite.** A lattice vector \(v\ne0\) is Voronoi-relevant if its perpendicular-bisector inequality supports a facet of \(V\). If it is not relevant, the standard midpoint criterion gives a lattice point \(u\ne0,v\) with \(\|v-2u\|\le\|v\|\). Write \(a=u\), \(b=v-u\); then \(v=a+b\), \(\langle a,b\rangle=(\|v\|^2-\|v-2u\|^2)/4\ge0\), and \(\|a\|,\|b\|<\|v\|\). For any \(t\ge0\), the inequalities for \(a,b\), namely
\[
2\langle x,a\rangle\le\|a\|^2-t,\qquad 2\langle x,b\rangle\le\|b\|^2-t,
\]
imply \(2\langle x,v\rangle\le\|v\|^2-t\), since \(\|v\|^2=\|a\|^2+\|b\|^2+2\langle a,b\rangle\). Strictly descending lengths give an induction showing that the inequalities of Voronoi-relevant vectors alone define \(P_\varepsilon\) whenever \(t=\lambda-\varepsilon\ge0\). There are finitely many such vectors: each relevant vector's midpoint belongs to the bounded cell \(V\), so its length is at most twice the circumradius of \(V\). This finite reduction also proves that \(H\) may be described with only nonshort relevant vectors.

**3. Rank controls the collapse.** The shortest-vector inequalities in \(P_\varepsilon\) reduce to
\[
|\langle x,s\rangle|\le\varepsilon/2\qquad(s\in S).
\]
Use the orthogonal decomposition \(x=\varepsilon z+y\) with \(z\in E\) and \(y\in E^\perp\). The shortest constraints become exactly \(z\in K\). The other constraints are
\[
2\langle y,v\rangle\le\|v\|^2-\lambda+\varepsilon-2\varepsilon\langle z,v\rangle,
\]
with their reflected counterparts. Their limiting section for every fixed \(z\in K\) is precisely \(H\).

The shortest vectors span \(E\), so \(K\) is bounded and contains a relative neighborhood of the origin. At \(\varepsilon=0\), all shortest inequalities force \(x\in E^\perp\). The remaining strict positive slacks near the origin show that \(H\) has nonempty relative interior. Moreover \(H\subset V\cap E^\perp\) and is thus bounded. The same holds for all \(y\)-sections above because \(P_\varepsilon\subset V\). With only finitely many relevant inequalities, the indicators of these sections converge almost everywhere on the bounded product region \(K\times\pi_{E^\perp}V\) to the indicator of \(K\times H\). Dominated convergence and the Jacobian \(\varepsilon^r\) give
\[
\lim_{\varepsilon\downarrow0}\frac{\operatorname{vol}_d(P_\varepsilon)}{\varepsilon^r}=\operatorname{vol}_r(K)\operatorname{vol}_{d-r}(H)>0.
\]
For \(r=d\), the orthogonal factor has dimension zero; the nonshort inequalities are uniformly slack on the bounded set \(\varepsilon K\) for all sufficiently small \(\varepsilon\), giving **exactly** \(P_\varepsilon=\varepsilon K\) there.

**4. Exact endpoint polynomial.** The halfspace normals of \(P_\varepsilon\) belong to a fixed finite list, and each right-hand side is affine in \(\varepsilon\). For each linearly independent \(d\)-tuple of normal vectors, the prospective vertex is affine in \(\varepsilon\). The feasibility of that vertex against each remaining inequality is a linear condition in \(\varepsilon\), so its sign changes at most once unless it vanishes identically. There are finitely many such conditions. Therefore, for some \(\varepsilon_0>0\), the face incidences of these full-dimensional polytopes are constant for all \(0<\varepsilon<\varepsilon_0\). Choose a fixed combinatorial triangulation and evaluate simplex determinants of affine vertex coordinates: the total volume is a polynomial of degree at most \(d\) in \(\varepsilon\). The preceding strictly positive limit forces its first nonzero degree to be exactly \(r\), proving the stated \(O_\Lambda(\varepsilon^{r+1})\) remainder. Taking logarithms yields the recovery of \(r\).

**5. Exact planar contrast.** For \(\Lambda_1=\mathbb Z(1,0)+\mathbb Z(2/5,6/5)\), shortest vectors are just \(\pm(1,0)\), so \(r=1\) and \(\det\Lambda_1=6/5\). Here \(K=[-1/2,1/2]\) along the horizontal axis, and \(H=[-1/4,1/4]\) along the vertical axis. Therefore \(C_{\Lambda_1}=5/12\), and exact clipping of the two active strip pairs gives, for all sufficiently small positive \(\varepsilon\),
\[
\mathbb P(G>1-\varepsilon)=\frac5{12}\varepsilon+\frac{25}{36}\varepsilon^2.
\]
For \(\Lambda_2=\mathbb Z(1,0)+\mathbb Z(5/13,12/13)\), the shortest vectors are the four vectors \(\pm(1,0),\pm(5/13,12/13)\), and \(r=2\). Since \(\det\Lambda_2=12/13\), the shortest strip intersection \(K\) has area \(13/12\); hence for all sufficiently small positive \(\varepsilon\),
\[
\mathbb P(G>1-\varepsilon)=\frac{169}{144}\varepsilon^2.
\]
The contrast uses nonorthogonal full-rank lattices and is not a rectangular-coordinate artifact. For comparison, for an orthogonal lattice with mutually perpendicular basis vectors of lengths \(a_1,\ldots,a_d\), the entire survival law for \(0\le t\le\min_i a_i^2\) is \[\mathbb P\{G>t\}=\prod_{i=1}^d(1-t/a_i^2).\] Its upper-endpoint multiplicity is the number of basis lengths equal to the smallest one, as predicted by the general theorem.

## Verification
The included self-contained standard-library script `check_lattice_margin.py` was executed and returned `LATTICE_MARGIN_TAIL_OK`. It clips exact rational halfplanes for both nonorthogonal planar examples, checks the Voronoi covolume, computes survival areas at three exact rational thresholds each, confirms the leading coefficients and (in the well-rounded case) the exact monomial, and compares 125 rational query points in an orthogonal three-dimensional lattice against direct competitor enumeration. The computations provide finite cross-checks, not proof of the all-lattice statement; that relies on the finite-constraint, collapse, and parametric-polytope arguments above.

## Relationship to prior work
The Voronoi-cell and closest-point framework is classical; Sloane and Beferull-Lozano (2002) develop lattice quantization by intersecting Voronoi cells. McKilliam, Grant and Clarkson (2014, Section 2) describe Voronoi-relevant vectors and shortest vectors, but do not give a second-nearest squared-distance margin distribution. Baake, Scharlau and Zeiner (2013) define and enumerate well-rounded planar lattices, rather than recovering shortest-vector rank from a probability-tail exponent. Koçak and Ratiu (2010) prove piecewise polynomiality of the **ordinary Euclidean inner parallel volume** for polytopes; general polytope polynomiality alone is not claimed here as new. The present margin corresponds to facets receding at rates depending on the lattice-vector lengths, and the new assertion connects its top-order collapse to the rank of the shortest-vector span with an explicit mixed-dimensional coefficient.

A published BCC/FCC lattice-cell note on Euclidean boundary-clearance distributions gives exact laws for two individual cells. Euclidean clearance is the minimum facet slack divided by each facet-normal length, whereas \(G\) is twice the minimum unnormalized facet slack. For equal-length facet normals, individual clearance laws may imply specialized margin laws; such covered special cases are not claimed as new. They do not imply the arbitrary-dimensional rank-recovery theorem. Similarly, an earlier spherical tetrahedral score-gap law concerns four cosine scores on a sphere and does not cover a uniform Voronoi-cell point and its infinite set of lattice competitors.

## Limitations
This is a population law for a fixed, full-rank Euclidean lattice. The endpoint exponent determines only the *dimension* of the shortest-vector span, not the shortest vectors or lattice shape. The leading coefficient generally depends on the full Voronoi geometry; no statistically stable finite-sample reconstruction guarantee is proved. The near-endpoint polynomial need not hold unchanged over the whole support, because the active Voronoi facets can change at positive thresholds. Historical priority remains subject to specialized lattice-decoding literature not fully accessible through the searches and primary texts inspected. 

## References
1. N. J. A. Sloane and B. Beferull-Lozano, *Quantizing Using Lattice Intersections*, arXiv:math/0207147v1 (2002-07-17), https://arxiv.org/pdf/math/0207147.
2. Ş. Koçak and A. V. Ratiu, *Inner tube formulas for polytopes*, arXiv:1008.2040v1 (2010-08-12), https://arxiv.org/pdf/1008.2040.
3. M. Baake, R. Scharlau and P. Zeiner, *Well-rounded sublattices of planar lattices*, arXiv:1311.6306v1 (2013-11-25), https://arxiv.org/pdf/1311.6306.
4. R. G. McKilliam, A. Grant and I. V. L. Clarkson, *Finding a closest point in a lattice of Voronoi's first kind*, arXiv:1405.7014v1 (2014-05-27), https://arxiv.org/pdf/1405.7014.
