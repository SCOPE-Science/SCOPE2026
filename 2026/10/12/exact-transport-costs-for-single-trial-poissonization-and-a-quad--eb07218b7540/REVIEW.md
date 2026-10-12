# Scientific review: single-trial Poissonization transport

## Correctness — PASS
The two cost identities follow from pointwise inequalities for \(\|e_I-Y\|_1\) and \(\|e_I-Y\|_2^2\). The maximal-coordinate tie-break respects the uniform categorical marginal by permutation symmetry, attaining both lower bounds. Exact Poisson factorial moments establish the nonnegative collision functional and strictness. The uniform factorial-tail bound at levels four and above proves that the \(7/12\) asymptotic coefficient covers the entire unbounded state space. Numerical truncated linear programs and symbolic-series diagnostics were separately executed; they cannot replace the proof.

## Originality — PASS, with residual risk
Inspection of the original methods and relevant full-article sections of Pianoforte and Turin (arXiv:2105.01599, DOI:10.1017/jpr.2022.33) found \(\ell_1\)-Wasserstein approximation bounds for the Bernoulli-vector setting, not the exact squared Euclidean distance or the maximal-coordinate collision asymptotic. An earlier Deheuvels–Pfeifer (1988) theorem for precisely the multinomial/Poisson pair was also inspected in the author-hosted article and concerns total variation, not quadratic transport. Targeted mathematical record searches for quadratic optimal transport, one-hot multinomial Poissonization, and maximum-Poisson-cell couplings did not identify a dominating statement. The generic semidiscrete optimal-transport literature and earlier Poisson approximation sources, not all available in full text, create a remaining priority risk. A failed search alone is not evidence of novelty; the claim-versus-prior metric and implication comparison is the operative reason.

## Value — PASS
Poissonization replaces exclusive categorical occupancy by independent counts and is a recurring approximation problem. The exact squared transport cost quantifies a nontrivial, dimension-dependent obstruction; its maximizing-cell optimal coupling is constructive. Comparing the invariant first-order cost \(2/e\) with the strictly larger quadratic cost and its canceled \(d^{-1}\) collision term gives a precise calibration benchmark for strong probability metrics. The fact is restricted to the natural one-trial uniform model; no broader approximation theorem is asserted.

## Sources and limitations
Pianoforte–Turin (2021 preprint, 2023 article), Section 3.1 and Corollary 3.1; Deheuvels–Pfeifer (1988), introduction and Section 2, Theorem 2.2; Novak (2019), published abstract; Rüschendorf (1985), published abstract. The latter two were not wholly inspected, and unrecognized equivalent formulations remain possible. The experiment tests only finite truncated laws. A further independent literature and proof review is warranted before public priority claims.

Self-review: passed. Independent audit: not yet performed.
