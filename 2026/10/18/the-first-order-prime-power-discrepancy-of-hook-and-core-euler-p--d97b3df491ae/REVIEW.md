# Scientific review: first-order hook/core discrepancy

**Correctness — PASS.** The infinite formal-series proof computes every coefficient of the relevant \(p\)-adic logarithm, checks the valuation needed to exponentiate, and uses Frobenius only in characteristic \(p\). The dyadic boundary is included. The standard-library verifier checks 873 coefficients, and independent product expansion confirms the recurrence for selected small instances; neither finite check replaces the infinite proof.

**Originality — PASS with residual risk.** The exact formula determines the complete first-order residue series. Existing abstract-level congruence and accessible prior exact-gcd/first-witness results do not imply all later residues, and searches of mathematically equivalent formulations found no stronger explicit coverage. The full motivating paper and some earlier primary full texts could not be read. Those are real unresolved coverage risks, not novelty evidence.

**Mathematical value — PASS.** A sharp global congruence naturally asks what the next-order coefficient errors are. The answer is a uniform explicit Lambert-series law, clarifying all residue positions and their relationship to divisor sums and the partition product, a structural object strictly stronger than a modulus or finite cutoff. It does not establish higher-order corrections or global distribution statistics.

**Closest literature:** M. Sharma, arXiv:2610.01422 (2026); G.-N. Han, Ann. Inst. Fourier 60 (2010). Standard Euler-product logarithms are used as established background.

Self-review: passed. Independent audit: not yet performed.
