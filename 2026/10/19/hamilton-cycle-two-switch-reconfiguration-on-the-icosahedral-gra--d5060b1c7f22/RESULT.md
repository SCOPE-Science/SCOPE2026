# Hamilton-cycle two-switch reconfiguration on the icosahedral graph

## Finding
Let \(I\) be the undirected icosahedral graph. Define \(\mathcal H_2(I)\) to have one vertex for each Hamiltonian cycle of \(I\), with cycles identified under reversal and cyclic rotation. Join distinct cycles precisely when two edges of one can be deleted and two previously unused edges inserted to obtain the other Hamiltonian cycle (a **two-edge switch**, or a legal two-opt move). Then
\[
\boxed{\mathcal H_2(I)\cong 30H_{36}\;\sqcup\;60K_2\;\sqcup\;80K_1,}
\]
where \(H_{36}\) is one connected graph on 36 vertices and 58 edges, of diameter 8. All 30 components of this size are mutually isomorphic. In particular, \(\mathcal H_2(I)\) has 1,280 vertices, 1,800 edges, and 170 components.

Under the order-120 automorphism group of \(I\), the connected components form four orbits: one orbit containing the 30 copies of \(H_{36}\), one containing the 60 isolated edges, and two containing respectively 20 and 60 isolated vertices. Each copy of \(H_{36}\) has degree multiset \(\{1^2,2^{11},3^8,4^8,5^6,6^1\}\). The maximum connected reachability class therefore contains only 36 of the 1,280 undirected Hamiltonian cycles.

## Assumptions and scope
The graph is explicitly labeled as follows. Its vertices are \(0,1,\ldots,11\). For \(i\in\{0,1,2,3,4\}\), define an upper-ring vertex \(a_i=1+i\) and a lower-ring vertex \(b_i=6+i\); subscripts are modulo 5. The 30 undirected edges consist of
\[
\{0a_i,\ 11b_i,\ a_ia_{i+1},\ b_ib_{i+1},\ a_ib_i,\ a_ib_{i-1}: 0\le i<5\}.
\]
This is the standard graph of the regular icosahedron: it has 12 vertices, degree five throughout, 30 edges, and 20 triangular faces. The four-cycle-exchange rule excludes disjoint cycle covers: every intermediate state must remain **one** spanning cycle. The result is about this finite, fixed graph and this precise move; no analogous statement for all triangulations or other Hamiltonian reconfiguration models is asserted.

## Proof
First enumerate Hamiltonian cycles without multiplicity. Anchor every candidate cyclic ordering at vertex 0, follow only graph edges, visit all other vertices exactly once, require the last vertex to be adjacent to 0, and retain exactly the orientation whose second vertex label is smaller than its last. This traverses every undirected Hamiltonian cycle once: anchoring removes rotations and the strict comparison removes the two possible orientations. There are 1,280 retained cycles.

Encode each of the 30 graph edges by a bit position, and represent a Hamiltonian cycle by its 30-bit edge-incidence mask. Suppose \(C\) and \(C'\) differ by a legal two-edge switch. Their symmetric difference comprises the two removed and the two inserted edges. Because both have degree two at all vertices, this four-edge symmetric difference is necessarily an alternating four-cycle in \(I\). Conversely, if the symmetric difference of a Hamiltonian cycle mask and the mask of a graph four-cycle is itself one of the enumerated Hamiltonian cycle masks, their difference is exactly such a legal switch. The last membership test rejects swaps that produce two cycles. The graph has exactly 30 four-cycles, obtained by examining all four-vertex subsets and all three possible cyclic orderings.

Consequently, to construct \(\mathcal H_2(I)\), for every enumerated mask \(m\) and four-cycle mask \(s\), test whether \(m\mathbin{\mathrm{xor}}s\) is another enumerated Hamiltonian mask. Deduplicating unordered pairs constructs **exactly** 1,800 switch edges. Breadth-first searches on this complete adjacency table yield 30 components of size 36, 60 of size 2, and 80 of size 1. Each 36-vertex component has 58 edges and diameter 8. The explicit table of 1,280 masks and 1,800 adjacency pairs is in `certificate.json` and can be checked by `verify_flips.py`.

For the symmetry statement, enumerate graph automorphisms by extending partial vertex bijections while preserving adjacency and nonadjacency to every already mapped vertex. This exhaustive backtracking produces 120 maps. Apply each map to the edge mask of a representative Hamiltonian cycle in each connected component. Since graph automorphisms preserve legal switches, the orbit of the resulting component is well defined. The component-orbit sizes are precisely 30, 60, 60, 20, classified respectively by component orders 36, 2, 1, 1. The first orbit implies that all components of order 36 are isomorphic. Their degree multiset and diameter follow from the complete adjacency computation.

The exhaustiveness is finite and exact: the vertex-order recursion covers all paths with no repeated vertex; the four-cycle loop covers every admissible two-edge symmetric difference; and the graph traversal covers all reachable cycles. No probabilistic sampling, bounded-depth truncation, or inference from a timeout enters the argument.

## Verification
Run with Python 3, using only the standard library, from a directory containing the three named files:

```text
python verify_flips.py certificate.json
python verify_direct.py certificate.json
```

`verify_flips.py` reconstructs the graph from its six edge families, independently enumerates all anchored Hamiltonian cycles, constructs all four-cycle-mask switches, determines component sizes and diameters, enumerates the full automorphism group, and checks component orbits. `verify_direct.py` instead builds the graph from its 20 triangular faces, enumerates the cycles as explicit vertex orderings, and implements two-opt by reversing the intervening tour segment. Both recompute and compare the **entire** 1,280-row cycle table and the **entire** 1,800-pair switch table in `certificate.json`, rather than only aggregate totals. The expected terminal messages are recorded in `VERIFICATION.md`.

## Relationship to prior work
Hopkins (2004) proves topological uniqueness of Hamiltonian cycles of the dodecahedral graph and demonstrates different symmetry types on the icosahedron, using incidences with Platonic faces. That is an analysis of cycles and symmetry, not a switch-adjacency classification. A 2010–2011 discussion by O'Rourke and Wynn counts 512 undirected icosahedral Hamiltonian cycles through any fixed edge and classifies their symmetry types. The global number 1,280 is already implicit in this count, since every Hamiltonian cycle contains 12 of the 30 graph edges; **the cycle count is not presented as novel**.

Takaoka (2018) formally studies precisely the two-edge Hamiltonian-cycle switch, proves reconfiguration complexity results, and supplies connectivity theorems for unit interval and bipartite permutation graphs. Those theorems do not cover the icosahedral graph, and the material inspected contains no icosahedron-specific component or adjacency data. The contribution here is the complete finite switch graph, its severe disconnection, and its component-symmetry classification, not the operation, the known cycle count, or a general complexity theorem.

## Limitations
This is a self-contained finite result, checked by two computationally independent formulations but not independently audited by another mathematician. Neither the listed references nor searches exclude an earlier unindexed enumeration of the same switch graph. Component isomorphism follows from the explicitly checked automorphism action, not a closed-form all-graph theorem. The 36-vertex component \(H_{36}\) is specified by its induced adjacency from `certificate.json`; no simpler canonical graph identification is claimed. There is no extrapolation to other polyhedral graphs or different notions of Hamiltonian-cycle move.

## References
1. B. Hopkins, *Hamiltonian Paths on Platonic Graphs*, International Journal of Mathematics and Mathematical Sciences **2004** (2004), 1613–1616, DOI: 10.1155/S0161171204307118. First published online 18 July 2004. https://doi.org/10.1155/S0161171204307118
2. A. Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration*, Algorithms **11** (2018), article 140, DOI: 10.3390/a11090140. https://doi.org/10.3390/a11090140
3. J. O'Rourke, question (5 September 2010) and E. Wynn, answer (16 January 2011), *Why are there 1024 Hamiltonian cycles on an icosahedron?*, MathOverflow 37788. https://mathoverflow.net/questions/37788/
