# Self-review

## Correctness — PASS

The fixed-sum linearity lemma rules out two shared distinct values between different three-part partitions, including repeated-part cases. A nontrivial intersecting family admits a triangle of three distinct intersection values. When all three triangle members have distinct parts, a fourth member must touch a base intersection value; pair-sum uniqueness leaves at most one extension. When a triangle member repeats a part, the two potential opposite-side extensions have incompatible leftover values, since equality would force the repeated and unrepeated parts to coincide. The proof handles arbitrary positive integers, and counts both multiplicity and nonidentical partitions correctly. Full stars have size the number of unordered pairs of positive summands, and the boundary cases follow by direct listing. The supplied finite verification independently enumerates maximal intersection cliques through order twenty, but is not used to infer the infinite bound.

## Originality — PASS with residual priority risk

Borg (2016), Problem 1.3 and Conjecture 1.6, poses the problem; Remark 1.5 already explicitly exhibits the order-eight exceptional four-member family and recognizes its maximum. Borg proves the canonical-star assertion for small sums and at sums at least the broad large-order cutoff, not the fixed-length three-part exact global determination or the sharp four-member nontrivial upper bound. Person and Schweser (arXiv:2610.01747v1, first posted 2026-10-01) analyze a cubic bound under sufficiently large partition length and provide counterexamples at large length; neither their quantifiers nor their constructions cover the exact three-part theorem. The additional source on strongly intersecting integer partitions concerns coordinatewise, rather than position-free, matching. Published mathematical-record searches using statement variants yielded no equivalent theorem. Unseen sources or independent priority analysis remain a residual risk, so this is not an independent novelty certificate.

## Value — PASS

The theorem finishes a natural fixed-length, one-intersection case of a published exact extremal problem, separates the known exceptional sum eight from the stable regime, identifies every large-order extremal family, and supplies a sharp absolute nontrivial bound. The fixed-sum restriction gives a structural obstruction invisible in ordinary linear triple systems. This is a concrete exact classification problem, not a relabeling, routine known-table recomputation, or arbitrarily selected finite instance.

## Limits

Only \(k=3,t=1\) is determined. The order-eight counterexample is prior literature and is not itself novel. The evidence is a direct mathematical argument with bounded computational cross-checks; external independent audit has not occurred.

## References

- P. Borg, *Intersecting integer partitions*, Australas. J. Combin. 66(2) (2016), 265–275, https://ajc.maths.uq.edu.au/pdf/66/ajc_v66_p265.pdf (Introduction, Remark 1.5, Conjecture 1.6, Theorem 1.8).
- Y. Person and T. Schweser, *Intersecting integer partitions: star bounds and counterexamples at every scale*, arXiv:2610.01747v1, https://arxiv.org/html/2610.01747v1 (Introduction, Theorems 1.1–1.2, proof and counterexample sections).
- P. Borg, *Strongly intersecting integer partitions*, Discrete Math. 336 (2014), 80–84, https://www.um.edu.mt/library/oar/handle/123456789/54963 (different positional intersection property).

Self-review: passed. Independent audit: not yet performed.
