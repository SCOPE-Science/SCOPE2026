# Rare-corner extremality and exact endpoint stability of first-order Bernoulli ANOVA projection

## Finding
Let \(n\ge1\), let \(X=(X_1,\ldots,X_n)\) have independent Bernoulli coordinates with arbitrary \(0<p_i<1\), and let \(P\) be the \(L^2\)-orthogonal projection onto all real affine functions of the coordinates, equivalently the order-at-most-one Hoeffding/ANOVA projection. Set \(r_i=\min\{p_i,1-p_i\}\). Let \(Y_i\) be independent Bernoulli variables with success probabilities \(r_i\). Then the exact attained endpoint norm is
\[
\boxed{\|P\|_{L^\infty\to L^\infty}=\mathbb E\left|\sum_{i=1}^n\frac{Y_i}{r_i}-(n-1)\right|.}
\]
A maximizing evaluation point chooses, in every coordinate, the **less probable outcome**. Its sign-kernel function attains the norm. The largest possible undershoot of \(Pf\) over \(0\le f\le1\) and all evaluation points is exactly \((\|P\|-1)/2\); the same constant is the largest overshoot above \(1\).

The norm is nonincreasing when any \(r_i\) moves towards \(1/2\). Consequently the fair product measure minimizes it globally. Writing \(m=\lfloor n/2\rfloor\), its exact minimum is
\[
\boxed{\min_{0<p_i<1}\|P\|=\frac{(2m+1)\binom{2m}{m}}{4^m}.}
\]
In particular the fair-minimum norms at dimensions \(2m\) and \(2m+1\) coincide. For \(n\ge2\), the sharp supremum over all nondegenerate product biases is \(2n-1\), approached when all rare-outcome probabilities tend to zero but not attained in the open parameter cube.

For a common rare probability \(r\in(0,1/2]\), let \(B_j\sim\operatorname{Bin}(j,r)\) and \(k=\lceil(n-1)r\rceil-1\). With the convention \(\Pr(B_j\le-1)=0\), an equivalent exact formula is
\[
\boxed{\|P\|=1+2\left[(n-1)\Pr(B_n\le k)-n\Pr(B_{n-1}\le k-1)\right].}
\]
At fixed \(r\) and \(n\to\infty\), \(\|P\|\sim\sqrt{2n(1-r)/(\pi r)}\). In the rare-event scaling \(r=\lambda/n\) with fixed \(\lambda>0\),
\[
\boxed{\lim_{n\to\infty}\frac{\|P\|}{n}=2e^{-\lambda}\frac{\lambda^{\lceil\lambda\rceil-1}}{(\lceil\lambda\rceil-1)!}.}
\]
The Poisson profile is continuous and strictly decreasing, piecewise smooth, and has a corner at each positive integer.

## Assumptions and scope
All coordinates and functions are real. Every Bernoulli probability lies strictly between zero and one; hence the product measure has full support. The \(L^\infty\) norm is the maximum over vertices. Coordinate outcome labels may be independently reversed without affecting the norm, permitting \(r_i\le1/2\) throughout. The projection \(P\) includes the constant term as well as all first-order terms; it is **not** the projection onto the homogeneous first chaos alone. All formulas, including boundary conventions, apply to \(n=1\). The Poisson limit uses fixed positive \(\lambda\) and sufficiently large \(n\) so that \(\lambda/n\le1/2\).

## Proof
**Projection kernel.** After flipping each coordinate if needed, write \(\Pr(Y_i=1)=r_i\le1/2\). The mutually orthonormal affine basis consists of \(1\) and \(\phi_i(y)=(y_i-r_i)/\sqrt{r_i(1-r_i)}\). Thus, for every vertex \(x\),
\[
(Pf)(x)=\mathbb E[K_x(Y)f(Y)],\qquad K_x(y)=1+\sum_i\frac{(x_i-r_i)(y_i-r_i)}{r_i(1-r_i)}.
\]
The row norm is exactly \(\mathbb E|K_x(Y)|\), attained by \(f(y)=\operatorname{sgn}K_x(y)\), so maximizing over \(x\) gives the operator norm.

**Convex-order comparison.** If \(x_i=1\), its centered contribution to \(K_x\) is \(U_i=Y_i/r_i-1\); if \(x_i=0\), it is \(V_i=(r_i-Y_i)/(1-r_i)\). Both have mean zero and lower support endpoint \(-1\). Their upper support endpoints are \((1-r_i)/r_i\) and \(r_i/(1-r_i)\), respectively, in decreasing order. For any convex function \(\Phi\), the expectation under the mean-zero two-point law on \(\{-1,b\}\) is
\[
\frac{b\Phi(-1)+\Phi(b)}{1+b},
\]
which is nondecreasing as \(b\) grows: it is the secant interpolation of \(\Phi\) at zero, and convex secant slopes can only increase as the right endpoint expands. Hence \(V_i\preceq_{\mathrm{cx}}U_i\). Adding an independent summand preserves convex order. Replacing each \(V_i\) by an independent \(U_i\) therefore cannot decrease the expectation of \(\Phi(t)=|1+t|\). All row norms are at most the row with \(x_i=1\) for every \(i\). At this rare corner, \(K_x(Y)=\sum_iY_i/r_i-(n-1)\), proving the exact norm and attaining signs.

**Positive-input defect.** Every row integrates to \(1\), so its negative kernel mass equals \((\mathbb E|K_x|-1)/2\). Choosing \(f=1_{\{K_x<0\}}\) attains the smallest value of \(Pf(x)\) among \(0\le f\le1\). Replacing \(f\) by \(1-f\), using \(P1=1\), gives the same sharp overshoot.

**Bias monotonicity and extrema.** For \(U(r)=Y/r-1\), where \(Y\sim\mathrm{Bernoulli}(r)\), its lower support endpoint remains \(-1\), while its upper endpoint \((1-r)/r\) decreases as \(r\) increases. The same secant argument proves \(U(r')\preceq_{\mathrm{cx}}U(r)\) whenever \(r\le r'\le1/2\). Apply the independent-sum property and \(\Phi(t)=|1+t|\); the norm is nonincreasing in each rare probability and is minimized at the fair product. Moreover, the rare-corner kernel is bounded below by \(-(n-1)\), so its negative mass is at most \(n-1\) and \(\|P\|\le2n-1\). If \(n\ge2\) and all probabilities are strictly positive, there is positive probability of a nonnegative kernel, and the bound is strict. On the all-zero event, whose probability tends to one as all \(r_i\to0\), the kernel equals \(-(n-1)\). Therefore the norm tends to \(2n-1\). For \(n=1\), \(P\) is the identity.

**Fair-product parity identity.** When every \(r_i=1/2\), the rare-corner kernel is \(1+\sum_i\varepsilon_i\) with independent fair signs. Put \(Z=\sum_{i=1}^{2m}\varepsilon_i\). The symmetric integer-valued \(Z\) is even, so
\[
\mathbb E|Z+1|=\mathbb E|Z|+\Pr(Z=0),\quad
\mathbb E|Z+2|=\mathbb E|Z|+2\Pr(Z=0).
\]
Conditioning on the last sign shows \(\mathbb E|Z+1+\varepsilon|=\mathbb E|Z+1|\). Finally \(\mathbb E|Z|=2m\binom{2m}{m}/4^m\) and \(\Pr(Z=0)=\binom{2m}{m}/4^m\), giving the displayed minimum in both dimensions \(2m\) and \(2m+1\). The case \(m=0\) is immediate.

**Homogeneous and asymptotic formulas.** If \(Y_i\) have common success probability \(r\), set \(B_n=\sum_iY_i\), so \(K=B_n/r-(n-1)\) with \(\mathbb EK=1\). Therefore \(\mathbb E|K|=1+2\mathbb E[((n-1)-B_n/r)_+]\). With \(k\) as defined above, \(\mathbb E[B_n1_{\{B_n\le k\}}]=nr\Pr(B_{n-1}\le k-1)\); substitution proves the binomial-tail formula, including integer thresholds. For fixed \(r\), the centered binomial central limit theorem and uniform integrability (bounded normalized second moments) yield the square-root asymptotic. If \(r=\lambda/n\), the binomial count converges to a Poisson variable \(N_\lambda\) of mean \(\lambda\), with uniformly bounded second moments. Consequently \(\|P\|/n\to\mathbb E|N_\lambda/\lambda-1|\). With \(k=\lceil\lambda\rceil-1\), the identity \(\mathbb E[N_\lambda1_{\{N_\lambda\le k\}}]=\lambda\Pr(N_\lambda\le k-1)\) reduces this to \(2\Pr(N_\lambda=k)\), as claimed. On each interval \((j,j+1]\) the profile is \(2e^{-\lambda}\lambda^j/j!\), strictly decreasing there. At each positive integer, adjacent Poisson masses agree, so the profile is continuous; the one-sided derivatives differ, establishing the corners.

## Verification
The accompanying standalone program `verify_bernoulli_affine.py` uses exact rational arithmetic to enumerate finite product measures and independently compute projection-kernel row norms, sharp sign witnesses, positive-input undershoots, the direct conditional-expectation projection formula, fair-product parity identities and bias monotonicity samples. It also compares finite rare-event values with their Poisson limits as diagnostics. The program reported `PASS checks= 54049`; the explicit four-coordinate asymmetric profile yielded operator norm \(203/75\) and sharp positive-input undershoot \(-64/75\). These finite checks support but do not replace the all-dimensional proof or certify novelty.

## Relationship to prior work
The affine projection is the first Hoeffding/functional-ANOVA approximation, classically defined through conditional expectations; see Owen's treatment of best additive approximations. The uniform Boolean Fourier basis is standard (de Wolf, 2008), while Nayar (2014) studies biased first-level Fourier concentration and a different \(L^2\) approximation problem. Rzeszut and Wojciechowski (2019) study endpoint and \(L^p\) properties of Hoeffding projections on infinite products, rather than the finite, arbitrary-bias exact \(L^\infty\) norm and rare-corner extremizer here. The fair-weight exact identities are elementary consequences of binomial identities and are not asserted independently novel. The claimed contribution is the heterogeneous-bias maximization principle together with the resulting sharp stability, positivity and bias-comparison classification.

## Limitations
The formula is for product Bernoulli measures with full support and the orthogonal projection including constants and first-order functions; dependence, multinomial factors, higher-order ANOVA projections and alternate projection choices are not covered. The rare-corner row always maximizes but need not be the unique maximizing row. Monotonicity need not be strict in an individual bias parameter. The Poisson and Gaussian asymptotic regimes are separate scalings. A same-conclusion theorem hidden in earlier general projection or product-measure literature remains a possible originality risk; independent audit has not been performed.

## References
1. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1 (published 2008-09-25), DOI: 10.4086/toc.gs.2008.001, https://zesty2.cs.uchicago.edu/articles/gs001/gs001.pdf.
2. P. Nayar, *FKN Theorem on the biased cube*, Colloquium Mathematicum 137 (2014), 253–261, DOI: 10.4064/cm137-2-9, https://www.impan.pl/shop/en/publication/transaction/download/product/87851.
3. A. B. Owen, *The ANOVA decomposition of [0,1]^d*, Appendix A, especially Section A.4, https://artowen.su.domains/mc/A-anova.pdf.
4. M. Rzeszut and M. Wojciechowski, *Hoeffding decomposition in H1 spaces*, arXiv:1906.01405 (2019), https://arxiv.org/abs/1906.01405.
