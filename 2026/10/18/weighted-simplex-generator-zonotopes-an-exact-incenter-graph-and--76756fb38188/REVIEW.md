# Self-review

## Correctness
**PASS.** The single dependence among the simplex vectors forces every facet normal to be a coordinate difference. Their exact supports give a full halfspace description. Reflection symmetry establishes global optimality of the centered ball, and erosion of every facet yields all centers. Non-tangent constraints are strictly slack at zero inside the equality subspace, giving affine dimension equal to the number of connected components minus one. The outer radius is an exact projected-square norm of every signed corner. The claimed complexity threshold is exactly PARTITION. An exact-rational checker passed 48 independent finite instances, including 1,328 facet-rank comparisons and 3,936 signed vertices. Finite tests are corroboration, not the general proof.

## Originality
**PASS, with stated bibliographic risk.** The general zonotope support-function and signed-corner radius formulas (Joós–Lángi 2022, equations (2)–(3)) pre-exist; numerical radius identities obtained by specializing those formulas are not independently new. Živaljević (2013, Section 3) treats the unweighted simplex-generator facets. The focal claim here is the explicit classification of **every** Euclidean optimal-ball center and its minimum-weight-graph dimension and contact law, for arbitrary strictly positive weights, with a combinatorial contrast to the outer discrepancies. Relevant primary material and indexed mathematical claims were compared by their conclusions rather than title similarity. The possibility of an unlocated equivalent center-space theorem remains a residual risk.

## Mathematical value
**PASS.** The center polytope exhibits a natural, mathematically sharp stratification by multiplicities of the two smallest generator weights. A generic parameter has an \((n-2)\)-dimensional family of inball centers even though symmetric and certain special nonuniform profiles have a unique incenter. Simultaneously the outer contact set is governed by a different, combinatorially hard partition phenomenon. This is a full center-locus classification for a canonical \((n-1)\)-dimensional zonotope family, not merely a radius computation or an arbitrary small case.

## Literature and limitations
Directly compared the full HTML exposition of Joós–Lángi (arXiv:2206.03204, especially formulae (2)–(3), Section 3, and final problems) and Živaljević (arXiv:1307.5138, Section 3 and Proposition 7). The vector-balancing article Heck–Reis–Rothvoss (arXiv:2210.16460) was checked for its distinct invariant. The 2013 Δ-zonotope result controls the regular unweighted geometry; the 2022 radius identities imply scalar specialization but not the center-locus classification. Residual risk includes an older theorem in weighted root polytopes or metric-polytope erosions. Only self-review has been performed.

Self-review: passed. Independent audit: not yet performed.
