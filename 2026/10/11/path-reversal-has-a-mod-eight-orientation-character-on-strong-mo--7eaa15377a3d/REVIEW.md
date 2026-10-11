# Scientific review: path-reversal orientation character

## Correctness — PASS

The source's full strong matching complex, its downward-closed face condition, the number of graph edges, and the involution on directed incidences have been checked explicitly. The forbidden pairs in Theorem 10.6 are equivalent to exclusion of the two local patterns \(<>\) and \(<->\). Every setwise invariant face is a disjoint union of orientation-reversed vertex pairs, so the sign in the augmented Lefschetz formula is \(-(-1)^{a}\), including the empty-face term. The four-state transfer equations give \(S_{h+1}=-S_{h-1}\) with base values \(1,0\); this solves the signed count for every half-length. The source's Proposition 6.2 and Theorem 6.6 concentrate homology in a one-dimensional degree, converting the Lefschetz count to an actual representation character. The small cases and direct signed traces were checked separately using `verify.py`. The finite checks are corroboration only.

## Originality — PASS with residual risk

The closest primary source, Knudson–Owens–White, arXiv:2609.06844v1, supplies the combinatorial model and nonequivariant homotopy types, but does not compute reversal on homology; that character is not implied by a homotopy-sphere statement. Chari–Joswig, arXiv:math/0011234v1, treats ordinary, generally larger discrete Morse complexes rather than the full strong subcomplex. Published mathematical research records and the nearest matching-complex results were checked for equivariant formulations and stronger implications; no inspected result gives the mod-eight reversal sign for this family. An unindexed duplicate or unnoticed formulation remains possible, so originality is not asserted as an independent external certification.

## Value — PASS

Graph reversal is the canonical nontrivial automorphism of every nontrivial path; its degree on the strong Morse matching homology sphere is a natural invariant absent from the nonequivariant classification. Both signs occur infinitely often even though homology rank is always one in the relevant dimensions. The mod-eight law also distinguishes cases where the reflection quotient has nonzero reduced rational homology from those where its reduced rational homology vanishes. The result is a uniform complete character calculation, not an isolated computation or a small numerical improvement.

## Limits

Only the specified rational involution representation is classified. No integral module structure, equivariant homotopy splitting, or claim of independent review is supplied. The possibility of an equivalent unindexed calculation is a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
