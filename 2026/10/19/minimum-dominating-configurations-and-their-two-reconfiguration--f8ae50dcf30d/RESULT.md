# Minimum dominating configurations and their two reconfiguration geometries in the Johnson graph \(J(7,3)\)

## Finding

For the Johnson graph \(J(7,3)\), the domination number \(\gamma=4\) and the count of \(770\) minimum dominating sets have been reported previously. The finding here is a complete two-type classification of those sets and the exact structure of both their token-sliding and token-jumping reconfiguration graphs.

Write \(X=\{0,1,2,3,4,5,6\}\). Every minimum dominating set is uniquely assigned a three-subset \(B\subset X\), with four-set complement \(A=X\setminus B\), and belongs to exactly one of the following two types:

**Type I:** the vertex \(B\) and any three of the four triples from \(\binom A3\). There are four sets for each \(B\), hence \(140\) in total.

**Type II:** choose \(P\in\binom A2\), let \(Q=A\setminus P=\{u,v\}\), and choose \(b\in B\). The four vertices of the configuration are \(B\), \(P\cup\{u\}\), \(P\cup\{v\}\), and \(Q\cup\{b\}\). There are eighteen for each \(B\), hence \(630\) total. The two types are precisely the two orbits under permutations of \(X\), of sizes \(140\) and \(630\).

In **token sliding**, a move replaces one of the four selected triples by an adjacent triple of \(J(7,3)\). Its reconfiguration graph has \(770\) vertices and \(2100\) edges and splits into **exactly \(35\) components**, indexed by \(B\), each with \(22\) vertices, \(60\) edges, radius \(2\), and diameter \(3\). Each component is obtained from \(K_4\) by adjoining three additional vertices to each of its six edges, making a \(K_5\) on the edge's two endpoints and its three new vertices, without additional edges between edge groups. The four core vertices represent Type I, and the eighteen added vertices Type II.

In **token jumping**, the replacement triple need not be adjacent to the removed triple. This graph has \(2730\) edges, is connected, and has **radius and diameter both \(7\)**. Its Type I vertices have degree \(12\), and its Type II vertices degree \(6\). The \(630\) jump edges not already slides connect components whose indexing triples \(B,B'\) are disjoint. The simple component quotient is the Kneser graph \(\operatorname{KG}(7,3)\), with \(35\) vertices and \(70\) edges: exactly nine jump edges lie above each quotient edge.

## Assumptions and scope

The graph is finite, simple, undirected; its vertices are \(\binom X3\) and two different triples are adjacent if their intersection has size exactly two. A dominating set \(D\) satisfies \(\bigcup_{d\in D}N[d]=V\), with closed neighborhoods. A minimum set has cardinality \(\gamma\). A reconfiguration move preserves cardinality and domination at both endpoints; one selected vertex is removed and one unselected vertex is added. A slide further requires these two vertices to be adjacent in the original Johnson graph. Only this particular graph, and these fixed-cardinality move conventions, are asserted. No classification of \(J(n,3)\) for arbitrary \(n\) is claimed.

## Proof

**Dominating-set criterion.** A triple \(T\) is contained in the closed neighborhood of a selected triple \(d\) exactly when \(|T\cap d|\ge2\). Equivalently, the two-shadow \(\partial_2 D=\bigcup_{d\in D}\binom d2\) must meet each three-subset \(T\) in at least one pair. Hence \(D\) dominates exactly when the complementary graph of the two-shadow on \(X\) is triangle-free. This equivalence is both necessary and sufficient, without a search heuristic.

**Size lower bound.** If three triples dominate, their two-shadow has at most nine edges. Its complement therefore has at least twelve edges. Mantel's theorem gives a maximum of twelve edges to a triangle-free graph on seven vertices, with equality possible only for \(K_{3,4}\). Thus the two-shadow would have to equal \(K_3\sqcup K_4\), with nine edges. To cover all six edges of the \(K_4\) using only triples entirely inside it requires at least three triples (two distinct triples on four vertices cover at most five of its six edges). The three further edges of the \(K_3\) require another triple. This contradicts a three-triple cover, proving \(\gamma\ge4\). The explicitly constructed Type I and II sets dominate by the shadow criterion, so \(\gamma=4\). The numerical minimum is not asserted to be novel.

**Completeness certificate.** There are \(\binom{35}{4}=52360\) distinct four-subsets of the 35 Johnson vertices. `verify_python.py` enumerates all 52360 with no pruning and tests the complete union of closed neighborhoods. Independently, `verify_cpp.cpp` enumerates them and tests every possible three-subset for a covered pair, with independently constructed data representations. Each yields exactly 770 dominating four-sets. A separate constructive generator forms all Type I and Type II sets indexed by \(B\), asserts they are distinct, and matches their canonical set **exactly** to the exhaustive 770-set list. This establishes both exhaustive classification and unique ownership, not merely sample support. A complete lexically ordered list of all 770 optima is embedded in `certificate.tsv` (`D` records); each vertex index denotes a triple in lexicographic order.

**Reconfiguration certificate.** The programs examine every single-deletion/single-insertion pair among the complete list of 770 configurations, comparing the resulting chosen four-set with the exhaustive optimum index; their matching `S` and `J` records list **every** undirected edge once. Thus any excluded edge is mathematically excluded by a complete finite test, not by graph-search timeout. The independent reconstructions have exactly 2100 slide edges and 2730 jump edges. Graph traversal partitions slides into 35 components of size22 with the indicated 4+18 vertex partition; direct degree and adjacency tests certify each is the described edge-thickened \(K_4\). All slide moves preserve \(B\). Of the 630 extra jump edges, each connects two different, disjoint indexing triples; there are exactly 70 different unordered such pairs, each with multiplicity nine. The 770-vertex jump graph is connected. Complete breadth-first-search distances from **all 770 roots**, rather than selected representatives alone, certify its radius and diameter seven; similarly every slide-component vertex has eccentricity two or three. Every permutation of the seven ground elements was also checked on the 770 configurations, yielding exactly the two specified orbit sizes.

The foregoing finite exhaustive proof is fully reproducible using the two standalone sources and canonical certificate. It does not use extrapolation from smaller parameters.

## Verification

`certificate.tsv` contains 770 optimum-set records (`D`), 2100 slide-edge records (`S`) and 2730 jump-edge records (`J`), totaling 5600 lines and 59080 bytes. It is an ASCII certificate with SHA-256 `97ffabe0e4e0ab21199e85ecfea0697de63fb6b375a70e72197515d5aabade5b`. The two independently coded implementations generated identical certificates byte-for-byte and identical recorded summaries. Their source files are `verify_python.py` (Python standard library) and `verify_cpp.cpp` (C++17). See `VERIFICATION.md` for commands and exact replay expectations; inspection of printed summaries alone is not regarded as sufficient verification.

## Relationship to prior work

Minimum domination in Johnson graphs has been studied via lotto designs and covering numbers. Cornet–Dravec–Torres, **Domination and Total Domination in Johnson graphs**, arXiv:2610.04675 (2026), provides scalar domination-number results and cites earlier work of Bate (1978). Lee–Oh, **Domination in Johnson graphs J(n, 3) for odd n**, arXiv:2606.10326 (2026), expressly highlights characterization of extremal configurations as a separate problem; they determine the ordinary domination-number value for odd parameters, rather than describing the optimal-set exchange graph. The **770** scalar count for \(J(7,3)\) already appears in OEIS A323494 (2019) and is expressly **not** claimed as new. Cornet–Dravec–Torres (2025) treated domination in Johnson graphs; complete relevant full text could not be accessed, so an undetected overlap with a structural result in that paper remains possible. Reconfiguration using additions/removals under a cardinality cap was studied by Suzuki–Mouawad–Nishimura (arXiv:1401.5714, posted 2014-01-22), whereas the present graphs use fixed-cardinality one-for-one sliding and jumping. No inspected source establishes the two-family classification together with its 35-component slide graph and connected diameter-seven jump graph. This is a best-knowledge literature comparison, not a proof of publication priority.

## Limitations

The statement concerns one finite graph. Unindexed publications, unpublished computations, supplementary tables and material inaccessible in the 2025 Johnson-graph paper could contain equivalent statements. Finite exhaustive enumeration is a complete proof for 35 vertices, but does not establish a theorem for arbitrary Johnson graph parameters. The scientific review is same-model only; there has been no independent audit. The degree, component and diameter conclusions depend on the stipulated one-for-one move rule.

## References

- D. Cornet, T. Dravec and P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675 (first publicly posted October 2026), https://arxiv.org/abs/2610.04675.
- D. Lee and S. Oh, *Domination in Johnson graphs J(n, 3) for odd n*, arXiv:2606.10326 (first publicly posted June 2026), https://arxiv.org/abs/2606.10326.
- OEIS A323494, https://oeis.org/A323494; minimum dominating-set enumeration includes the value 770 for \(J(7,3)\).
- Cornet, Dravec and Torres, *Domination in Johnson graphs*, Procedia Computer Science (2025), DOI 10.1016/j.procs.2025.10.302; relevant full text was not accessible.
- A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of dominating sets*, arXiv:1401.5714, first public January 22, 2014, https://arxiv.org/abs/1401.5714.
- P. C. Bate, *A generalized covering problem* (1978), as cited in the 2026 Johnson-graph domination literature; earlier numerical coverage credited, no unpublished date claimed.
