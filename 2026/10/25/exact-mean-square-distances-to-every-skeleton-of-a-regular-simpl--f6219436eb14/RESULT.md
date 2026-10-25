# Exact mean-square distances to every skeleton of a regular simplex

## Finding
Let \(k\geq 2\), let \(\Delta\) be a regular Euclidean \((k-1)\)-simplex of edge length \(s>0\), and let \(X\) be uniformly distributed with respect to its \((k-1)\)-dimensional volume. For \(1\leq m\leq k-1\), let \(\mathcal S_{m-1}\) denote the union of its faces of dimension at most \(m-1\), and put \(D_m=\operatorname{dist}(X,\mathcal S_{m-1})\). Write \(H_j=\sum_{i=1}^j 1/i\). Then the simultaneous mean-square distance profile is
\[
\boxed{\mathbb E[D_m^2]/s^2=\frac{1}{2m}-\frac{H_k-H_m}{k}-\frac{m+1}{2k(k+1)}.}
\]

There is also an explicit joint law for \((D_1^2,\ldots,D_{k-1}^2)\): if \((U_1,\ldots,U_k)\) is uniformly distributed on the probability simplex (the Dirichlet law with all parameters one), then simultaneously for every \(m\),
\[
\boxed{\frac{2D_m^2}{s^2}\ \overset{\mathrm d}=\ \sum_{r,s'=m+1}^k\left(\frac1m-\frac{1}{\min(r,s')}\right)U_rU_{s'}.}
\]
The same \(U\) is used for every \(m\). Consequently, all joint polynomial moments of the squared skeleton distances reduce to finite Dirichlet moments.

Three distinct sharp asymptotic regimes follow, with simplex edge length held fixed: for fixed \(m\), \(\mathbb E[D_m^2]/s^2\to 1/(2m)\); when \(m/k\to\alpha\in(0,1)\),
\[
\frac{k\mathbb E[D_m^2]}{s^2}\longrightarrow\frac12\left(\frac1\alpha-\alpha+2\log\alpha\right);
\]
and when \(q=k-m\geq1\) is fixed,
\[
\frac{k^4\mathbb E[D_{k-q}^2]}{s^2}\longrightarrow\frac{q(q+1)(q+2)}6.
\]
The nearest \((m-1)\)-face of \(X\) is obtained by retaining the \(m\) largest barycentric coordinates (uniquely except on measure-zero tie sets).

## Assumptions and scope
All distances are ordinary ambient Euclidean distances, not geodesic distances in the simplex. A face is closed, and the \((m-1)\)-skeleton includes all lower-dimensional faces. Uniform sampling means normalized intrinsic volume of the full simplex. The formula holds for every integer pair \(k\ge2\), \(1\le m\le k-1\); \(m=k\) would give zero distance by definition and is intentionally excluded. Vertices correspond to \(m=1\), and the boundary to \(m=k-1\). Boundary sampling configurations and coordinate ties form volume-zero events.

## Proof
**Euclidean face projection.** By a rigid motion and scale, embed the simplex as the convex hull of \(s e_i/\sqrt2\) in the affine hyperplane \(\sum_i x_i=s/\sqrt2\) of \(\mathbb R^k\). A point has barycentric vector \(\lambda=(\lambda_1,\ldots,\lambda_k)\) with nonnegative entries totaling one. Fix a subset \(S\) of \(m\) vertices and let \(T=\sum_{j\notin S}\lambda_j\). The nearest point on its face has barycentric coordinates \(\mu_j=\lambda_j+T/m\) on \(S\) and zero elsewhere: this is the orthogonal projection onto the face's affine span, and every retained coordinate is nonnegative. Hence
\[
\frac{2\operatorname{dist}(X,\operatorname{face}(S))^2}{s^2}=\sum_{j\notin S}\lambda_j^2+\frac{T^2}{m}.
\]
If a retained coordinate is smaller than an omitted one, exchanging them strictly decreases both terms, except in a tie. Therefore the optimal face retains the \(m\) largest coordinates. Write the decreasing rearrangement as \(\lambda_{(1)}\ge\cdots\ge\lambda_{(k)}\). We obtain, pointwise,
\[
\frac{2D_m^2}{s^2}=\sum_{j=m+1}^k\lambda_{(j)}^2+\frac1m\left(\sum_{j=m+1}^k\lambda_{(j)}\right)^2.\tag{1}
\]

**Ordered-gap transformation.** Uniform intrinsic volume on this simplex induces \(\operatorname{Dirichlet}(1,\ldots,1)\) barycentric coordinates. Put \(\lambda_{(k+1)}=0\), and define \(U_r=r(\lambda_{(r)}-\lambda_{(r+1)})\). Since \(\sum_r U_r=\sum_j\lambda_{(j)}=1\), this triangular linear change maps the ordered barycentric chamber bijectively to the standard probability simplex. The original density is constant on this chamber and the Jacobian is constant, so \(U\) is again \(\operatorname{Dirichlet}(1,\ldots,1)\). Inverting gives \(\lambda_{(j)}=\sum_{r=j}^k U_r/r\).

Substituting into (1) yields
\[
\frac{2D_m^2}{s^2}=\sum_{r,s'=m+1}^k\left(\frac{\min(r,s')-m}{rs'}+\frac{(r-m)(s'-m)}{mrs'}\right)U_rU_{s'}.
\]
The coefficient simplifies exactly to \(1/m-1/\min(r,s')\). This proves the stated simultaneous quadratic-form law, including its dependence across distinct skeleton dimensions.

**Exact expectation.** Dirichlet second moments are \(\mathbb E[U_rU_{s'}]=(1+\mathbf1_{r=s'})/[k(k+1)]\). With \(q=k-m\) and \(h=H_k-H_m\), the off-diagonal-plus-diagonal coefficient sum is
\[
\sum_{r,s'>m}\left(\frac1m-\frac1{\min(r,s')}\right)=\frac{q^2}{m}+2q-(2k+1)h,
\]
and the trace is \(q/m-h\). Thus
\[
\frac{2\mathbb E[D_m^2]}{s^2}=\frac{q(q+1)/m+2q-2(k+1)h}{k(k+1)}.
\]
The identity \(q(q+1)/m+2q=k(k+1)/m-(m+1)\) gives the boxed closed form.

**Asymptotics.** For fixed \(m\), use \(H_k=\log k+\gamma+o(1)\). If \(m/k\to\alpha\in(0,1)\), use \(H_k-H_m\to-\log\alpha\). If \(q=k-m\) is fixed, index the nonzero coefficients by \(r=m+a\) and \(s'=m+b\), where \(1\le a,b\le q\). Then \(k^2(1/m-1/\min(r,s'))\to\min(a,b)\), and \(k^2\mathbb E[U_rU_{s'}]\to 1+\mathbf1_{a=b}\). It follows that
\[
\lim_{k\to\infty}\frac{k^4\mathbb E[D_{k-q}^2]}{s^2}=\frac12\left(\sum_{a,b=1}^q\min(a,b)+\sum_{a=1}^q a\right)=\frac{q(q+1)(q+2)}6.
\]
All limits concern precisely the stated scaling regimes; no simultaneous regime beyond them is asserted.

## Verification
The accompanying standalone `verify_skeleton.py` uses only Python's standard library. It verifies the exact rational moment identity for every \(2\le k\le12\) and each permitted \(m\), compares direct enumeration of all candidate faces to the sorted-coordinate rule for sampled points through \(k=7\), and independently compares seven Monte Carlo means to the proved formula. The listed finite checks are corroboration; the preceding argument proves the formulas for unbounded integer parameters.

## Relationship to prior work
Conway and Sloane (1982) give second moments of uniform points **about a fixed centroid** in arbitrary and regular simplices and study nearest-lattice quantization. Those targets are not the variable nearest point on an entire simplex skeleton. Kyrillidis, Becker, Cevher and Koch (arXiv:1206.1529, initially posted 7 June 2012) establish a sparse Euclidean projection algorithm onto the probability simplex; their exact support-selection rule covers the nearest-face *optimization* step here. The new statement is the joint Dirichlet quadratic-form law and evaluated mean-square geometric profile for **all** skeleton dimensions, with distinct dimensional regimes. Published work on convexification by averaging a simplex skeleton concerns Minkowski sums and filling thresholds, not the random Euclidean distance law. These differences do not exclude an uncatalogued equivalent derivation.

## Limitations
No independence of the squared skeleton distances is claimed, and the result does not optimize vertex placements or investigate nonregular simplices. The checker does not constitute an infinite-dimensional proof. Earlier equivalent integrations in unindexed geometric-probability or sparse-approximation literature remain possible; novelty assessment is provisional pending independent literature review.

## References
1. J. H. Conway and N. J. A. Sloane, “Voronoi Regions of Lattices, Second Moments of Polytopes, and Quantization,” *IEEE Transactions on Information Theory* 28 (1982), 211–226, DOI: 10.1109/TIT.1982.1056483; public full text: https://neilsloane.com/doc/Me82.pdf. Section II-D/E was inspected.
2. A. Kyrillidis, S. Becker, V. Cevher and C. Koch, “Sparse Projections onto the Simplex,” arXiv:1206.1529v1, 7 June 2012; https://arxiv.org/abs/1206.1529. The introduction and support-selection theorem were inspected in the publicly available full PDF.
