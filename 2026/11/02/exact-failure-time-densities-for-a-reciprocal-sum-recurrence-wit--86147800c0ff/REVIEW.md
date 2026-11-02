# Scientific review

## Correctness — PASS
The result reduces the integer-square condition to \(\gcd(h,u_m)=1\) using the exact reduced-numerator recurrence. Odd and even prime divisors are treated separately, including the parity valuation that rules out a disguised square after cancellation. A valuation check restricts dangerous starting residues to \(v_p(x_0)=v_p(h)\). For primes \(13,17\pmod{20}\), the discriminant \(-5\) eliminates all second-level preimages; for \(5\), the discriminant \(-3\) eliminates all third-level preimages; for \(2\) only a first-level preimage exists. The Chinese remainder theorem makes the resulting local probabilities independent, establishing exact periodic densities. A separate exact-rational computation tests the original recurrence in addition to extensive reduced-pair tests. Finite computations corroborate, but are not used as the proof of the all-parameter statement.

## Originality — PASS, with residual priority risk
The principal comparison is Matijasevick–Rodríguez–Salazar, arXiv:2610.00765v1 (2026-09-30), whose Propositions 2.3 and 4.1 and Theorem B are inputs to the proof; Section 7, Question (1), explicitly poses the failure-count density question. The present claim answers that question for an infinite class, yielding exact *joint time* frequencies and a sharp two-failure regime, rather than simply repeating their bound. Jones–Manes, arXiv:1101.4339, treats broad arboreal Galois phenomena, not the explicit modular frequencies here. Mathematical-record searches found no statement entailing the theorem. A Matijasevick 2026 companion preprint on \(z+k/z\) was identified in the source references but could not be read; an equivalent explicit local-tree result there would threaten priority. An unlocated earlier theorem may also exist. No search result is treated as proof of uniqueness.

## Mathematical value — PASS
The 2026 primary source explicitly raises failure-count densities. The theorem resolves that motivated question for a nontrivial multiplicatively generated infinite parameter class allowing arbitrarily many prime factors, proves a uniform temporal cutoff independent of their number, and provides an exact product formula for all possible failure patterns. The positive-density two-failure family distinguishes this answer from a simple always-square or single-prime calculation. No general solution for arbitrary prime factors is asserted.

## Scope and limits
The parameter class is essential; primes outside it can have deeper preimage trees. Complete source priority is not independently established because the named companion preprint was unavailable, and the result has received no external mathematical audit. The attached verification is finite, with exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
