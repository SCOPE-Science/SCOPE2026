# Facet-area Wiener identity and Brownian surface separation for tree root polytopes

## Finding
Let \(T\) be any finite unweighted tree on \(n\ge3\) labelled vertices, and let
\[
P_T=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(T)\}\subset H=\{x\in\mathbb R^n:\sum_v x_v=0\},
\]
with the intrinsic Euclidean metric inherited from \(\mathbb R^n\). There are \(2^{n-1}\) simplex facets. Write \(A_F\) for the intrinsic \((n-2)\)-volume of a facet and \(S_T=\sum_F A_F\) for boundary surface area. Put \(W(T)=\sum_{u<v}\operatorname{dist}_T(u,v)\), the Wiener index. Then
\[
\boxed{\frac1{2^{n-1}}\sum_F A_F^2=\frac{W(T)}{((n-2)!)^2}.}\tag{1}
\]
Furthermore, if \(\varepsilon_e\) are independent uniform signs, root \(T\) arbitrarily, and let \(\phi(v)\) be the sum of signed edge increments along the path from the root to \(v\), then
\[
\boxed{S_T=\frac{2^{n-1}\sqrt n}{(n-2)!}\,\mathbb E\left[\left(\sum_v(\phi(v)-\bar\phi)^2\right)^{1/2}\right],\quad \bar\phi=n^{-1}\sum_v\phi(v).}\tag{2}
\]
The expectation \(m_T\) inside (2) obeys universal bounds
\[
\sqrt{\frac{W(T)}{3n}}\le m_T\le\sqrt{\frac{W(T)}n}.\tag{3}
\]
For the \(n\)-vertex star \(\mathsf{Star}_n\) and path \(\mathsf{Path}_n\), with facet \(F\) sampled uniformly in each polytope,
\[
\frac{(n-2)! A_F(\mathsf{Star}_n)}n\ \xrightarrow{\mathbb P}\ 1,
\qquad
\frac{(n-2)! A_F(\mathsf{Path}_n)}{n^{3/2}}\ \xrightarrow{d}\ Q^{1/2},\tag{4}
\]
where \(Q=\int_0^1(B(t)-\int_0^1B(s)\,ds)^2\,dt\) for standard Brownian motion \(B\). Its law is nondegenerate and admits the independent-Gaussian representation
\[
Q\ \overset d=\ \sum_{k\ge1}\frac{Z_k^2}{\pi^2 k^2},\qquad Z_k\overset{\mathrm{iid}}\sim N(0,1).\tag{5}
\]
Consequently the exact sharp path-to-star surface-area asymptotic is
\[
\boxed{\frac{S_{\mathsf{Path}_n}}{S_{\mathsf{Star}_n}}\sim c\sqrt n,\qquad c=\mathbb E\sqrt Q=\sqrt{\frac2\pi}\int_0^\infty\frac{1-\sqrt{u/\sinh u}}{u^2}\,du=0.3781319637\ldots.}\tag{6}
\]
The word "sharp" refers to the explicit first-order constant for this specified pair of tree families, **not** an asserted extremum among all trees.

## Assumptions and scope
All edges have unit length; vertices are the standard coordinate roots in the zero-sum hyperplane, not an arbitrary unimodularly transformed crosspolytope. \(S_T\) is the sum of intrinsic facet measures, not spherical mean width or normalized lattice volume. Facets are sampled uniformly among the \(2^{n-1}\) actual facets; the signs in (2) induce exactly this law. The convergence in (4) concerns this uniform facet law; it is not a claim about random trees.

## Proof
Orient the \(d=n-1\) tree edges and let \(B:H\leftarrow\mathbb R^d\) be the incidence-column linear isomorphism. Deleting any one row of the incidence matrix gives determinant \(\pm1\). Cauchy--Binet gives \(\det(B^\top B)=n\), so its intrinsic determinant is \(\sqrt n\). The polytope is the image of the standard \(d\)-dimensional crosspolytope \(\{t:\sum_e|t_e|\le1\}\), whose facets are indexed by \(s\in\{\pm1\}^d\) and have vertices \(s_eb_e\). Every facet pyramid with apex zero has volume \(\sqrt n/d!\).

For each sign vector \(s\), the outward facet normal \(h_s\in H\) normalized by \(\langle h_s,s_eb_e\rangle=1\) is the unique centered vertex potential satisfying \(B^\top h_s=s\). The facet lies at Euclidean distance \(1/\|h_s\|\) from the origin. Equating the simplex-pyramid volume with base-area times height divided by \(d\) gives
\[
A_s=\frac{\sqrt n}{(d-1)!}\|h_s\|.\tag{7}
\]
The potential difference \(h_s(u)-h_s(v)\) is the signed sum along the unique \(u\)-to-\(v\) path. Centering does not affect differences, and the identity
\[
\|h_s\|^2=\frac1n\sum_{u<v}(h_s(u)-h_s(v))^2\tag{8}
\]
is an exact expansion of variance. Independence of the signs gives \(\mathbb E(h_s(u)-h_s(v))^2=\operatorname{dist}_T(u,v)\); hence \(\mathbb E\|h_s\|^2=W(T)/n\). Squaring (7) proves (1), and summing it proves (2).

For (3), express \(h_s=\sum_e s_e q_e\) with fixed centered cut-indicator vectors \(q_e\in H\). Put \(X=\|h_s\|\) and \(a=\mathbb E X^2=W(T)/n\). Expansion of the fourth moment yields \(\mathbb E X^4=a^2+4\sum_{e<f}\langle q_e,q_f\rangle^2\le3a^2\). Jensen gives \(\mathbb E X\le\sqrt a\), while Hölder interpolation \(a\le(\mathbb E X)^{2/3}(\mathbb E X^4)^{1/3}\) gives \(\mathbb E X\ge\sqrt{a/3}\). Both bounds are uniform in the tree.

For the star, choose its center as root and write \(Y=\sum_{j=1}^{n-1}s_j\). The potential norm is exactly \(\|h_s\|^2=n-1-Y^2/n\). Since \(Y/n\to0\) in probability and \(0\le\|h_s\|/\sqrt n\le1\), both convergence in probability and convergence of the mean \(\mathbb E\|h_s\|/\sqrt n\to1\) follow.

For the path, root an endpoint and set \(R_0=0\), \(R_j=\sum_{i=1}^j s_i\) for \(1\le j<n\). Then \(\|h_s\|^2=\sum_{j=0}^{n-1}(R_j-\bar R)^2\). Donsker's invariance principle, the continuous mapping theorem for the squared demeaned \(L^2\)-norm and a Riemann-sum approximation give \(\|h_s\|/n\Rightarrow\sqrt Q\). Uniform integrability follows from the exact second-moment identity because \(W(\mathsf{Path}_n)=n(n^2-1)/6\), whence \(\mathbb E(\|h_s\|/n)^2=(1-n^{-2})/6\le1/6\). Thus \(\mathbb E\|h_s\|/n\to c\).

For completeness, the covariance kernel of the centered Brownian process is the mean-zero Neumann Green kernel of \(-d^2/dt^2\) on \([0,1]\). Its positive eigenvalues are \((\pi k)^{-2}\), with orthonormal eigenfunctions \(\sqrt2\cos(k\pi t)\), proving (5). For \(Q\ge0\) the identity \(\sqrt Q=(2\sqrt\pi)^{-1}\int_0^\infty(1-e^{-tQ})t^{-3/2}\,dt\) and Tonelli's theorem give an exact Laplace integral. Euler's product \(\sinh u/u=\prod_{k\ge1}(1+u^2/(\pi^2k^2))\), with \(u=\sqrt{2t}\), yields (6). The constants in (4) follow by inserting (7). Finally, the common surface prefactor in (2) cancels from the path/star ratio, which tends to \(c\sqrt n\).

## Verification
The standalone file `tree_crosspolytope_verify.py` uses integer determinant expansion of actual facet edge Gram matrices (not the normal-form determinant formula) and independently compares each squared facet measure with centered signed-path potentials. It checks \(360\) facet instances across \(13\) explicitly constructed trees of orders \(3\) through \(7\), including star, path and branched shapes, then verifies the exact Wiener averages and \(n=4\) values. It also computes the integral constant in (6) by deterministic quadrature; this numerical step checks the decimal only, not the probabilistic limit.

For example, at \(n=4\), the star has \(W=9\) and surface area \(\sqrt3+3\sqrt{11}\), while the path has \(W=10\) and surface area \(2(1+2\sqrt2+\sqrt5)\). Their identical intrinsic volume is \(2^3\sqrt4/3!=8/3\). Running `python tree_crosspolytope_verify.py` from this package prints `VERIFY_OK`.

## Relationship to prior work
D'Alì, Delucchi and Michałek establish the standard signed-root construction and the fact that every tree symmetric edge polytope is unimodularly equivalent to a crosspolytope (2019, Example 2.3). Their facet-labeling theorem provides a combinatorial description. Chen, Davis and Korchevskaia (2021) study facet subgraphs and combinatorial incidence. Delucchi and Hoessly (2016) develop face enumeration for fundamental polytopes of tree metrics. Those results justify the setting and are not presented as new. Crucially, unimodular equivalence does not preserve intrinsic Euclidean facet areas. The claimed contribution here is the Wiener/facet-area quadratic identity **in the standard coordinate metric**, its all-tree norm comparison, and the nondegenerate Brownian facet-area limit with the sharp path-to-star surface ratio. The Brownian spectral representation and invariance principle are standard probability tools, not new general results.

## Limitations
This theorem does not classify trees by their entire facet-area distributions, assert that paths maximize or stars minimize surface area at fixed order, or establish a rate of convergence in (6). The factor \(1/\sqrt3\) in (3) is not claimed optimal. The decimal for \(c\) is approximate; its exact definition is the convergent integral in (6). The finite checker cannot by itself prove the statements for arbitrary orders; those use the displayed analytical arguments. Independent mathematical validation and exhaustive historical bibliographic certainty are not asserted.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), especially Example 2.3 and Theorem 3.1; https://arxiv.org/abs/1910.05193.
2. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (first public 2021-07-26); https://arxiv.org/abs/2107.12315.
3. E. Delucchi, L. Hoessly, *Fundamental polytopes of metric trees via parallel connections of matroids*, arXiv:1612.05534v1 (first public 2016-12-16); https://arxiv.org/abs/1612.05534.
4. P. Billingsley, *Convergence of Probability Measures*, second edition, Wiley (1999), standard functional invariance principle and continuous mapping theorem.
