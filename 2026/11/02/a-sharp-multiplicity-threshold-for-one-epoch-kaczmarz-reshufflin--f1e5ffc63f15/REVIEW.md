# Scientific review: multiplicity threshold for one-epoch Kaczmarz reshuffling

## Correctness — PASS

The statement fixes normalized, consistent, full-column-rank two-dimensional systems, a particular deterministic starting error, exact orthogonal projection, and a comparison at the same \(m\)-update horizon. An initial repeated-type projection kills the error. Otherwise the remaining norm is exactly \((1-k)k^N\), with \(N\) the switch count between the two projection lines. A permutation can begin with the lone exceptional row with probability \(1/m\), followed by exactly one switch, whereas IID sampling gives the explicit two-state generating matrix. The resulting difference of risks is \((1-k)(k-G_m(k))/m\).

The generating polynomial has positive constant coefficient and a strictly positive coefficient at degree two. Its derivative at one exceeds one for every \(m\ge3\), proving a unique interior threshold by strict convexity. The zero- and one-switch coefficients yield the superexponential asymptotic, and a Poisson limit of isolated exceptional draws proves the risk-ratio limit. Exact projection enumerations independently verify the stated special values and all-distinct witness. The general theorem rests on the proof, not on finite enumeration.

## Originality — PASS, with residual priority risk

Relevant full-text inspections were the 2024 Kaczmarz row-action survey (arXiv:2401.02842), the 2024 reshuffling convergence analysis (arXiv:2410.01140), and the 2026 shuffled-SGD rate analysis (arXiv:2606.32005). The survey compares empirical performance of sampling with and without replacement. Han–Xie compare convergence bounds and provide three-row illustrations, not the exact fixed-start expected squared solution error under a repeated-row pattern. Liu's result compares rate *bounds* for averaged SGD iterates at stepsizes up to \(1/(6L)\), not pointwise terminal risk at the full unrelaxed Kaczmarz projection step. A 2014 exact randomized-Kaczmarz MSE analysis was checked at abstract level only; its accessible description addresses IID selection, not this RR comparison. Searches for repeated-row, rare-type, switch-generating and sharp-angle-threshold equivalents found no matching statement, but absence of a match is not a uniqueness certificate.

A related two-row comparison for relaxed Kaczmarz analyzes a distinct two-update, two-row system. It does not settle the \(m\ge3\) multiplicity transition, the superexponential boundary or the exact distinct-row three-projection witness. Other related analyses concern adaptive row choices, cyclic noisy Kaczmarz, or stationary scalar SGD, and their claims do not imply this one-epoch theorem.

Residual risk: an older specialized comparison of redundant Kaczmarz row schedules may already contain the precise switch-count polynomial or an equivalent threshold, despite no match in the inspected sources and searches. Independent literature review remains necessary for publication priority.

## Value — PASS

The result answers a concrete algorithm-selection question raised by favorable empirical reshuffling comparisons: an epoch-wise sample-without-replacement rule need not dominate independent sampling for a specified solution-error direction, even in a consistent full-column-rank system and without overrelaxation. It identifies a *unique* exact angular boundary at every multiplicity, its unexpectedly rapid collapse as duplicate measurements accumulate, and a limiting relative loss approaching the factor \(e\). The signed effect persists after perturbing the repeated rows to three pairwise nonparallel rows. These are structural, parameter-sharp conclusions rather than a single arbitrary negative numerical example.

Limits: no claim of superiority or inferiority for all initial directions, over multiple epochs, or for general matrices; repeated rows are an intentionally transparent extremal test case. The all-distinct example establishes robustness but not a full classification for all-distinct matrices.

Self-review: passed. Independent audit: not yet performed.
