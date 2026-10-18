# Scientific review

## Correctness: PASS
On an unlabeled directed permutation cycle every formula is globally rotation invariant, so program tests reduce to identity or empty relation on each truth-profile cell. A regular program without tests has an effectively semilinear set of net displacements by the Parikh-image theorem. The integer congruence condition on one linear component is exactly \(\gcd(n,c_1,\ldots,c_r)\mid b\); allowing nonnegative coefficients via residues modulo \(n\) is essential to the reverse implication. Components with all zero generators yield finite divisibility sets or the universal set. Induction handles arbitrary nesting. The converse follows from explicit prime-power divisibility and singleton formulas. The Chinese remainder theorem yields the nondefinability separation. The finite checker passed \(7{,}490\) checks, without substituting experiments for proof.

## Originality: PASS, subject to literature coverage risk
Full text of Bednarczyk–Swoboda (2026) was inspected in its preliminaries, main construction, conclusions and relevant appendices; it addresses finite satisfiability on arbitrary frames rather than this precise cycle-length expressivity algebra. Their 2026 workshop article was inspected for related loop semantics and scope; its restricted finite-model problem does not imply the spectrum characterization. The constructive Parikh semilinearity theorem supplies a known proof ingredient but not the combined expressivity, converse construction and separation. General expositions of dynamic logic and broader first-order spectrum theory do not establish this exact result. Targeted semantic database and primary-literature searches found no direct or dominating theorem. A mathematically equivalent result may nevertheless exist under a different automata-theoretic formulation; that remains a priority risk.

## Value: PASS
The result completely identifies the Boolean algebra of cycle-length observations made by an expressive looping program logic, despite unrestricted negation and nested tests. It gives constructive normalization and equivalence checking for a natural family of finite transition systems, and exhibits a sharp separation from arbitrary regular unary arithmetic predicates. The exact arithmetical closure is the central structural result, not a size-limited computation or cosmetic corollary.

## Scientific boundaries
The proof applies only to unlabeled single-cycle permutation frames. It is not a general finite-satisfiability result, and the checker is finite-only. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
