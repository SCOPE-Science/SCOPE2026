# Scientific review

## Correctness — PASS

The complete theorem concerns nilpotent partial isometries of \(K_{a,b}\) with \(a,b\geq2\). The graph metric forces every nonempty partial isometry to have exactly one of two global orientations, preserving or exchanging the bipartition. In either orientation, nilpotency is equivalent to absence of directed cycles. The labeled exponential formula counts each disjoint path assembly once, with its arrow count and longest path length correctly tracked. The empty map is the unique overlap of the orientations and is subtracted once. For maximal index, the side-preserving bound is the larger side size and the alternating bound is twice the smaller size, plus one in the unequal case; counting Hamiltonian paths and remaining isolated labels gives the four cases. Reproduction from `verify.py` independently checks every rank/index coefficient for 15 small bipartition sizes and matches the sharp extremizer formulas.

## Originality — PASS against inspected evidence

The 2022 star partial-isometry paper (arXiv:2203.05504) studies the monoid's structural description, cardinality, Green relations, generators and presentation for a one-vertex part. The 2022 cycle paper (arXiv:2205.02196) gives presentations, cardinality and Green relations; \(K_{2,2}\) is its four-cycle case. A previous complete nilpotent rank/index census for every cycle already covers \(K_{2,2}=C_4\); a separate star nilpotent enumeration covers the excluded one-vertex-part case, and earlier square-zero results cover further individual slices. None of those special graph or index slices implies the uniform two-sided alternating path census or side-imbalance transition. The 2019 inverse-algebra representation study (arXiv:1906.06415) does not specialize to these rank/index counts. Searches also checked colored partial permutation, nilpotency-index, and graph inverse-monoid terminology. No decisive covering theorem was located, although no search guarantees publication priority.

## Value — PASS

Nilpotency index and domain rank are natural structural statistics of inverse transformation monoids. The theorem determines their entire joint distribution for a canonical graph family, and the exact threshold \(a=2b+1\) exhibits a competition between two qualitatively different maximal-chain mechanisms. This is more informative than a fixed small-size census or a star-only extension, and the resulting formulas permit exact computations for arbitrary side sizes without enumerating partial maps. Further random-assembly and representation questions can use the precise component polynomial, but no unproved downstream theorem is claimed.

## Closest literature and limitations

The main comparisons are Fernandes–Paulista's star and cycle partial-isometry papers and FitzGerald's partial-automorphism inverse-algebra framework. The general combinatorial exponential formula is standard, and the proof uses it rather than claiming to invent it. The index-one convention includes the zero partial map. The theorem excludes one-vertex sides from its new claims and acknowledges the already-known \(K_{2,2}\) specialization, makes no claim of an asymptotic distribution, and does not classify nonnilpotent maps. Search gaps remain for an equivalent formulation in colored partial-permutation or graph partial-automorphism literature.

Self-review: passed. Independent audit: not yet performed.
