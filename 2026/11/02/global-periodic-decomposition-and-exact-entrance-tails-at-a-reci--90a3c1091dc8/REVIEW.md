# Scientific review: reciprocal-slope periodic decomposition

## Correctness — PASS

The statement fixes exact branches, endpoint conventions, a full real parameter interval \(k>1\), and an explicit normalization. Four half-open intervals permute cyclically, with pointwise fourth-return identity; they exhaust all four-cycles. The complementary strips alternate if they avoid the periodic set, and the two-step affine expansion with slope \(k^2>1\) forces the unique repelling pair \(\{-k/(k+1),k/(k+1)\}\). Explicit treatment of three leftover boundary points closes the global argument. Affine inverse slopes prove an exact finite-time survivor measure \(2/k^{n+1}\); dividing by normalized domain length establishes the entrance-time law. Poincaré recurrence plus the canonical interval selector yields every invariant probability. Symbolic identities and rational interval calculations were independently checked with the packaged source, but finite tests are not used as infinite proofs.

## Originality — PASS within inspected evidence

The 2021 defining paper and 2023 full open-access follow-up provide the PWL family, fixed-point absence, selected chaotic parameter conditions and numerical bifurcations. A prior restricted-itinerary result on the same map already establishes a continuum of four-cycles precisely when the slopes are reciprocal; that component is explicitly excluded from the novelty claim. Its restricted statement does not imply that *all* other orbits eventually enter those cycles, that there are exactly two non-four-periodic points, that the nonentrance probability has a geometric law, or that every invariant probability has the stated orbit-mixture decomposition. A prior three-cycle census for the same family addresses a different invariant, and a prior sharp derivative-expansion bound assumes a disjoint parameter regime. Related periodic-zeta and neutral-fiber results concern different maps. Targeted literature, indexed finding and parameter-alias searches revealed no statement covering this combined global classification.

The substantial residual originality risk is incomplete access to the original 2021 defining paper. Only its abstract and first-page information were accessible, although the complete accessible 2023 follow-up was inspected. The 2022 comparative chapter was also abstract-only. These risks require later expert or full-text verification before any external publication-priority assertion.

## Mathematical value — PASS

A codimension-one reciprocal-slope cancellation sits at the edge of the empirically observed period-four region. The complete transient-versus-periodic decomposition turns an incomplete local itinerary calculation into an exact global account of every orbit and every invariant measure. The geometric entrance law gives a natural finite-time metric for how rapidly generic starting points fall into the neutral four-cycle continuum, and its mean \(1/[k(k-1)]\) diverges at the sharp nonexpanding boundary \(k\downarrow1\). These are dynamical questions that numerical Lyapunov diagrams and the existence of four-cycles alone do not answer. The contribution is a complete natural classification with a sharp probabilistic transient law, not the already-known period-four identity in isolation.

## Scope and limitations

The theorem concerns exact real arithmetic on the reciprocal-slope curve only, not arbitrary slopes, finite-precision devices, or security claims. The distribution law assumes uniform initialization in the normalized state interval. The 2021 source and 2022 comparative chapter were not read in full. No external mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
