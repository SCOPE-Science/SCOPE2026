# Scientific review: prime-Fibonacci seed thresholds

**Correctness — PASS.** The recurrence, two-step maximum descent, and precise stopping convention are explicit. The exact census includes all 429680 ordered pairs of distinct odd primes at most 4919, with two independently implemented transition algorithms (trial division versus sieve-factor recurrence). Both yield the claimed complete 22-entry threshold prefix and exactly one length-\(23\) seed at the final ceiling. The extracted package checker is executable without external dependencies. This is a finite exact certificate, not a claim of exhaustive search over larger thresholds.

**Originality — PASS, with residual risk.** Alm and Herald (2015, arXiv:1507.04807) established termination and arbitrarily long trajectories, but do not supply sharp initial seed-ceiling thresholds or classify the 23-term extremizers. Guy, Khovanova, and Salazar (arXiv:1207.5099) study a different subprime recurrence. Searches for optimal seeds, stopping depths, equivalent smallest-odd-divisor formulations, and the specific \((4007,4919)\) witness yielded no dominating published theorem; a privately computed or poorly indexed identical table remains possible.

**Value — PASS.** The optimal initial maximum prime for a specified survival depth is a natural quantitative invariant of this previously qualitative terminating recurrence. A complete initial sequence of sharp thresholds, including a uniquely attained 23-term extremum, supplies exact comparison targets for future bounds and algorithms and is more informative than isolated long examples. The result is finite and does not purport to give an all-length growth law.

Self-review: passed. Independent audit: not yet performed.
