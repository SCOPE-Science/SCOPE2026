# Scientific review: triangle-local John ellipsoids of cut polytopes

## Correctness — PASS

The proposed ellipsoid is fully characterized for finite simple graphs with at least one edge and no \(K_5\) minor. Uniqueness of John's ellipsoid and elementary cut-switching fix the center at the half-vector and annihilate every off-diagonal shape-matrix entry. Barahona--Mahjoub Corollary 3.10 supplies every relevant supporting facet. Its odd-cycle slack is exactly \((k-2)/2\), while diagonal ellipsoid support is \(\sqrt{\sum_{e\in C}s_e}\). For lengths at least four, coordinate caps alone imply the required bounds; triangles alone impose the nontrivial coupled bounds. Existence and uniqueness follow from a strictly concave objective. Tangency equality determines *all* facet contacts. Explicit positive Lagrange multipliers certify the wheel and book parameter formulas. Exact-rational `verify.py` passes 22 finite instances, 1,522 signed-cycle inequalities, and 12,840 cut assignments; finite tests are corroboration, not the infinite proof.

## Originality — PASS, subject to priority uncertainty

The full-text Barahona--Mahjoub 1986 result is a **facet classification**, not an ellipsoid calculation. Chimani et al. (2019) extend minor-free facet/combinatorial studies without calculating inscribed ellipsoids. Nikolaev (2024, arXiv:2402.13591, primary MSC 52B05) studies graph-of-polytope adjacency, clique numbers, and graph diameter, rather than John semiaxes or facet contacts. Gartsman--Linial (2023) calculates the John ellipsoid of the **metric** polytope and explicitly asks about the **cut** polytope in Section 4, which does not logically cover the present minor-free result. Published-result searches for graph cut-polytope John ellipsoids, switching-diagonal forms, log-determinant triangle incidence, and longer-cycle redundancy revealed no exact or stronger coverage; this is evidence of noncoverage among inspected sources, not a global priority proof. A differently named or uninspected optimal-design treatment remains a risk. Comparisons are recorded in `AUDIT.json`.

## Value — PASS

This is a natural, complete structural invariant for a broad infinite minor-closed family of cut polytopes, not a one-off numerical fit. It reduces a potentially enormous and long-cycle facet system to a strictly concave program indexed just by edges and triangles, determines every principal semiaxis and contact facet, and proves genuinely nonuniform formulas for wheels and page-book graphs. The disappearance of length-five-and-higher facets from all contacts, together with the sharp length-four boundary case, is geometrically informative even though the defining cycle facets remain important for the polytope itself. The general graph solution is a finite variational characterization rather than a radical closed form, and general graphs with a \(K_5\) minor remain outside its scope.

## Residual risks and limits

The proof relies on the correct applicability of the complete cut-polytope facet description to graphs without a \(K_5\) minor. A distinct publication under D-optimal design, optimal-volume inscribed ellipsoid, or covariance switching could precede this formulation; independent literature and proof verification have not occurred. No claim is made about a minimum-volume circumscribed ellipsoid, graphs containing a \(K_5\) minor, or a closed-form polynomial in arbitrary graph parameters.

Same-model review: passed. Independent audit: not yet performed.
