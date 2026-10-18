# Independent mathematical audit

## correctness

PASS

For an unselected rook-graph cell (i,j), its fort-neighbor count is exactly r_i+c_j. Thus a nonempty binary selected-cell matrix is a fort iff no zero cell has r_i+c_j=1. The unique occupied p rows/q columns satisfy row bounds 1+1_{q<n} and column bounds 1+1_{p<m}; these conditions are necessary by testing empty lines and sufficient for all unselected cells. Hence the binomial-support double sum of H_{p,q}^{a,b} counts every fort once, and its three-state-per-row-class column DP is an exact finite recurrence. For m,n≥6, the only cardinality-four forts are 2×2 full rectangles; there are no size-five forts, and 2×3 full rectangles and 6-cycles give size six. For m,n≥7 the degree-six coefficient counts two full 2×3 orientations plus six labeled 3×3 cycles, agreeing with formula. Independent brute-force zero-cell test enumerated 2×3:28, 3×3:280, 3×4:2444, 4×4:44167 total forts; smaller dimensions do have degree-five terms and are properly excluded from gap claim. No finite enumeration substitutes for the all-m,n incidence proof.

## originality

PASS

Known fort hypergraph/minimal fort and Cartesian-product bounds concern existence/minimal obstructions, not the weight polynomial counting every nonempty fort of K_m□K_n, nor the universal internal gap with exact six-cell coefficient. Resultary related complete multipartite minimal forts and rook cut homology count different sets. No covering exact enumeration found; risk older zero-forcing appendix implicitly gives the same incidence recurrence.

## value

PASS

Forts are natural obstructions to zero-forcing. The exact all-fort size enumerator (not just minimal forts), polynomial-time integer recurrence, and sharp internal degree-five zero bracketed by positive degrees four/six give a complete counting/classification invariant for the central Cartesian-product family. This is a natural complete family result valuable despite simple elementary proof steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
