# Review of the three-disk hexagon covering claim

## Correctness — PASS

The proof first exhibits an exact full-body cover by three convex disk-containing pentagonal sectors and then proves a matching-and-boundary-gap lower bound with quantifiers over arbitrary disk centers. Every disk in a candidate cover of radius at most \(3/4\) must contain exactly one adjacent vertex pair, since the six vertices force a perfect matching. The gap-contact chord obeys \(\|P_a-Q_b\|_2^2\ge9/4+3(a-1/2)^2\) whenever \(a+b\ge1\). The three uncovered matching-gap edges each require opposite endpoint coverage fractions summing to at least one, and the remote disk cannot help because it is vertically separated by \(\sqrt3>3/2\). All inequalities are tight only at half-edge contacts, which force the radius and center. Exact arithmetic regression checks corroborate the endpoint data and algebra; the infinite proof is analytic. Risk: no independent peer review, but no open logical step identified in the given normalization.

## Originality — PASS, with residual priority risk

The constructive cover is clearly prior art (Borsuk's three-pentagon decomposition as used in Bezdek–Henderschedt 2024). Liu 2022 has directly comparable regular-hexagon three-center experiments but reports a time-limited numerical bound, not the exact equality rigidity. Birgin–Gardenghi–Laurain 2022 gives asymptotic covering estimates and regular-hexagon numerical results from ten disks upward. Those texts do not assert or imply the universal lower bound and complete two-configuration classification. Published research index searches for three-center regular-hexagon covering, aliases, and exact \(3/4\)-radius proofs did not surface a dominating result. Risk: earlier geometric covering or facility-location literature outside inspected records might contain the exact lower-bound proof; indexing absence alone cannot certify first publication.

## Mathematical value — PASS

This is the finite, smallest nontrivial complete three-facility certificate for a canonical convex service region used in the published continuous polygonal \(p\)-center benchmarks. It converts a known constructive upper bound into a sharp global minimum and classifies every minimizer by a structural matching/contact mechanism. It also distinguishes fixed-region exact optimal covering from Borsuk-style universal point-set partition bounds. Its usefulness does not rest on a claimed general theorem for arbitrary polygons.

## Prior work and limitations

Main comparators: Liu (2022), doi:10.1007/s43762-021-00032-9, full-text sections 1 and 4.3; Bezdek–Henderschedt (2024), arXiv:2407.03553v1, full text sections 2 and 5; Birgin–Gardenghi–Laurain (2022 preprint), https://john.pro.br/papers/bglcovering.pdf, geometric introduction, asymptotic theorem and finite numerical experiment section. The main omitted domain is unequal-radius or nonregular-polygon covering. Equality rigidity has not been externally certified.

Self-review: passed. Independent audit: not yet performed.
