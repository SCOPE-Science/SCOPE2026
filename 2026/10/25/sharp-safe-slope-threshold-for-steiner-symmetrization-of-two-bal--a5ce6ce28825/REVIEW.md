# Scientific review — sharp bounded-slope curvature preservation

## Correctness — PASS
The all-parameter conclusion is supported by a complete analytic proof: an exact cap-Hessian identity, the positive-normal-curvature test in the actual graph metric, a two-by-two matrix-Hessian determinant, a discriminant with the unique nontrivial nonnegative zero \(2+\sqrt6\), and midpoint Hessian failure above that threshold. The proof constructs honest two-unit-ball mixed fibers realizing the bad gradient pairs, with strict endpoint inequalities; this is not an inference from numerical experimentation. A standalone SymPy program checks derivative/determinant identities, the transition root, one strict radical example, and fiber feasibility. The theorem neither covers nonsmooth points nor general multi-ball intersections.

## Originality — PASS with residual risk
The closest first-public 2026 work, Artstein-Avidan–Florentin's *Symmetrizations of Ball-Bodies* (arXiv:2602.14090v1, especially Section 4), shows failure of curvature preservation in dimension three and produces arbitrarily severe curvature loss, but it does not classify the largest disk of cap gradients on which the complete two-dimensional spherical-cap curvature matrix is Loewner convex. The published result *Rank-one curvature loss under Steiner symmetrization of a two-ball lens* shows that at most one principal direction can be deficient and that transverse directions gain curvature; its full statement and proof establish neither the absence of a deficient direction below a universal cap-slope threshold nor sharpness of any such threshold. The geometric theorem here asks a stronger, different quantitative question from these existing results. Prior work on ball-bodies and ordinary Steiner convexity is background, not an implication of the exact slope law. Potentially unindexed earlier matrix-convexity calculations remain a genuine literature risk.

## Value — PASS
The 2026 counterexample creates a natural geometric gap: *how steep must active spherical caps be before symmetrization can first destroy the unit-curvature lower bound?* The finding answers it exactly, with a finite explicit optimal threshold, a complete local all-curvature preservation regime, and realized lens counterexamples arbitrarily near the boundary. This separates the safe part from the failure region of a newly studied convex-geometric operation; it is not just a numerical sample or routine finite verification.

## Independent status and limitations
The proof gives classical curvature conclusions only at smooth positive-length mixed fibers of two unit balls. It gives no claim for seams, three-ball lenses, or a uniform quantitative deficit outside the region. Novelty rests on comparisons with inspected accessible sources and published records rather than a logically complete search of all historical literature.

Self-review: passed. Independent audit: not yet performed.
