# Self-review

## Correctness — PASS

The complete finite-cycle theorem follows by an all-size induction on visited-arc length. The proof independently solves the gambler's-ruin Dirichlet equations for both exit probability and exit-time/event joint moment. Their coefficients imply exact first-moment recurrences for the direction-resolved occupancy process; substituting the explicit closed forms verifies those recurrences algebraically. The conditioning event is explicitly linked to the right-expansion count, and the final-stage holding-time contribution is exactly \(n-1\) for either endpoint. The checker performs exact rational recurrences for sixty levels and is not used as an infinite proof.

## Originality — PASS, qualified

The closest paper, Idnani and Salem (arXiv:2610.15115, October 10, 2026), derives the last-vertex marginal and the unweighted directional occupancy state probabilities. The reviewed relevant full-text sections do not give time-weighted occupancy moments or a conditional mean cover-time formula. Maiti and Sarkar (2019) give unconditional cycle cover-time moments and last-vertex uniformity, not this joint time/location formula in the relevant inspected sections. Targeted published-record searches did not reveal a covering conditional-moment theorem. Priority remains subject to independent literature verification, especially among older cycle-walk treatments.

## Mathematical value — PASS

The theorem characterizes the exact, previously unquantified dependence between **when** a symmetric cycle is covered and **which location** is covered last, despite the uniform marginal last-site law. Its strictly concave quadratic spatial profile has an order-\(n^2\) spread and a complete finite-size classification. This is a natural distributional refinement of the classical cover-time problem, not an isolated normalization or a small computational adjustment.

## Limits

No extension to directional bias, non-nearest-neighbour walks, or the full conditional time distribution is claimed. The claim does not assert independent priority certification.

Self-review: passed. Independent audit: not yet performed.
