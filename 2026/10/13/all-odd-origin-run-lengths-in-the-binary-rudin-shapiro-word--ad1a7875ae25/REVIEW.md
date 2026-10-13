# Scientific review: all odd origin-run lengths in Rudin–Shapiro

## Correctness — PASS

The first-change index exists for all differences by Sobolewski Theorem 1.4 for \(d\ge3\) and direct checks for \(d=1,2\); it cannot be even because appending a zero does not change the parity of binary adjacent \(11\) pairs. For each width \(L\), the number \((2^L+1)x\) concatenates two identical \(L\)-bit blocks whenever \(0\le x<2^L\), so its output parity is exactly the product of the end bits. For every odd prescribed \(k\ge3\), the specified odd multiplier \(a\) satisfies \((k-2)a<Q\le ka<2Q\); consequently all earlier progression terms have output zero and term \(k\) has output one. The \(k=1\) case and infinite multiplicity are handled explicitly. The stated cubic witness bound follows from choosing the least admissible power of two. The standalone checker independently recomputes outputs from digit strings and checks numerous finite cases, but the proof, not the tests, establishes all quantifiers.

## Originality — PASS

Sobolewski, arXiv:2204.05287, Section 6 Problem 8 explicitly asks for the attained fixed-origin lengths and conjectures all odd lengths occur for patterns ending with one. Its Proposition 5.4 already uses duplicated binary blocks and establishes a fixed-multiplier asymptotic, so that mechanism is fully credited. The new contribution is the exact all-odd attainment theorem and the controlled multiplier/width choice giving a cubic bound and infinitely many witnesses per length. Theorem 1.4 gives difference-dependent maxima, not the complete range. Joshi–Rust, arXiv:2501.05830, Section 3.3 and the OEIS records A364995/A380593 concern the supremum over all starting positions, not this fixed-origin spectrum. Targeted published-finding corpus searches returned no equivalent result; similarity matches about unrelated Shapiro Fourier constants and Rudin–Shapiro string attractors do not imply this theorem. Residual risk: an unindexed earlier elementary corollary of Sobolewski's doubled-block calculations may exist; search absence is not novelty proof.

## Value — PASS

The exact range resolves the Rudin–Shapiro component of a concrete published open problem, not an arbitrary slice or a known-table recomputation. Both exclusion and construction are genuinely uniform in the prescribed length. The explicit polynomial witness bound additionally makes every attainable length efficiently realizable. No result is claimed for the broader family of patterns or the extremal starting-position invariant.

Self-review: passed. Independent audit: not yet performed.
