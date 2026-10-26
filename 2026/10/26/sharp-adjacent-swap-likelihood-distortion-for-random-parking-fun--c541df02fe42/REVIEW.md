# Scientific review: sharp adjacent-swap likelihood distortion

## Correctness (C): PASS

The exact probability law \(p_n(\sigma)\propto\prod_j\ell_j(\sigma)\) is independently recoverable by counting permitted parking preferences for each car and is published in Colmenarejo et al. (2020, Proposition 3.3) and Pinsky (2024, Theorem 1). For an adjacent rise at positions \(i,i+1\), the two directly swapped suffix lengths change from \((A,B)\) to \((B-1,1)\). A later suffix length can change only if its value lies strictly between the two swapped values and is a new record beyond position \(i+1\); each such change multiplies the mass by \((j-i)/(j-i-1)\). This yields an exact product identity for every allowed permutation. The elementary bounds on the local factor and telescoping suffix product give the sharp envelopes, with explicit permutations realizing both endpoints. Finite global optimization is reduced to a convex one-variable function. The detailed proof covers \(n=2,3\) and both extreme positions, and makes no unjustified asymptotic inference from the finite checks.

Independent direct parking simulation through \(n=5\), complete permutation/swap enumeration through \(n=8\), and 475272 exact assertions in `checker.py` corroborate the formulas and witnesses. These experiments are auxiliary evidence only; the proof covers every \(n\ge2\).

## Originality (O): PASS, with a historical-priority caveat

Published ingredients **already include** the complete mass formula (Colmenarejo et al., arXiv:2009.01124, Proposition 3.3; Pinsky, arXiv:2404.11529, Theorem 1) and global maximum/minimum masses (Pinsky, Corollary 4). They are not claimed as new. The present statement instead optimizes a *ratio of two masses connected by a particular inversion-creating adjacent swap* simultaneously across all outcome permutations at every position, and identifies its sharp witnesses and worst-case growth. Inspection of the relevant primary full texts found no such adjacent-cover extremal statement. Searches for weak-order equivalents, likelihood-ratio extremizers, and permutation adjacent-transposition parking laws in mathematical literature and research records identified no stronger covering result. This finding is a nontrivial inequality extracted by new case analysis and telescoping, not a restatement of the pointwise mass identity or its global extremizers.

Closest comparisons: Pinsky (2024) studies exact mass, marginal last-car location, and records; Colmenarejo et al. (2020) study parking fibers and \(k\)-Naples enumeration; Diaconis–Hicks (2017) study parking preference coordinates; Harris et al. (2022) change the parking rule. Unseen earlier work on adjacent reordering of parking fibers is a residual risk. A missing independent exhaustive priority investigation is not evidence of novelty by itself.

## Value (V): PASS

The model has a strongly nonuniform permutation law whose global mode is increasing, making local inversion-change comparisons a natural structural question. The result determines exactly **how far** a single inversion-creating adjacent transposition can increase or decrease mass at each of the \(n-1\) locations, with opposite behavior at the terminal position and sharp amplification of linear order in \(n\). It supplies exact extremizers, the first sample size where monotonicity fails, and the optimal position scale \(i\asymp\sqrt n\). These quantitative effects are not captured by global extremizer formulas or the typical-mass asymptotics; they sharpen the local geometry of a probability measure on permutations.

## Restrictions and risk

Only classical successful parking functions with uniform preference-vector sampling and adjacent rising swaps are treated. No statement about arbitrary transpositions or modified parking laws follows. Historical priority remains to be examined independently; no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
