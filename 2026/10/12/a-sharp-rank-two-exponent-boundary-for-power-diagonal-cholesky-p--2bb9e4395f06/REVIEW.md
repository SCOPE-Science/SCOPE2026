# Self-review

**Correctness — PASS.** The rank-one trace expansion and spectral Cauchy–Schwarz lemma prove a universal decrease bound. Weighted Cauchy–Schwarz and arithmetic–geometric mean cover all real exponents in the claimed interval. The two-block law is obtained from the two possible exact residuals; its polynomial endpoint inequality is strictly positive for all real scaling parameters and integers \(m\ge2\), and the dimension asymptotics rigorously force failure for every \(\beta>4\). Exact rational package checks reproduce the stated finite witness and support algebraic bookkeeping; they are not an infinite proof.

**Originality — PASS, subject to residual priority risk.** Chen et al. analyze diagonal-proportional pivots, mainly for trace approximation; Steinerberger proves the \(\beta=2\) Frobenius guarantee and provides the pivot identity. Neither inspected full text states the exact rank-two cluster threshold at \(\beta=4\), and the continuum safe interval is not a quoted theorem there. published-finding corpus search also retrieved related adaptive randomized pivoting and ACA results, but none of their returned statements implies the one-step power-diagonal criterion. Unindexed specialized work and inaccessible relevant full texts remain plausible.

**Value — PASS.** The power parameter is an actual design choice in published partial-Cholesky sampling, and the problem distinguishes reasonable adaptive pivoting from over-greedy concentration. A sharp exponent cutoff, even on a rank-two family, identifies a structural failure mode for a dimension-dependent approximation guarantee. The general interval \(2<\beta\le4\) is deliberately not asserted. No multi-step claim is made.

Closest sources: arXiv:2207.06503 (algorithm and trace bounds), arXiv:2404.11487 (known \(\beta=2\) Frobenius bound, power-rule question, greedy fragility). Scientific limits: one step, one rank-two block threshold, exact arithmetic, no independent verification.

Self-review: passed. Independent audit: not yet performed.
