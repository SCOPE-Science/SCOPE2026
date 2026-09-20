# Review: exact local-limit asymptotics for weighted representation partitions

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The reduction to a finite sign count follows directly from the identity
\(2D_A(kq+s)=\sum_{j\le q}\varepsilon_j+\sum_{j\le q}\varepsilon_{kj+s}\): taking a difference at spacing \(k\) gives the deterministic tail recursion, so no uncounted compatibility condition remains after the \(k\) boundary equations.

The coefficient-vector calculation was checked adversarially for every residue of \(T\bmod k\). If \(T=ka+b\), then \(q_s=a+1\) for \(s<b\) and \(q_s=a\) otherwise, leaving exactly one transition column between the \(\mathbf1+e_r\) and \(e_r\) regimes. The covariance limit is therefore
\[
\Sigma_k=(kI+(k+2)J)/k^2,
\]
with determinant \((k+3)/k^k\). The lattice factor is \(2^k\), not 1: the Rademacher sum is confined to an even coordinate coset, and the repeated \(e_r\) columns make \(2\mathbb Z^k\) the full difference lattice. Each of the \(2^k\) Fourier major arcs has the same phase because every boundary equation has even total coefficient sum and the target is \(2c_T\mathbf1\).

The Fourier proof also checks the only two places where a local limit can fail: nondegeneracy and aperiodicity. Nondegeneracy follows from the two eigenvalues of \(\Sigma_k\); aperiodicity modulo the even lattice follows from the positive-density coordinate columns. For \(c_T/\sqrt T\to\gamma\), the Gaussian Fourier transform gives exponent \(-2k^2\gamma^2/(k+3)\). Setting \(\gamma=0\) recovers the fixed-\(c\) constant. Exact finite computations in `artifacts/verify.py` provide independent sanity checks of the coefficient construction, parity, covariance determinant, and representative counts.

## Originality

**PASS, to the best of our knowledge.** The principal source, Li--Xu--Yan, arXiv:2609.20385v1 (17 September 2026), was inspected in full through its HTML rendering. Its Theorem 1.2 proves only
\(F_{k,c}(T)\asymp_{k,c}2^T/T^{k/2}\), and Corollary 1.3 specializes this to \(f_k\); no leading constant or local-limit profile is stated there. Its proof obtains upper and lower bounds by conditioning on blocks and applying one-dimensional binomial estimates.

Searches covered the exact and synonymous formulations “weighted representation functions”, `f_k(t)`, `R_{1,k}(A,n)`, exact asymptotic constant, local central/local limit theorem, Gaussian profile, and the source title/authors. The 2025 Yan--Shan paper was checked at the abstract/full-text-summary level: it gives exact formulas only in a small-threshold regime and poses/answers different counting questions. The 2024 correct-order paper concerns the size of the representation function itself, not the number of admissible partitions. No source located states the constant
\((8k/\pi)^{k/2}/\sqrt{k+3}\) or the \(c_T/\sqrt T\) Gaussian factor.

The 2012 Yang--Chen article is the most relevant source not independently checked in full. Its role and relevant results were checked through Li--Xu--Yan's introduction and bibliographic records. Because Li--Xu--Yan explicitly present their 2026 theorem as the new correct-order estimate following Yang--Chen's logarithmic-rate result, undisclosed prior coverage of the exact constant in the 2012 paper appears unlikely but cannot be ruled out solely from the searches. A second residual risk is unindexed work following the very recent 2026 preprint.

## Value

**PASS.** The result converts a newly established order of magnitude into a full asymptotic formula for every fixed weight \(k>1\), identifies a simple closed leading constant, and strengthens the comparison between distinct weights from eventual inequality to an asymptotic ratio. The \(c_T\asymp\sqrt T\) extension additionally identifies the natural fluctuation scale and Gaussian profile, rather than supplying only a routine fixed-parameter constant refinement.
