# Review: The support-preserving three-prime cototient orbits

**Correctness — PASS.** Multiplicativity of Euler's totient gives the exact first-step factorization. A support argument proves necessity; three explicit induction segments prove sufficiency and the full orbit height. The game has only one move at each nonterminal position, so parity of the exact height gives the nim-value. No asymptotic, heuristic, or finite-experiment inference is used in the symbolic proof. Separate exact-integer replay covered 168 qualifying exponent triples and 59 excluded odd primes below 300.

**Originality — PASS relative to checked literature.** Ellis et al. (2023), Section 4, treat prime powers and two-prime starts; Iannucci–Larsson (2021), Section 3.1.2, establish rules and selected prime-power/two-prime values and leave broader classification open. The exact closure criterion for all triple supports with prime set \(\{2,3,q\}\) and the complete triple-support orbit do not follow as stated from those two-prime results. Mathematical-record queries for cototient iteration, NONTOTIENT, ternary-repunit primes, equivalent initial supports and exact heights found no matching formula. A possible unindexed or implicit earlier formulation remains a residual novelty risk.

**Value — PASS.** The question is a motivated arithmetic-dynamics extension to the first three-prime-support stratum. A sharp classification of precisely when the full support is closed under iteration is coupled to a complete orbit and an exact height, not merely a congruence observation. The result yields exact nim values for infinitely many starts already at the primes \(13\) and \(1093\), without claiming infinitely many eligible primes.

**Scope.** Assumptions require prime \(q>3\), \(a,b,c\ge1\), and iteration only until \(1\). Neither the number of admissible primes nor arbitrary leaking supports are classified. The finite verifier cannot substitute for the universal proof.

Self-review: passed. Independent audit: not yet performed.
