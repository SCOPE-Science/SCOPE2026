# Scientific assessment

## Correctness — PASS

For every integer \(n\ge s\ge2\) and \(r\ge s\), the proof reduces a refitted identity-matrix Gaussian generalized Nyström residual to an orthogonal Gaussian part and a random least-squares coefficient. A direct conditional-density change of variables establishes the Student/chi-square-ratio law with exactly \(r-s+2\) denominator degrees of freedom. This supplies the sharp fractional moment cutoff, the finite-mean formula, and the sharp single-term regular-variation constant. The pooled moments follow from deterministic max/sum inequalities without falsely treating leave-out terms as independent. When \(n=s=r\), a rank-one oblique-projection complement gives the beta angular law and the distinct half-moment cutoff for pair and twin diagnostics. No finite experiment is substituted for the infinite-tail proofs.

## Originality — PASS with residual bibliographic risk

The underlying diagnostic definitions and efficient update formula belong to Lazzarino, Pearce and Pritchard (arXiv:2601.11493), and elementary chi-square, multivariate Student and beta identities are prior mathematics. The asserted distinction is the **joint exact diagnostic-specific classification**: the complete right-leave-out marginal law in arbitrary sketch dimensions, the sharp pooled moment/oversampling frontier, and the square-case angular law separating pair/twin tails from right-leave-out tails. Relevant equations and result discussions in the 2026 source, the Gaussian oversampling theorem of Nakatsukasa (arXiv:2009.11392), the leave-one-out unbiasedness theorem of Epperly and Tropp (arXiv:2207.06342), and the parameter-dependent randomized approximation analysis (doi:10.1002/nla.2576) were compared by mathematical implication. Their stated conclusions concern estimator construction, conventional approximation bounds, or unbiased expectation identities, not the full combination of exact laws and moment cutoffs. An unpublished/unindexed or differently formulated equivalent calculation remains possible; absence from searches alone does not prove uniqueness.

## Mathematical value — PASS

A user of the recently proposed inexpensive leave-out diagnostics may mistakenly interpret a few numerical samples of a score as having well-behaved mean or variance. This theorem identifies the **minimal amount of left oversampling needed for each moment**, and a qualitative separation between leave-right-out and scalar leave-pair/twin diagnostics. The identity input is the minimal transparent benchmark: the full approximation can be exact while a refitted validation statistic remains heavy-tailed. The classification is a reproducible quantitative reliability limit, not a generic substitution or arbitrary numerical slice.

## Limitations and comparison risks

The result does not claim Gaussian sketch laws for arbitrary matrices, complex sketches, finite precision, or stabilized inverses. The individual leave-out terms are dependent, so the theorem gives pooled asymptotic order but not an exact pooled tail constant. The full-model exactness and the rank-reduced leave-out risk answer different questions. No independent bibliographic audit has been performed.

Self-review: passed. Independent audit: not yet performed.
