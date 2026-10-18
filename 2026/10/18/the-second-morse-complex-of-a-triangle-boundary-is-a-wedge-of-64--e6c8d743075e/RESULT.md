# The second Morse complex of a triangle boundary is a wedge of \(64\) four-spheres

## Finding
Let \(\mathcal M(K)\) be the ordinary discrete Morse complex of a finite simplicial complex \(K\): its vertices are primitive vertex--coface incidence matchings, and its simplices are acyclic collections of such matchings. For the boundary \(\partial\Delta^2\) of a triangle,
\[
\boxed{\mathcal M\bigl(\mathcal M(\partial\Delta^2)\bigr)\simeq\bigvee^{64}S^4.}
\]
Equivalently, if \(P=C_3\square K_2\) is the triangular-prism graph, regarded as a one-dimensional simplicial complex, then \(\mathcal M(P)\simeq\bigvee^{64}S^4\). The equivalence follows because the first Morse complex \(\mathcal M(\partial\Delta^2)\) is simplicially isomorphic to the triangular-prism graph, as also identified in Scoville's 2026 work.

## Assumptions and scope
Use the labeled prism with vertex set \(\{0,1,2,3,4,5\}\) and ordered edge set
\[
E=((0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)).
\]
A vertex of \(\mathcal M(P)\) is an incident pair \((u,e)\), interpreted as a vector pointing from \(u\) across \(e\) to its other endpoint. A simplex consists of such pairs with each graph vertex and each graph edge used at most once and with no directed cycle. The criterion is equivalent to Forman acyclicity in dimension one: a closed nontrivial gradient path is a directed cycle among the chosen arrows. For a graph, under the distinct-source condition, a selected set of arrows has a directed cycle if and only if its underlying unoriented selected edges contain a cycle. Indeed, a cyclic undirected edge set with outdegree at most one forces cyclic orientation along every selected cycle. Consequently the simplices are exactly rooted oriented forests.

## Proof
Encode each primitive incidence by a bit in \(\{0,\ldots,17\}\). For the edge at zero-based index \(i\), bit \(2i\) points from its first displayed endpoint toward its second, and bit \(2i+1\) points in the reverse direction. Encode a face by the bitwise union of its incidence bits. The empty face is mask zero.

Every face is enumerated exactly by choosing for each of the nine edges either no arrow or one of its two orientations, rejecting choices that reuse a source or contain a directed cycle. There are precisely \(3^9=19683\) candidate choices. Independently, disjoint-set recursion over the nine edges enumerates exactly the acyclic choices while recording used sources; the two finite constructions agree on all face masks. By number of selected incidences \(k=0,1,2,3,4,5\), the face counts are
\[
(1,18,126,428,705,450).
\]
Thus the augmented face poset contains \(1728\) elements; no face uses six incidences.

Define a staged element matching using the exact incidence-bit order
```
(8,17,9,2,10,1,5,12,14,13,0,7,3,6,4,16,15,11)
```
At the stage of bit \(j\), for every as-yet-unmatched face mask \(s\) not containing \(j\), pair \(s\) with \(s\cup\{j\}\) precisely if the latter is also as-yet-unmatched. Remove both from further stages. Within a stage the pairs are disjoint because each lower mask omits \(j\) and each upper mask contains \(j\). The complete resulting matching has \(832\) pairs; precisely \(64\) unmatched masks remain, all of cardinality five (dimension four). In particular, the augmented empty face is matched to a singleton, so on the ordinary nonempty face poset that singleton becomes one critical zero-cell.

Acyclicity is certified without a numerical approximation: construct every cover relation \(s\subset s\cup\{j\}\) between valid masks. Orient an unmatched cover upward and a matched cover downward. The resulting directed graph has \(1728\) vertices and \(6624\) directed cover relations. A full topological sort removes all \(1728\) vertices, hence no directed cycle exists. The enclosed standalone program supplies the complete finite enumerator, matching, directed-cover construction, and topological-sort assertions; its proof obligations involve only finite sets of masks of at most \(18\) bits, exhaustive fixed loops, and integer operations.

Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(\mathcal M(P)\) with exactly one zero-cell and exactly \(64\) four-cells, and no cells in dimensions one through three or above four. Every four-cell attaching map lands in a point, so the CW complex is the wedge of \(64\) four-spheres. The simplicial graph isomorphism \(\mathcal M(\partial\Delta^2)\cong P\) transfers this conclusion to the indicated second iterate.

## Verification
Run `python3 verify_prism_morse.py` using Python's standard library, without auxiliary data. The program checks two independently implemented simplex-enumeration constructions, the full \(3^9\) candidate search, all face numbers, all \(832\) disjoint matched pairs, all \(6624\) Hasse cover incidences, complete directed acyclicity, and the \(64\) critical four-cells. As a non-homotopy cross-check it computes exact \(\mathbb F_2\) simplicial-boundary ranks \((17,109,319,386)\) in positive dimensions; the only nonzero reduced \(\mathbb F_2\) Betti number is \(\widetilde\beta_4=64\). The finite homotopy proof is the complete discrete-Morse matching and acyclicity check, **not** an inference from these Betti numbers.

## Relationship to prior work
Scoville's 2026 paper identifies \(\mathcal M(\partial\Delta^2)\) as the triangular-prism graph; it studies Morse complexes of simplices and their structural behavior but does not state the homotopy type of this graph's own Morse complex. Chari and Joswig describe graph Morse complexes through rooted forests, establishing the underlying combinatorial model. Jojić gives shellability results for directed graphs having complete sources or underlying trees; the bidirected triangular prism has neither property, and the inspected paper does not classify its Morse complex. Scoville and Zaremsky give general lower connectivity bounds for such complexes, but those bounds do not imply the wedge classification. An earlier published record computes reduced mod-two homology of exactly \(\mathcal M(P)\) and obtains dimension-four rank \(64\), explicitly leaving integral homology and homotopy type undetermined. The present exhaustive acyclic matching establishes the stronger **integral homotopy type** of that same object. A closely relevant thesis on directed forest complexes of Cayley graphs could not be read in full and remains a specifically identified possible overlap.

## Limitations
This theorem concerns the single canonical second iterate starting from a triangular boundary, equivalently the single triangular-prism graph. It does not give a formula for further iterates, other prism graphs, equivariant actions, or canonical sphere generators. The full homotopy classification rests on reproducible finite combinatorial verification in the accompanying code, not an independently audited formal proof. The partially accessible directed-forest thesis remains a residual literature-coverage risk.

## References
1. Nicholas A. Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results*, arXiv:2604.18172v1, first publicly posted 2026-04-20, https://arxiv.org/abs/2604.18172.
2. Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234, https://arxiv.org/abs/math/0011234.
3. Duško Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475, https://arxiv.org/abs/1109.4475.
4. Nicholas A. Scoville and Matthew C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, https://arxiv.org/abs/2004.10481.
5. *Mod-\(2\) homology of the triangular-prism Morse complex*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-triangular-prism-morse-complex--4af8059de6d1.
6. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, Boise State University M.S. thesis (2020), DOI 10.18122/td/1684/boisestate, https://doi.org/10.18122/td/1684/boisestate (full text inaccessible during comparison).
