# Independent mathematical audit

## correctness

PASS

Used the published exact Hamming-graph equivalence: a total mutual-visible set in Q8 is exactly a set containing no distance-two pair. All distance-two pairs preserve parity, so Q8 splits into two independent 128-vertex halved cubes with edges at Hamming distance two. Inclusion maximality is equivalent to independent domination in each half. Since each half closed neighborhood has 1+C(8,2)=29 vertices, k<=4 cannot dominate 128. An independently implemented C++20 exhaustive search normalized an anchored vertex to 0 using even XOR transitivity and enumerated every independent subset of sizes k=5,6,7,8 using strictly increasing candidate indices and exact 128-bit domination masks. Counts (independent,dominating) are (611100,0),(2984625,0),(7490595,0),(9234285,142380). Hence i(H8)=8. Double-counting pairs (vertex, size-eight independent dominating set) gives 128*142380/8=2,278,080 such sets per parity class; squaring the independent choices yields exactly 5,189,648,486,400 labeled total-visibility minimum maximal sets, and lower total mutual visibility=16. Search examined 9,234,285 anchored independent size-eight candidates; exhaustive recursion correctness was independently reviewed, not inferred from opaque verifier log. No result for unbounded dimension claimed.

## originality

PASS

Best-of-knowledge PASS for the specific lower minimum-maximal value and complete labeled census in dimension eight. Prior source proves distance-two equivalence; the published upper visibility and ordinary domination tables concern other extrema. Searches for exact 142380, 2278080 and 5189648486400 and published records did not establish an earlier same minimum independent-dominating enumeration; unindexed coding-theory data remain a genuine risk.

## value

PASS

PASS: The dimension-eight lower total mutual-visibility number is a natural independently posed graph invariant, and the exact 13-digit census of minimum inclusion-maximal objects is not implied by the known upper value or ordinary domination tables. The parity reduction plus a reproducible exhaustive count produces a meaningful finite mathematical benchmark, including distinguishing ordinary and independent domination. The claim deliberately does not extrapolate beyond dimension eight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
