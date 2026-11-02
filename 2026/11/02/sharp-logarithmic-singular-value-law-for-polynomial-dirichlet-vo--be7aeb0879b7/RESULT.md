# Sharp logarithmic singular-value law for polynomial Dirichlet Volterra operators

## Finding
For every nonconstant finite Dirichlet polynomial \(g(s)=b_1+\sum_{k=2}^{N}b_k k^{-s}\), the associated Volterra operator \(T_g\) on the Hilbert space \(\mathscr H^2\) of square-summable Dirichlet coefficients is compact and has the sharp asymptotic law
\[
\lim_{n\to\infty}(\log n)s_n(T_g)=K_g:=\sup_{t\in\mathbb R}|g'(it)|>0.
\]
Here \(s_n\) denotes the decreasing positive singular values, counted with multiplicity. Equivalently, for \(N_g(\lambda)=\#\{n\ge1:s_n(T_g)>\lambda\}\),
\[
\lim_{\lambda\downarrow0}\lambda\log N_g(\lambda)=K_g.
\]
In particular \(T_g\) lies in no finite Schatten class. The constant is the supremum norm of the finite Dirichlet polynomial \(-g'\), not in general the sum of the coefficient magnitudes.

For the explicitly interacting symbol \(g(s)=2^{-s}+4^{-s}-8^{-s}\),
\[
K_g=\frac8{\sqrt3}\log2,
\]
whereas the sum of the absolute coefficients of \(-g'\) is \(6\log2\).

## Assumptions and scope
The complex Hilbert space \(\mathscr H^2\) consists of \(f(s)=\sum_{n\ge1}a_n n^{-s}\) with \(\|f\|_{\mathscr H^2}^2=\sum_{n\ge1}|a_n|^2\). All logarithms are natural. For a Dirichlet polynomial \(f\), define
\[
(T_gf)(s)=-\int_s^{+\infty}f(w)g'(w)\,dw,
\]
where integration follows a horizontal ray. The operator extends boundedly to the stated Hilbert space. Its symbol may contain a constant term, which contributes nothing; the hypothesis of at least one nonzero coefficient with index at least two ensures \(K_g>0\). The first-public motivating research source is dated October 15, 2026.

The class concerns finite Dirichlet symbols on the **unweighted Hilbert Hardy space**; no analogous constant is claimed for infinite symbols, weighted Bergman spaces, or non-Hilbert exponents.

## Proof
**1. Exact coefficient factorization.** Put
\[
h(s)=-g'(s)=\sum_{k=2}^{N}b_k(\log k)k^{-s}.
\]
Termwise integration for polynomials gives the coefficient identity
\[
(T_g f)_m=\frac1{\log m}\sum_{\substack{k\mid m\\2\le k\le N}}b_k(\log k)a_{m/k},\qquad m\ge2,
\]
with constant coefficient zero. Let \(M_h\) be multiplication by \(h\) and define the diagonal compact operator \(De_1=0\), \(De_m=(\log m)^{-1}e_m\) for \(m\ge2\), with \(e_m(s)=m^{-s}\). Then \(T_g=DM_h\) first on polynomials and, by boundedness, everywhere.

Let \(\mathcal P=\{p_1,\ldots,p_r\}\) be the finite set of primes dividing the indices \(k\ge2\) with \(b_k\ne0\); for a \(\mathcal P\)-smooth index \(k\), let \(\nu(k)\in\mathbb N_0^r\) be its exponent vector. Multiplication by \(h\) is unitarily the analytic-polynomial multiplier associated with
\[
H(z)=\sum_{k=2}^{N}b_k(\log k)z^{\nu(k)},\qquad z\in\mathbb T^r.
\]
The norm of this multiplier on the Hardy-polydisk Hilbert space equals \(\max_{z\in\mathbb T^r}|H(z)|\): the upper bound follows from the boundary integral model, while normalized interior point kernels approaching a maximizing boundary point give the reverse inequality. Density permits finite \(\mathcal P\)-smooth polynomial norming vectors. Unique prime factorization makes the numbers \(\log p_1,\ldots,\log p_r\) rationally independent; Kronecker density therefore yields
\[
\|M_h\|=\max_{z\in\mathbb T^r}|H(z)|=\sup_{t\in\mathbb R}|g'(it)|=K_g.
\]
Since the nonzero diagonal values of \(D\) decrease as \(1/\log2,1/\log3,\ldots\), its approximation numbers are \(s_n(D)=1/\log(n+1)\). The ideal inequality gives
\[
s_n(T_g)\le\frac{K_g}{\log(n+1)}.
\]
This also proves compactness of \(T_g\).

**2. Orthogonal finite-support fibers.** Fix \(\varepsilon\in(0,K_g)\). Select a finite \(\mathcal P\)-smooth Dirichlet polynomial \(F\) with \(\|F\|=1\) and \(\|hF\|>K_g-\varepsilon\). Write \(Q\ge2\) for the greatest index occurring in \(hF\). For every positive integer \(m\) coprime to \(P=\prod_{p\in\mathcal P}p\), set \(F_m(s)=m^{-s}F(s)\). The vectors \(F_m\) are mutually orthonormal: each natural number factors uniquely as a \(\mathcal P\)-smooth factor times a factor coprime to \(P\). The vectors \(T_gF_m\) are likewise mutually orthogonal, by the same factorization applied to the supports of \(hF_m\).

For \(X\ge1\), \(m\in[X,2X]\) with \((m,P)=1\), every output coefficient is multiplied by \(1/\log(mq)\) with \(2\le q\le Q\). Therefore
\[
\|T_gF_m\|\ge\frac{\|hF\|}{\log(2XQ)}\;>\;\frac{K_g-\varepsilon}{\log(2XQ)}.
\]
Elementary finite inclusion–exclusion shows that the number of such \(m\) is
\[
\delta_P X+O_P(1),\qquad \delta_P=\prod_{p\in\mathcal P}\left(1-\frac1p\right)>0.
\]
For all sufficiently large integers \(n\), choose \(X=C_Pn\), with \(C_P>1/\delta_P\), so at least \(n\) such fibers occur. On their \(n\)-dimensional orthonormal span, \(T_g\) has minimum norm at least \((K_g-\varepsilon)/\log(2C_PQn)\). The min–max characterization of singular values then implies
\[
s_n(T_g)\ge\frac{K_g-\varepsilon}{\log(2C_PQn)}.
\]
Taking the logarithmically scaled lower limit and then \(\varepsilon\downarrow0\), together with the upper bound, proves the first boxed limit.

**3. Counting inversion and example.** Monotonicity of singular values and \(s_n\sim K_g/\log n\) give for every fixed \(\varepsilon>0\) and small \(\lambda>0\) exponential upper and lower bounds of the form \(\exp((K_g\pm\varepsilon)/\lambda)\) for \(N_g(\lambda)\), up to harmless integer factors. Hence \(\lambda\log N_g(\lambda)\to K_g\), and divergence of \(\sum_n (\log n)^{-p}\) for every finite \(p>0\) excludes all finite Schatten classes.

For \(g(s)=2^{-s}+4^{-s}-8^{-s}\), the boundary multiplier is \((\log2)(z+2z^2-3z^3)\) on the unit circle. Writing \(c=\cos\theta\), its squared modulus divided by \((\log2)^2\) equals \(20-8c-12c^2\). This concave quadratic has unique maximum \(64/3\) at \(c=-1/3\), yielding \(K_g=(8/\sqrt3)\log2\).

## Verification
The supplementary standalone script `verify.py` checks the exact coefficient factorization on random complex polynomials, the explicit one-term singular spectrum against finite-matrix SVD, the extremal quadratic example, and orthogonality and norm inequalities for concrete finite-support fibers. It passed **10,046 finite assertions** using Python and NumPy. These finite consistency checks are not proofs of the infinite-dimensional limit; the proof is the preceding analytic min–max argument. To reproduce, run `python verify.py` with Python 3.9+ and NumPy 1.20+.

## Relationship to prior work
Brevig–Perfekt–Seip (2016 preprint; later published) established the Hardy-space Volterra framework, including compactness for polynomial symbols and a non-Schatten result, without the asserted sharp logarithmic coefficient. Bommier-Hato (2020) and Gómez-Cabello–Lefèvre–Queffélec (2024) treat weighted Bergman analogues and Schatten properties but do not state the present unweighted \(\mathscr H^2\) exact singular-value limit. Tong–Wang–Yuan (October 15, 2026) establish the complementary BMOA Dirichlet-series boundedness/compactness theory; their results do not imply this \(\mathscr H^2\) singular-value coefficient.

The coefficient is recovered by localizing multiplier norming polynomials on many mutually orthogonal, coprime arithmetic fibers. Existing published finite-dimensional Cesàro singular-value coefficients do not subsume this arithmetic Dirichlet-series result.

## Limitations
The result only treats nonconstant **finite** Dirichlet-polynomial symbols on \(\mathscr H^2\). It asserts neither second-order singular-value asymptotics nor results for arbitrary Dirichlet-series symbols or different ambient norms. Numerical tests are finite consistency checks. Novelty is assessed from identified sources and mathematical-record comparisons; undiscovered equivalent formulations or general abstract singular-value asymptotic theorems remain a publication-priority risk. Independent mathematical validation has not been performed.

## References
1. C. Tong, M. Wang, Z. Yuan, *Volterra operators on the BMOA space of Dirichlet series*, arXiv:2610.21873v1, first public October 15, 2026, https://arxiv.org/abs/2610.21873.
2. O. F. Brevig, K.-M. Perfekt, K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729v1, first public February 15, 2016, https://arxiv.org/abs/1602.04729.
3. H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, arXiv:2004.04087, https://arxiv.org/abs/2004.04087.
4. C. Gómez-Cabello, P. Lefèvre, H. Queffélec, *Volterra operator acting on Bergman spaces of Dirichlet series*, arXiv:2402.12524, https://arxiv.org/abs/2402.12524.
