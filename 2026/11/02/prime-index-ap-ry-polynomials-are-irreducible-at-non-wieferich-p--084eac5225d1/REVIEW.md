# Mathematical review

**Correctness — PASS.** The full proof isolates interior binomial coefficients modulo \(p^2\), proves \(\binom{2p}{p}\equiv2\pmod{p^2}\), and verifies the translated polynomial satisfies Eisenstein's coefficient and constant-term conditions. A separate exact arithmetic program checked 189 instances, all coefficients of each shift, and independent evaluations. The theorem is proved symbolically; finite checks are supporting evidence, not universal certification.

**Originality — PASS, with explicit residual risk.** The March 2013 OEIS A005258 and A005259 comments explicitly propose irreducibility of the two Apéry polynomial families as conjectures. The examined Guo–Zeng, Sun, and Pan primary preprints establish related sum congruences and do not supply the stated prime-index irreducibility theorem. Comparable p-adic binomial/Wieferich results do not imply the new polynomial irreducibility. A general irreducibility criterion specialized elsewhere could cover the result, and bibliographic searching is not a proof of novelty.

**Mathematical value — PASS.** Both conjectures are natural number-theoretic polynomial questions. Proving the non-Wieferich prime-index layers by one explicit rational affine Eisenstein shift reveals a structural Fermat-quotient mechanism and yields a uniform result for \(r\ge2\) and \(p\nmid s\), not just a collection of finite computations.

**Closest sources and scientific limits.** See Guo–Zeng (arXiv:1101.0983), Sun (arXiv:1101.1946), Pan (arXiv:1108.1546), OEIS A005258, and OEIS A005259. The theorem does not handle composite indices, the exceptional Wieferich primes, or arbitrary exponents divisible by the index. It does not assert infinitely many non-Wieferich primes. Independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
