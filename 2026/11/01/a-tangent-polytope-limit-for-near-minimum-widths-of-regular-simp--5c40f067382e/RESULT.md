# A tangent-polytope limit for near-minimum widths of regular simplices

## Finding
For each integer \(n\ge3\), let \(\Delta_{n-1}\) be a Euclidean regular \((n-1)\)-simplex with unit edge lengths. A Haar-uniform direction \(U\) in its affine span determines the projection width \(W(U)\). Put
\[
a=\lfloor n/2\rfloor,\quad b=\lceil n/2\rceil,\quad m=n-2,\quad w_*=\sqrt{\frac{n}{2ab}},\quad H_n=\binom na\begin{cases}1,&a=b,\\2,&a<b.\end{cases}
\]
Let \(\sigma_m=2\pi^{(m+1)/2}/\Gamma((m+1)/2)\) be the area of the unit \(m\)-sphere. Then the **sharp small-excess probability** is
\[
\Pr\{W(U)\le w_*+\varepsilon\}
=C_n\varepsilon^m+O_n(\varepsilon^{m+1}),\qquad
C_n=\frac{H_n\,2^{m/2}\,a^{a-1/2}b^{b-1/2}}{m!\,\sigma_m}.
\]
For \(n=3,4,5\), respectively, \(C_n=12/\pi,\ 12/\pi,\ 120\sqrt3/\pi^2\). The exponent \(m\) is the dimension of the sphere of directions.

More strongly, near-minimizing directions have a **complete angular scaling limit**, not merely a scalar width distribution. For each of the \(H_n\) minimizing directions \(u_0\), partition the \(n\) coordinates into the positive block \(A\) and negative block \(B\), of sizes \(p,q\in\{a,b\}\). Set
\[
T_{A,B}=\{v\in\mathbb R^n:\sum_{i\in A}v_i=\sum_{j\in B}v_j=0\},\qquad
\phi_{A,B}(v)=\max_{i\in A}v_i-\min_{j\in B}v_j,
\]
\[
K_{A,B}=\{v\in T_{A,B}:\phi_{A,B}(v)\le1\}.
\]
Condition on \(W(U)\le w_*+\varepsilon\), and choose the unique nearest minimizer \(u_0\) (ties have probability zero for sufficiently small \(\varepsilon\)). Define the tangent coordinate
\[
V_\varepsilon=\frac1{\sqrt2\varepsilon}
\left(\frac{U}{\langle U,u_0\rangle}-u_0\right).
\]
As \(\varepsilon\downarrow0\), the selected minimizer becomes uniformly distributed over all \(H_n\) possibilities, and, conditionally on that minimizer, \(V_\varepsilon\) tends **in total variation** to the uniform probability distribution on \(K_{A,B}\). In the natural Euclidean volume on \(T_{A,B}\),
\[
\operatorname{Vol}_m(K_{A,B})=\frac{p^{p-1/2}q^{q-1/2}}{m!}.
\]
When both blocks contain at least two indices, a point \(V\) uniform on \(K_{A,B}\) obeys
\[
\bigl(\max_{i\in A}V_i,\; -\min_{j\in B}V_j,\;1-\phi_{A,B}(V)\bigr)
\sim\operatorname{Dirichlet}(p-1,q-1,1).
\]
When a block is a singleton its corresponding coordinate is identically zero; the remaining nonzero range, \(\phi_{A,B}(V)\), has the \(\operatorname{Beta}(m,1)\) law. The beta law for total range also holds for larger blocks.

There are also **sharp angular stability slopes**. If \(\vartheta\) denotes spherical distance from a direction to the set of minimizing directions, then, as \(\vartheta\downarrow0\), the smallest and largest possible limits of \((W-w_*)/\vartheta\) are exactly
\[
L_n=\frac1{\sqrt{2b(b-1)}},\qquad
R_n=\sqrt{\frac12\left(\frac{a-1}{a}+\frac{b-1}{b}\right)}.
\]
Both endpoints are attained by explicit tangent directions; the bounds are uniform over minimizing directions.

## Assumptions and scope
The simplex is nondegenerate, has unit edge lengths, and is viewed from a direction chosen according to normalized surface area in its \((n-1)\)-dimensional affine span. An equivalent coordinate model uses the subspace \(H=\{u\in\mathbb R^n:\sum_i u_i=0\}\) and its unit sphere, with
\[
W(u)=\frac{\max_i u_i-\min_i u_i}{\sqrt2}.
\]
All limits are taken for fixed integer \(n\ge3\), with excess \(\varepsilon\downarrow0\). Euclidean volumes on block zero-sum subspaces use the metric induced from \(\mathbb R^n\). Gamma, Dirichlet and beta symbols have their standard probability meanings.

## Proof
**1. Equality cases of the minimum width.** Fix a zero-sum unit vector \(u\) and let \(R=\max_i u_i-\min_i u_i\). Replacing any intermediate coordinate with an endpoint while retaining its range strictly increases the centered squared norm. Hence a range-minimizing unit vector must have exactly two coordinate levels. If \(p\) entries are at the higher level and \(q=n-p\) at the lower, the zero-sum and norm constraints determine
\[
u_i=\sqrt{\frac{q}{np}}\ (i\in A),\qquad
u_j=-\sqrt{\frac{p}{nq}}\ (j\in B),\qquad
R=\sqrt{\frac{n}{pq}}.
\]
The product \(pq\) is maximal precisely for \(\{p,q\}=\{a,b\}\). This proves the minimum \(w_*\), the precise finite minimizing set, and its cardinality \(H_n\). This equality characterization also follows from the cited regular-simplex width theorem.

**2. Exact local chart.** At any minimizing vector \(u_0\), the tangent space of the unit sphere in \(H\) is exactly \(T_{A,B}\): the two constraints follow from \(\sum_i v_i=0\) and \(\langle u_0,v\rangle=0\), because the levels differ. Parameterize a neighborhood of \(u_0\) by
\[
\Psi(v)=\frac{u_0+v}{\sqrt{1+\|v\|^2}}.
\]
The sphere-area Jacobian is \((1+\|v\|^2)^{-(m+1)/2}\). For sufficiently small \(v\), all maximum coordinates stay in \(A\), all minimum coordinates in \(B\), and exactly
\[
W(\Psi(v))=\frac{\sqrt{n/(ab)}+\phi_{A,B}(v)}{\sqrt2\sqrt{1+\|v\|^2}}.
\]
The function \(\phi\) is nonnegative, positively homogeneous and vanishes on \(T_{A,B}\) only at the origin (each block has zero mean). Thus \(\phi(v)\) bounds \(\|v\|\) above and below by positive constants. Compactness and the isolation of the equality cases imply that every sufficiently near-minimal global direction belongs to one of these disjoint charts, with \(\|v\|=O_n(\varepsilon)\).

**3. Scaling and total-variation limit.** In the chart set \(v=\sqrt2\varepsilon z\). The exact inequality \(W(\Psi(v))\le w_*+\varepsilon\) becomes \(\phi(z)\le1+O_n(\varepsilon)\), uniformly in bounded \(z\), while the area Jacobian tends uniformly to one. Coercivity makes the scaled domains uniformly bounded. Their characteristic functions converge almost everywhere to \(1_{K_{A,B}}\); the boundary of this full-dimensional convex polytope has zero \(m\)-volume. Dominated convergence yields \(L^1\) convergence of the conditional densities (therefore total variation). Since the \(H_n\) local charts are congruent up to coordinate permutation and global sign, their masses are equal, giving the uniform minimizing-label law. The same chart bounds yield an \(O_n(\varepsilon)\) relative error in chart volume (the polytope has finite surface area), proving the stated \(O_n(\varepsilon^{m+1})\) remainder.

**4. Exact tangent-polytope volume and Dirichlet splitting.** For a centered \(p\)-vector \(x\) the region \(\max_i x_i\le s\) is the simplex obtained from \(y_i=s-x_i\ge0\) with \(\sum_i y_i=ps\). Its induced \((p-1)\)-volume is
\[
F_p(s)=\frac{\sqrt p\,p^{p-1}}{(p-1)!}\,s^{p-1},\qquad s\ge0.
\]
The same formula applies to the opposite block. For \(p=1\), read \(F_1(s)=1\) for \(s\ge0\) as zero-dimensional volume. Stieltjes convolution of \(dF_p\) and \(dF_q\) over \(s+t\le1\), or the beta integral for \(p,q\ge2\), gives
\[
\operatorname{Vol}_m(K_{A,B})
=\frac{p^{p-1/2}q^{q-1/2}}{(p+q-2)!}.
\]
The joint density of the two block maxima is proportional to \(s^{p-2}t^{q-2}\) on \(s,t\ge0,s+t\le1\), giving the stated Dirichlet law and the singleton convention. Homogeneity yields \(\Pr(\phi(V)\le r)=r^m\) for \(0\le r\le1\). Multiplying the tangent volume by the chart factor \((\sqrt2\varepsilon)^m\), summing \(H_n\) charts and dividing by sphere area \(\sigma_m\) proves \(C_n\).

**5. Sharp slope endpoints.** On the zero-sum subspace of \(p\) coordinates, for any nonzero \(x\),
\[
\frac{\|x\|}{\sqrt{p(p-1)}}\le\max_i x_i\le
\sqrt{\frac{p-1}{p}}\,\|x\|\qquad(p\ge2).
\]
The first follows because \(\max_i x_i\le s\) implies \(\|x\|^2\le p(p-1)s^2\), attained by one low coordinate and \(p-1\) equal high coordinates. The second is Cauchy–Schwarz against the projection of a coordinate vector to the zero-sum subspace, attained by one high coordinate and \(p-1\) equal low coordinates. Applying the two bounds to the independent block spaces shows that \(\min_{\|v\|=1}\phi(v)=1/\sqrt{b(b-1)}\) and \(\max_{\|v\|=1}\phi(v)=\sqrt{(a-1)/a+(b-1)/b}\). Zero-dimensional singleton blocks contribute zero. Since the spherical angle of \(\Psi(rv)\) to \(u_0\) is \(\arctan r\), the linear coefficient for width is \(\phi(v)/\sqrt2\). This proves both globally sharp local slopes.

## Verification
The standalone `verify.py` checks the exact values for \(n=3,4,5\), computes the exact near-minimum triangle distribution, evaluates the nonlinear tetrahedral spherical area by independent quadrature, and tests the precise nonlinear chart and both sharp slope bounds for random tangent directions in dimensions corresponding to \(3\le n\le10\). It reports `ALL_CHECKS_PASSED` when executed with Python, NumPy and SciPy. These finite calculations support but do not replace the analytic proof. In particular, the tangent-polytope volume formula and all-dimensional limit follow from Steps 2–4, not from an extrapolation of samples.

## Relationship to prior work
Har-Peled and Robson establish the exact minimum width of a regular simplex and classify balanced two-level minimizing directions. Kabluchko, Litvak and Zaporozhets study random projection widths of regular polytopes through Gaussian ranges, with moment and high-dimensional results. Classical work on the internally studentized Gaussian sample range provides scalar distribution information under a deterministic rescaling; consequently the mere existence of the marginal width distribution is **not** claimed as new. The present contribution is the fixed-dimensional **joint conditional angular blow-up law**, its explicit product-simplex/Dirichlet structure, the induced sharp rare-orientation coefficient, and the extremal local angular slopes. A scalar CDF alone does not specify the distribution of the tangent-coordinate vector conditional on a near-minimal range.

## Limitations
The results require an exactly regular simplex, Haar-uniform directions and fixed dimension before the small-excess limit. They do not establish analogous laws for perturbed simplices, other polytopes, or a joint large-dimension/small-excess regime. The leading scalar tail is related to classical internally studentized-range distributions; historical priority for all possible equivalent angular refinements is not exhaustive. The complete text of a potentially relevant 1954 statistics article could not be inspected, although its bibliographic identification and later discussion were available.

## References
- S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616, first public version January 6, 2023. https://arxiv.org/abs/2301.02616
- Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, first version November 26, 2015. https://arxiv.org/abs/1511.08479
- H. A. David, H. O. Hartley and E. S. Pearson, *The Distribution of the Ratio, in a Single Normal Sample, of Range to Standard Deviation*, Biometrika 41 (1954), 482–493. DOI:10.1093/biomet/41.3-4.482.
- D. F. Ferreira, L. M. Chaves and D. J. de Souza, *The Theory of the Internally Studentized Range Distribution Revisited*, Brazilian Journal of Biometrics 36 (2018), 802–826. DOI:10.28951/rbb.v36i4.308.
