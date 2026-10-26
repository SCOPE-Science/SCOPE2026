# Sharp logarithmic singular-value law for Dirichlet-polynomial Volterra operators

## Finding
Let \(\mathcal H^2\) be the Hilbert space of ordinary Dirichlet series \(f(s)=\sum_{n\ge 1}a_n n^{-s}\), with \(\|f\|_{\mathcal H^2}^2=\sum_{n\ge1}|a_n|^2\). For any nonconstant Dirichlet polynomial
\[
g(s)=b_1+\sum_{m\in F}b_m m^{-s},\qquad \varnothing\ne F\subset\{2,3,\ldots\}\text{ finite},\quad b_m\ne0,
\]
consider the Volterra operator \(T_g f(s)=-\int_s^{+\infty}f(w)g'(w)\,dw\), defined first on Dirichlet polynomials and extended to \(\mathcal H^2\). Let \(S=\{p_1,\ldots,p_d\}\) be the distinct primes dividing the elements of \(F\), and let \(\nu(m)=(\nu_{p_1}(m),\ldots,\nu_{p_d}(m))\). Define the finite-torus multiplier norm
\[
C_g=\max_{z\in\mathbb T^d}\left|\sum_{m\in F}b_m(\log m)z^{\nu(m)}\right|>0.
\]
If \(s_N(T_g)\) denotes the \(N\)-th singular value (equivalently, the \(N\)-th approximation number) in nonincreasing order, then
\[
\boxed{\displaystyle\lim_{N\to\infty}(\log N)\,s_N(T_g)=C_g.}
\]
In particular \(T_g\) is compact, but belongs to no Schatten class \(\mathcal S_p\) for finite positive \(p\). It is quasinilpotent; more quantitatively,
\[
\|T_g^k\|\le \frac{(C_g/\log2)^k}{k!}\qquad(k\ge1).
\]
For the single-frequency symbol \(g(s)=b_m m^{-s}\) the whole singular sequence, not just its asymptotic, is
\[
s_N(T_g)=\frac{|b_m|\log m}{\log(mN)}\qquad(N\ge1).
\]
For multiple frequencies the limiting coefficient is the *supremum norm* of the logarithmically differentiated symbol, rather than its coefficient \(\ell^2\)-norm. For instance \(g(s)=2^{-s}+3^{-s}\) has \(C_g=\log6\).

## Assumptions and scope
The scalar field is complex; \(F\) is any finite nonempty subset of integers at least two; its coefficients are arbitrary nonzero complex numbers. Zero coefficients can be removed from \(F\), and the constant term \(b_1\) has no effect. No primeness, multiplicative independence, or sign restriction is imposed on the frequencies in \(F\). The singular values are those of the compact operator on the unweighted coefficient Hilbert space \(\mathcal H^2\), not of its realizations on BMOA, Bergman spaces or weighted Dirichlet series spaces. All logarithms are natural.

## Proof
**Coefficient identity and compact factorization.** Write \(e_n(s)=n^{-s}\), an orthonormal basis, and let \(h=-g'=\sum_{m\in F}b_m(\log m)m^{-s}\). Direct integration on the horizontal ray, for sufficiently large real part, gives
\[
T_g e_n=\sum_{m\in F}\frac{b_m\log m}{\log(mn)}e_{mn}.
\]
Let \(M_h\) be Dirichlet-series multiplication by \(h\), and define the diagonal operator \(D e_1=0\) and \(D e_n=(\log n)^{-1}e_n\) for \(n\ge2\). Then the coefficient identity is \(T_g=DM_h\). Under the Bohr lift to \(H^2(\mathbb D^d)\) in the finitely many prime variables of \(h\), multiplication by \(h\) has norm exactly \(\max_{z\in\mathbb T^d}|h(z)|=C_g\). In the full Dirichlet Hilbert space, \(M_h\) is the same multiplier on each orthogonal prime-fiber, and has the same norm. Since \(D\) is compact, \(T_g\) is compact.

**Upper singular-value bound.** Let \(P_{N-1}\) be the projection onto \(\operatorname{span}\{e_1,\ldots,e_{N-1}\}\). Every input basis frequency at least \(N\) is taken by \(M_h\) to output frequencies at least \(2N\). Consequently
\[
\|T_g(I-P_{N-1})\|\le\frac{C_g}{\log(2N)}.
\]
As \(T_gP_{N-1}\) has rank at most \(N-1\), the Hilbert-space approximation-number variational principle yields \(s_N(T_g)\le C_g/\log(2N)\). Hence \(\limsup_{N\to\infty}(\log N)s_N(T_g)\le C_g\).

**Sharp lower bound via coprime fibers.** Fix \(\epsilon>0\). Since polynomials are dense in \(H^2(\mathbb D^d)\) and \(C_g=\|M_h\|\), there is a finite Dirichlet polynomial \(q\), supported on integers having all prime factors in \(S\), with \(\|q\|=1\) and \(\|hq\|>C_g-\epsilon\). Write \(hq=\sum_{2\le\ell\le K}c_\ell e_\ell\) for a fixed integer \(K\ge2\). Put \(P=\prod_{p\in S}p\). For each positive integer \(r\) coprime to \(P\), let \(q_r=e_r q\). Unique prime factorization implies that the vectors \(q_r\) are mutually orthonormal, and their images \(T_gq_r\) are mutually orthogonal. More explicitly,
\[
T_gq_r=\sum_{2\le\ell\le K}\frac{c_\ell}{\log(r\ell)}e_{r\ell}.
\]
For \(R/2\le r\le R\), \(\gcd(r,P)=1\), every denominator is at most \(\log(RK)\), so
\[
\|T_gq_r\|\ge\frac{\|hq\|}{\log(RK)}>\frac{C_g-\epsilon}{\log(RK)}.
\]
The number \(J(R)\) of such \(r\) is \(J(R)=\frac{\varphi(P)}{2P}R+O_P(1)\), by elementary inclusion-exclusion. On the \(J(R)\)-dimensional span of these orthonormal vectors the operator is bounded below by \((C_g-\epsilon)/\log(RK)\). The min-max formula for compact Hilbert-space singular values therefore gives
\[
s_{J(R)}(T_g)\ge\frac{C_g-\epsilon}{\log(RK)}.
\]
For arbitrary sufficiently large \(N\), choose \(R=c_P N\) with a fixed sufficiently large \(c_P\) so that \(J(R)\ge N\). Monotonicity of singular values gives \(s_N(T_g)\ge(C_g-\epsilon)/\log(c_PKN)\). Thus \(\liminf_{N\to\infty}(\log N)s_N(T_g)\ge C_g-\epsilon\). Letting \(\epsilon\downarrow0\) completes the sharp limit.

**Further consequences.** The positive limiting constant implies \(\sum_Ns_N(T_g)^p=\infty\) for every finite \(p>0\), since \(\sum_N(\log N)^{-p}\) diverges. The range of \(T_g^j\) is supported on basis indices at least \(2^j\), because every term in \(h\) has frequency at least two. Thus at step \(j+1\) the diagonal factor \(D\) has norm at most \(1/((j+1)\log2)\), giving \(\|T_g^{j+1}\|\le C_g\|T_g^j\|/((j+1)\log2)\). Iteration proves the factorial estimate and spectral radius zero. For a monomial symbol the images of different basis vectors are orthogonal, so the displayed singular-value formula follows directly from the weights \(|b_m|\log m/\log(mN)\), which decrease in \(N\).

## Verification
The proof of the limit needs no numerical limit extrapolation. Its critical infinite-dimensional steps are the exact coefficient factorization, the multiplier norm identity in finitely many prime variables, the rank truncation, the elementary positive density of integers coprime to \(P\), and the compact-operator min-max principle. The standalone `CHECKER.py` verifies finite coefficient identities, coprime-fiber orthogonality and exact monomial Gram diagonals for representative symbols. Such finite tests are consistency checks, not substitutes for the analytical limit or for the density argument.

## Relationship to prior work
Brevig, Perfekt and Seip established compactness of Dirichlet-polynomial Volterra operators on \(\mathcal H^2\) and proved that every nonconstant symbol yields an operator outside all finite Schatten classes (arXiv:1602.04729, Section 7.1, especially Theorem 7.2). The present statement does not claim these facts as new; it identifies the exact leading constant of every singular value at the natural slow logarithmic scale, for all finite polynomial symbols including interfering frequencies. Tong, Wang and Yuan (arXiv:2610.21873v1, first posted 15 October 2026) prove compactness and other properties on Dirichlet BMOA and endpoint Bergman spaces rather than this singular-value asymptotic on \(\mathcal H^2\). Bommier-Hato (2020) treats boundedness, compactness and Schatten questions on weighted Dirichlet Hilbert spaces; the inspected results do not give the stated unweighted sharp logarithmic law. A previous monomial-Volterra commutator formula concerns a different, higher-order operator and does not imply this full polynomial-symbol law.

## Limitations
This is an asymptotic singular-value theorem for **finite Dirichlet-polynomial symbols** only. It does not assert the same coefficient for infinite series, a second-order error term, or exact individual singular values for multi-term polynomials. The pre-existing compactness and non-Schatten conclusions are cited as prior knowledge. Although the source comparisons identified no implication covering the limit, the possibility of an older equivalent formulation in abstract slowly-varying singular-number theory remains a historical-priority risk. No independent external audit has been performed.

## References
- C. Tong, M. Wang and Z. Yuan, *Volterra operators on the BMOA space of Dirichlet series*, arXiv:2610.21873v1 (first publicly posted 2026-10-15), especially Introduction and Theorems 1.1–1.4. https://arxiv.org/html/2610.21873v1
- O. F. Brevig, K.-M. Perfekt and K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729 (first posted 2016-02-15; examined full-text Section 7.1, pages 33–34). https://arxiv.org/pdf/1602.04729
- H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, *Monatshefte für Mathematik* 193 (2020), 247–289. https://doi.org/10.1007/s00605-020-01396-6
