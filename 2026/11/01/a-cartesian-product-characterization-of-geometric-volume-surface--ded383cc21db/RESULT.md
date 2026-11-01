# A Cartesian-product characterization of geometric volume–surface convex order

## Finding
Let \(E_1,\ldots,E_m\) be mutually orthogonal Euclidean spaces, \(m\ge2\), and let \(K_i\subset E_i\) be full-dimensional compact convex bodies of dimensions \(d_i\ge1\). Write \(\mu_i\) for normalized Lebesgue measure on \(K_i\), \(\nu_i\) for normalized Euclidean \((d_i-1)\)-dimensional surface measure on \(\partial K_i\), and \(K=\prod_{i=1}^m K_i\). Let \(\mu\) and \(\nu\) denote the corresponding normalized volume and surface measures on \(K\). Then the following equivalence holds:

\[
\boxed{\mu\preceq_{\mathrm{cx}}\nu\quad\Longleftrightarrow\quad\mu_i\preceq_{\mathrm{cx}}\nu_i\text{ for every }i.}
\]

Here \(\preceq_{\mathrm{cx}}\) means that integration of every continuous convex function against the first measure does not exceed integration against the second. In particular, the geometric Jensen property is **both inherited by and reflected from** any finite orthogonal Cartesian product; no adverse factor can be concealed by adding other factors.

The equivalence has an explicit weighting law. Writing \(V_i=\operatorname{vol}_{d_i}(K_i)\), \(S_i=\mathcal H^{d_i-1}(\partial K_i)\), and
\[
 p_i=\frac{S_i/V_i}{\sum_{j=1}^m S_j/V_j},
\]
one has the exact probability-measure decomposition
\[
\nu=\sum_{i=1}^m p_i\bigl(\nu_i\otimes\!\bigotimes_{j\ne i}\mu_j\bigr).
\]
Whenever the factor inequalities hold, every continuous function convex separately in each of its \(k\) point arguments satisfies
\[
\mathbb E\Phi(X^1,\ldots,X^k)\le\mathbb E\Phi(Y^1,\ldots,Y^k),
\]
where the \(X^a\) are independent uniform-volume points of \(K\) and the \(Y^a\) are independent uniform-surface points.

A fully explicit new high-dimensional class is obtained when each \(K_i\) is either a Euclidean ball or a centrally symmetric convex polytope all of whose facets are tangent to one sphere centered at its symmetry center \(c_i\). Different factors may have different radii, dimensions, and shapes. For these products, for every \(\lambda\ge0\) and every \(\lambda\)-strongly convex continuous function \(f\) on \(K\),
\[
\boxed{\int f\,d\nu-\int f\,d\mu\ \ge\ \frac{\lambda}{2}\sum_i p_i\frac{2}{d_i+2}\int_{\partial K_i}\|y-c_i\|^2\,d\nu_i(y).}
\]
This is sharp on each such product: equality holds for \(f(x)=\frac\lambda2\|x\|^2+\ell(x)\), with any affine \(\ell\). For the right circular cylinder \(K=B^2_1\times[-2,2]\subset\mathbb R^3\), the exact quadratic boundary–volume gap is \(14/15\), so the sharp strong-convexity gap is \(7\lambda/15\).

## Assumptions and scope
All dimensions are positive integers, and all bodies are compact, convex, and have nonempty interior in their Euclidean summands. The surface measures are intrinsic Euclidean Hausdorff measures; in dimension one, the boundary surface measure is counting measure on the two endpoints. The product decomposition is **orthogonal**; arbitrary affine transformations generally do not preserve uniform Euclidean surface measure. Convex order is tested against continuous finite-valued convex functions on compact bodies. In the strong-convexity assertion, \(f(x)-\frac\lambda2\|x\|^2\) is convex, and \(c_i\) is the stated symmetry center. The displayed numerical cylinder example has radius one and height four.

## Proof
**1. Boundary disintegration.** The boundary of \(K\), modulo sets of \((\sum_i d_i-1)\)-dimensional Hausdorff measure zero, is the union of strata \(F_i=\partial K_i\times\prod_{j\ne i}K_j\). Two such strata intersect in codimension at least two, hence contribute zero hypersurface measure. Orthogonality makes the hypersurface measure on each \(F_i\) the product of \(\mathcal H^{d_i-1}|_{\partial K_i}\) and the other volume measures. Thus
\[
\mathcal H^{D-1}(\partial K)=\sum_i S_i\prod_{j\ne i}V_j
=\Bigl(\prod_j V_j\Bigr)\sum_i\frac{S_i}{V_i},\quad D=\sum_i d_i,
\]
and normalization yields the stated mixture identity. Meanwhile \(\mu=\bigotimes_i\mu_i\).

**2. Sufficiency.** Suppose \(\mu_i\preceq_{\rm cx}\nu_i\) for all \(i\). Fix any continuous convex \(f:K\to\mathbb R\). For fixed coordinates \(x_j\), \(j\ne i\), the function \(x_i\mapsto f(x_1,\ldots,x_m)\) is convex. Integrating the factor inequality over the other \(\mu_j\) gives
\[
\int f\,d(\nu_i\otimes\!\bigotimes_{j\ne i}\mu_j)\ge\int f\,d\mu.
\]
Multiplying by \(p_i\), summing, and using the boundary mixture proves \(\mu\preceq_{\rm cx}\nu\). For separately convex \(\Phi\) on \(K^k\), replace independent \(\mu\)-distributed arguments successively by independent \(\nu\)-distributed arguments. Each replacement increases expectation by convex order, proving the stated multi-point inequality.

**3. Necessity.** Conversely suppose \(\mu\preceq_{\rm cx}\nu\). For a fixed index \(i\) and any continuous convex \(g:K_i\to\mathbb R\), take \(f(x_1,\ldots,x_m)=g(x_i)\). By the explicit surface mixture,
\[
\int f\,d\nu-\int f\,d\mu
=p_i\Bigl(\int g\,d\nu_i-\int g\,d\mu_i\Bigr).
\]
Every \(p_i>0\), so the parenthesized difference must be nonnegative. This is exactly \(\mu_i\preceq_{\rm cx}\nu_i\) for every factor. Notice that this argument rules out compensation from the remaining factors.

**4. Independently verified building blocks.** Translate a centrally symmetric body \(K_i\) so that its symmetry center is the origin, and denote its radial function by \(\rho(\omega)\). If \(X\) is uniform in it, polar coordinates show that
\[
 X=T\rho(\Omega)\Omega,\qquad
 \mathbb P(T\le t)=t^{d_i}\quad(0\le t\le1),
\]
where \(T\) is independent of the direction \(\Omega\), and \(\Omega\) has density proportional to \(\rho(\omega)^{d_i}\) against spherical measure (for \(d_i=1\), use the two unit directions with counting measure). Conditional on \(X\), choose \(\varepsilon\in\{-1,1\}\) with
\[
\mathbb P(\varepsilon=1\mid X)=\frac{1+T}{2},\qquad
Y=\varepsilon\rho(\Omega)\Omega.
\]
Then \(\mathbb E[Y\mid X]=X\). Central symmetry ensures that the law of \(Y\) is the cone probability measure of the body: the direction law of \(\Omega\) is invariant under sign, so mixing positive and negative endpoints preserves its distribution. On the boundary of a Euclidean ball this cone measure is normalized surface measure. On the facets of a polytope tangent to a sphere about the origin, the support height \(\langle y,n(y)\rangle\) is the same constant on every facet. Since \(d\mathrm{Vol}_{\rm cone}(y)=(\langle y,n(y)\rangle/d_i)\,d\mathcal H^{d_i-1}(y)\), its normalized cone measure is again normalized Euclidean surface measure. Thus the construction directly gives a martingale coupling from \(\mu_i\) to \(\nu_i\), with no reliance on a planar directional-order implication. After restoring the symmetry center the conditional expectation remains valid.

**5. Sharp quantitative gap.** For every factor covered by Step 4, radial integration gives
\[
\int_{K_i}\|x-c_i\|^2\,d\mu_i(x)
=\frac{d_i}{d_i+2}\int_{\partial K_i}\|y-c_i\|^2\,d\nu_i(y).
\]
Applying the mixture identity to \(\sum_i\|x_i-c_i\|^2\) therefore yields the exact second-moment gap
\[
\int\|x-c\|^2\,d\nu(x)-\int\|x-c\|^2\,d\mu(x)
=\sum_i p_i\frac{2}{d_i+2}\int\|y-c_i\|^2\,d\nu_i(y).
\]
Apply convex order to \(f(x)-\lambda\|x\|^2/2\) to obtain the claimed inequality. Equality holds for a quadratic of this form plus an affine function, proving optimality of its coefficient. In the cylinder, the surface-to-volume ratios of the disk and interval are \(2\) and \(1/2\), so their mixture weights are \(4/5\) and \(1/5\). Their respective second-moment gaps are \(1/2\) and \(8/3\), giving \((4/5)(1/2)+(1/5)(8/3)=14/15\).

## Verification
The measure disintegration, both implications of the equivalence, radial independence, symmetry-preserving sign randomization, and factor second-moment identities are proved symbolically above for arbitrary dimensions and arbitrary admissible factors. The accompanying independent arithmetic checker recomputes the cylinder numbers and tests the second-moment mixture identity on a deterministic collection of rational-radius products of Euclidean balls of varying dimensions. It is an arithmetic regression check; no finite set of tests substitutes for the preceding general proof. Run the included source with \(\texttt{python3 verify.py}\); only the Python standard library is needed.

## Relationship to prior work
Pasteczka's *Jensen-type geometric shapes* (first publicly available in 2018, journal 2020) proves this volume-to-surface convex comparison for balls, parallelotopes, and a tangential-polytope class, **not** a necessary-and-sufficient Cartesian-product law. In particular, its parallelotope case is already known and is not asserted as new. Tokmachev's *Inequalities for convex functions of random points inside and on the boundary of convex bodies* (July 9, 2026) gives convex-order consequences and new planar hypotheses, but does not characterize stability under Cartesian products. Shen's *The Zaporozhets–Tarasov Conjecture on Mean Distances* (August 6, 2026) constructs counterexamples in dimension at least three and uses products to raise dimensions, without proving the iff property for the stronger convex order. The present law explains precisely why taking a product preserves a positive instance and cannot repair an offending factor; the cylinder and products with unlike tangency radii lie outside those earlier stated sufficient classes. The radial martingale coupling gives direct verification for all explicitly claimed building blocks.

## Limitations
The iff property pertains to **orthogonal Cartesian products** and normalized ordinary Euclidean surface measure; it is not a statement about Minkowski sums or arbitrary linear images of products. It does not imply that all convex bodies satisfy volume-to-surface convex order; higher-dimensional counterexamples to even the mean-distance inequality exist. For centrally symmetric factors that are neither balls nor tangential polytopes, Step 4's radial construction yields cone-volume boundary measure rather than uniform surface measure and does not establish the desired factor condition. An equivalent characterization in unindexed or differently phrased historical literature cannot be ruled out solely by the searches carried out here.

## References
1. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869 (first submitted July 9, 2026). https://arxiv.org/abs/2607.08869
2. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470 (first submitted August 6, 2026). https://arxiv.org/abs/2608.06470
3. P. Pasteczka, *Jensen-type geometric shapes*, arXiv:1804.03688 (first submitted April 10, 2018); published in *Annales Universitatis Paedagogicae Cracoviensis. Studia Mathematica* 19 (2020), 27–33. https://arxiv.org/abs/1804.03688
4. V. Strassen, *The existence of probability measures with given marginals*, Annals of Mathematical Statistics **36** (1965), 423–439 (martingale characterization of convex order).
