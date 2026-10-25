# Third-order concentration of random cross-polytope hyperplane shadows

## Finding
Let \(d\ge 2\) be an integer and let
\[
C_d=\{x\in\mathbb R^d:\ \sum_{i=1}^d|x_i|\le 1\}.
\]
For a uniformly sampled unit vector \(U\in S^{d-1}\), let \(A_d(U)\) be the \((d-1)\)-dimensional volume of the orthogonal projection of \(C_d\) onto \(U^\perp\). Define the dimensionless normalized brightness
\[
B_d=\frac{(d-1)!}{2^{d-1}}A_d(U).
\]
Then, for every integer \(d\ge2\), with \(f(r)=\sqrt{1-r^2}+r\arcsin r\) on \([-1,1]\),
\[
\mathbb E B_d=\frac{\sqrt d\,\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},
\qquad
\mathbb E B_d^2=\frac{2}{\pi 2^d}\sum_{k=0}^d\binom dk f\left(1-\frac{2k}{d}\right).
\]
In particular the variance undergoes a third-order cancellation:
\[
\boxed{\lim_{d\to\infty}d^3\operatorname{Var}(B_d)=\frac1{3\pi}.}
\]
The constant is strictly positive. Equivalently, the coefficient of variation satisfies
\[
\frac{\sqrt{\operatorname{Var}(B_d)}}{\mathbb EB_d}
\sim\frac1{\sqrt6\,d^{3/2}}.
\]
For any fixed \(t\ge0\), the same formulas govern the normalized random increment in the volume of the convex hull of \(C_d\) and its translate by \(tU\):
\[
\frac{(d-1)!}{t\,2^{d-1}}
\left[\operatorname{vol}_d\bigl(\operatorname{conv}(C_d\cup(C_d+tU))\bigr)-\operatorname{vol}_d(C_d)\right]=B_d
\quad(t>0).
\]
This is an equivalent interpretation, not an additional independent result.

## Assumptions and scope
The direction \(U\) has normalized rotation-invariant probability measure on \(S^{d-1}\). All volumes use ordinary Euclidean Lebesgue measure in the stated subspace. Projection is orthogonal, not central section or line projection. The integers \(d\ge2\) are unrestricted; the limit takes \(d\) through integers. The cross-polytope has axial vertices \(\pm e_i\), so every facet has area \(\sqrt d/(d-1)!\), outward normal \(\sigma/\sqrt d\) for \(\sigma\in\{-1,1\}^d\), and there are \(2^d\) facets. All gamma functions have positive arguments. At \(r=\pm1\), the definition of \(f\) is its continuous value \(\pi/2\). The translation identity for \(t>0\) uses the same uniform unit direction.

## Proof
**1. Exact brightness reduction.** The orthogonal projections of the facets cover almost every interior point of the projected body exactly twice, counting multiplicity. Projection of a facet of area \(a\) and normal \(n\) has \((d-1)\)-volume \(a|\langle n,u\rangle|\). Therefore the Cauchy projection formula gives, for every unit \(u\),
\[
A_d(u)=\frac1{2(d-1)!}\sum_{\sigma\in\{-1,1\}^d}|\sigma\cdot u|
=\frac{2^{d-1}}{(d-1)!}\,\mathbb E_\varepsilon|\varepsilon\cdot u|,
\]
where \(\varepsilon\) is a vector of independent fair signs. Thus \(B_d(U)=\mathbb E_\varepsilon|\varepsilon\cdot U|\).

**2. Exact first moment.** Each sign vector has Euclidean norm \(\sqrt d\). By spherical rotational invariance, for every such vector \(\sigma\), \(\sigma\cdot U\) has the distribution of \(\sqrt d\,U_1\). The spherical beta integral is
\[
\mathbb E|U_1|=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
Averaging first in \(U\), then in the signs yields the stated mean.

**3. Exact second moment.** Introduce independent sign vectors \(\sigma,\tau\). Their normalized inner product is \(r=(\sigma\cdot\tau)/d=1-2K/d\) with \(K\sim\operatorname{Binomial}(d,1/2)\). If \(G\) is a standard Gaussian vector in \(\mathbb R^d\), write \(G=RU\), where \(R^2\) is chi-squared with \(d\) degrees of freedom, independent of \(U\). For unit vectors \(a,b\) with dot product \(r\), the bivariate standard Gaussian absolute-product identity is
\[
\mathbb E|G\cdot a|\,|G\cdot b|=\frac2\pi\bigl(\sqrt{1-r^2}+r\arcsin r\bigr)=\frac2\pi f(r).
\]
It follows either by direct bivariate integration or by integrating the derivative \(\frac2\pi\arcsin r\) of the absolute-product expectation from \(r=0\). As \(\mathbb E R^2=d\), the corresponding spherical expectation is \(2f(r)/(\pi d)\). Apply it to \(\sigma/\sqrt d,\tau/\sqrt d\), multiply by \(d\), and average over the binomial law of \(K\). This proves the exact second-moment formula, including \(r=\pm1\) by continuity.

**4. Sharp third-order cancellation.** Set \(R_d=d^{-1}\sum_{j=1}^d\xi_j\) with independent symmetric signs \(\xi_j\). Direct counting of partitions of \(2,4,6\) indices into even-multiplicity blocks gives
\[
\mathbb ER_d^2=\frac1d,\quad
\mathbb ER_d^4=\frac3{d^2}-\frac2{d^3},\quad
\mathbb ER_d^6=\frac{15}{d^3}-\frac{30}{d^4}+\frac{16}{d^5}.
\]
Also \(\mathbb ER_d^8=O(d^{-4})\), and Hoeffding's bound implies \(\Pr(|R_d|>1/2)\le2e^{-d/8}\). Since
\[
f(r)=1+\frac{r^2}2+\frac{r^4}{24}+\frac{r^6}{80}+O(r^8)
\]
uniformly on \([-1/2,1/2]\), while \(f\) is bounded on \([-1,1]\), the second moment becomes
\[
\mathbb EB_d^2=\frac2\pi\left(1+\frac1{2d}+\frac1{8d^2}+\frac5{48d^3}+O(d^{-4})\right).
\]
For the first moment, the Stirling expansion of the log-gamma ratio gives
\[
\log\!\left(\frac{\mathbb EB_d}{\sqrt{2/\pi}}\right)
=\frac1{4d}-\frac1{24d^3}+O(d^{-5}),
\]
hence
\[
(\mathbb EB_d)^2=\frac2\pi\left(1+\frac1{2d}+\frac1{8d^2}-\frac1{16d^3}+O(d^{-4})\right).
\]
Subtracting cancels the constant, first-order, and second-order terms. The third-order term is \((2/\pi)(5/48+1/16)=1/(3\pi)\). This proves the claimed limit and the coefficient of variation.

**5. Translation interpretation.** The convex hull of \(C_d\) and \(C_d+tU\) is the Minkowski sum \(C_d+[0,tU]\). Fiberwise integration along lines parallel to \(U\) shows its volume is \(\operatorname{vol}_d(C_d)+t A_d(U)\), for \(t\ge0\). Substitution establishes the equivalent increment identity.

## Verification
A self-contained Python program, `verify.py`, separately constructs actual planar shadows of the three-dimensional cross-polytope from its six projected vertices, compares their convex-hull areas with the facet-normal formula, checks exact Rademacher moment identities using integer arithmetic, verifies the two-dimensional moments analytically, and evaluates the exact finite-dimensional formula against the asymptotic coefficient. Run with `python3 verify.py` using Python's standard library; it prints numerical finite-dimensional diagnostics and a success count. These tests are neither exhaustive over directions nor proofs of the unbounded-dimensional statements. The algebraic and asymptotic arguments above supply those proofs.

## Relationship to prior work
The classical Cauchy projection identity and bivariate Gaussian absolute-product integral are used as inputs, not claimed as new. Horváth and Lángi (2013, arXiv:1302.6164) study volumes of convex hulls of translated congruent convex bodies, including the volume-increment identity. Kabluchko, Litvak and Zaporozhets (2015, arXiv:1511.08479) compute moments and limits of **line-projection widths** of regular polytopes, including cross-polytopes, which is a different random functional from hyperplane-projection \((d-1)\)-volume. Ivanov (arXiv:1808.09165) studies extremal volumes of lower-dimensional projections of cross-polytopes, including context for hyperplane extrema, but his results concern extrema rather than the spherical second moment or this sharp variance law.

The contribution assessed here is the explicit all-dimensional **spherical second moment of hyperplane brightness** and the sharp \(d^{-3}\) cancellation with coefficient \(1/(3\pi)\). A general second-moment surface-area identity could be specialized to recover the finite binomial formula; such an abstract identity alone does not give the evaluated third-order limit without additional computation. No claim is made that the exact formula or asymptotic could not have been derived in older projection-body literature.

## Limitations
The theorem concerns only the standard, equal-axis cross-polytope, uniformly random **hyperplane** normals, and first two moments. It does not provide a central limit theorem or an optimal concentration inequality for the whole distribution. The leading variance coefficient does not by itself establish a Gaussian fluctuation law. Independent historical-priority checking remains desirable, especially for older spherical second-moment and brightness studies. No independent audit is claimed.

## References
1. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies* (first public arXiv version 2013-02-25), arXiv:1302.6164, https://arxiv.org/abs/1302.6164.
2. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables* (first public arXiv version 2015-11-26), arXiv:1511.08479, https://arxiv.org/abs/1511.08479.
3. G. Ivanov, *On the volume of projections of the cross-polytope* (first public arXiv version 2018-08-28), arXiv:1808.09165, https://arxiv.org/abs/1808.09165.
