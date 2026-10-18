# Higher-degree Hermite limits for endpoint norms of product-measure polynomial projections

## Finding
Fix \(k\ge3\). Let \(\mu\) be a compactly supported nondegenerate probability measure on the real line with at least \(k+1\) distinct support points, mean \(m\), variance \(v\), and maximal centered support radius \(B=\max_{x\in\operatorname{supp}\mu}|x-m|\). Let \(P_{d,k}\) denote the exact continuous \(L^2(\mu^{\otimes d})\)-orthogonal projection onto total-degree-at-most-\(k\) real polynomials on the product support. If \(H_k\) is the probabilists' Hermite polynomial and \(Z\sim N(0,1)\), then

\[
\lim_{d\to\infty}\frac{\|P_{d,k}\|_{L^\infty\to L^\infty}}{d^{k/2}}
=\lim_{d\to\infty}\frac{\|P_{d,k}\|_{L^1\to L^1}}{d^{k/2}}
=\frac{B^k}{v^{k/2}k!}\,\mathbb E|H_k(Z)|.
\]

The two endpoint norms coincide for each finite \(d\). More precisely, for any sequence \(x^{(d)}\) of points of the product support, its pointwise Lebesgue function is asymptotically maximal if and only if

\[
\frac1d\sum_{i=1}^d(x_i^{(d)}-m)^2\longrightarrow B^2.
\]

For example, the standard uniform probability on \([-1,1]\) gives the leading coefficient \(3^{k/2}\mathbb E|H_k(Z)|/k!\), and the arcsine probability gives \(2^{k/2}\mathbb E|H_k(Z)|/k!\). At degree three these are approximately \(1.307710\) and \(0.711827\), respectively; at degree four they are approximately \(1.050225\) and \(0.466767\).

## Assumptions and scope
The polynomial degree \(k\) and one-dimensional law \(\mu\) remain fixed while the number of coordinates \(d\) tends to infinity. The support need not be an interval, symmetric or absolutely continuous; atomic and asymmetric measures are permitted. The lower bound of \(k+1\) distinct support points guarantees orthonormal polynomial degrees \(0,1,\ldots,k\). There is no assertion uniform over varying \(k\), over varying marginal laws, or for unbounded supports. Endpoint norms are measured against the product probability, not counting measure, discrete cubature or an empirical least-squares design. An asymptotically maximal evaluation sequence means the ratio of its Lebesgue function to the global operator norm tends to one.

## Proof
Choose real orthonormal one-dimensional polynomials \(\phi_0,\ldots,\phi_k\) in \(L^2(\mu)\), normalized so \(\phi_0=1\), \(\phi_1(x)=(x-m)/\sqrt v\). For multi-indices \(\alpha\in\mathbb N_0^d\) with \(|\alpha|\le k\), the tensor products \(\Phi_\alpha(x)=\prod_i\phi_{\alpha_i}(x_i)\) form an orthonormal basis of the target polynomial space. Thus the reproducing kernel is

\[
K_{d,k}(x,y)=\sum_{|\alpha|\le k}\Phi_\alpha(x)\Phi_\alpha(y).
\]

Separate the terms of support size exactly \(k\), necessarily the multi-indices with \(k\) distinct entries equal to one. Put \(a_i=\phi_1(x_i)\), \(Z_i=\phi_1(Y_i)\) for independent \(Y_i\sim\mu\). The leading term is the elementary symmetric polynomial

\[
E_{d,k}(x,Y)=\sum_{1\le i_1<\cdots<i_k\le d}\prod_{j=1}^k a_{i_j}Z_{i_j}.
\]

Every omitted tensor basis term involves at most \(k-1\) coordinates. As the \(\phi_j\) are bounded on compact support, there are \(O_k(d^{k-1})\) such terms and their coefficients at \(x\) are uniformly bounded. Orthogonality in \(Y\) gives

\[
\sup_x\|K_{d,k}(x,\cdot)-E_{d,k}(x,\cdot)\|_{L^2(\mu^{\otimes d})}=O_{k,\mu}(d^{(k-1)/2}).
\]

The same bound holds in \(L^1\). It suffices to analyze the square-free term at scale \(d^{k/2}\).

For a sequence \(x=x^{(d)}\), set \(R_d^2=\sum_i a_i^2\). First assume \(R_d^2/d\to\rho>0\), and write \(U_i=a_iZ_i/R_d\). The bounded triangular-array central limit theorem yields \(p_1=\sum_i U_i\Rightarrow Z\). Also \(p_2=\sum_i U_i^2\to1\) in \(L^2\), because its mean is one and its variance is \(O(d^{-1})\). For each fixed \(j\ge3\), boundedness implies \(p_j=\sum_iU_i^j\to0\) deterministically in absolute value at rate \(O(d^{1-j/2})\). Newton's identities, equivalently the formal generating identity

\[
\sum_{j\ge0}e_j(U)t^j=\exp\left(\sum_{r\ge1}\frac{(-1)^{r-1}}{r}p_rt^r\right),
\]

show that \(e_k(U)\Rightarrow H_k(Z)/k!\), using the generating identity \(\exp(tZ-t^2/2)=\sum_{j\ge0}H_j(Z)t^j/j!\). Moreover independence and centering imply

\[
\mathbb E|e_k(U)|^2=\frac{e_k(a_1^2,\ldots,a_d^2)}{R_d^{2k}}\le\frac1{k!}.
\]

Hence the absolute values are uniformly integrable and

\[
\frac{\mathbb E|E_{d,k}(x,Y)|}{d^{k/2}}\longrightarrow\frac{\rho^{k/2}}{k!}\mathbb E|H_k(Z)|.
\]

If instead \(R_d^2/d\to0\), the direct inequality \(\mathbb E|E_{d,k}|\le R_d^k/\sqrt{k!}\) gives a zero limit. Every sequence admits subsequences along which \(R_d^2/d\) converges in the compact interval \([0,B^2/v]\); applying the preceding alternatives proves the sharp upper limit. Taking every coordinate equal to a farthest support point attains the lower limit and proves the formula. The same subsequence argument proves the claimed characterization of all asymptotic maximizing evaluation sequences because \(\rho^{k/2}\) is strictly increasing for \(\rho\ge0\).

Finally, a symmetric finite-rank integral kernel has equal \(L^1\) and \(L^\infty\) operator norms. The latter is \(\max_{x\in(\operatorname{supp}\mu)^d}\int|K_{d,k}(x,y)|\,d\mu^{\otimes d}(y)\), since the kernel is continuous on compact product support; consequently both endpoint limits follow.

## Verification
The bundled stand-alone script `projection_checker.py` constructs orthonormal polynomial bases for the uniform and arcsine distributions, and uses weighted QR for an asymmetric discrete five-atom law. For degrees three and four and coordinate counts two, three and four, it compares a direct multi-index kernel sum to an independent total-degree coefficient recursion, producing 1,281 finite kernel comparison assertions. Its quadrature for \(\mathbb E|H_k(Z)|\) integrates separately between the real Hermite roots. Monte Carlo evaluations of the sharp corner Lebesgue function in dimensions 80, 180 and 400 illustrate the predicted constants; these finite tests do not establish the limits or the extremizer criterion.

## Relationship to prior work
Cohen, Davenport and Leviatan (2011 preprint, 2013 journal publication) study stability of least-squares approximation and a basis-dependent diagonal kernel bound. Zhou, Narayan and Xu (2014) provide multivariate polynomial approximation constructions. Bialas-Ciez, Kenne, Sommariva and Vianello (2023 preprint) rigorously estimate projector Lebesgue constants on fixed geometric domains by polynomial meshes. Minabutdinov (2015) develops Krawtchouk-to-Hermite asymptotics for a related discrete orthogonal-polynomial family; this supplies a classical analogous limit but not the stated arbitrary-marginal product-projection operator norm and asymptotic maximizing locus. The 2014 study of hyperinterpolation operator norms on a cube concerns discrete cubature and mainly growth in approximation degree at fixed spatial dimension. A related quadratic product-measure projector theorem covers only \(k=2\), in a symmetric setting, whereas the present claim is restricted to all fixed \(k\ge3\) and covers asymmetric or atomic product measures. All new conclusions have been derived here independently from the stated kernel formula; no claim is made that the Hermite or central-limit ingredients themselves are new.

## Limitations
The theorem determines only the leading order as \(d\to\infty\) with fixed \(k\), not an exact finite-dimensional norm, a second asymptotic term, or a uniform statement for growing degree. It concerns continuous orthogonal projection rather than random sampled least squares or cubature hyperinterpolation. Some relevant historical full texts were inaccessible; a previously published equivalent theorem under Krawtchouk, chaos-projection or Lebesgue-constant terminology remains possible. Independent bibliographic and proof validation have not been performed.

## References
1. A. Cohen, M. A. Davenport, D. Leviatan, *On the stability and accuracy of least squares approximations*, first public preprint 2011-11-18, arXiv:1111.4422; *Foundations of Computational Mathematics* 13 (2013), 819–834.
2. T. Zhou, A. Narayan, Z. Xu, *Multivariate discrete least-squares approximations with a new type of collocation grid*, arXiv:1401.0894 (2014).
3. L. Bialas-Ciez, D. J. Kenne, A. Sommariva, M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex, and ball*, arXiv:2311.18656 (2023), *Electronic Transactions on Numerical Analysis* 60 (2024).
4. A. Minabutdinov, *The higher order asymptotic expansion of the Krawtchouk polynomials*, arXiv:1508.07421 (2015).
5. *On the norm of the hyperinterpolation operator on the d-dimensional cube*, *Computers & Mathematics with Applications* (2014), doi:10.1016/j.camwa.2014.07.009 (abstract consulted; full-text comparison incomplete).
