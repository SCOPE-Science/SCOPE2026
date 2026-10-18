# Self-review

## Correctness — PASS

The theorem is exact for the defined leading-asymptotic minimax functionals. Weighted Hölder gives every fixed-mixture optimum; simplex first-order optimality produces a feasible minimax density, and strict convexity makes it unique. The local proof subtracts separately normalized powers so that all second-order individual curvature terms cancel. The exact first variation of normalized elementary symmetric curvature gives a unit interval of harmonic coefficients; its sharp variance bound yields the quadratic constant. Direct Gaussian-curvature and spherical fourth-moment formulas prove the spheroid specialization. `verify_minimax.py` passed exact rational checks and numerical quadrature for dimensions 3, 4 and 6; these are corroboration only. No finite-sample optimizer, global uniform stability, or independent verification is asserted.

## Originality — PASS, subject to residual priority risk

Hoehner's complete arXiv primary text (arXiv:2602.18547v1, Section 3) establishes the individual random intrinsic-volume asymptotics and the qualitative rigidity used here; it does not give the worst-relative-loss minimax dual or the all-index near-sphere variance law. The complete published scientific record *Unique minimax area–perimeter sampling law for random polygons in ellipses* covers the analogous planar ellipse theorem and is explicitly excluded by the dimension restriction. The complete indexed record *Exact Hellinger curvature gap for optimal polytope vertex laws* gives a different scalar distance between individually optimal laws, not the common minimax regret. Relevant older joint-approximation work was compared using its available public abstract only, leaving priority risk; no absence-of-hit is taken as novelty proof.

## Mathematical value — PASS

The natural unsolved quantitative question after simultaneous-optimality rigidity is how much every one-density approximation must sacrifice. The d-simplex dual solves this minimax problem for each positively curved body, and the near-ball theorem extracts a universal sharp coefficient and endpoint dominance across all intrinsic volumes. The fully computed ellipsoid series supplies a concrete nontrivial benchmark in each dimension at least three.

## Limitations and closest literature

All error comparisons concern sharp leading expected intrinsic-volume deficits for random inscribed polytopes with a fixed positive boundary density. The proof does not interchange minimax with finite-sample limits. A fixed planar ellipse theorem, a global all-dimension Hellinger-gap identity, and qualitative random rigidity are excluded or distinguished by their exact implications. Unindexed generalizations remain possible; independent scientific audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
