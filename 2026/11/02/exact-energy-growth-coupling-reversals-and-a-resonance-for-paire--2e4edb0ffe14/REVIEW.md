# Research review

## Correctness

**PASS.** The claim fixes the physical quadratic energy and conditions on a complete fair two-choice joint distribution. Every admissible joint law has a single parameter, and the paired Gram matrices average to scalar multiples of the identity by exact polynomial multiplication. This gives a conditional energy identity at any state; independence between blocks justifies iteration for every integer horizon. The affine sign of the derivative with respect to the coupling parameter supplies both sharp transitions. The resonance is verified by the characteristic polynomial and Cayley–Hamilton, and its uniqueness follows from the nonnegative endpoint energy defects. The included SymPy verifier checks exact identities and a small separate enumeration, not merely a finite Monte Carlo estimate.

## Originality

**PASS, qualified by publication-priority risk.** The complete 2021 McLachlan preprint is the closest motivating source: it treats fixed split order and optimized composition methods, but not a joint stochastic coupling of the two adjoint first-order orderings. The Cohen–Vilmart 2020 stochastic Poisson analysis treats additive forcing and deterministic energy-preserving flows, rather than random ordering of a deterministic oscillator. Chen et al. (2020) also investigate additive-noise energy drift rather than the present two-step order coupling. Full-text and semantic searches did not identify a theorem that implies the exact affine multiplier, its double switch or its pathwise resonance. Basic symplectic Euler matrices, Cayley–Hamilton and fixed-order leapfrog are prior results, and no novelty is claimed for them. Older random-matrix and symplectic-product literature has not been exhaustively checked; independent publication-priority review remains necessary.

## Value

**PASS.** Choosing temporal correlation in a fair randomized splitting is a natural design variable because both choices have identical marginal cost and the same individual characteristic polynomial. The exact all-horizon energy law reveals a nontrivial reversal in which opposite-order pairing is better for small steps but same-order pairing is better for moderate steps, including a finite-step exact energy resonance. The result separates deterministic symplectic spectral stability from random-switching mean-energy stability and yields a complete sharp benchmark for coupling strategies, rather than a parameter-free textbook stability observation.

## Boundaries and residual risks

The result is confined to a single-frequency planar oscillator, two equal-length elementary steps per block, exactly fair marginal ordering and independent identical blocks. The energy-optimal policy may not minimize phase error, pathwise energy deviation, expected trajectory error or costs. Exact symbolic verification supports algebraic correctness but cannot replace publication-priority review. The main published source was inspected in full using its openly available preprint. An older specialized study of random products of symplectic Euler maps could potentially supersede the claimed combination; no such direct source was found in the searches recorded with this result.

Self-review: passed. Independent audit: not yet performed.
