# Self-review

## Correctness — PASS

The exact identities are reconstructed for the finite configuration space using the Fourier/Vandermonde eigenfunction identity, Cauchy--Binet normalization, a projection-determinantal two-point occupancy calculation, and the continuous-time path likelihood. With stationary starts, the endpoint logarithm has mean zero, leaving an exact traffic correction. The strictly positive coefficients agree with direct rate-formula relative entropy and all enumerated test cases. The sparse expansion follows from a uniform Taylor expansion at fixed particle number; the two-particle intercepts follow from the sine product identity and a convergent beta integral. The attached standalone checker executed 8,839 assertions. This computation checks finite instances only; the analytic argument establishes the general quantifiers.

## Originality — PASS, with historical-priority risk

Johnston, *Continuous Kasteleyn theory for the bead model* (arXiv:2207.13538), Theorems 1.11 and 1.12 and Section 6, already supplies the noncolliding Vandermonde stationary process and the exact traffic-based change of measure; Shiatis (arXiv:2610.00741v1, Section 1 and main comparison) generalizes this relationship. Neither inspected text states the **pair of stationary path-entropy coefficients**, their diverging ratio for fixed particle count, or the two-particle mesoscopic-time constants. The new claim concerns quantitative information loss under both directions of an explicitly different initial law, not the pre-existing change-of-measure construction. General relative-entropy formulas for conditioned processes are relevant and are acknowledged; the extraction of these two closed ring-specific coefficients and their competing scaling regimes is the additional content. Searches for exact entropy comparisons, equivalent process names, and sparse-asymmetry limits produced no directly covering source. This is a qualified priority assessment, not independent confirmation: a related implicit derivation may exist in older determinantal or conditioned-chain literature.

## Mathematical value — PASS

Two Markov chains with identical allowed jumps, and mutually absolutely continuous finite-time path laws, have different rates of statistical distinguishability according to the direction of KL divergence. Here the exact rates have distinct powers of ring size when the particle number is fixed, while in the macroscopic-density regime both are extensive. The two-particle result identifies the natural \(n^2\)-time crossover including nonzero stationary information costs, making precise a boundary between essentially indistinguishable and strongly distinguishable stationary histories. This is a natural quantitative observable of the exclusion-versus-noncollision comparison, rather than an arbitrary parameter slice or a numerical improvement.

## Closest literature and limitations

- Samuel G. G. Johnston, arXiv:2207.13538: the closest original transfer-operator and stationary-law source. The explicit KL and sharp scaling statement are not present in the inspected text.
- Rohan Shiatis, arXiv:2610.00741v1: the recent motivating extension and exact traffic transformation. The inspected text does not give a two-way information comparison.
- Raphaël Chetrite and Hugo Touchette, arXiv:1506.05291: general conditioned-process and relative-entropy ideas. Only its accessible abstract was evaluated for relevance, not an exhaustive full-text priority decision.

The results require stationary starts on a finite ring, uniform clockwise unit rates and the specified Doob transform. They do not claim new spectral identities, transition kernels, or a universal result for arbitrary exclusion processes. The precise formulas may be implicit in the earlier cited theoretical framework; this remains the chief priority risk.

Self-review: passed. Independent audit: not yet performed.
