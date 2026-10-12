# Scientific review

**Correctness — PASS.** The binary zero-run case split proves adjacent accepted indices are exactly the starts of the pairs at \(4^t-1\). The greedy-arch lemma is supplied with both constructive universality and an explicit shortest absent subsequence witness. The initial six-symbol arch offset, the single correction at a trailing doublet, and the Fibonacci count give the claimed formula with all initial boundaries handled. A standalone direct generator checked every prefix through \(2^{20}\) and exhaustive target subsequences through length 29. The infinity result relies on the symbolic argument, not test coverage.

**Originality — PASS with residual risk.** Full-text reading of the main relevant arch-factorization paper (arXiv:2304.11932v1) and introductory/theorem material of the regular-language universality paper (arXiv:2311.10658v1) found general methods but no Baum–Sweet all-prefix identity, Fibonacci dyadic formula or exponent statement. Literature and indexed research comparisons sought equivalent sparse automatic-word, factorization and counting formulations. A generic algorithm that can compute each finite prefix does not automatically imply a uniform explicit formula. An unindexed prior specialization remains a live risk and no absolute novelty guarantee is asserted.

**Value — PASS.** The complete invariant for every prefix of a canonical automatic sequence is naturally motivated by subword-universality theory, with a structural characterization and precise sublinear exponent; its behaviour is unlike the linear-density examples. The exact formula and logarithmic digit algorithm supply a reusable benchmark for sparse automatic words rather than an arbitrary finite sample.

The shortest-absent-subsequence census and exact interior-factor universality are outside scope. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
