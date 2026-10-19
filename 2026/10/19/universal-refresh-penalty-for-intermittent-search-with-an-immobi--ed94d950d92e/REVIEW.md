# Self-review

**Correctness — PASS.** At the reset site, the difference of inactive and active mean times follows from a one-step switching/refresh equation. Eliminating the inactive state reduces every active mean to a reset-only renewal at an effective rate; this yields the universal penalty exactly. The independently built finite killed-generator checker passed 864 direct comparisons, with maximum absolute discrepancy approximately 1.35×10⁻¹². The infinite-state theorem is analytic, not inferred from those numerical checks.

**Originality — PASS.** Evans and Majumdar (arXiv:1808.06450) treat two ballistic velocity states and distinguish internal-state resetting protocols; Bressloff (DOI:10.1088/1751-8121/ab97e0) treats switching diffusion with internal state refreshed at resets. The present result applies to a strictly immobile off mode and any active Markov search, with a precise universal all-eta penalty and on-start invariant. Available published-finding corpus and literature checks found no direct implication. A general renewal formalism may implicitly subsume the result, and the full Bressloff paper was inaccessible. Independent priority assessment remains necessary.

**Value — PASS.** The theorem gives a geometry-free quantitative design rule for a natural partial reset of a searcher's mobility, without computing spatial hitting times. The off-state immobility is essential; no such universality is claimed for two moving modes or for general non-Poisson protocols.

Self-review: passed. Independent audit: not yet performed.
