# Scientific review

## Correctness — PASS

The proof derives the eight-codeword Singleton ceiling by injecting the code into any three consecutive coordinates, and it rules out lengths above seven by an explicit 28-pair / four-symbol convexity count. Normalizing by XOR translation is a genuine pair-metric isometry. For every remaining length, every admissible code through zero is exactly a seven-clique of the explicitly defined finite graph; the forward-neighbor recursion enumerates every such clique without omission. Its code checks all counted codeword sets for XOR closure. A distinct all-linear-subspace enumeration matches the through-zero counts, and a 78,125-case endpoint enumeration checks the length-seven conclusion independently. The total labeled counts then follow by counting affine cosets. Re-run the supplied actual files, not detached logs; all three succeed.

## Originality — PASS, with stated uncertainty

The comparison distinguishes unrestricted **nonlinear-allowed** codes from the prior existence and uniqueness-up-to-isomorphism result for **linear** binary three-dimensional codes. Chee et al. (2013) establish Singleton bounds and MDS constructions. Yang–Li–Feng (2016) analyze Plotkin bounds and constructions. Luo–Ezerman–Güneri–Özbudak, Section 4, Theorem 4.2 and its following remark, give a unique linear isomorphism class for the small dimensions, but do not assert that every eight-word nonlinear candidate is affine or give the complete labeled unrestricted counts. Prior related work already obtains length-six affine rigidity and its count of 32; that case is not treated as a separate novel assertion. Search results on the precise claim and aliases did not yield a dominating full unrestricted theorem. Some later plausible sources could not be read completely; lack of search hits alone is not evidence of uniqueness.

## Value — PASS

This resolves the natural **entire feasible range** of binary three-bit-payload, Singleton-optimal cyclic pair-read codes: there are no nonlinear extremizers and only five finite length cases, with exact design multiplicities. It is a complete structural classification for the endpoint of an information-theoretic bound, rather than a random numerical parameter. In practical terms there is no alternative nonlinear optimal design to the known affine families at this high-redundancy-distance boundary. The count for length six was previously known and is included solely to complete the classification.

## Limits and residual risks

The exhaustive classification is small and fully reproducible but depends on running inspectable finite-search code; the supplied proof explains completeness. No claims about other code sizes, alphabet sizes, or read widths follow. The 2024 equiweight-code paper was available at abstract level but its full text could not be read. An additional 2020 source includes a length-seven optimal example but the PDF could not be fully retrieved; earlier unindexed enumerations remain a risk.

Self-review: passed. Independent audit: not yet performed.
