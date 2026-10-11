# The cuboctahedral matching complex is a wedge of \(57\) three-spheres

## Finding
Let \(Q_3\) be the ordinary three-dimensional cube graph and \(C=L(Q_3)\) its line graph, i.e. the cuboctahedral graph. The ordinary matching complex of \(C\), whose simplices are sets of pairwise vertex-disjoint edges of \(C\), satisfies the integral homotopy equivalence
\[\operatorname{Match}(C)\simeq\bigvee^{57} S^3.\]
Equivalently, the reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{57}\) and vanishes in all other degrees. No assumption on a coefficient field is made.

## Assumptions and scope
Use the labeled cube vertex set \(\{0,\ldots,7\}\), with edges \(\{a,b\}\) exactly when the binary XOR of \(a\) and \(b\) is one of \(1,2,4\). These twelve cube edges label the vertices of \(C\), and two are adjacent exactly when the underlying cube edges meet. Hence \(C\) has twelve vertices, twenty-four edges, and all degrees four. Every (possibly empty) matching of \(C\) determines one face of its matching complex; the empty set is included only for bookkeeping and is not a cell of the ordinary CW complex. All face counts and orientations below concern this exact labeled finite object.

## Proof
**Complete face enumeration.** Index the twenty-four edges of \(C\) lexicographically as \(e_0,\ldots,e_{23}\). Encode a face by a twenty-four-bit mask, with bit \(j\) set when \(e_j\) belongs to the matching. Start with the empty face. For each index \(j=0,\ldots,23\), append the masks obtained by setting bit \(j\) in each existing mask whose edges are all disjoint from \(e_j\). This inductively enumerates each matching exactly once. The resulting number of nonempty faces in dimensions zero through five is
\[(24,204,744,1116,528,32),\]
so there are exactly \(2648\) nonempty faces.

**Explicit acyclic matching.** On the ordinary nonempty face poset, process pivots \(j=0,\ldots,23\) in this order. At pivot \(j\), pair every still-unmatched face lacking bit \(j\) with its union with \(\{e_j\}\), if both are still unmatched faces; delete both from the unmatched set. This constructs precisely \(1287\) face pairs. Reorient every matched codimension-one Hasse edge upward and every other Hasse edge downward. The complete resulting digraph has \(2648\) vertices and \(9936\) arrows. Kahn's exact topological-sort algorithm visits all \(2648\) vertices; thus there is no directed cycle. The unmatched cells consist of one zero-cell, sixty-five three-cells, and eight four-cells, with none in any other dimension. The discrete-Morse CW reduction is therefore a wedge of sixty-five \(3\)-spheres before the eight \(4\)-cells are attached.

**Integral attaching degrees.** Orient each simplicial face by its increasing edge-index order. For a dimension-three face \(\tau\), its coefficient in the Morse boundary is computed recursively: (i) a critical \(\tau\) contributes its corresponding basis vector; (ii) a \(\tau\) matched downward to a two-face contributes zero; and (iii) if \(\tau\) is the lower member of a three-to-four match with upper face \(\beta\), use the boundary relation \(\partial\beta=0\) to replace \(\tau\) by the negative signed sum of all other three-faces in \(\partial\beta\). The already verified acyclicity ensures these gradient expansions terminate. Summing reductions of the oriented facets of each critical four-face computes the *integral* \(65\times8\) Morse boundary matrix, not a field approximation.

Order the sixty-five critical three-faces by increasing mask and the eight critical four-faces the same way. The rows with zero-based indices \(2,15,5,40,42,19,51,56\) form the diagonal matrix \[-I_8.\] The corresponding row masks, in that order, are `0x20888`, `0x80148`, `0x22410`, `0x402044`, `0x402802`, `0x82104`, `0x800148`, and `0x800908`. Therefore the degree matrix has rank eight and a unimodular eight-by-eight minor: its eight attaching vectors generate a primitive rank-eight direct summand of \(\mathbb Z^{65}\).

The critical three-skeleton is \(\bigvee^{65}S^3\), for which \(\pi_3\cong H_3\cong\mathbb Z^{65}\). Thus the signed degrees completely classify each four-cell attaching map up to homotopy. A change of basis of this free group is realized by a homotopy equivalence of the wedge, and the eight primitive independent four-cell attachments cancel eight of the three-spheres. The resulting homotopy type is exactly \(\bigvee^{57}S^3\), proving the assertion.

## Verification
Run `python3 verify_cubocta_morse.py` and `python3 verify_cubocta_mod2.py` from this directory. Both use only the Python standard library. The first reconstructs the graph, enumerates all faces, constructs and checks every matching pair, topologically sorts the complete reversed Hasse digraph, expands the signed Morse gradient paths, and verifies the displayed unimodular minor. It prints `VERIFY_OK` after its assertions pass.

The second independently enumerates matchings through combinations and endpoint-disjointness, then computes mod-two boundary ranks \(23,181,563,496,32\). They imply the reduced mod-two Betti vector \[(0,0,0,57,0,0),\] independently checking the combinatorial census and the rational rank pattern. The integral homotopy assertion relies specifically on the first program's signed unimodular matrix check, *not* on these mod-two data alone. Euler characteristic is \(24-204+744-1116+528-32=-56=1-57\), another consistency check.

## Relationship to prior work
Engström's study of claw-free independence complexes applies as a general setting because \(\operatorname{Match}(C)=\operatorname{Ind}(L(C))\) and line graphs are claw-free, but its connectivity results do not give this exact integral homotopy type. Kozlov developed explicit combinatorial simple-homotopy techniques for graph-related complexes; no theorem in the inspected paper specializes to the cuboctahedral matching complex. Matsushita treats strips and grid-derived families, not the double line graph \(L(L(Q_3))\). Bayer, Jelić Milutinović and Vega prove that matching complexes of **outerplanar** graphs are sphere wedges, and explicitly propose the wider planar case as a conjecture. The cuboctahedron is planar but cannot be outerplanar, since it has \(24>2\cdot12-3\) edges. Thus this computation supplies one explicit, non-outerplanar positive case of their planar wedge conjecture; it does *not* settle that conjecture in general. Their polygonal-line results also do not cover a quartic polyhedral graph.

The object is the matching complex on twenty-four graph edges, **not** the matching complex of the cube itself and **not** a Vietoris--Rips complex on the twelve cuboctahedral vertices. Relevant published research records on the matching complexes of the Heawood and Möbius--Kantor graphs concern different graphs, with no evident implication of the present numerical or homotopy statement.

## Limitations
The theorem concerns this one specified graph; it does not classify matching complexes of all planar graphs, all Archimedean graphs, or cube line graphs in higher dimension. The calculation is exhaustive only because the graph is finite; its certificate is a finite proof of this finite homotopy statement, not a general asymptotic claim. Literature searches cannot rule out an equivalent calculation in unindexed or unpublished material. No independent audit has been carried out.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (first public version December 17, 2005), Sections 1--2.
2. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1 (March 28, 2005), Sections 2 and 6--7.
3. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000v1 (December 28, 2018), Theorems 1.1--1.2.
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1 (November 7, 2024), Theorem 2 and Conjecture 11 (checked in v2 full text).
5. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, doi:10.1016/j.disc.2023.113428 (2023), Theorem 13.
6. E. W. Weisstein, *Cuboctahedral Graph*, MathWorld, https://mathworld.wolfram.com/CuboctahedralGraph.html (graph identity and structure).
