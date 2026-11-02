# A sharp two-to-three-class trade threshold for optimal strong edge-colourings of the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the vertex–line incidence graph of the Fano plane. A strong edge-colouring is a partition of its edges into induced matchings. Ignore permutations of colour names, and let \(\mathcal P\) be the set of all strong edge-colourings using the minimum possible seven colours. For \(k\in\{2,3\}\), define the \(k\)-class trade graph \(\mathcal T_k\) on \(\mathcal P\): two distinct partitions are adjacent precisely when at least \(7-k\) of their seven unordered colour classes agree. Equivalently, at most \(k\) whole colour classes can be repartitioned while leaving the others intact, with the result again an optimal strong edge-colouring.

**Theorem.** The set \(\mathcal P\) has exactly \(416\) elements. The two-class trade graph \(\mathcal T_2\) has no edges. The three-class trade graph \(\mathcal T_3\) has \(416\) vertices, \(1568\) edges, one component, radius \(6\), and diameter \(6\). Its degree distribution is \(112\) vertices of degree \(5\), \(280\) of degree \(8\), and \(24\) of degree \(14\). Under the full automorphism group of \(H\), these optimal colourings form exactly six orbits, of sizes \(8,16,56,112,112,112\).

In particular, no nontrivial optimum can be reached by retuning two colour classes, but **every optimum can be reached from any other by at most six three-class trades**, and this bound is sharp. The value of the strong chromatic index itself, \(\chi'_s(H)=7\), is known and is not claimed as new.

## Assumptions and scope

This is an exact theorem about the fixed fourteen-vertex simple Heawood graph and the stated simultaneous whole-class trade operation. All seven colours are used; colour names carry no data; a move may change the membership of three classes simultaneously, rather than being required to pass through intermediate proper colourings. No result about arbitrary other graphs, labelled-colour transition distances, or more restrictive Kempe-chain moves is asserted.

A self-contained incidence model has points \(p\in\mathbb Z/7\mathbb Z\), lines indexed by \(j\in\mathbb Z/7\mathbb Z\), and line \(L_j=\{j,j+1,j+3\}\) (arithmetic modulo \(7\)). The \(21\) graph edges are the incident flags \((p,j)\) satisfying \(p\in L_j\). Distinct flags \((p,j)\) and \((q,h)\) may share an induced matching exactly when \(p\ne q\), \(j\ne h\), \(p\notin L_h\), and \(q\notin L_j\).

## Proof

**Maximum induced-matching size.** Any four pairwise compatible flags would use four different points, with each of their four lines meeting this four-point set in exactly one point. But a four-point set of the Fano plane has either no collinear triple (then every line through each of its points meets another selected point), or one collinear triple (then its fourth point has no tangent through it). Hence no four flags can be pairwise compatible. There are compatible triples, exhibited by the verification programs, so the maximum induced matching size is exactly \(3\). Because \(H\) has \(21\) edges, at least seven induced-matching colour classes are needed.

**Existence and classification.** One explicit seven-class edge partition, writing every class as three \((p,j)\) flags in the incidence model above, is:

\[
\begin{aligned}
&\{(0,4),(1,5),(2,2)\},\quad \{(0,6),(1,1),(3,2)\},\\
&\{(0,0),(4,3),(5,2)\},\quad \{(2,6),(3,3),(5,5)\},\\
&\{(2,1),(5,4),(6,3)\},\quad \{(3,0),(4,1),(6,5)\},\\
&\{(1,0),(4,4),(6,6)\}.
\end{aligned}
\]

Every class above is an induced triple; the seven classes partition all \(21\) flags. Thus seven is optimal. To enumerate **all** optima, enumerate the \(\binom{21}{3}=1330\) edge triples, retaining exactly the \(84\) pairwise compatible triples. Start with all edges uncovered; choose the least-index uncovered edge, branch over each of the retained triples containing it and disjoint from already chosen triples, and continue until the entire \(21\)-edge set is covered. Since every optimum consists of seven triples, this recurrence reaches every optimum. Since the chosen least uncovered edge uniquely identifies its class at each stage, it reaches no unordered partition twice. Exhausting this exact finite recurrence produces precisely \(416\) partitions.

**Trade threshold and distances.** Regard an optimum as a seven-element set of triple-edge masks. Two distinct optima admit a two-class trade exactly when they share at least five masks; they admit a three-class trade exactly when they share at least four masks. A complete comparison of the \(\binom{416}{2}=86320\) unordered optimum pairs yields no pair with five shared classes and exactly \(1568\) pairs with four shared classes. A stronger check lists all disjoint pairs of induced triples: their unions have \(2296\) unique two-triple decompositions and \(14\) fourfold decompositions. None of those fourteen ambiguous unions is the union of two classes of a complete optimum. This directly certifies two-class rigidity rather than assuming it from the absence of detected paths.

Form the graph on the \(416\) enumerated partitions from the \(1568\) four-common-class pairs. Exact breadth-first searches from **every** vertex visit all \(416\) vertices and yield eccentricity exactly \(6\). The degree multiset is \(5^{(112)},8^{(280)},14^{(24)}\). Hence the graph is connected with radius and diameter \(6\).

**Symmetry.** All \(168\) permutations of the seven points preserving the Fano lines are enumerated. Each induces a permutation of the seven lines. Adjoining the explicit point–line duality \(p\mapsto L_{-p}\), \(L_j\mapsto -j\) gives \(336\) distinct graph automorphisms, the full known Heawood automorphism group. Apply their edge actions to each exact-cover partition and exhaust its orbit. The six disjoint orbit sizes are \(8,16,56,112,112,112\), summing to \(416\). The corresponding three-class degrees are \(14,14,8,8,8,5\). This proves the stated symmetry classification.

## Verification

The embedded `verify.py` uses the cyclic Fano incidence model. It checks pairwise incidence compatibility, all \(\binom{21}{4}=5985\) potential four-edge matchings, the exact-cover recurrence, the two-colour union decomposition check, every three-class adjacency, every shortest-path eccentricity, and all \(336\) automorphism actions. The second embedded implementation `verify_alt.cpp` independently constructs the Fano plane from the seven nonzero vectors of \(\mathbb F_2^3\), checks every potential four-edge induced matching, enumerates all unordered seven-triple edge partitions, compares every pair of partitions, and recomputes the exchange distances. Both execute successfully. The finite work is exhaustive, not a random sample or an extrapolation to an unbounded family.

Run `python3 verify.py`. Independently compile and run `c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. Both programs are self-contained and require no external data. A source file by itself is not a proof of execution; actual checks are described in `VERIFICATION.md`.

## Relationship to prior work

Strong edge-colouring and its equivalence to proper vertex colouring of the square of the line graph are standard; Kloks, Ung and Wang (2011) study this problem in particular graph classes. Faudree, Schelp, Gyárfás and Tuza had already recorded the Heawood value \(7\), and Skupień (2023; first available online 2021) gives an explicit Heawood seven-colour construction and proves uniqueness of the analogous induced-triple decomposition for the Petersen graph, not the Heawood graph. Lužar, Mačajová, Škoviera and Soták (2021) also acknowledge the known Heawood index \(7\) in their study of cubic graphs and Kneser covers. None of those inspected papers states the present Heawood optimum-partition count or the exact two-versus-three-class trade threshold. Ordinary proper three-edge-colourings and vertex harmonious colourings of \(H\) are different objects and do not determine this classification.

## Limitations

The result is limited to the Heawood graph and the precisely defined whole-colour-class trade, not conventional single-edge recolouring or Kempe-chain equivalence. There is no claim of uniqueness in the global mathematical literature: potentially equivalent unpublished, unindexed, or inaccessible work remains a priority risk. The exact enumeration and the group-orbit computation depend on executing the supplied small, deterministic programs; they are not replaced by a hand-derived closed orbit-count formula. No independent scholarly audit is asserted.

## References

1. T. Kloks, C.-T. Ung and Y.-L. Wang, *On the strong chromatic index and maximum induced matching of tree-cographs, permutation graphs and chordal bipartite graphs*, first available 17 October 2011, arXiv:1110.3583, https://arxiv.org/abs/1110.3583.
2. Z. Skupień, *The Petersen and Heawood graphs make up graphical twins via induced matchings*, Discussiones Mathematicae Graph Theory **43** (2023), 677–683, DOI:10.7151/dmgt.2394, https://geodesic.mathdoc.fr/item/DMGT_2023_43_3_a5/ (first publicly online in 2021).
3. B. Lužar, E. Mačajová, M. Škoviera and R. Soták, *Strong edge colorings of graphs and the covers of Kneser graphs*, arXiv:2101.04768 (2021), https://arxiv.org/abs/2101.04768.
4. R. J. Faudree, R. H. Schelp, A. Gyárfás and Zs. Tuza, *The strong chromatic index of graphs*, Ars Combinatoria **29B** (1990), 205–211, as cited in references 2 and 3.
