# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The reduction to a finite sign system is exactly the boundary reduction proved in Li--Xu--Yan. Writing signs as centered Bernoulli variables converts the count to a lattice point probability for a triangular array of bounded integer columns. The normalized Gram matrix converges to
\[
G_k=k^{-1}I_k+(k+2)k^{-2}J_k,
\]
whose determinant is \((k+3)/k^k\). The source paper's sets \(P_s\) contain \((k-1)T/k^2+O_k(1)\) columns equal to the standard basis vectors \(e_s\); this gives full lattice span and exponential suppression of every noncentral Fourier region. The central Fourier expansion then gives the stated multivariate local central limit with covariance \(G_k/4\). The factor \(2^{T+k}\), the determinant, and the Gaussian shift combine to the constant
\[
C_k=(8k/\pi)^{k/2}/\sqrt{k+3}.
\]
Exact dynamic-programming counts independently check the finite boundary system and converge toward both the fixed-discrepancy constant and the \(c\asymp\sqrt T\) Gaussian profile.

Potential failure modes were checked explicitly. The two indicator parts of a boundary row can overlap, so matrix entries may equal 2; the Gram calculation treats rows as sums of the two indicator vectors and therefore includes all four intersection terms. There is no hidden parity obstruction because every boundary-row coefficient sum is \(2(q_s+1)\), while the right side is \(2c_s\). The columns in \(P_s\) are exactly \(e_s\), which rules out a proper sublattice and additional Fourier saddle points. The fixed vector shift is negligible at the central-limit scale, while a \(\sqrt T\)-scale shift produces the stated quadratic exponential.

## Originality

**PASS, to the best of our knowledge.** The full 2026 motivating preprint arXiv:2609.20385v1 was inspected. Its Theorem 1.2 gives only
\[
F_{k,c}(T)\asymp_{k,c}2^T/T^{k/2}
\]
for fixed scalar \(c\), and Corollary 1.3 gives the same order for \(f_k(T)\). Its proof uses blockwise central-binomial upper and lower bounds. No leading constant, covariance matrix, lattice local-limit theorem, \(\sqrt T\)-scale discrepancy profile, or asymptotic ratio constant for \(f_k/f_\ell\) is stated there. Remark 1.5 likewise provides only order of magnitude for the Yan--Shan function.

Searches for the exact constant, synonymous weighted-representation counting formulations, local-limit formulations, and the older cited literature did not identify prior coverage. The related 2024 paper of Chen--Ding--Lü--Zhang concerns the size of representation values under eventual equality, rather than the number of admissible partitions. The 2020 Li--Ma and other structural papers on equal weighted representation functions address existence/structure, not this counting asymptotic.

The most relevant source not inspected in full is Q.-H. Yang and Y.-G. Chen, *Partitions of natural numbers with the same weighted representation functions*, J. Number Theory 132 (2012), 3047--3055. The 2026 primary source explicitly summarizes its contribution to \(f_k\) as finiteness and \(\log f_k(t)/t\to\log2\), so overlap with the sharp constant is unlikely but cannot be excluded solely from direct full-text inspection. For the secondary \(g_{k,m}\) corollary, the 2025 Yan--Shan article (DOI 10.1007/s11139-025-01113-7) has accessible metadata and abstract describing exact small-threshold formulas and existence/uniqueness results; no large-threshold sharp constant is indicated. The motivating preprint is very recent, so unindexed contemporaneous work remains a residual risk.

## Value

**PASS.** The result upgrades a newly proved order-of-magnitude theorem to a complete first-order asymptotic with an explicit closed constant. The multivariate extension identifies the full Gaussian fluctuation law for residue-dependent tail discrepancies, explaining why the fixed scalar \(c\) disappears from the leading constant. It also sharpens the paper's qualitative comparison of different weights to an explicit asymptotic ratio and gives the corresponding leading constant for the Yan--Shan counting function. The argument exposes a concrete covariance structure rather than merely improving numerical bounds.

## Limitations

The theorem is for fixed \(k\); no uniformity in growing \(k\) is asserted. It gives the central and \(\sqrt T\)-scale local-limit regime, not moderate or large deviations. The verification code supports the algebra and constants but is not a substitute for the Fourier proof. No independent validation or formal proof-assistant verification is asserted.
