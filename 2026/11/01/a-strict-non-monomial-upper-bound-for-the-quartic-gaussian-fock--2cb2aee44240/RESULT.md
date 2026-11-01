# A strict non-monomial upper bound for the quartic Gaussian Fock Korenblum radius

## Finding
For the Gaussian Fock space of entire functions with norm
\[
\|h\|_4^4=\frac{2}{\pi}\int_{\mathbb C}|h(z)|^4e^{-2|z|^2}\,dA(z),
\]
write \(\mathcal K_4\) for the supremum of radii \(R>0\) for which every pair \(f,g\) in the space satisfying \(|f(z)|\le |g(z)|\) for all \(|z|>R\) also satisfies \(\|f\|_4\le\|g\|_4\). Then
\[
\boxed{\frac1{\sqrt2}\le \mathcal K_4\le \frac{2063}{2500}<2^{-1/4}.}
\]
In particular the standard constant-versus-monomial upper bound \(2^{-1/4}\) is not sharp. The upper bound is witnessed by two explicit quadratic polynomials and exact rational Gaussian moments.

## Assumptions and scope
Use planar Lebesgue area measure \(dA\) and the displayed normalization; changing the common positive multiplier of the norm does not change admissibility. Let \(r=2063/2500\), \(a=99/100\), and \(b=1/7\). The statement concerns the standard Gaussian exponent \(p=4\) and parameter \(\alpha=1\) in the convention with weight \(e^{-p\alpha|z|^2/2}\). No exact evaluation of \(\mathcal K_4\) is asserted.

## Proof
Define
\[
f(z)=(r-az)(1+bz),\qquad g(z)=(z-ar)(1+bz).
\]
Both are polynomials, hence are in the Fock space. Since \(a,b,r\) are positive real numbers,
\[
|g(z)|^2-|f(z)|^2
=\bigl(|z-ar|^2-|r-az|^2\bigr)|1+bz|^2
=(1-a^2)(|z|^2-r^2)|1+bz|^2.
\]
Thus \(|f(z)|\le|g(z)|\) for every \(|z|>r\). It remains to prove the reverse strict Fock norm inequality.

If \(h(z)=\sum_{j=0}^{2}h_jz^j\), set \(d_k=\sum_{j=0}^k h_jh_{k-j}\), with absent coefficients taken as zero. Orthogonality of powers of \(z\) for the Gaussian measure \((2/\pi)e^{-2|z|^2}dA(z)\) gives
\[
\|h\|_4^4=\|h^2\|_{F^2_2}^2
=\sum_{k=0}^{4}\frac{k!}{2^k}|d_k|^2.
\]
For these particular polynomials their coefficient triples are
\[
(h_0,h_1,h_2)_f=(r,rb-a,-ab),\qquad
(h_0,h_1,h_2)_g=(-ar,1-arb,b).
\]
Substitution and rational arithmetic yield the exact identity
\[
\boxed{\|g\|_4^4-\|f\|_4^4
=-\frac{23857292957391399561}{18757812500000000000000000}<0.}
\]
This is reproducible by the standalone standard-library program in \(verify.py\); the computation is a five-term sum of rational numbers, not a numerical estimate. Hence \(r\) and every greater radius fail the defining implication, so \(\mathcal K_4\le r\). Moreover \(r^4<1/2\), proving \(r<2^{-1/4}\).

For the lower bound, let \(R=1/\sqrt2\). If \(f,g\) have exterior domination beyond \(R\), then their squares have exterior domination in the Hilbert Fock space with weight \(e^{-2|z|^2}\). The sharp Hilbert-space Korenblum theorem at Gaussian parameter \(2\) gives \(\|f^2\|_{F^2_2}\le\|g^2\|_{F^2_2}\). Taking squares and using the displayed identity gives \(\|f\|_4\le\|g\|_4\). Therefore \(R\) is admissible, establishing the lower bound.

## Verification
The rational Gaussian moment identity follows by polar integration:
\[
\frac{2}{\pi}\int_{\mathbb C}|z|^{2k}e^{-2|z|^2}\,dA(z)=\frac{k!}{2^k}
\quad(k=0,1,\dots).
\]
The checker independently convolves both coefficient triples, computes all five moments using exact integer fractions, checks the asserted strict negative difference, and verifies the rational inequalities bounding \(r\). The pointwise domination is an algebraic identity, so no discretization or finite sampling is needed. Exact fraction arithmetic covers the entire proof of the polynomial counterexample; the lower bound uses the cited Hilbert-space theorem.

## Relationship to prior work
Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space* (arXiv:2609.39622, first posted September 30, 2026), establishes the exact Hilbert-space radius, and Section 7.2 identifies the non-Hilbert exponents as unresolved; for \(p=4\) it records the power-reduction lower bound and the monomial upper bound. The present claim is the strict separation from that upper bound using a polynomial multiplier, which the cited Hilbert argument alone does not imply. Wee and Le's earlier articles give upper bounds for weighted Fock classes using elementary test functions; their accessible descriptions do not establish the precise rational separation here. The complete texts of those historical articles were unavailable for a decisive all-results comparison.

## Limitations
The result gives only an explicit upper obstruction and the inherited lower bound, not the exact value of \(\mathcal K_4\), extremizers, or results for all non-Hilbert exponents. The improved rational upper bound is not claimed optimal within the quadratic test family. Earlier implicit coverage of the same counterexample in unavailable historical full texts remains an originality risk. No independent mathematical audit has been performed.

## References
1. F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622, September 30, 2026, https://arxiv.org/abs/2609.39622, especially Theorem 1.1, Corollary 5.2 and Section 7.2.
2. J. Wee and H. K. Le, *Korenblum constants for some function spaces*, Proc. Amer. Math. Soc. 148 (2020), 1175–1185, https://doi.org/10.1090/proc/14778.
3. J. Wee and H. K. Le, *Korenblum constants for various weighted Fock spaces*, Complex Var. Elliptic Equ. 68 (2023), 1385–1406, first online June 29, 2022, https://doi.org/10.1080/17476933.2022.2052862.
