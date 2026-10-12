# The Möbius–Kantor graph recurs as a component of its edge-Kempe reconfiguration graph

## Finding

Let \(G=GP(8,3)\) be the Möbius–Kantor graph. The simple reconfiguration graph \(\mathcal K(G)\) of **unlabeled** proper three-edge-colorings, with an edge for one nontrivial bichromatic-cycle Kempe switch, satisfies
\[\boxed{\mathcal K(G)\cong G\sqcup K_{1,3}.}\]
It has twenty vertices, twenty-seven edges and two connected components of orders sixteen and four. The sixteen-vertex component has twenty-four edges and is isomorphic to the original Möbius–Kantor graph; the other is a three-leaf star. There are twenty one-factorizations (equivalently, 120 proper edge-colorings using three named colors). This is a statement about the color-permutation **quotient**, not the 120-vertex graph of named edge-colorings.

The sixteen colorings in the self-isomorphic component each have three two-color spanning factors of cycle lengths \(6\) and \(10\). The star center has three two-color factors of type \((8,8)\); its three leaves each have one type \((8,8)\) and two Hamiltonian types \((16)\). These profiles distinguish the components without referring to the certificate labels.

## Assumptions and scope

All graphs are finite, undirected and simple. Number the vertices \(0,\ldots,15\), with \(u_i=i\) and \(v_i=8+i\) for \(0\leq i<8\). The edges are \(u_i u_{i+1}\), \(u_i v_i\) and \(v_i v_{i+3}\), with indices taken modulo \(8\). This gives exactly sixteen vertices and twenty-four edges.

A one-factorization is an unordered set of three disjoint perfect matchings covering every edge. It is the same as a proper three-edge-coloring up to renaming its three colors. The vertices of \(\mathcal K(G)\) are these one-factorizations. Two distinct ones are joined when, after choosing a pair of color classes, the two colors can be exchanged on exactly one connected cycle of the corresponding bichromatic two-factor. The graph is simple: switches fixing the unordered factorization do not create loops, and repeated switches between the same pair give one edge.

## Proof

The argument uses two elementary exhaustive finite searches with explicit completeness invariants, and an edge-preserving bijection certificate. It is not an inference from partial sampling.

**1. Exhaust every matching.** Sort the twenty-four edges lexicographically and encode each edge set as a 24-bit integer. On a nonempty set of uncovered vertices, select its lowest numbered vertex \(u\). Every perfect matching on these vertices contains exactly one of the three incident edges \(uv\), with \(v\) uncovered; recurse on the remaining vertices. The empty vertex set has the unique empty matching. By induction on the number of uncovered vertices this enumerates every perfect matching once and only once. The exact result is thirty-three perfect matchings. Their complementary two-factor profiles are twenty-four of type \((6,10)\), six of type \((16)\), and three of type \((8,8)\). The thirty-three matching count is used as an input census here, not claimed as a new historical total.

**2. Exhaust every coloring.** For each ordered pair of disjoint enumerated matchings \(A,B\), the only possible third color class is the edge complement \(C=E(G)\setminus(A\cup B)\). Retain the triple exactly if \(C\) is another perfect matching, then sort its three matching indices and deduplicate. This gives twenty one-factorizations. Their unordered triples of complementary two-factor types occur with multiplicities \(16\) for \(((6,10),(6,10),(6,10))\), \(3\) for \(((8,8),(16),(16))\), and \(1\) for \(((8,8),(8,8),(8,8))\). Since every three-edge-coloring has three perfect-matching classes, and the pair-complement enumeration considers each such triple, no coloring can be omitted.

**3. Exhaust every switch.** For each of the twenty triples and each of its three pairs of color classes, the union is a two-regular spanning subgraph. Its connected components are exactly its alternating cycles. For each such component \(Q\), exchange the membership in the two matchings along its edges and canonically sort the resulting triple. Every permitted one-cycle Kempe switch occurs on one of these pairs and one of these components, so this procedure constructs the complete adjacency set. Removing loops and duplicates gives exactly twenty-seven unordered adjacency pairs. A component search gives components of orders sixteen and four. The former has twenty-four edges and all sixteen vertices have degree three; the latter has three edges with degree sequence \((3,1,1,1)\), so is \(K_{1,3}\). The color-type profile of the former is uniformly \(((6,10),(6,10),(6,10))\); the latter consists of the three Hamiltonian leaves and the \((8,8)\) center.

**4. Identify the sixteen-vertex component.** The accompanying `certificate.json` lists all twenty-four original edges; every one of the thirty-three perfect-matchings as a bitmask; all twenty factorizations as triples of matching indices; all twenty-seven switch-edges as pairs of factorization indices; the star component; and an explicit mapping of the sixteen indices in the other component onto \(\{0,\ldots,15\}\). The verifier checks that this map is bijective and that the image of the set of twenty-four component edges equals, pair for pair, the entire original edge set. Thus the isomorphism is certified directly, not inferred merely from degrees, girth or matching a few invariants.

The two independent enumerators implement distinct completeness arguments. `verify.py` recursively branches on uncovered vertices to generate all perfect matchings; `verify_independent.py` recursively assigns one of three colors directly to the twenty-four edges, forbids repeated colors at every vertex and fixes the color permutation at vertex zero. The latter independently obtains twenty colorings and the same exact set of twenty-seven Kempe adjacencies. Both check the embedded certificate. These exhaustive finite procedures, including their runnable implementations and complete finite outputs, prove the stated fixed-graph theorem.

## Verification

Run from the directory containing the three named artifacts:

```sh
python3 verify.py certificate.json
python3 verify_independent.py certificate.json
```

Both use Python 3 standard-library modules only. The first prints `VERIFY_CERTIFICATE_OK`, the matching and profile census, component sizes, and the verified explicit self-isomorphism. The second prints `VERIFY_INDEPENDENT_CERTIFICATE_OK`, the twenty normalized colorings (hence 120 named colorings), and exact agreement of the twenty-seven adjacency pairs.

The certificate uses a completely specified ordering: graph edges are sorted endpoint pairs; perfect matchings are sorted increasing by integer bitmask; one-factorizations are sorted triples of matching indices; reconfiguration edges are sorted pairs of factorization indices. Its isomorphism keys are the corresponding factorization indices. No network access, computer algebra system, external package or unverifiable log is needed.

## Relationship to prior work

Belcastro and Haas introduced and studied edge-Kempe equivalence classes for three-edge-colored cubic graphs [1], including constructions with several classes. They later studied the structure of associated reconfiguration graphs and of normalized colorings at a fixed vertex, providing product theorems and examples such as a generalized Petersen graph on fourteen vertices with a cycle as its normalized reconfiguration graph [2]. The present calculation uses their existing notion; it does not claim that Kempe switching or the normalized graph construction is new.

Goedgebeur and Östergård [3] systematically enumerated numbers of Kempe classes of cubic graphs, including all connected bipartite cubic graphs on sixteen vertices. Their table aggregates how many base graphs have each possible number of classes and does not print this Möbius–Kantor graph's complete twenty-coloring adjacency or the self-isomorphic component. Thus the bare fact of two classes is not presented here as a priority claim independent of their exhaustive census. The proposed distinction is the **complete, explicitly labeled reconfiguration-graph isomorphism** and the componentwise two-factor profiles. The source's general algorithm could reproduce these data when run on this particular base graph; that computational recoverability is acknowledged rather than denied.

Ye and Zhang's semi-Kotzig work [4] concerns Hamiltonian pairs of colors and switching on even subgraphs, but does not classify this particular finite reconfiguration graph. Existing records on the Möbius–Kantor matching complex and identifying codes concern different invariants of the same base graph, and neither implies the claimed Kempe adjacency structure.

## Limitations

The theorem concerns precisely the sixteen-vertex graph \(GP(8,3)\); it is not a statement for other generalized Petersen graphs or arbitrary cubic graphs. It concerns colorings up to global permutation and explicitly discards self-switches and parallel switch labels; different conventions yield different reconfiguration graphs. The exhaustive programs are finite exact proofs at this fixed order, not proofs about an infinite family. The available published evidence leaves a residual priority risk from graph-specific information that may be present in unindexed code/data or earlier enumerations not located in this literature comparison. No independent mathematical audit is asserted.

## References

[1] s.m. belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (first publicly submitted 8 September 2012); Discrete Mathematics 325 (2014), 77–84. https://arxiv.org/abs/1209.1730

[2] s.m. belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, Australasian Journal of Combinatorics 69(2) (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf

[3] J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363 (2021). https://arxiv.org/abs/2105.01363

[4] D. Ye and C.-Q. Zhang, *Cycle Double Covers and Semi-Kotzig Frame*, arXiv:1105.5190 (26 May 2011). https://arxiv.org/abs/1105.5190
