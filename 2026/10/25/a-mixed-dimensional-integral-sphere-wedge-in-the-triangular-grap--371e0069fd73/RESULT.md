# A mixed-dimensional integral sphere wedge in the triangular-graph neighborhood complex

## Finding
Let \(T_7=L(K_7)=J(7,2)\) be the graph whose 21 vertices are the two-element subsets of \(\{0,1,2,3,4,5,6\}\), two being adjacent exactly when they intersect in one element. Let \(\mathcal N(T_7)\) be its ordinary *open* Lovász neighborhood complex: a nonempty set of graph vertices is a simplex precisely when all its members have a common adjacent graph vertex.

There is an integral homotopy equivalence
\[
\boxed{\mathcal N(T_7)\simeq\left(\bigvee^{246}S^3\right)\vee\left(\bigvee^{7}S^4\right).}
\]
Thus the only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{246}\) and \(\widetilde H_4\cong\mathbb Z^{7}\). In particular there is no integral torsion or nontrivial attaching map between the sphere dimensions. The conclusion is the complete nonequivariant homotopy type for this one natural finite graph, not an assertion about all triangular graphs.

## Assumptions and scope
Write the 21 unordered edges of \(K_7\) in lexicographic order, indexed \(0,\ldots,20\). Encode each nonempty set of these edges by a 21-bit positive integer, with bit \(j\) representing the \(j\)-th edge. For an edge \(e\) of \(K_7\), its open neighborhood \(N(e)\) in \(T_7\) consists of the ten *other* edges sharing an endpoint with \(e\). The simplices of \(\mathcal N(T_7)\) are exactly the nonempty subsets of the 21 neighborhoods \(N(e)\). No graph loops and no closed neighborhoods are allowed. The proof treats only \(T_7\); no assertion for \(T_8\), higher graph powers, or symmetry modules follows.

## Proof
**Exact combinatorial model.** Enumerating each nonempty subset of each ten-vertex open neighborhood and deduplicating produces exactly 18,494 nonempty simplices. The face vector, indexed by dimension from zero to nine, is
\[
(21,210,1190,3780,5187,4410,2520,945,210,21).
\]
This enumeration is exhaustive because every neighborhood face has, by definition, at least one common adjacent vertex.

**An acyclic integral discrete-Morse certificate.** The accompanying `matching_certificate.json.gz` supplies 9,120 distinct facet/cofacet pairs \((\sigma,\tau)\), each with \(\tau\) obtained from \(\sigma\) by adjoining a single vertex. Every listed face belongs to exactly one pair, and exactly 254 unpaired faces remain: one vertex, 246 three-simplices and seven four-simplices. Independently orient every cover relation in the entire face poset downward, except the matched relations, which point upward. The accompanying verifier reconstructs all cover relations and proves that this 18,494-vertex directed Hasse diagram is acyclic by a complete topological sort. This is the acyclic-matching hypothesis of the discrete-Morse CW theorem, not merely a rank computation or an incomplete sample.

**The seven signed attaching-degree vectors vanish integrally.** Give every simplex its orientation induced by increasing vertex indices. For each critical four-simplex, its integral Morse boundary is computed by signed gradient-path propagation to critical three-simplices, using integer coefficients only. At every matched pair \((\sigma,\tau)\), the coefficient of the facet is \(\pm1\), so no division by a nonunit occurs. For each of the seven critical four-simplices, all 246 coefficients are exactly zero. The standalone verifier recomputes this seven-by-246 integral boundary matrix and checks that every entry vanishes; it does not infer vanishing from numerical ranks modulo a prime.

**From the Morse model to the homotopy type.** Discrete Morse theory gives a CW complex homotopy equivalent to \(\mathcal N(T_7)\), having one zero-cell, 246 three-cells and seven four-cells, with no cells in dimensions one or two. Its three-skeleton is \(\bigvee^{246}S^3\). Because this skeleton is 2-connected, Hurewicz identifies its third homotopy group with its third integral homology group. Therefore a four-cell attaching map is nullhomotopic precisely when its full integral cellular degree vector is zero. The preceding signed calculation makes all seven attaching maps nullhomotopic, and hence the Morse CW complex is the stated wedge of spheres. This proves the homotopy assertion and integral torsion-freeness simultaneously.

## Verification
With Python 3 standard library, place `verify.py` beside `matching_certificate.json.gz` and execute `python verify.py`. The executable reconstructs the graph and all faces afresh, checks every matched pair and every critical cell, tests acyclicity on the complete directed Hasse diagram, and evaluates all signed gradient-path coefficients using exact integers. It finishes with `VERIFY_OK_TRIANGULAR_T7_NEIGHBORHOOD_INTEGRAL_WEDGE`. `verification_output.txt` records the completed run; the executable certificate, rather than that log, is the proof's finite input. Decoding, byte counts and SHA-256 hashes of the embedded artifacts are checked separately by the package importer.

## Relationship to prior work
The ordinary Lovász neighborhood complex is a classical topological construction, used in Kahle's study of random graphs and Matsushita's work on combinatorial fundamental groups. Those works give definitions and general theory, not this finite homotopy calculation. Fröberg's open-access study considers Stanley–Reisner resolutions of neighborhoods of paths, complete graphs and multipartite graphs, and does not compute this triangular-graph homotopy type.

A directly relevant published calculation, *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)* (published-finding corpus, 2026-10-11), already proves \(\widetilde H_3(\mathcal N(T_7);\mathbb F_2)\cong\mathbb F_2^{246}\) and \(\widetilde H_4(\mathcal N(T_7);\mathbb F_2)\cong\mathbb F_2^7\). That prior result explicitly does **not** determine integral homology, attaching maps or the homotopy type. The present exact acyclic matching and integral attaching calculation are the additional facts. The mod-two ranks are not claimed anew.

## Limitations
The result is a finite, computationally certified mathematical theorem about this specified complex. It does not determine an \(S_7\)-equivariant homotopy decomposition, the homotopy types for \(n\ge8\), or a uniform formula in \(n\). The proof depends on a publicly inspectable finite certificate and the standard discrete-Morse and Hurewicz theorems; the execution log alone is not sufficient. Bibliographic comparison is limited to the cited and inspected material, so independently discovered or unindexed equivalent calculations remain a residual risk. No independent external audit is asserted here.

## References
1. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first publicly posted 2005-12-04, https://arxiv.org/abs/math/0512077.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first posted 2012-10-10, https://arxiv.org/html/1210.2803v4.
3. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, *Journal of Algebraic Combinatorics* 63 (2026), 56, https://doi.org/10.1007/s10801-026-01530-x.
4. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, public research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec.
5. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145 (standard acyclic-matching CW theorem).
