# Scientific assessment: total perfect codes on \(Q_4\)

## Correctness — PASS
The size-four constraint follows from double counting open neighbourhoods; each code induces two independent edges. Fixing one such edge reduces the remaining vertices to the unique antipodal edge by pairwise open-neighbourhood disjointness, yielding the complete affine classification. The antipodal quotient is exactly \(K_{4,4}\); code intersections coincide with edge incidence, establishing the entire two-replacement graph as \(L(K_{4,4})\). The full distance profile, strongly regular parameters, absence of single replacements, and 24 partitions follow as proved corollaries. The two independent, reproducible Python scripts verify the complete labelled finite state space, not a statistical sample. No conclusion is asserted for higher cube dimensions.

## Originality — PASS, with stated access risk
The nearest primary source is S. Zhou, *Total perfect codes in Cayley graphs*, first posted 2016-01-14, especially Lemma 3.1, Corollary 4.2 and Example 4.3. The cited work already constructs four total perfect codes partitioning \(Q_4\), and the general existence and translation facts are excluded from novelty. Y. S. Kwon and J. Lee (2014) already establish that \(Q_4\) covers \(K_{4,4}\); this is also excluded. The new statement shows that **all** total perfect codes are full preimages of antipodal quotient edges and derives the complete reconfiguration graph and sharp batch threshold, exact distance formula, and all 24 code partitions. Neither these specific metric claims nor the full partition classification appeared in the actually inspected public primary materials. Searches for the aliases *efficient open dominating set*, *perfect total dominating set*, *total perfect code*, antipodal quotient and exchange graph found no equivalent result. The full text of Kwon–Lee was inaccessible; a decisive hidden local computation cannot be ruled out. No claim of certified absolute priority is made.

## Value — PASS
This is a full structural and mobility classification for the smallest nontrivial four-regular binary cube admitting efficient open domination. The sixteen optimal exact-one-neighbour sensor configurations form a connected metric space only when two sensors may be replaced together; every transformation requires at most two batches, and all four-code global decompositions are classified and counted. These questions concern solution flexibility and simultaneous fault-free reconfiguration, not just the already-known existence of an efficient open dominating set. The finite theorem is self-contained and its sharp threshold is intrinsic rather than a chosen arbitrary numerical slice. Its value does not depend on an unproved extrapolation or a downstream conjecture.

## Closest literature and limits
- S. Zhou, arXiv:1601.03471, §§2–4, particularly Example 4.3 (one exhibited four-code partition, not a reconfiguration analysis), and the known existence criterion.
- Y. S. Kwon and J. Lee, *Perfect domination sets in Cayley graphs* (2014), DOI 10.1016/j.dam.2013.09.020 (published abstract verifies hypercube-to-complete-bipartite covering, but full text was not accessible).
- H. Huang, B. Xia and S. Zhou, arXiv:1609.03755 (subgroup and automorphism-based construction rather than all code-exchange distances on the four-cube).
- Exact finite verification cannot establish historical priority. The statement concerns only \(Q_4\); larger cubes can admit nonlinear codes.

Self-review: passed. Independent audit: not yet performed.
