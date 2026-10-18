# Scientific review: transpose Lefschetz identity

## Correctness — PASS

The chain trace is calculated in the reduced augmented simplicial chain complex, with the empty face contributing negative one. An invariant face comprises diagonal singleton orbits and off-diagonal pairs. The oriented permutation sign is one negative factor per selected off-diagonal pair, and its alternating chain sign produces minus one negative factor per chosen orbit. For a fixed off-diagonal simple graph, all diagonal selections cancel unless every degree exactly equals the cap. The remaining edge count is exactly half the total degree, proving the formula for all stated integers without asymptotics or reliance on computation. The absolute-trace inequality, cycle EGF, and extremal orientation character follow as detailed in RESULT.md. Independent direct oriented-chain calculations agree for all caps at \(n\le4\), and separate graph-count and cycle-recurrence calculations agree for the tested instances.

## Originality — PASS (residual risk acknowledged)

The nearest primary sources are Singh, arXiv:2006.13632 (2020), particularly Theorem 1.2, and Reiner–Roberts, DOI: 10.1023/A:1008728115910 (2000), particularly Theorem 3.3. The latter supplies rational homology representations under separately permuted rows and columns, but does not identify the additional factor-swapping automorphism's character. The former supplies the extremal sphere equivalence, not its transpose orientation. A documented comparison with other closely matched topology findings distinguishes ordinary graph Morse complexes, rectangular-grid matching complexes, and nonequivariant two-matching complexes from this uniform involution identity. Search did not reveal an equal or stronger statement; it does not establish worldwide uniqueness. An unindexed general equivariant trace theorem could subsume this formula.

## Value — PASS

The central identity is uniform in both graph size and capacity, associates an equivariant topological character to the enumeration of arbitrary regular graphs, and yields an unconditional all-parameter homology lower bound. The two-regular specialization produces an explicit cycle-decomposition exponential generating function, while the extremal cap gives an orientation character not specified by the known nonequivariant sphere classification. These are motivated structural invariants, not an arbitrarily selected instance or a restatement of a known homotopy type.

## Limits and external review

The theorem concerns the alternating character of one involution, not all graded traces or a full automorphism-module decomposition. Finite computation confirms small cases but is not the general proof. The literature comparison has an explicit residual unindexed-source risk. The existing extremal sphere classification is credited as prior work.

Self-review: passed. Independent audit: not yet performed.
