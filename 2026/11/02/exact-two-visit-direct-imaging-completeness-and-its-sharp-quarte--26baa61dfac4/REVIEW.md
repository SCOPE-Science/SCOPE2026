# Review of an exact two-visit direct-imaging completeness theorem

## Correctness — PASS

For the exact circular-orbit, isotropic orientation and separation-only observation model, the proof reconstructs detection as the complement of two unions of antipodal spherical caps. Four disjoint signed cap overlaps produce the probability law. The lens formula is derived using two equal spherical triangles and their excess; the derivative formula is checked by differentiation and drives strict monotonicity and equality-case classification. The rank-two eigenvalue argument proves the worst-case guarantee for *all* orbital orientations, not only in probability. The near-tangency integral proves the \(3/2\) exponent. Standalone `checker.py` replayed 7584 finite assertions including independent spherical-grid quadrature. No finite experiment is used as proof for continuous parameters.

## Originality — PASS within inspected evidence

Brown and Soummer (2010, https://arxiv.org/abs/1003.4700) establish dynamic and accumulated completeness and numerical orbital sampling, and Stark et al. (2015, https://arxiv.org/html/1506.01723v1) already numerically optimize revisits in richer multi-planet mission simulations, including circular orbits. Greco and Burrows (2015, https://arxiv.org/abs/1505.07832) study orbital visibility and phase restrictions; Shao et al. (2010, https://arxiv.org/abs/1003.4702) study circular-orbit images and astrometric synergy. These results cover the general physical concepts, but their stated results do not prove the present explicit IWA-only two-visit phase diagram, plateau/equality conditions, minimax formula, and sharp \(3/2\) onset. Related spherical-cap overlap formulas are acknowledged as geometric ingredients. Mathematical-record and search comparisons found no decisive equivalent statement, not a proof of novelty. A previously published equivalent analytic simplification remains possible.

## Value — PASS

This is a natural idealized instrument-design and observational completeness question: how far apart should exactly two visits be to maximize the chance of seeing a circular-orbit planet, and when can two visits guarantee visibility independent of orbital tilt? The answer is an exact, interpretable schedule classification with a sharp physical threshold and probability law, rather than a sampled ranking or an arbitrary narrow constant. For a normalized working angle of \(4/5\), completeness improves from \(0.6\) on one visit to about \(0.932449\) on two optimally delayed visits. The exact threshold law gives a structural benchmark for simulations.

## Closest literature and limits

The defining completeness notion and repeated-visit problem are not new; Brown--Soummer and Stark et al. are especially close in model motivation. Their richer Monte Carlo and numerical methods can evaluate this ideal case, but the inspected published results do not provide the exact special-case theorem. No claim is made for brightness-limited, noncircular, uncertain-period, finite-exposure or cost-constrained missions. Independent historical-priority assessment and proof validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
