# Sharp finite distance-moment tomography of solid Euclidean ellipsoids

## Finding
For every integer \(d\ge 2\), let \(E\subset\mathbb R^d\) be a filled, nondegenerate Euclidean ellipsoid with unknown positive semiaxes \(a_1,\ldots,a_d\). Choose \(X,Y\) independently from normalized volume measure on \(E\), and write \(\mu_k=\mathbb E\|X-Y\|^{2k}\), with \(\mu_0=1\).

Set \(b_{d,0}=1\), and for \(1\le k\le d\), define the positive rational normalization constants
\[
b_{d,k}=b_{d,k-1}\frac{2(d+2k-1)(d+2k-2)}{(d+2k)(d+k)}.
\]
With the rising factorial \((q)_k=q(q+1)\cdots(q+k-1)\), put
\[
c_k=\frac{(d/2)_k}{k!}\frac{\mu_k}{b_{d,k}},\qquad c_0=1.
\]
Then the following identity holds exactly, including all multiplicities:
\[
\boxed{\left[\left(1+\sum_{k=1}^d c_k t^k\right)^{-2}\right]_{\le d}=\prod_{i=1}^d(1-a_i^2t).}
\]
Here \( [F(t)]_{\le d} \) denotes truncation of a formal series at degree \(d\). Thus the first \(d\) positive even distance moments determine the unordered semiaxes, with no volume, center, or orientation supplied in advance. For example, in dimension \(3\), the moments \(\mu_1=14/5\), \(\mu_2=312/25\), \(\mu_3=12864/175\) recover the squared semiaxes \(1,2,4\), because the recovered polynomial is \(1-7t+14t^2-8t^3\).

The number \(d\) is generically necessary: at every ellipsoid with pairwise distinct semiaxes, there are arbitrarily close noncongruent ellipsoids with the same \(\mu_1,\ldots,\mu_{d-1}\).

The inverse has a sharp global stability exponent. Given \(0<\alpha<\beta<\infty\), there is a constant \(C=C(d,\alpha,\beta)\) such that any two such ellipsoids whose squared semiaxes lie in \([\alpha,\beta]\) satisfy
\[
\boxed{\min_{\pi\in S_d}\max_i |a_i^2-\widetilde a_{\pi(i)}^2|\le C\left(\max_{1\le k\le d}|\mu_k-\widetilde\mu_k|\right)^{1/d}.}
\]
No larger uniform Hölder exponent is valid on any neighborhood of any Euclidean ball with squared radius strictly between \(\alpha\) and \(\beta\).

## Assumptions and scope
The ellipsoid is a translated and rotated image of \(\operatorname{diag}(a_1,\ldots,a_d)B_d\), where \(B_d\) is the Euclidean unit ball. Sampling is independent and uniform with respect to \(d\)-dimensional volume, not surface measure. Moments are exact population moments. The reconstruction determines the unordered semiaxes only: distances cannot determine the ellipsoid's location or orientation. The stability statement uses squared semiaxes and the maximum difference of the \(d\) listed raw moments; its constant is allowed to depend on the dimensional and semiaxis bounds.

## Proof
**1. Dimension-only radial normalizations.** Let \(U,V\) be independent and volume-uniform on \(B_d\). Their difference \(Z=U-V\) is spherically symmetric, hence \(Z=R\Theta\), with \(\Theta\) Haar-uniform on the unit sphere and independent of \(R\). Write \(\kappa_j\) for the unit \(j\)-ball volume. At separation \(r\in[0,2]\), two unit balls overlap in volume
\[
H_d(r)=2\kappa_{d-1}\int_{r/2}^{1}(1-u^2)^{(d-1)/2}\,du.
\]
The density of \(Z\) equals \(H_d(\|z\|)/\kappa_d^2\). Polar integration and reversing the integration order give
\[
\begin{aligned}
\mathbb ER^{2k}&=\frac{d}{\kappa_d}\int_0^2r^{d+2k-1}H_d(r)\,dr\\
&=\frac{d\,2^{d+2k}\Gamma(d/2+1)\Gamma((d+2k+1)/2)}{(d+2k)\sqrt\pi\,\Gamma(d+k+1)}.
\end{aligned}
\]
At \(k=0\) this equals \(1\). Taking consecutive ratios yields exactly the stated recursion for \(b_{d,k}=\mathbb ER^{2k}>0\).

**2. Angular generating identity.** By an orthogonal change of variables, \(X-Y\) has the same length distribution as \(\operatorname{diag}(a_1,\ldots,a_d)Z\). Put \(s_i=a_i^2\) and \(Q=\sum_i s_i\Theta_i^2\). Then \(\mu_k=b_{d,k}\mathbb E Q^k\). The squared coordinates \((\Theta_1^2,\ldots,\Theta_d^2)\) follow the Dirichlet distribution with all parameters \(1/2\). Their monomial moments give
\[
\mathbb EQ^k=\frac{k!}{(d/2)_k}\sum_{j_1+\cdots+j_d=k}\prod_{i=1}^d\frac{(1/2)_{j_i}s_i^{j_i}}{j_i!}.
\]
Consequently, as a formal power series,
\[
1+\sum_{k\ge1}\frac{(d/2)_k}{k!}\frac{\mu_k}{b_{d,k}}t^k=\prod_{i=1}^d(1-s_it)^{-1/2}.
\]
Squaring the reciprocal and retaining degrees at most \(d\) yields the boxed polynomial identity. Its \(d\) reciprocal roots are exactly \(s_i\), including repeated roots. Translation and rotation cancel from all distances.

**3. Minimality.** For distinct \(s_i>0\), the monic polynomial \(p(z)=\prod_i(z-s_i)\) has simple positive real roots. For every sufficiently small nonzero real \(\varepsilon\), the polynomial \(p(z)+\varepsilon\) still has \(d\) simple positive real roots by the implicit-function theorem at each simple root. The two polynomials differ only in their constant term. Thus they have identical first \(d-1\) elementary symmetric functions of their root multisets. The formal-series identity in step 2, applied in reverse, implies equality of \(\mu_1,\ldots,\mu_{d-1}\). Their constant coefficients differ, so the semiaxis multisets are distinct. The roots vary continuously, giving arbitrarily close examples at every distinct-axis ellipsoid.

**4. Uniform stability.** On the compact range \(s_i\in[\alpha,\beta]\), the reciprocal-square series coefficients through degree \(d\) depend polynomially on the first \(d\) normalized moments. Therefore the coefficients of two monic characteristic polynomials \(p(z)=\prod(z-s_i)\) and \(\widetilde p(z)=\prod(z-\widetilde s_i)\) differ by at most \(C_0\delta\), where \(\delta=\max_{1\le k\le d}|\mu_k-\widetilde\mu_k|\). For small \(\delta>0\), put \(r=(2C_1\delta)^{1/d}\), with \(C_1\) chosen so that \(|p(z)-\widetilde p(z)|<r^d\) throughout \(|z|\le\beta+1\). Form the union of closed complex disks of radius \(r\) centered at all roots of \(p\). Every point on the boundary of each connected component has distance at least \(r\) from every root of \(p\), so \(|p(z)|\ge r^d\) there. Rouché's theorem gives the same number of zeros of \(p\) and \(\widetilde p\) in each component, counting multiplicity. A component contains at most \(d\) overlapping disks and has diameter at most \(2dr\). The positive real roots can therefore be matched, with multiplicity, at distance at most \(2dr\). A larger constant handles non-small \(\delta\) using the fixed compact range. This proves the uniform \(1/d\)-Hölder bound.

**5. Optimal exponent.** Choose distinct real numbers \(v_1,\ldots,v_d\), and a sufficiently small fixed nonzero \(\varepsilon\) so that \(\prod(z-v_i)+\varepsilon\) still has distinct real roots \(w_1,\ldots,w_d\). Their two monic polynomials differ only in the constant term. Fix any \(s_0\in(\alpha,\beta)\). For \(h>0\) small, take the two sets of squared semiaxes \(s_0+hv_i\) and \(s_0+hw_i\). Their moments through order \(d-1\) agree *exactly*, while the difference of the \(d\)-th moments is a nonzero constant times \(h^d\) by step 2. Their optimally matched squared semiaxes differ by a positive constant times \(h\). An estimate with Hölder exponent greater than \(1/d\) would imply \(h=O(h^{d\gamma})\), which is impossible as \(h\downarrow0\) when \(\gamma>1/d\). These examples approach the ball with squared radius \(s_0\).

## Verification
The accompanying standalone rational-arithmetic program independently expands \(\mathbb E\|X-Y\|^{2k}\) from Cartesian moments of two independent uniform-ball points; it does not use the radial/Dirichlet factorization to compute the left-hand side. For dimensions \(2\) through \(5\), it checks all \(k=1,\ldots,d\) against the factorized formula, then checks exact polynomial inversion for unequal and equal semiaxes. It also checks the first two radial normalizations for dimensions \(2\) through \(8\). The program reports `ALL_CHECKS_PASSED`. These finite exact checks support—but do not replace—the all-dimensional proof and do not establish novelty or statistical robustness.

## Relationship to prior work
Bonnet, Gusakova, Thäle and Zaporozhets (2020, first public version) develop sharp mean-distance inequalities for general convex bodies and record a classical integral formula for the *first* distance moment of an ellipsoid. Ohanyan and Khalatyan (2022) derive a general forward relation between the covariogram and distance distributions and give examples for disks, balls and triangles. Hillier (2001) gives a density theory for spherical quadratic forms, the angular random variable used here. These are important analytical antecedents; the Dirichlet moment expansion is classical. The statement assessed here is the exact minimum finite set of **unoriented pair-distance** moments, the reconstruction polynomial, and its optimal inverse Hölder exponent. A published theorem on recovering ellipsoid axes from reciprocal central-section-volume moments uses the **same Dirichlet generating product**, but measures a different random variable; the determinant-dependent conversion between that measurement and raw pair-distance moments is not supplied by the data. The same algebraic mechanism is not claimed as a new general identity.

## Limitations
No claim is made for arbitrary convex bodies, surface-uniform samples, finite noisy samples, or recovering ellipsoid centers/orientations. The stability constant is not optimized. Exact population moments rather than finite-sample estimates are assumed. The strongest historical-priority uncertainty concerns classical spherical-quadratic-form density theory and related moment identities; the 2001 full article could not be inspected in this assessment. Independent external review has not occurred.

## References
1. G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, initial arXiv submission 2020-10-07, arXiv:2010.03351, https://arxiv.org/abs/2010.03351 .
2. V. K. Ohanyan and V. H. Khalatyan, *Relation between the covariogram and distribution function of the distance between two uniform and independent points*, 2022, DOI:10.46991/PYSU:A/2022.56.1.033, https://doi.org/10.46991/PYSU:A/2022.56.1.033 .
3. G. Hillier, *The density of a quadratic form in a vector uniformly distributed on the n-sphere*, 2001, DOI:10.1017/S026646660117101X, https://doi.org/10.1017/S026646660117101X .
