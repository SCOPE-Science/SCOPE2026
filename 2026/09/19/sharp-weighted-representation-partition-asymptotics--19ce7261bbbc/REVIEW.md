# Review: sharp weighted-representation partition asymptotics

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The reduction to a finite sign problem follows directly from the two identities proved by Li--Xu--Yan: the boundary values determine the eventual constant difference, while all later signs obey \(\varepsilon_n=-\varepsilon_{\lfloor n/k\rfloor}\). Thus the infinite-set count is exactly a lattice probability for \(T+k\) independent initial signs.

The covariance computation was checked both symbolically and by direct finite construction. Its limit is
\[
B_k=\frac1kI_k+\frac{k+2}{k^2}J_k,
\]
with determinant \((k+3)/k^k\). The coordinate-only blocks have linear size \((k-1)T/k^2+O_k(1)\), which forces the Fourier modulus-one set to be exactly \(\{0,\pi\}^k\). The target lattice is even in every coordinate, and every boundary coefficient sum is even, so all \(2^k\) Fourier peaks contribute equally. A fourth-order Taylor expansion of \(\log\cos\) on shrinking neighborhoods and exponential suppression outside them gives the stated lattice local limit. Substitution of \(y=2c_T\mathbf1\) produces the exponent \(-2k^2\lambda^2/(k+3)\) and the constant \((8k/\pi)^{k/2}/\sqrt{k+3}\).

Adversarial checks included parity, possible extra Fourier peaks, overlap terms in the covariance, the factor \(2^{T+k}\) rather than \(2^T\), and the eigenvalue in the all-ones direction. Each is explicitly accounted for in the proof. Exact finite enumeration and covariance calculations agree with the predicted limits.

## Originality

**PASS, to the best of our knowledge.** The full accessible text of Li--Xu--Yan, arXiv:2609.20385, was inspected. Its Theorem 1.2 establishes only two-sided order for fixed \(c\), and its proof uses binomial upper and lower bounds rather than a multivariate local-limit evaluation. No explicit leading constant, fixed-\(c\) asymptotic equivalence, or \(c\asymp\sqrt T\) Gaussian profile was located there.

The 2025 Yan--Shan paper concerns the same weighted representation setting and gives an exact formula for its related \(g_k(t)\) only for \(t\le k\); its accessible abstract and text do not indicate a large-threshold asymptotic of the form proved here. The 2024 Li--Shan--Yan paper addresses existence of constant differences, while Chen--Ding--Lü--Zhang (2024) improves lower bounds on the representation function itself. Qu's and other earlier works found in the search concern structural or finite-group questions rather than this enumeration.

The 2012 Yang--Chen article was not fully inspected. The new 2026 primary source describes the relevant earlier counting information as finiteness together with a substantially coarser exponential-scale result, which does not suggest the constant or Gaussian profile proved here. This is retained as an access limitation rather than treated as evidence of absence. The principal residual originality risk is unindexed concurrent work prompted by the very recent 2026 preprint.

Searches used the exact problem title, \(f_k(t)\), weighted representation functions, the order \(2^T/T^{k/2}\), local/central-limit terminology, Gaussian-profile terminology, and the explicit candidate constant. No prior statement of the result was located.

## Value

**PASS.** The result upgrades a correct-order theorem to an asymptotic equivalence with a closed leading constant and simultaneously identifies the full central \(\sqrt T\)-scale distribution of the eventual difference. It also gives a sharp asymptotic ratio for the original Yang--Chen counts for different weights. The covariance/Fourier mechanism is reusable for related finite-sign reductions with several coupled boundary equations.

## Limitations

The result is for fixed \(k\) and \(c_T/\sqrt T\to\lambda\). It does not provide uniform asymptotics as \(k\) grows, a moderate- or large-deviation regime, or an optimized quantitative error term. The finite verification is supplementary and is not formal verification. No independent validation is asserted.
