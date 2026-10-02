# Independent audit — Universal cubic-error Gromov--Hausdorff asymptotic for a deleted geodesic ball

Audited: 2026-10-01 UTC

## Correctness — PASS

For sufficiently small radius, the ambient Hausdorff distance is exactly the radius. In normal coordinates the metric on the ball is \(1+O(r^2)\) bilipschitz to Euclidean space. Transporting the sharp Euclidean deleted-ball correspondence therefore changes its distortion by only \(O(r^3)\), giving the upper bound \(c_n r+O(r^3)\). For the lower bound, rescaling the metric by \((h/r)^2\) fixes the deleted radius at \(h\), sends the curvature upper bound to \(O(r^2)\), and makes the convexity-radius branch nonbinding. The Adams--Frick--Majhi--McBride lower bound then has coefficient \(c_n+O(r^2)\), and scaling back gives \(c_n r-O(r^3)\). The one-dimensional small-hole case follows from their exact circle bound.

Risks: The Schott full text was inaccessible in this run, so the exact Euclidean correspondence theorem was checked through the record's quoted theorem statement and the source abstract rather than by direct full-text inspection.

## Originality — PASS

No prior source located before this record states the universal \(c_n r+O(r^3)\) deleted-geodesic-ball asymptotic. Schott supplies the sharp Euclidean coefficient and a weaker Riemannian converse, while Adams--Frick--Majhi--McBride supply the curvature-sensitive lower bound. A later published archive record broadens the local Jung-constant phenomenon but explicitly builds on this deleted-ball result.

Equivalent-formulation search: The search compared the quantified all-closed-manifold deleted-ball asymptotic, not merely the coefficient name.

Broader-coverage search: The earlier ingredients bound the two sides but do not state the matched cubic-error asymptotic.

Database/table check: This is a local geometric theorem, not a tabulated finite invariant.

Claim-versus-prior implication: Neither inspected prior statement alone mechanically implies the claimed \(O(r^3)\) two-sided estimate.

### Source inspections

- **Hausdorff vs Gromov--Hausdorff distances** — Theorem 4 statement and surrounding proof excerpt, including the curvature-dependent coefficient and convexity-radius branch. Assessment: The theorem supports the rescaled lower-bound step and does not state the audited deleted-ball asymptotic.
- **A converse bound for dGH vs. dH for Euclidean space and Riemannian manifolds** — Abstract and bibliographic/version material; full text was unavailable through attempted arXiv, open-access, and institutional routes. Assessment: The accessible material confirms the sharp Euclidean coefficient and a Riemannian converse but does not itself expose the audited cubic-error statement.

## Scientific value — PASS

The result identifies a sharp universal tangent coefficient for a natural local surgery on every closed Riemannian manifold and quantifies convergence at order \(r^2\) in the ratio. This is a motivated structural boundary between Hausdorff and Gromov--Hausdorff distance, not an arbitrary finite specialization.

## Limitations

The theorem concerns the ambient subspace metric on the deleted-ball complement. The cubic coefficient itself is not identified and optimality of the cubic remainder is not claimed. Full text of the very recent Schott preprint could not be obtained through the attempted lawful routes; its abstract and the exact theorem statement cited in the record were compared, so source-version wording remains a residual risk.
