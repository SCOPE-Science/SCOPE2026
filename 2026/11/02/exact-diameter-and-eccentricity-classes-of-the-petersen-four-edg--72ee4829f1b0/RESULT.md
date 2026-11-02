# Exact diameter and eccentricity classes of the Petersen four-edge-colouring Kempe graph

## Finding
Let \(P=KG(5,2)\) be the Petersen graph. Give its fifteen edges four individually named colours, with adjacent edges required to have different colours. The **edge-Kempe graph** \(\mathcal K(P,4)\) has these proper colourings as vertices; two colourings are adjacent when one results from interchanging two colours on a *single connected component* of the two-coloured edge-induced subgraph of \(P\). Thus a maximal alternating path or cycle is exchanged, not necessarily all edges of those colours.

An exact exhaustive classification establishes that \(\mathcal K(P,4)\) has \(49{,}920\) vertices and \(377{,}280\) edges, and is connected. The complete degree distribution is \(44{,}160\) vertices of degree \(15\) and \(5{,}760\) of degree \(16\). Under the natural action of graph automorphisms and palette permutations, it has exactly \(21\) configuration orbits. Its radius is \(7\), its diameter is \(8\), and the eccentricities occur as \(7\) at \(45{,}600\) vertices and \(8\) at \(4{,}320\) vertices. Exactly \(2{,}880\) unordered pairs lie at distance eight.

The size \(49{,}920\) and Kempe connectivity follow from previously available sources; the proposed contribution is the **exact local-degree, symmetry-orbit, eccentricity, and distance-eight-pair classification**.

## Assumptions and scope
The underlying graph is the fixed simple Petersen graph \(KG(5,2)\), not an arbitrary cubic graph. Four labels \(0,1,2,3\) are distinct and are not identified by a colour permutation when counting states. No individual edge recolouring or exchange of two nonmaximal segments is allowed. Two-coloured components may be single edges, alternating paths, or alternating cycles; the exchange must act on an entire connected component. Parallel candidate exchanges leading to the same state yield only one reconfiguration edge. The analysis is finite and exact, not an asymptotic or universal cubic-graph assertion.

For reproducible canonical coordinates, enumerate the ten two-subsets of \(\{0,1,2,3,4\}\) lexicographically as \(V_0,\ldots,V_9\); the fifteen Petersen edges are the lexicographically ordered pairs \((i,j)\), \(i<j\), with \(V_i\cap V_j=\varnothing\). The exact ordered list is recorded in `certificate.json`. A 15-digit word specifies the colour on each such edge in that order.

## Proof
**Complete states.** On a graph with fifteen edges, recursively choose an uncoloured edge whose legal-colour list is shortest, and branch over every available colour. The legal list excludes precisely those colours already used on adjacent edges. If a partial assignment has an empty list it has no extension. Therefore this recursion enumerates *every* proper named four-edge-colouring exactly once, regardless of the order of branching. The included `verify_petersen_kneser.py` realizes this recursion and obtains \(49{,}920\) distinct states.

**All moves.** For each state and each unordered colour pair \(\{a,b\}\), restrict the line graph of \(P\) to those edges coloured \(a\) or \(b\). Its connected components correspond precisely to the connected components of the two-coloured edge subgraph of \(P\). Interchanging \(a,b\) on each component gives every and only permitted Kempe neighbour, because properness at endpoints is preserved. The verifier deduplicates neighbours, verifies reciprocal adjacency, and obtains exactly \(377{,}280\) unordered moves and the stated degree distribution.

**Exhaustive metric certification with symmetry.** The symmetric group on the five ground symbols acts as graph automorphisms of \(KG(5,2)\); adjacent transpositions generate this group. Adjacent transpositions of the four colour labels generate the palette permutation group. Both actions preserve proper colourings and commute with the definition of Kempe moves; hence each is an automorphism of \(\mathcal K(P,4)\), preserving degree, distances, and eccentricity. By applying these generators, the code partitions all \(49{,}920\) states into exactly \(21\) disjoint orbits. A complete breadth-first search from one representative of **each** orbit traverses the entire state set. Consequently those twenty-one distance-sphere vectors, weighted by orbit sizes, determine distances from **every** state, not merely sampled distances. The recorded certificate and both verifiers yield radius \(7\), diameter \(8\), and eccentricity multiplicities \(45{,}600\) and \(4{,}320\).

Exactly two symmetry orbits have eccentricity \(8\): one has \(1{,}440\) elements, each with two states at distance eight, and the other has \(2{,}880\) elements, each with one. Every remaining orbit has none. Since unordered pairs are counted twice, the number of diametral unordered pairs is
\[
\frac{1{,}440\cdot 2+2{,}880\cdot1}{2}=2{,}880.
\]
In the canonical edge order, the colourings `012120203023101` and `203320031301220` form an explicit distance-eight pair. The orbit-root and target lists in `certificate.json` make this witness and all orbit-based totals independently replayable.

**Independent reconstruction.** The second program, `verify_petersen_gp.cpp`, constructs the Petersen graph instead as the generalized Petersen graph \(GP(5,2)\), enumerates ordered decompositions of its fifteen edges into four matchings, calculates bichromatic connected components using union-find on the *original* ten vertices, independently enumerates all \(120\) graph automorphisms by adjacency-preserving permutations, and repeats the orbit/BFS metric census. This distinct graph model and state enumerator independently produce the same global statistics and the same multiset of orbit sphere profiles. The procedures are exhaustive finite algorithms whose source is included, not an extrapolation from small examples or an appeal to a black-box log.

## Verification
From a directory containing all embedded artifacts, run `python3 verify_petersen_kneser.py --certificate regenerated.json`. Its regenerated certificate can be compared structurally with `certificate.json`; key order is nonmathematical. Compile `g++ -std=c++17 -O2 verify_petersen_gp.cpp -o independent_gp` and run `./independent_gp`. Neither algorithm needs external data or software beyond Python 3 standard library and a C++17 compiler. The independent program uses a different edge numbering, so the two sets of representative words are not directly comparable; their distance-sphere/degree/orbit-size multisets and global counts are. Both code paths have been executed on the submitted source.

## Relationship to prior work
OEIS A159233 already records the total number of proper four-edge-colourings of the Petersen graph as \(49{,}920\). McDonald, Mohar and Scheide prove that all proper four-edge-colourings of any subcubic graph are Kempe equivalent (their Theorem 3); connectedness for \(P\) is therefore **not** new. Belcastro and Haas study edge-Kempe-equivalence structures of *three*-edge-colourable cubic and class-one regular graphs; their results do not identify the degree/metric profile of the four-colour Kempe graph of the class-two Petersen graph. The present claim adds the complete precise finite reconfiguration metrics and symmetry structure in the minimum permitted palette for the smallest snark.

## Limitations
This is a finite exact result for \(P\), not a bound for general snarks or a new proof of universal Kempe connectivity. The enumerative proof is executable, so reproduction requires running and checking the included algorithms; `certificate.json` alone is a summary, not a self-proving independent certificate. The two implementations share the mathematical definition of a Kempe move but differ in graph representation, generation method, and bichromatic-connectivity method. A statement equivalent to the metric classification may exist under alternate terminology or in older unindexed computation tables. No independent scholarly review or audit has been performed.

## References
- OEIS Foundation, *A159233*, edge-colouring count sequence (entry created 6 April 2009), https://oeis.org/A159233 .
- J. McDonald, B. Mohar, D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248 (submitted 13 May 2010), especially Theorem 3, https://arxiv.org/pdf/1005.2248 .
- S. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (2012), https://arxiv.org/abs/1209.1730 .
- S. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, Australasian Journal of Combinatorics 69 (2017), 197–214.
- C. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956 (2020), https://arxiv.org/abs/2003.05956 .
