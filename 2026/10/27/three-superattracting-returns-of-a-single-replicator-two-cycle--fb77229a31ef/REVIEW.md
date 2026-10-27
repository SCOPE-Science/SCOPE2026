# Scientific review

## Correctness — PASS

The statement requires only three distinct zero multipliers, not an exhaustive root census. The proof rigorously parametrizes all nontrivial two-cycles by their amplitude, establishes strict monotonicity of the intensity-amplitude relation, derives the derivative-product identity, and checks four signs in the required order. Two nontrivial interior sign witnesses use rational orbit coordinates and inequalities for logarithms proved from finite exponential series. The boundary signs are analytical limits. Continuity supplies three disjoint roots and a robust open equilibrium interval. Standard-library verifier arithmetic confirms the fractions and limiting examples but is not taken as an infinite proof.

## Originality — PASS under inspected sources

Closest mathematical result: *Singular symmetry-breaking threshold for the period-two orbit of a replicator map* (2026) establishes a unique multiplier \(-1\) crossing near equilibrium symmetry, but says nothing about the count of crossings of zero; neither assertion implies the other. The original map literature in arXiv:2412.16379 and arXiv:2108.06739 treats existence, bifurcation, and stability, not a rigorous triple zero crossing at fixed equilibrium. Crucially, Chotibut et al.'s NeurIPS 2020 supplemental analysis **already investigates superstable parameter curves** (Sec. F, pp. 23–27): the novelty is only the exact three-intensity fixed-equilibrium theorem in an open parameter set, not the existence of superstable curves. The inspected figures and approximations do not state an implication proving the present theorem. Search cannot exclude an unindexed earlier exact classification or a covered implication hidden in other literature; this is the main priority risk.

## Value — PASS

The natural invariant being studied is the number and ordering of the critical passages of a distinguished unique periodic branch as intensity changes at fixed game equilibrium. Repeated superattraction might be obscured by the uniqueness of that branch and the previously derived unique stability exit. A rigorous open-family nonmonotonicity certificate is a motivated boundary/counterexample to the tempting single-passage picture, rather than an arbitrary fixed-value computation. The result is intentionally an existence lower bound, not a global classification.

## Scope and integrity

The result is independent of the approximate root values displayed by the verifier; no extrapolation or independence claims are made. The theorem does not give an exact maximum number of superattracting intensities and admits residual historical-priority uncertainty. No third-party paper is republished. Independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
