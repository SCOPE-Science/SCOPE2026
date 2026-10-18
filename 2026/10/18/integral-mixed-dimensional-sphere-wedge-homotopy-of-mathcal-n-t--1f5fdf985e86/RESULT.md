# Integral mixed-dimensional sphere-wedge homotopy of \(\mathcal N(T_7)\)

## Finding
Let \(T_7=L(K_7)=J(7,2)\) denote the triangular graph. Its vertices are the \(21\) unordered pairs of distinct elements of \(\{0,1,\ldots,6\}\), two vertices adjacent precisely when the pairs intersect in one element. Write \(X=\mathcal N(T_7)\) for the ordinary **open**-neighborhood complex, whose simplices are vertex sets with at least one common adjacent vertex of \(T_7\). Then
\[
X\simeq \bigvee^{246}S^3\vee\bigvee^{7}S^4.
\]
In particular the only nonzero reduced integral homology groups are \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{246}\) and \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{7}\); they are torsion-free.

## Assumptions and scope
The graph is finite, simple, undirected and has no loops. The definition uses *open*, not closed, neighborhoods. If a vertex represents the edge \(e\subset\{0,\ldots,6\}\), its open neighborhood is the set of the \(10\) distinct edges sharing exactly one endpoint with \(e\). A nonempty face of \(X\) is precisely a nonempty subset of one of these 21 neighborhoods. The empty face is included in the abstract complex but is not counted in the nonempty-face statistics. The theorem concerns this one canonical 21-vertex graph, its full integral homotopy type, and no larger-parameter family.

## Proof
**1. Exact face-poset description.** Enumerate the \(21\) unordered pairs lexicographically and represent each simplex by its \(21\)-bit incidence mask. For every potential common neighbor \(e\), form the corresponding ten-bit neighborhood mask, and include all of its nonempty submasks. Deduplication yields exactly \(18{,}494\) simplices, with face vector (dimensions zero through nine)
\[
(21,210,1190,3780,5187,4410,2520,945,210,21).
\]
The accompanying program also independently checks *every* one of the \(2^{21}-1=2{,}097{,}151\) nonempty masks against the direct common-neighbor predicate, establishing that the generated face set is complete. These finite checks are exact integer computations, not sampling.

**2. Explicit matching.** Initially mark every nonempty simplex unmatched. Process the \(21\) vertices in the lexicographic order. At step \(v\), for every still-unmatched face \(\sigma\) not containing \(v\) such that \(\sigma\cup\{v\}\) remains unmatched, match \(\sigma\) with \(\sigma\cup\{v\}\) and remove both from the unmatched set. Pairs at one step are disjoint because every pair has one member containing \(v\) and one without \(v\). This precisely specifies \(9{,}120\) pairs and leaves \(254\) critical faces, with dimensions
\[
\#\mathrm{Crit}_0=1,\qquad\#\mathrm{Crit}_3=246,\qquad\#\mathrm{Crit}_4=7,
\]
and none in any other dimension.

**3. Acyclicity certificate.** For each inclusion of a codimension-one face \(\alpha\subset\beta\), direct the edge \(\beta\to\alpha\), reversing it to \(\alpha\to\beta\) when the pair is matched. The program constructs all \(98{,}805\) such Hasse incidences, checks that the matching arrows are exactly the reversed ones, and performs a full topological sort visiting all \(18{,}494\) faces. The directed graph is acyclic. Hence Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(X\) with exactly the critical-cell dimensions and counts above.

**4. Signed integral attaching matrix.** Give each ordered simplex the orientation induced by lexicographically increasing vertices and use the integral incidence \(\partial[v_0,\dots,v_k]=\sum_{i=0}^k(-1)^i[v_0,\dots,\widehat v_i,\dots,v_k]\). For each critical four-cell, start with its oriented simplicial boundary. In a full directed-Hasse topological order, eliminate every matched lower three-face \(\alpha\) paired with a four-face \(\beta\) by subtracting the integer coefficient of \(\alpha\) times \(\partial\beta\), divided by the unit incidence \([\beta:\alpha]\in\{+1,-1\}\). Because the matching is acyclic, no eliminated lower three-face is reintroduced by a later elimination. The final chains lie on critical three-faces. For each of the seven critical four-cells, the final chain is identically **zero** over \(\mathbb Z\), not just modulo two. The verifier also computes the same seven columns independently by reverse-order signed gradient-path recursion, with identical zero output. Thus the integral Morse cellular boundary \(\partial^M_4:\mathbb Z^7\to\mathbb Z^{246}\) vanishes exactly.

**5. Upgrade from homology to homotopy.** The Morse CW complex has one zero-cell, no one- or two-cells, \(246\) three-cells and \(7\) four-cells. Its three-skeleton is therefore \(\bigvee^{246}S^3\). The attaching maps of the four-cells lie in \(\pi_3(\bigvee^{246}S^3)\cong H_3(\bigvee^{246}S^3;\mathbb Z)\cong\mathbb Z^{246}\), by the Hurewicz theorem. Their coordinate degrees are precisely the corresponding columns of the integral Morse boundary, which are all zero. Every attaching map is therefore null-homotopic. Attaching the seven four-cells produces seven additional four-sphere summands, proving the claimed integral homotopy equivalence.

## Verification
Run `python3 verify.py` with standard Python \(3\), without third-party dependencies; the exact expected output is `verification_output.json`. The checker directly enumerates all \(2{,}097{,}151\) nonempty vertex subsets for its independent membership check, verifies the full face vector, reconstructs the \(9{,}120\) Morse pairs, topologically sorts all \(98{,}805\) reversed Hasse incidences, and computes all seven signed integral boundary columns by two independently implemented exact-integer algorithms. Both give seven zero columns. The reduced Euler characteristic independently checks as \(-239=-246+7\). The executable and expected output are included alongside this statement, with SHA-256 hashes in the enclosing package.

## Relationship to prior work
Shukla's 2018 work establishes neighborhood-complex homotopy types for maximum-degree-at-most-three graphs and four-regular circulant graphs; \(T_7\) is ten-regular and falls in neither class. Matsushita and Wakatsuki (2023) relate neighborhood complexes to Alexander duals of dominance complexes. Their duality applies to \(X\cong\mathcal D(KG(7,2))^\vee\) but provides no homotopy-type calculation for this particular graph.

The closest published indexed finding, *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, determines \(\widetilde H_3(X;\mathbf F_2)\cong\mathbf F_2^{246}\) and \(\widetilde H_4(X;\mathbf F_2)\cong\mathbf F_2^7\), and its complete inspected RESULT.md explicitly says that integral torsion, homotopy type, and attaching maps are **not determined**. Mod-two homology does not rule out an even nonzero integral attaching degree. The present theorem establishes the zero integral differential and upgrades the known profile to the exact sphere-wedge homotopy type. The independence complex, graph Čech nerve, and clique complex of \(T_7\) are distinct constructions and are not substituted here.

## Limitations
The classification is for \(T_7\) only, not a claim about arbitrary triangular graphs. The proof is a complete finite combinatorial certificate, not a symbolic all-parameter matching formula. The verification gives an exact combinatorial-homotopy argument but has not undergone independent mathematical audit. A literature search cannot exclude an equivalent result in unindexed literature, especially under Hom-complex or Kneser-complement terminology. The statement makes no claims about higher operations or the symmetry-group action.

## References
1. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1 (first posted 2018-02-13), https://arxiv.org/abs/1802.04526.
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first posted 2023-12-05), https://arxiv.org/abs/2312.02639.
3. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, published RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec/RESULT.md.
