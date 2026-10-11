# Scientific review: A sharp Steiner-area phase diagram for regular disk triangles

## Correctness — PASS
The geometry gives the exact normalized area, perimeter and Steiner-offset objective. The parameter interval is bijective with finite radii. The decisive slope-ratio curvature inequality is supported by a complete, executable exact Laurent-Fourier and degree-20 Taylor coefficient certificate plus a rigorous uniform remainder bound on the entire continuous interval. The coefficient inequalities are proved by elementary estimates. Exact endpoint derivatives, derivative signs and all boundary-attainment cases were reconstructed. Finite symbolic verification supplements but does not replace the infinite-interval inequality.

## Originality — PASS (literature-limited)
The initiator Fodor–Robock–Sagmeister (arXiv:2602.19300, Theorem 1.1) establishes a fixed-radius isominwidth area theorem. Bezdek (arXiv:0903.5361, Remark 1.4) gives **known** area and perimeter functions for regular disk triangles in alternative parameters; the scalar formulas and Steiner identity are not claimed as novel. The new nontrivial step is the exact global curvature inequality for the area–perimeter tradeoff, giving a unique intermediate optimizer and two sharp transitions. Published records checked for equivalent offset minimizers, aliases, radius reparameterizations, stronger covering theorems, and exact tables did not supply this classification. The full text of arXiv:2606.02882 was not accessible; it remains an explicit originality risk. The absence of a matching search result is not a novelty certificate.

## Value — PASS
The Euclidean isominwidth extremizers provide a canonical interpolation from an equilateral triangle to a Reuleaux triangle. Outer-parallel area depends on the natural independent area and perimeter invariants. It is mathematically meaningful that an *interior* curved body outperforms both endpoints on an exact nonempty offset interval. The theorem classifies sharp constants, optimizer uniqueness, endpoint attainment and the shape transition; it does not infer a global inequality for arbitrary convex bodies.

## Scientific limitations and residual risks
Only regular disk triangles at fixed minimal width are compared, not all disk-polygons. Primary work by Bezdek already supplies scalar formulas, and a related 2026 stability source was only partially accessible. No independent proof check or comprehensive historical uniqueness claim is represented. The reproducibility certificate requires Python 3 and SymPy.

Same-model review: passed. Independent audit: not yet performed.
