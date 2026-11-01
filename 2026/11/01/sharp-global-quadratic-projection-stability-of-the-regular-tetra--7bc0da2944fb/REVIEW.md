# Scientific assessment: sharp tetrahedral projection stability

## Correctness (C): PASS
The projection formula is re-derived independently from Cauchy's facet formula, with exact facet areas and unit normals. The distance to all six maximizing normals is an exact largest-two-coordinates identity. Permutation and sign invariances exhaust the unit normal sphere in two sign chambers. The two-positive case has exact ratio \(1/2\). The one-positive case has a lower bound from the average of the three negative entries and Cauchy--Schwarz, followed by an explicitly decreasing rational function. Simultaneous equality occurs at the signed permutations of \((3,-1,-1,-1)/\sqrt{12}\). A seeded numerical test is supplementary, not proof. Boundary cases including zero coordinates and maximizing directions have been checked.

## Originality (O): PASS, with limits
The exact all-direction area formula and maximum are previously established in Pandis (arXiv:2601.18436, §1.1, relevant full text inspected), hence not new. Jakimiuk--Pandis (arXiv:2610.23489, §1.2 and §2, relevant full text inspected) establishes quadratic projection stability in dimension three with numerical coefficient \(1/10\), and optimality of the exponent, but does not establish the global optimum coefficient or the nonmaximizing equality directions. Their result follows from, but does not imply, the present sharp estimate; the difference is numerically strict, \((3-\sqrt3)/8>1/10\). Published research-record searches for regular simplex projections, geometric aliases, stability constants and projected-area inequalities found no equivalent claim. Relevant section-stability work concerns planar sections of a simplex, not its planar orthogonal projections. Residual risk: uncatalogued earlier sharp-constant calculations or equivalent norm inequalities may exist. No absence-of-search-hit is treated as a proof of novelty.

## Value (V): PASS
The 2026 quantitative projection theorem motivates determining its best coefficient. The tetrahedron is the smallest nonplanar regular simplex and already has competing square-shadow and triangular-shadow normal orbits. The result gives the exact global coefficient, improves the available numerical bound, and identifies all unexpected nonmaximizing sharpness directions. It is a complete natural invariant for the first nontrivial dimension, not an arbitrary numerical specialization or a local Taylor expansion. Future quantitative projection estimates can use this sharp base case.

## Closest literature and scientific limits
- J. Jakimiuk and C. Pandis, arXiv:2610.23489v1, full text §1.2/§2: all-dimensional quadratic bound with coefficient \(1/10\) when dimension is three.
- C. Pandis, arXiv:2601.18436v1, full text §1.1/§3: exact projection formula and extrema; no sharp coefficient.
- H. Martini and B. Weissbach, *On quermasses of simplices* (1992): earlier projection-volume identity as cited by the two inspected articles; not independently inspected.
- Full-historical-priority verification and independent proof audit remain outstanding. The claim does not extend to dimensions above three.

Self-review: passed. Independent audit: not yet performed.
