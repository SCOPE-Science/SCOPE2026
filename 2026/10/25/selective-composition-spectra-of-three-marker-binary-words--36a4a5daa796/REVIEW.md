# Review of selective composition spectra

## Correctness

**PASS.** The gap decomposition is unique for weight-three binary words. Consecutive differences of the zero-only substring histogram recover all four zero-gap lengths as a multiset, including the number of zeros among gap lengths. The three-one generating polynomial factors as a known shift times two finite geometric sums, whose coefficient growth identifies the unordered outer-gap pair. Exactly two candidate reversal classes remain when both gap pairs are unequal, and the difference of their one-one polynomials is a nonzero product in \(\mathbb Z[z]\) in precisely those cases. The proof covers all nonnegative zero-gap lengths. Literal exhaustive checks through length 24 are corroborative only.

## Originality

**PASS, subject to a residual unindexed-priority risk.** The closest primary study of full-spectrum equicomposability is Acharya et al. (2014/2015), including their length-eight four-one counterexample. Ye–Elishco (2022) investigates prefix/suffix and length-bounded partial observations, not filtering by the number of marked symbols. Gupta–Mahdavifar (2022) improves reconstruction from the full spectrum. The publicly available exact length-two composition classification similarly has a different observation channel. These stronger or adjacent results do not assert the exact zero-plus-three ambiguity formula or the one-one layer's resolution for every three-one word. The fact that an indexed search did not return the same theorem is not, by itself, proof of novelty.

## Value

**PASS.** Partial mass/composition measurements can lose all substrings of a given number of marked symbols; the theorem gives a closed, sharp ambiguity census rather than only a sufficient decoding condition. It locates a precise one-bit orientation obstruction and removes that obstruction with one natural additional observation layer, for every blocklength. This is a meaningful low-weight boundary case for reconstruction with selective substring measurements, not a numeric table or a routine substitution into a length restriction.

## Limits

The theorem is confined to noise-free weight-three sources and does not establish robustness or optimality of the observation-layer selection. Unindexed early observations of an equivalent low-weight formula cannot be excluded without broader expert literature review.

Self-review: passed. Independent audit: not yet performed.
