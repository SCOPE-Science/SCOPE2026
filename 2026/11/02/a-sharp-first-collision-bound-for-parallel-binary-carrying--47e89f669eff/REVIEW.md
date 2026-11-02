# Correctness, originality, and value review

## Correctness: PASS

The asserted update is synchronous and applies only to finite nonnegative coefficient sequences. Weighted-value conservation follows from the quotient/remainder decomposition at each position. Any coefficient at least two at round \(t+1\) requires a predecessor at least two one index lower at round \(t\); induction forces surviving nonbinary coefficients into positions at least \(r+t\). At round \(\lfloor\log_2N\rfloor-r\), such a coefficient would alone exceed the preserved value \(N\). This establishes the universal finite bound. In a binary convolution, coefficient zero is at most one, establishing the sharper product-bit bound. Explicit binary digits of \((2^k+1)/3\) for odd \(k\) give a carry wave lasting exactly \(k-1\) rounds, proving uniform sharpness. The verifier checks 1,359 coefficient vectors, 65,025 multiplier pairs, and 25 sharpness-family cases; no finite test is treated as an infinite proof.

## Originality: PASS, with residual priority risk

Iizumi (2026), Definition 4 and Lemma 1, defines the same model and proves termination without the claimed quantitative bound. Its Remark 6 gives the original upper bound as an empirical observation and its Question 9.5.3 explicitly asks for proof. Proposition 1 already proves the sharpness family, which is attributed rather than claimed as new. The stronger index-sensitive theorem and resulting proof of the conjecture were not found in the inspected text or targeted research-index searches. Izsak and Pippenger (2011) investigate the expected longest carry-propagation chain under a different randomized computational schedule, so their distributional results do not imply this deterministic all-input bound. Residual risk: an equivalent first-collision argument might occur implicitly in literature on parallel normalization or be discoverable from an unindexed source; indexed full-text inspection is not a guarantee about every appendix or later publication.

## Mathematical value: PASS

The result settles a precisely formulated new number-theory question, upgrading a finite experimental inequality to a theorem for all positive factors, with a strictly more informative first-collision parameter and a universally sharp product-bit bound. It supplies a finite-speed propagation principle that can be reused to bound parallel carry normalization of general nonnegative integer sequences. The proof does not settle separate height-dependent conjectures or classify equality cases.

## Closest literature and scientific limits

M. Iizumi, *Binary convolution height: Structural invariants of integer factorisations*, DOI: 10.1080/27684830.2026.2727395, online 2026-09-11, especially Definition 4, Lemma 1, Proposition 1, Remark 6, and Question 9.5.3. A. Izsak and N. Pippenger, *Carry Propagation in Multiplication by Constants*, DOI: 10.1145/2000807.2000822, analyzes a distinct probabilistic task. No independent priority or proof assessment is asserted.

Self-review: passed. Independent audit: not yet performed.
