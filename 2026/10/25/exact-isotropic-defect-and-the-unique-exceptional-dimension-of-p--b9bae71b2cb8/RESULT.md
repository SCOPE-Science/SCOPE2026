# Exact isotropic defect and the unique exceptional dimension of parity halfcubes

## Finding

For each integer \(n\ge3\), let the parity halfcube (demihypercube) be
\[
H_n=\operatorname{conv}\bigl\{\varepsilon\in\{-1,1\}^n:\prod_{i=1}^n\varepsilon_i=1\bigr\}\subset\mathbb R^n.
\]
Let \(X_n\) be uniformly distributed with respect to ordinary \(n\)-dimensional Euclidean volume on \(H_n\). Define
\[
a_n=\frac{2^{n-1}}{n!},\qquad
m_n=\frac{n^2-n+2}{(n+1)(n+2)}.
\]
Then its volume, centroid, and complete covariance matrix are
\[
\boxed{\operatorname{vol}_n(H_n)=2^n(1-a_n),\qquad
\mathbb E X_n=0,\qquad
\operatorname{Cov}(X_n)=\frac{\frac13-a_nm_n}{1-a_n}\,I_n.}
\tag{1}
\]

Define the affine-invariant isotropic constant of a full-dimensional convex body \(K\subset\mathbb R^n\) by
\[
L_K^{2n}=\frac{\det\operatorname{Cov}(X_K)}{\operatorname{vol}_n(K)^2},
\]
where \(X_K\) has uniform Euclidean-volume distribution on \(K\). For the cube \(C_n=[-1,1]^n\), \(L_{C_n}=1/\sqrt{12}\). The exact halfcube profile is
\[
\boxed{12L_{H_n}^2=\frac{1-3a_nm_n}{(1-a_n)^{1+2/n}}.}
\tag{2}
\]
A sharp comparison holds **in every admissible dimension**:
\[
\boxed{L_{H_3}>L_{C_3},\qquad L_{H_n}<L_{C_n}\quad(n\ge4).}
\tag{3}
\]
There is no equality case. The isotropic deficit is superfactorially small but nonzero:
\[
\boxed{\lim_{n\to\infty}\frac{1-L_{H_n}/L_{C_n}}{2^{n-1}/n!}=1.}
\tag{4}
\]
The sign of the comparison at \(n=3\) is classical for the regular tetrahedron; the \(n=4\) halfcube is a cross-polytope. The new geometrically motivated content is the explicit all-dimensional volume-uniform covariance and isotropic profile, its complete transition, and its sharp asymptotic scale for higher halfcubes.

## Assumptions and scope

All volumes and covariances use the **intrinsic standard Euclidean metric** in \(\mathbb R^n\), without a lattice-normalized-volume convention. In the formula for \(H_n\), the product constraint selects the sign vectors with an even number of negative coordinates. This is an affine copy of the even-parity \(0/1\) polytope. The restriction \(n\ge3\) is essential for full dimension and for the signed-symmetry covariance argument. No assertion is made for arbitrary parity-constrained subsets, nonuniform densities, or affine images with respect to a fixed metric (although the isotropic constant itself is affine invariant).

## Proof

**1. Disjoint removal of forbidden corners.** The classical halfspace description of the even parity polytope, after the change of variables from \(0/1\) coordinates to \(\pm1\) coordinates, is
\[
H_n=[-1,1]^n\cap\bigcap_{\substack{s\in\{-1,1\}^n\\ \prod_i s_i=-1}}\{x:s\cdot x\le n-2\}.
\tag{5}
\]
For each forbidden sign vector \(s\), the portion of the cube removed by \(s\cdot x>n-2\) is the interior, relative to the cube, of
\[
T_s=\biggl\{x_i=s_i(1-2y_i):y_i\ge0,\ \sum_{i=1}^ny_i\le1\biggr\}.
\tag{6}
\]
Each \(T_s\) is an \(n\)-simplex of volume \(2^n/n!\). Two distinct forbidden vectors differ in at least two coordinates. If both strict cuts held at \(x\), adding them would give \((s+t)\cdot x>2(n-2)\), but the cube bounds give \((s+t)\cdot x\le2(n-h)\le2(n-2)\), where \(h\ge2\) is their Hamming distance. Therefore removed simplex interiors are disjoint. As there are \(2^{n-1}\) forbidden corners, the fraction of cube volume removed is exactly \(a_n\). This proves the volume formula in (1). In particular, \(0<a_n<1\) for all \(n\ge3\).

**2. Second moment of one removed simplex.** A uniformly distributed point \(Y\) in the standard simplex \(\{y_i\ge0,\ \sum_i y_i\le1\}\) has, for every coordinate,
\[
\mathbb E Y_i=\frac1{n+1},\qquad
\mathbb E Y_i^2=\frac2{(n+1)(n+2)}.
\]
These follow by integrating a monomial on the simplex, or by the \(\mathrm{Dirichlet}(1,\ldots,1)\) distribution with an additional slack coordinate. Under (6),
\[
\mathbb E_{T_s}x_i^2=\mathbb E(1-2Y_i)^2
=1-\frac4{n+1}+\frac8{(n+1)(n+2)}=m_n,
\tag{7}
\]
independently of \(s\) and \(i\). On the full cube, \(\mathbb E_{C_n}x_i^2=1/3\). Removing the disjoint simplices and dividing by the remaining volume gives
\[
\mathbb E_{H_n}x_i^2=\frac{\frac13-a_nm_n}{1-a_n}.
\tag{8}
\]

**3. Centroid and mixed moments.** The coordinate-permutation group and all sign changes of an even number of coordinates preserve \(H_n\). Given any coordinate \(i\), choosing \(j\ne i\) and changing the signs of \(i,j\) shows \(\mathbb EX_{n,i}=0\). For distinct \(i,j\), choose \(k\) distinct from both (possible because \(n\ge3\)); changing the signs of \(i,k\) reverses \(X_{n,i}X_{n,j}\), so its expectation is zero. Equation (8) thus gives exactly the scalar covariance in (1), with no unverified independence assumptions.

**4. Affine-invariant normalization and exceptional dimensions.** Substituting the scalar covariance and \(\operatorname{vol}_n(H_n)=2^n(1-a_n)\) into the definition of \(L_K\) yields (2). Write \(b_n=3m_n\) and \(p_n=1+2/n\), so
\[
\left(\frac{L_{H_n}}{L_{C_n}}\right)^2
=\frac{1-b_na_n}{(1-a_n)^{p_n}},
\qquad
b_n-p_n=\frac{2(n^3-4n^2-n-2)}{n(n+1)(n+2)}.
\tag{9}
\]
In dimension three, the exact squared ratio is
\[
\left(\frac{L_{H_3}}{L_{C_3}}\right)^2=\frac35\,3^{2/3}>1,
\]
since its cube equals \(243/125>1\). In dimension four, the squared ratio is \((4/5)\sqrt{3/2}<1\), since its square equals \(24/25<1\). For \(n\ge5\), \(n^3-4n^2-n-2=n^2(n-4)-(n+2)>0\), hence \(b_n>p_n>1\). Bernoulli's inequality (strict for \(0<a_n<1\) and \(p_n>1\)) implies
\[
(1-a_n)^{p_n}>1-p_na_n>1-b_na_n.
\]
Consequently the ratio in (9) is strictly less than one for all \(n\ge5\). This proves every case of (3).

**5. Sharp asymptotic.** We have \(a_n\to0\), \(b_n\to3\), and \(p_n\to1\). Taking logarithms in (9) and expanding uniformly for sufficiently large \(n\),
\[
\log\frac{L_{H_n}}{L_{C_n}}
=\frac12\bigl(\log(1-b_na_n)-p_n\log(1-a_n)\bigr)
=-\frac{b_n-p_n}{2}a_n+O(a_n^2).
\]
Moreover, \((b_n-p_n)/2\to1\). Therefore \(1-L_{H_n}/L_{C_n}\sim a_n\), yielding (4). No finite-dimensional enumeration is substituted for any of these all-dimensional arguments.

## Verification

The embedded pure-standard-library checker `verify.py` reproduces the exact rational moments and ratios for the first eighty dimensions, checks the algebraic identity (9), tests the two exceptional cases by raising positive quantities to integer powers, and checks the sign of the cubic numerator throughout its finite regression range. The cubic's positivity for **all** \(n\ge5\) is proved above, rather than inferred from finite tests.

The independent integration checker `verify_polytope.py`, executed with Python, NumPy and SciPy, constructs each halfcube's sign-vertex convex hull for \(n=3,4,5,6\). It triangulates visible boundary facets from the origin, integrates the simplex first and second moments directly using determinant weights, and compares the resulting full covariance matrix and volume with (1). The direct checks matched to floating-point precision for all four dimensions (maximum covariance error below \(5\cdot10^{-15}\)). Such finite calculations provide a reproducible stress test, not a proof beyond their tested dimensions.

## Relationship to prior work

Ermel and Walter (2018) provide the even-parity polytope outer description underlying (5), crediting its earlier development to Jeroslow; their main results concern formulations and optimization rather than uniform-volume inertia. Manecke, Sanyal and So (2018) investigate halfcube faces, triangulations, and related polytope structures. Neither inspected paper states the covariance identity (1), all-dimensional comparison (3), or asymptotic (4). The volume follows easily from these existing halfspace descriptions; the new claim does not assert priority over the parity-polytope description or cube-corner triangulations.

An existing published calculation of John and Löwner ellipsoids of type-\(D\) spin weight polytopes treats precisely the same vertex orbit as \(H_n\), up to a factor of two. Its extremal enclosing and contained ellipsoids do not determine the covariance of a **uniformly volume-distributed interior point** and do not imply the isotropic profile. A separate published sharp isotropic-constant theorem for Hanner polytopes covers the four-dimensional cross-polytope special case but not the general halfcube family (in particular, the odd-dimensional noncentrally symmetric members). Kipp (2024/2025) gives relevant isotropic-constant benchmarks and structural theorems for different polytope classes; the inspected text does not supply (1)--(4).

## Limitations

The comparison is with the cube in the same dimension, not a universal isotropic-constant extremum among all convex bodies. The three-dimensional sign reversal is already explained by classical simplex geometry; the four-dimensional comparison follows from known cross-polytope geometry. The profile for higher halfcubes is the principal object of the claim. An equivalent volume-moment calculation might exist in older parity-polytope, Coxeter-polytope, or solid-inertia literature not identified in the available searches; search absence is not a mathematical uniqueness certificate. The result has not undergone independent mathematical validation.

## References

1. Dominik Ermel and Matthias Walter, *Parity Polytopes and Binarization*, arXiv:1803.10561v1, first public 2018-03-28, Section 1 and equation (2), https://arxiv.org/abs/1803.10561.
2. Sebastian Manecke, Raman Sanyal and Jeonghoon So, *\(S\)-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491v1, first public 2018-12-18, Sections 1–3, primary MSC 52B20, https://arxiv.org/abs/1812.07491.
3. Christian Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353v1, first public 2024-07-01, https://arxiv.org/html/2407.01353v2.
4. *Exact John–Löwner ellipsoids of type-D spin weight polytopes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-l-wner-ellipsoids-of-type-d-spin-weight-polytopes--15c85fee505a.
5. *Sharp isotropic-constant range of all Hanner polytopes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2.
