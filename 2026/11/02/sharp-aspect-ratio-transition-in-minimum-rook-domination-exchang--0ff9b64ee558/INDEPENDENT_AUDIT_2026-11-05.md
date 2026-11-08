# Independent mathematical audit

## correctness

PASS

For 2<=m<=n, minimum domination requires covering every row or every column; when m<n only one rook per row is possible, giving a Hamming exchange graph. For m=n, configurations are the union of row functions and column functions with permutation overlap; counting near-permutation cross edges gives the stated three-degree classes and exact edge count. A permutation placement has eccentricity <=n; disjoint Hamming targets give radius >=n. For cross-layer A_f,B_g, expected matched overlap of random permutation bridges is 2; if no bridge attains >=3, all 2x2 additive differences vanish, forcing both functions constant for n>=3. Direct bridge for constant functions gives distance <=2n-3, and row/column support changes give >=2n-3 for a full-column/full-row pair. The n=2 Johnson graph is handled separately. Independently enumerated all min dominating subsets and full exchange BFS for n=2,3,4: (vertices,edges,diameter)=(6,12,2),(48,234,3),(488,3936,5), and exact predicted degree strata; finite enumeration only corroborates all n theorem.

## originality

PASS

Best-of-knowledge PASS for evaluated jump minimum-domination graph degree distribution and radius/diameter transition. Mertens explicitly already gives minimum domination counts, which are not new. Existing gamma-graph survey and add/delete reconfiguration results do not yield the exact rook jump metric in inspected material.

## value

PASS

A natural jump-reconfiguration graph exhibits a sharp aspect-ratio transition: a single rectangular Hamming layer versus two overlapping Hamming layers with new degree strata and unexpectedly exact 2n-3 diameter. The proof captures a genuine constraint absent from unconstrained subset exchanges; useful to domination reconfiguration and token-jumping geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
