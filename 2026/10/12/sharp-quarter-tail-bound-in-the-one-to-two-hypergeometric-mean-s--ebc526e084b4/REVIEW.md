# Scientific assessment: sharp hypergeometric quarter tail

## Correctness — PASS

The claim is exactly \(n\ge4k\), \(k\ge2\), \(1<ik/n\le2\), with a uniform hypergeometric sample. The stochastic monotonicity reduction brings all admissible parameters to the just-above-one boundary \(n=rk-1\), \(r\ge5\). A pointwise fifth-order Bonferroni minorant yields an exact factorial-moment expression. The small-sample rational identities are strictly positive; for \(r,k\ge5\), the displayed 36 strictly positive coefficients of an exact bivariate polynomial imply global positivity. Its bidegree bound plus exact interpolation, not finite statistical simulation, proves the symbolic identity. The extremal sequence \(k=2\), \(n=2i-1\) tends to \(1/4\).

The packaged `check.py` passed 28,288 exact assertions, including the coefficient identity, so the nonstandard arithmetic step was reproduced before acceptance. The remaining steps are combinatorial couplings and a pointwise finite binomial identity.

## Originality — PASS, residual risk disclosed

Ai–Pelekis arXiv:2601.09485v2, Theorem 1.1, obtains the weaker right side \(k/n\) under the stronger restriction \(n\ge8k\). Its introductory discussion (Sections 1–3) expressly leaves the \(4k\) regime open and describes a related universal one-quarter lower bound as numerical evidence. The present theorem supplies an analytic, sharp one-quarter estimate in a structurally motivated subregion \(1<\mu\le2\) while retaining the proposed \(4k\) ratio. Greenberg–Mohri arXiv:1306.1433v3, Theorem 2.1, covers binomial trials with replacement, not finite-population samples. Searches for hypergeometric two-hit quarter bounds, rare-success crossing aliases, analogous factorial-moment bounds, and mathematical records did not identify a statement implying this one. Search absence is not proof of absolute priority; older equivalent tail bounds may exist.

## Value — PASS

The discontinuity immediately above expected count one is a genuinely delicate edge of the proposed \(n\ge4k\) hypergeometric/MMS-extremizer inequality: Gaussian approximations do not apply there and a \(1/4\) bound is asymptotically best possible. The theorem settles that entire infinite strip simultaneously for all sample sizes, populations and marked counts, and strengthens \(k/n\) to a sharp constant. It is a meaningful boundary result, not an isolated tabulation or a restatement of the binomial theorem. It does not settle higher expectation strips or the complete MMS problem.

Self-review: passed. Independent audit: not yet performed.
