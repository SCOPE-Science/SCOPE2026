# Scientific review: triangle reconstruction from boundary distance moments

## Correctness — PASS

The claim assumes a genuine triangle, known perimeter and two independent arclength-uniform boundary points. The exact conditional same-side and adjacent-side integrals give both moment identities, including the fourth moment. The nondegenerate Heron invariant \(h>0\) permits inversion; Vieta's formulas reconstruct the normalized three side lengths uniquely. The sharp global ratio bounds are supported by a positive polynomial/monotonicity certificate, including the limiting unattained upper constant. Lagrange multipliers and connectedness of a fixed-product level set give the complete fixed-perimeter-and-area fourth-moment envelope. The attached reproducibility code checks the conditional integrals, symbolic identities, inverse, and direct Monte Carlo examples; the continuum claims rely on written arguments, not empirical extrapolation.

## Originality — PASS, subject to stated bibliographic risk

The closest published 2026 triangle-boundary-distance result gives only the second moment. Published work on fourth chord moments of parallelograms has a different body family and observable. Bonnet et al. (2020) concern the mean distance between interior random points in convex bodies; Bäsel (2021) studies distance moments for area-uniform points in regular polygons. Their statements do not imply the combination of arbitrary-triangle boundary fourth moment, explicit finite-moment shape inversion, sharp ratio range and fixed-area extremizers. An earlier Gates (1982) abstract treats triangle recognition from odd moments of a random-chord distribution, but it does not establish the present sampling convention or this particular finite set of even boundary-endpoint moments; its full text was unavailable for comparison. Unindexed or inaccessible earlier results remain a genuine residual originality risk.

## Mathematical value — PASS

The observable addresses an identifiable inverse question: how little information about boundary-to-boundary random distances suffices to determine a triangle's shape? The second moment alone measures only normalized area, whereas adding the fourth moment yields the missing independent symmetric parameter and an exact cubic reconstruction. The sharp fourth-to-second moment range and complete isosceles envelopes at prescribed perimeter and area provide independently meaningful geometric statistics, equality classifications, and diagnostics of near-degeneracy. The result is not a re-labeling of a known moment bound or an arbitrary finite table.

## Scope and limits

The inverse requires known perimeter and positive area. At small area the reconstruction is ill-conditioned in general because an invariant is divided by \(h\). It neither identifies oriented triangles nor extends immediately to other sampling conventions. The literature review is not exhaustive; no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
