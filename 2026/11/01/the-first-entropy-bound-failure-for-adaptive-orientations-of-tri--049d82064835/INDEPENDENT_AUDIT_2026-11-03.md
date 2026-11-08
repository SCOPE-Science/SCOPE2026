# Independent mathematical audit

## correctness

PASS

For each triangular book B_r=K_(1,1,r), 1≤r≤7, an acyclic orientation is specified by a spine direction and three allowed spoke pairs per page; any directed four-cycle forces a forbidden oriented triangle. Thus |A_r|=2·3^r. The exact complete online-shattering recursion F_r(S,d)⇔∨_q(F_r(S∩Q_q,0,d−1)∧F_r(S∩Q_q,1,d−1)), with F(S,0) iff nonempty and |S|<2^d pruning, is equivalent by induction to existence of a depth-d complete adaptive edge-query tree. Independently implemented the entire exact bitmask recursion, obtaining Ldim r=1..7 as (2,4,5,7,8,10,11) and memoized state counts (11,72,224,1298,5396,28117,236276). Also directly inspected actual CERTIFICATE.json (187748 bytes, matching frozen Git blob) and independently validated its 3508 leaf witnesses, seven complete trees, acyclicity, uniqueness, query-path agreement and 2048 leaves for r=7. Consequently depth 12 fails at r=7 while entropy cardinality allows 12; r≤6 attain their cardinality upper bounds. This is a complete finite proof, not a timeout or extrapolation.

## originality

PASS

Static VC shattering of acyclic orientations along forests and the 2·3^r concept count are established or routine; the assessed result is the exact Littlestone/adaptive query depths for r=1..7 and first sharp cardinality-bound failure at r=7. Searches against graph-orientation learning literature, Resultary and complete multipartite enumeration do not locate a prior equivalent finite adaptive table. No all-r extrapolation is claimed.

## value

PASS

An adaptive versus cardinality obstruction has a mathematically natural first crossover within the canonical family of two-hub triangular book graphs. The exact finite classification resolves when the counting upper bound on Littlestone dimension first ceases to be sharp, contrasting online adaptivity with known VC/forest shattering. The bounded n=7 cutoff is meaningful even without a conjectured formula for all r≥8.

The dated certificate retains the supplied scientific assessment, sources and limitations.
