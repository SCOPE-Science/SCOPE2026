# Scientific assessment: exact binomial gcd valuations

**Correctness — PASS.** Guo et al. [1, Lemmas 4 and 9] are the published inputs: they exclude extraneous primes and settle whether each prime divides the gcd. The new argument establishes lower valuations using two disjoint carry intervals, then supplies an admissible explicit multiplier achieving equality. The digit-block identity is reconstructed in full, including the prime-power boundary and the case \(m=1\). The finite verifier separately tests exact formulae and witnesses; it is supplementary, not a proof.

**Originality — PASS (best-knowledge, residual risk).** Direct inspection of [1, §§1–2, Theorem 1 and Lemmas 4 and 9] shows its stated target is the prime-support or gcd-one criterion, not the exact exponent formula. Classic binomial gcd literature cited there changes the fixed-upper/lower-index family. Searches for the exact valuation, equivalent multiplier-gcd formulation, and a pre-existing sequence/table description did not reveal an equivalent statement. An unindexed classical identity, or an implicit derivation in older gcd literature, remains possible. Search absence alone does not certify novelty.

**Mathematical value — PASS.** This computes the *full value of the natural gcd* underlying the recent OEIS A080170 resolution; its exact prime powers, witness multipliers, and the bound \(D(k)\mid k+1\) are not consequences of a support-only criterion. It is a natural complete invariant rather than an arbitrary cutoff. The proof requires a nontrivial carry-versus-multiplier optimization.

The closest primary literature is Guo–Qiu–Cao–Feng–Gao, arXiv:2606.22997v1, and the standard Kummer–Legendre identities. Limitations include the specific multiplier range, dependence on the published support lemmas, potential implicit older coverage, and the absence of independent validation.

Self-review: passed. Independent audit: not yet performed.
