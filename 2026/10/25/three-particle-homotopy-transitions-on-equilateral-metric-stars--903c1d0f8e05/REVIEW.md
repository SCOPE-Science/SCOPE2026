# Self-review

## Correctness — PASS

The domain is the unordered third Cartesian power subject to the weak pairwise distance constraint; at positive separation there are no collisions, and the zero-constraint stage is explicitly the symmetric cube. For each arm-occupation vector, the chamber inequalities define a compact convex polytope. A configuration common to distinct chambers has exactly one center particle, so every intersection is a convex center-face polytope. The finite polyhedral nerve theorem applies, including at equality thresholds. Distinct center-face simplices intersect in at most one vertex, reducing the nerve to an incidence graph. Occupancy and intersection feasibility are characterized by necessary inequalities with explicit witnesses. The connectedness arguments and graph Euler characteristic give the two free ranks; the disconnected end stage and the empty stage are handled separately. The standalone combinatorial checker verifies the stage arithmetic for eleven-arm bounds, while an independent LP feasibility stress-test covered all occupancy types for three through six arms at critical and adjacent values. These checks are corroboration, not a substitute for the uniform proof.

## Originality — PASS

The closest inspected primary source is Dover–Özaydın (arXiv:1301.5693), whose convex cells and bound on the number of types apply more generally but do not state the exact three-unordered-particle equal-star homotopy classification. Deeley (AGT 2011) treats two thick particles; the separate thesis abstract describes general Morse methods but its full text was unavailable and remains a risk. Li–Özaydın (arXiv:2603.00914) explicitly studies second configurations, and Wawrykow (arXiv:2401.13821) treats ordered unrestrained configurations. The checked mathematical-record searches and accessible previous claims did not return or imply the positive-separation three-particle thresholds and rank formula. The unrestrained star-braid rank agrees with, but does not imply, the restricted-stage results. Residual database coverage and thesis access risks are described in the structured audit.

## Value — PASS

The equal-arm family is a canonical packing problem in topological robotics. Two sharp geometric separation thresholds produce a nontrivial rank decrease for every number of arms, followed by a discrete component-splitting phase. The result gives exact integral homotopy types across all radii and all \(m\ge3\), not a single computer-generated instance, and makes the general polyhedral critical-value approach explicit in a natural higher-particle example.

Limitations: equal arm lengths, three indistinguishable particles, and stagewise homotopy only; full thesis comparison unavailable. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
