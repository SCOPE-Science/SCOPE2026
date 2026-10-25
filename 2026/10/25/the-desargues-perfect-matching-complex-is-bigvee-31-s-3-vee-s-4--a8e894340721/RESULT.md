# The Desargues perfect-matching complex is \(\bigvee^{31} S^3\vee S^4\)

## Finding

For the twenty-vertex Desargues graph \(D=GP(10,3)\), let \(\mathcal P(D)\) be the simplicial complex on graph edges whose faces are exactly the edge sets contained in at least one perfect matching. There is an integral homotopy equivalence
\[
\boxed{\mathcal P(D)\simeq\bigvee^{31}S^3\vee S^4.}
\]
In particular, its reduced integral homology is free of rank 31 in degree 3, free of rank 1 in degree 4, and zero in all other degrees. Its 60 perfect matchings produce a pure nine-dimensional complex, but the homotopy is concentrated in degrees 3 and 4.

There are 113,192 ordinary matchings including the empty matching, of which 68,910 are not extendible to a perfect matching. Among these, exactly 220 three-edge and 180 four-edge matchings are inclusion-minimal nonextendible matchings.

## Assumptions and scope

Use the labeled generalized Petersen graph with vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and graph edges
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+3}\}
\quad (i\in\mathbb Z/10\mathbb Z).
\]
The concrete encoding in `verify_desargues.py` is \(u_i=i\) and \(v_i=10+i\), with all 30 undirected edges indexed by ascending lexicographic endpoint pairs. An edge subset is represented by the bitmask of its graph-edge indices. All face and Morse calculations use this fixed ordering and increasing vertex orientation. The empty face is included in the complex, but excluded from the nonempty face poset on which the Morse matching is constructed.

The graph is the bipartite Levi graph of the Desargues \((10_3)\) configuration. No claims are made here about all generalized Petersen graphs, all cubic bipartite graphs, or the inclusion-induced homology map from this complex into the ordinary matching complex.

## Proof

**Exhaustive facets and faces.** Recursively take the lowest-index uncovered graph vertex and match it to each available neighbor, repeating until all 20 vertices are covered. Every perfect matching is produced once, because its edge incident to the lowest uncovered vertex is forced at each stage. Exactly 60 perfect matchings, each with ten graph edges, result. Independently, a subset-dynamic-programming count of perfect matchings gives the same total. Taking all submasks of the 60 facet masks yields exactly 44,281 nonempty faces with face counts in dimensions zero through nine:
\[
(30,375,2320,7320,12096,11700,7080,2700,600,60).
\]
These are complete: by definition every face is a subset of a perfect matching, and all such subsets have been generated.

**Complete acyclic discrete-Morse matching.** Begin with all 44,281 nonempty faces unpaired. For each indexed graph edge \(e=0,1,\ldots,29\), and for each currently unpaired face \(\sigma\) not containing \(e\), pair \(\sigma\) with \(\sigma\cup\{e\}\) precisely if the latter also remains unpaired. Sort face bitmasks increasingly to make the procedure deterministic. It yields 22,113 pairs and precisely 55 critical cells: one of dimension zero, 42 of dimension three, and 12 of dimension four. Orient each unmatched codimension-one Hasse incidence down and each matched incidence up. A complete topological sort of the oriented graph visits all 44,281 vertices across all 244,830 nonempty face incidences. This checks every possible directed cycle and establishes that the matching is acyclic. Discrete Morse theory therefore gives a CW model with the indicated critical cells.

**Exact integral attaching matrix.** Orient a \(k\)-simplex by ascending graph-edge indices, so deleting the edge with position \(j\) contributes sign \((-1)^j\). For a paired lower simplex \(L\) and upper simplex \(U\) having incidence \(\epsilon=\pm1\), the relation \(\partial U=\epsilon L+\sum_G\alpha_GG\) eliminates \(L\) as \(-\epsilon\sum_G\alpha_G G\). Recursive elimination along the verified acyclic gradient relations expresses the boundary of every critical four-cell in the 42 critical three-cells. Critically, this computes an integral cellular attaching-degree matrix, rather than ranks over a finite field.

The resulting matrix \(B:\mathbb Z^{12}\to\mathbb Z^{42}\) has exactly 64 nonzero entries, each equal to \(+1\) or \(-1\). A completely explicit sequence of integer elementary row and column operations using eleven unit pivots reduces it to
\[
B\sim_{\mathrm{GL}_{42}(\mathbb Z)\times\mathrm{GL}_{12}(\mathbb Z)}
\begin{pmatrix}I_{11}&0\\0&0\end{pmatrix}.
\]
No divisibility or rational approximation is invoked; the standalone verifier and `CERTIFICATE.json` enumerate the critical cell masks and signed matrix entries, reproduce every pivot, and check that the residual matrix is identically zero. A separate Smith-normal-form calculation also returns eleven unit invariant factors.

**Recovering the homotopy type.** The three-skeleton of the Morse CW model is \(\bigvee^{42}S^3\), since it has a single zero-cell and no cells in dimensions one or two. The Hurewicz isomorphism identifies \(\pi_3(\bigvee^{42}S^3)\) with \(\mathbb Z^{42}\); hence the twelve attaching maps of its four-cells are completely determined by the columns of \(B\). Integral basis changes are realized by self-homotopy equivalences of the wedge of three-spheres and elementary changes of the four-cell attachments. Eleven degree-one attachments cancel eleven three-sphere summands, while the remaining attachment is nullhomotopic and gives a four-sphere. This leaves 31 three-spheres and one four-sphere. The face Euler characteristic is \(-29=1-31+1\), providing an independent numerical consistency check.

**Minimal matching-extension obstructions.** Independently enumerate all graph matchings by adjoining only disjoint graph edges in strictly increasing index order. This produces 113,192 matchings including the empty face. Subtracting the perfect-matching subcomplex leaves 68,910 nonextendible matchings. Such a matching is minimal exactly when every one-edge deletion is in the subcomplex. The complete test gives 220 minimal matchings of cardinality three and 180 of cardinality four, with none of any other cardinality.

## Verification

In a directory containing the two standalone files, execute `python3 verify_desargues.py --certificate CERTIFICATE.json` using ordinary Python 3; no third-party packages, external data, or network access are required. Successful output ends with `CERTIFICATE_OK` after reporting `VERIFY_OK`. The checker regenerates the complete graph, counts perfect matchings independently by dynamic programming, generates every face, checks the entire Morse Hasse diagram for cycles, reconstructs the signed integer boundary, verifies eleven unimodular cancellations and the complete zero residual, and independently counts all ordinary and minimal nonextendible matchings. The certificate contains explicit graph edges, critical-cell masks, signed boundary triplets, and pivot choices. All calculations use exact integers. The bound is finite and exhaustive for the stated graph, not a general theorem about all graphs.

## Relationship to prior work

Taylan's 2015 work develops Morse-matching methods for arbitrary simplicial complexes and obtains graph-complex homotopy classifications, but does not analyze this graph's perfect-matching complex. Bayer, Jelić Milutinović and Vega define perfect-matching complexes and classify particular honeycomb families; their conclusion asks about such complexes for more general graphs, including bipartite examples. The Desargues graph is a nonplanar bipartite incidence graph, outside the honeycomb families treated there.

A publicly available result for the **ordinary** Desargues matching complex determines \(\operatorname{Match}(D)\simeq\bigvee^5 S^5\vee\bigvee^{45}S^6\), and explicitly distinguishes that object from the perfect-matching subcomplex. It does not determine the homotopy type of the subcomplex: the latter omits 68,910 ordinary matching faces. Likewise, the known exact perfect-matching complex of the Heawood graph concerns a different incidence graph with 14 rather than 20 graph vertices. Neither published result implies the present matrix calculation or wedge classification.

## Limitations

The result is one exact finite topological classification of a canonical graph, not a formula for arbitrary bipartite or cubic graphs. It does not determine the automorphism-group action on homology, the inclusion map into the ordinary matching complex, or a uniform description of perfect-matching complexes of incidence graphs. Originality has been compared with accessible full texts and mathematical research records, but equivalent unindexed work is possible. Reproduction requires running and independently inspecting the supplied finite enumeration and Morse-boundary checker; computational correctness and originality have not undergone independent external validation.

## References

1. Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first public 2015-01-27. Sections 2–5 address Morse methods for nonflag complexes.
2. Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public 2022-09-06; Definition 1 and Section 5 describe the exact invariant and the remaining bipartite-graph questions.
3. *The Desargues matching complex is a mixed-dimensional wedge of spheres*, public published-finding corpus research record `2026/10/11/SCOPE-the-desargues-matching-complex-is-a-mixed-dimensional-wedge-of-s--67ff1e627721`, particularly its finding, assumptions, and limitations distinguishing the ordinary from the perfect-matching complex.
4. *Perfect Morse reduction of the Heawood perfect-matching complex*, public published-finding corpus research record `2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d`, as an exact neighboring incidence-graph comparison.
5. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for the discrete-Morse homotopy equivalence.
