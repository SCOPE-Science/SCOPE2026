# Sharp logarithmic singular-value law for polynomial Volterra operators on Bergman–Dirichlet spaces

## Finding

For any nonconstant Dirichlet polynomial \(g(s)=a_1+\sum_{k\in F}a_k k^{-s}\), where \(F\subseteq\{2,3,\dots\}\) is finite and each displayed nonconstant coefficient is nonzero, define its derivative Bohr polynomial
\[
B(z)=\sum_{k\in F}a_k(\log k)\prod_{j=1}^d z_j^{\nu_j(k)},\qquad M_g=\max_{z\in\mathbb T^d}|B(z)|.
\]
Here \(p_1,\ldots,p_d\) are precisely the primes dividing members of \(F\), and \(\nu_j(k)\) is the exponent of \(p_j\) in \(k\). The sharp singular-value law is
\[
\boxed{\lim_{n\to\infty}(\log n)s_n(T_g)=M_g>0.}
\]
It holds throughout the weighted Hilbert Bergman–Dirichlet family below; the constant is independent of its defining measure. Equivalently, the best rank-less-than-\(n\) approximation error is asymptotic to \(M_g/\log n\).

For example, with \(g(s)=2^{-s}+4^{-s}-8^{-s}\), the coherent norm is
\[
M_g=\log2\max_{|z|=1}|z+2z^2-3z^3|=\frac{8\log2}{\sqrt3}.
\]
This is not the Euclidean norm of the three derivative coefficients.

## Assumptions and scope

Let \(\mu\) be any Borel probability measure on \((0,\infty)\) such that every neighborhood of zero has positive \(\mu\)-mass. Put
\[
w_n=\int_0^\infty n^{-2\sigma}\,d\mu(\sigma),\qquad
\mathcal A^2_\mu=\left\{\sum_{n\ge1}c_n n^{-s}:\sum_{n\ge1}|c_n|^2w_n<\infty\right\}.
\]
The Hilbert completion is understood via Dirichlet coefficients. Its orthonormal basis is \(e_n(s)=n^{-s}/\sqrt{w_n}\). For a Dirichlet polynomial \(f\), the operator
\[
T_gf(s)=-\int_s^\infty f(w)g'(w)\,dw
\]
is evaluated first where the integral converges and then extended by continuity to \(\mathcal A^2_\mu\). Singular values \(s_1\ge s_2\ge\cdots\) are counted with multiplicity, and coincide with Hilbert-space approximation numbers.

## Proof

**1. Coefficient factorization and the upper bound.** Define \(b_k=a_k\log k\). For every Dirichlet polynomial \(f(s)=\sum_{n\ge1}c_n n^{-s}\), direct integration yields
\[
T_g f(s)=\sum_{n\ge1}\sum_{k\in F}\frac{b_k c_n}{\log(nk)}(nk)^{-s}.
\]
Write \(M_B\) for coefficient multiplication by the Dirichlet polynomial \(\sum_{k\in F}b_k k^{-s}\), and let \(D^{-1}e_1=0\), \(D^{-1}e_n=(\log n)^{-1}e_n\) for \(n\ge2\). Thus \(T_g=D^{-1}M_B\) on polynomials.

The Bohr lift and the definition of \(w_n\) give
\[
\|f\|_{\mathcal A^2_\mu}^2
=\int_0^\infty\|f(\sigma+\cdot)\|_{\mathcal H^2}^2\,d\mu(\sigma).
\]
On each translate, multiplication by \(\sum b_k k^{-s}\) has norm at most \(\max_{\mathbb T^d}|B|=M_g\), since its Bohr polynomial has contracted coordinates \(p_j^{-\sigma}z_j\) and hence maximum no greater than its boundary maximum. Therefore \(\|M_B\|\le M_g\).

Let \(P_{<N}\) project to \(e_1,\dots,e_{N-1}\), and \(Q_N=I-P_{<N}\). Every nonconstant term in the symbol has index at least two, so \(M_B Q_N\) is supported on output indices \(\ge2N\). Consequently
\[
\|T_gQ_N\|\le\frac{M_g}{\log(2N)}.
\]
As \(T_gP_{<N}\) has rank at most \(N-1\), the approximation-number characterization gives
\[
s_N(T_g)\le\frac{M_g}{\log(2N)}.
\]
This also proves compactness. In particular the limsup in the theorem is at most \(M_g\).

**2. A universal moment-ratio lemma.** For each fixed positive integer \(q\),
\[
\lim_{m\to\infty}\frac{w_{mq}}{w_m}=1.
\]
Indeed, \(w_{mq}/w_m\) is the expectation of \(q^{-2\sigma}\) under the probability measure with density \(m^{-2\sigma}/w_m\) relative to \(\mu\). For any \(\delta>0\), the tilted mass of \(\sigma\ge\delta\) is at most
\[
\frac{m^{-2\delta}}{\mu((0,\delta/2))m^{-\delta}}
=\frac{m^{-\delta}}{\mu((0,\delta/2))}\longrightarrow0.
\]
The tilted measure therefore converges weakly to point mass at zero, proving the claim. Only the stated support hypothesis is needed; no density, doubling, or moment regularity is assumed.

**3. Orthogonal arithmetic fibers.** Let \(P=p_1\cdots p_d\). Every positive integer has the unique factorization
\[
n=m\prod_{j=1}^d p_j^{\alpha_j},\qquad \gcd(m,P)=1,\quad \alpha_j\in\mathbb N_0.
\]
Therefore \(\mathcal A^2_\mu\) is the orthogonal direct sum of subspaces
\[
E_m=\overline{\operatorname{span}}\{e_{m\prod p_j^{\alpha_j}}:\alpha\in\mathbb N_0^d\},\qquad\gcd(m,P)=1.
\]
Each \(E_m\) is invariant under \(M_B\), \(D^{-1}\), and \(T_g\). Define the unitary coefficient identification \(U_m:H^2(\mathbb D^d)\to E_m\) by mapping \(z^\alpha\) to \(e_{m\prod p_j^{\alpha_j}}\).

For every *fixed polynomial* \(x\in H^2(\mathbb D^d)\),
\[
\lim_{\substack{m\to\infty\\\gcd(m,P)=1}}
\big\|(\log m)U_m^*T_gU_m x-Bx\big\|_{H^2}=0.
\]
To verify this, expand the finitely many coefficients. The coefficient from input \(m r\) to output \(m r k\) is
\[
b_k\frac{\sqrt{w_{mrk}/w_{mr}}}{\log(mrk)}.
\]
After multiplication by \(\log m\), it tends to \(b_k\) by the moment-ratio lemma. There are finitely many output monomials, so convergence holds in norm.

**4. A positive-density family of almost extremizers.** Multiplication by a bounded analytic polynomial on \(H^2(\mathbb D^d)\) has operator norm its polydisk supremum \(M_g\). Because polynomials are dense, for any \(\varepsilon>0\) there is a normalized polynomial \(x\) such that \(\|Bx\|>M_g-\varepsilon\). The preceding finite-coefficient convergence implies that for every sufficiently large \(m\) coprime to \(P\),
\[
\|T_gU_m x\|\ge\frac{M_g-2\varepsilon}{\log m}.
\]
For \(K\to\infty\), take every integer \(m\in[\lceil\sqrt K\rceil,K]\) coprime to \(P\). The corresponding unit vectors \(U_mx\) are orthogonal, as are their images; hence the operator is bounded below by \((M_g-2\varepsilon)/\log K\) on their span. Elementary inclusion-exclusion gives the dimension
\[
r_K=\#\{m\in[\lceil\sqrt K\rceil,K]:\gcd(m,P)=1\}
=\frac{\varphi(P)}P K+o(K).
\]
By the Hilbert-space min–max characterization,
\[
s_{r_K}(T_g)\ge\frac{M_g-2\varepsilon}{\log K}.
\]
For each large \(n\) choose \(K=\lceil 2Pn/\varphi(P)\rceil\); then \(r_K\ge n\), so \(s_n\ge s_{r_K}\). Since \(\log K/\log n\to1\), the liminf of \((\log n)s_n\) is at least \(M_g-2\varepsilon\). Let \(\varepsilon\downarrow0\) and combine with Step 1.

**5. Exact three-term example.** For \(g(s)=2^{-s}+4^{-s}-8^{-s}\), factor out \(\log2\) and a unimodular \(z\). With \(u=\cos\theta\),
\[
|1+2e^{i\theta}-3e^{2i\theta}|^2=20-8u-12u^2
=\frac{64}{3}-12\left(u+\frac13\right)^2.
\]
The maximizing point \(u=-1/3\) is admissible, so the displayed exact constant follows.

## Verification

The standalone `verify.py` reproduces the exact three-term algebra, tests 1,001 phase samples, checks positive-density fiber counts and moment-ratio behavior for gamma-distributed measures, and numerically verifies the coefficient limit on many finite polynomial fibers. Run `python verify.py` from a directory containing the attached file. Its finite checks do not replace the proofs of the moment-ratio lemma, the min–max lower bound, or the infinite-dimensional singular-value limit.

## Relationship to prior work

Gómez-Cabello, Lefèvre, and Queffélec, *Volterra operator acting on Bergman spaces of Dirichlet series*, arXiv:2402.12524 (initial public version 19 February 2024), establish in their Section 7.3, Theorem 7.10, the absence of finite Schatten membership for a nonconstant symbol on \(\mathcal A_\mu^2\), and in Section 7.4, Proposition 7.12, compactness for Dirichlet-polynomial symbols. Neither theorem determines the leading coefficient of the complete approximation-number sequence. The present theorem refines both conclusions simultaneously and specifies the sharp coefficient for all admissible \(\mu\).

Brevig, Perfekt, and Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729, Theorem 7.2, establish non-Schatten membership on the Hardy space. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, arXiv:2004.04087, analyzes a related weighted space and proves non-Schatten membership; neither result states a logarithmic singular-value coefficient on the current \(\mu\)-family. Fu, Guo, and Yan, *Generalized multiplicative Hilbert operators and Volterra operators on McCarthy-Bergman spaces of Dirichlet series* (2023), give boundedness and compactness criteria on a specialized scale, rather than the current asymptotic. As with any priority comparison, an unlocated earlier general result might imply the asymptotic indirectly.

## Limitations

The theorem is for nonconstant *finite* Dirichlet-polynomial symbols and Hilbert exponent two. It does not assert an analogous limit for infinite symbols, arbitrary \(p\)-spaces, or a second-order remainder. The singular-value coefficient concerns compact approximation, not the operator norm \(\|T_g\|\), which can depend on the measure. The finite numerical tests are supplementary only. Priority against every possible general compact-operator asymptotic theorem has not been established.

## References

1. C. Gómez-Cabello, P. Lefèvre, H. Queffélec, *Volterra operator acting on Bergman spaces of Dirichlet series*, arXiv:2402.12524, first version 19 February 2024; Sections 5 and 7, especially Theorem 7.10 and Proposition 7.12. https://arxiv.org/abs/2402.12524
2. O. F. Brevig, K.-M. Perfekt, K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729; Section 7, Theorem 7.2. https://arxiv.org/abs/1602.04729
3. H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, arXiv:2004.04087; Section 7. https://arxiv.org/abs/2004.04087
4. X. Fu, K. Guo, F. Yan, *Generalized multiplicative Hilbert operators and Volterra operators on McCarthy-Bergman spaces of Dirichlet series*, 2023, author-posted full text, Theorem E and Section 5.
