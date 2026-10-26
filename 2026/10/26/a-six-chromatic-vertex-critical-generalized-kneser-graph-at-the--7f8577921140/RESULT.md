# A six-chromatic vertex-critical generalized Kneser graph at the first isolated-cycle boundary

## Finding

Let \(U=\{0,1,\ldots,9\}\). Give \(0,1,\ldots,8\) the cyclic edges \(\{i,i+1\pmod 9\}\), and make \(9\) isolated; thus \(G=C_9\sqcup K_1\). Let \(\mathcal F\) consist of all three-element independent sets of \(G\), and construct the disjointness graph \(H\), with vertex set \(\mathcal F\) and an edge between distinct disjoint sets.

**Theorem.** This graph has \(57\) vertices and \(498\) edges, and is **six-vertex-critical**:
\[
\chi(H)=6,\qquad \chi(H-S)=5\quad\text{for every }S\in\mathcal F.
\]
Moreover, \(\omega(H)=3\). In particular, \(C_9\sqcup K_1\) is \(3\)-tight: it attains the chromatic upper bound \(|V(G)|-2\cdot3+2=6\). This is the first boundary instance beyond the short-cycle exclusion in the cited \(G\)-stable Kneser-graph conjecture.

## Assumptions and scope

All graphs are finite, simple, and undirected. The nine cycle labels are \(0,\ldots,8\), with consecutive values understood modulo \(9\). The isolated label is \(9\). The ordering of \(\mathcal F\) used for computation is increasing lexicographic order of its sorted triples, with zero-based indices. Vertex-critical means \(\chi(H)=6\) and deleting any one vertex reduces the chromatic number to \(5\); it is not an assertion of edge-criticality.

## Proof

**Size and edge count.** The cycle has \(30\) independent triples, and there are \(27\) independent pairs in the cycle; adjoining the isolated label to the latter gives the other \(27\) triples. Therefore \(|V(H)|=30+27=57\). Pairs of triples both containing the isolated label are never disjoint. Among the \(30\) cycle-only triples there are \(138\) disjoint unordered pairs, and between cycle-only triples and isolated-label triples there are \(360\) disjoint pairs. Direct loops over the explicitly defined triples, checked independently in the supplied programs, thus give \(|E(H)|=138+360=498\).

**Six colors suffice.** If a triple contains one of \(0,\ldots,4\), color it by its least such element. Otherwise, give it color \(5\). Two triples given a color in \(0,\ldots,4\) intersect at that label; two triples colored \(5\) are both three-subsets of the five-element set \(\{5,6,7,8,9\}\), hence intersect. Therefore this is a proper six-coloring.

**Five colors do not suffice.** The standalone exact-search implementations `chromatic_obstruction.cpp` and `verify_kneser.py` construct \(\mathcal F\) afresh from its definition and explore proper five-colorings. At each search node the already used colors may, without loss of generality, be renamed \(0,\ldots,u-1\). The algorithm selects an uncolored vertex of maximum saturation (number of different neighbor colors already present), breaking ties by its number of remaining uncolored neighbors and then by lexicographic index. It branches on each permissible previously used color and, if fewer than five colors are used, a single fresh color \(u\). Any other unused color is equivalent under permuting color names. Thus every hypothetical proper five-coloring has a representative in the search. Both implementations exhaust the search and return *no* five-coloring after exactly \(122153\) recursive calls; neither accepts a time limit or treats an incomplete search as a proof. This finite exhaustive certificate proves \(\chi(H)\ge6\), and the preceding explicit coloring gives equality.

**Every vertex is critical.** Rotation and reflection of the labeled nine-cycle, fixing the isolated vertex, induce the dihedral automorphism group on \(H\). Directly under this action the \(57\) vertices form six orbits represented by the triples
\[
(0,2,4),\ (0,2,5),\ (0,2,9),\ (0,3,6),\ (0,3,9),\ (0,4,9),
\]
with sizes respectively \(9,18,9,3,9,9\). The file `deletion_orbit_witnesses.txt` contains a proper five-coloring after deletion of each of the six representatives. Each of its six rows specifies the zero-based index of the removed triple and a \(57\)-character assignment, with `-` at the removed index and color digits `0` through `4` elsewhere. The separate Python verifier reconstructs the graph, checks all six row assignments edge by edge, computes all \(18\) dihedral permutations, validates that they preserve adjacency, transports the six assignments under them, and confirms that all \(57\) possible deletion indices are covered by legal five-colorings. Thus \(\chi(H-S)\le5\) for all \(S\). Since adding one vertex to a graph can increase its chromatic number by at most one, \(\chi(H)=6\) implies \(\chi(H-S)\ge5\). Hence equality holds for every deletion.

**Clique number.** Three mutually disjoint independent triples are \(\{0,3,6\}\), \(\{1,4,7\}\), and \(\{2,5,8\}\), giving a triangle. Four pairwise disjoint triples would occupy at least twelve of the ten ground-set vertices, which is impossible. Therefore \(\omega(H)=3\).

## Verification

The self-contained files `verify_kneser.py`, `chromatic_obstruction.cpp`, and `deletion_orbit_witnesses.txt` are sufficient to reproduce the finite part of the proof. In one directory, run `python3 verify_kneser.py`; optionally compile `chromatic_obstruction.cpp` using a C++17 compiler and run its executable. Both independently regenerate the \(57\) vertices and \(498\) edges, rule out every canonical five-coloring in \(122153\) states, and the Python verifier additionally checks the six dihedral-orbit deletion witnesses. The Python program uses only the standard library, and the C++ program has no external dependencies. The five-color obstruction is established by complete finite search; it is not an unproved extrapolation or a claim of an independently audited proof.

## Relationship to prior work

Arana, Haxell, Kaiser, and Stehlík introduced \(G\)-stable Kneser graphs and formulated a sufficient-condition conjecture for \(k\)-tightness. Their Theorem 1.2 excludes a cycle of length at most \(4k-4\) with an additional vertex; their Theorem 1.4 proves eventual tightness for \(C_{n-1}\sqcup K_1\), but does not specify the first value for \(k=3\). They explicitly describe the cycle-plus-isolated-vertex case as open beyond asymptotics, while noting that computational tests support their conjecture. The present theorem settles the first \(k=3\) instance at cycle length \(9=4k-3\) and further establishes complete vertex-criticality. The length-eight comparison is already determined by their short-cycle bound together with Schrijver's cycle theorem; it is not claimed as new.

Schrijver's classical theorem proves vertex-criticality for stable Kneser graphs based on a single cycle. The graph here is not such a Schrijver graph: it has \(57\) vertices, whereas the corresponding \(\operatorname{SG}(10,3)\) has \(50\). Neither the classical one-cycle theorem nor its numerical equality directly establishes this graph's claim.

## Limitations

The asserted criticality concerns deletion of vertices of the *disjointness graph* \(H\), not deletion of vertices of its underlying graph \(G\). No corresponding statement for longer cycles, larger set sizes, arbitrary unions of paths and cycles, or edge deletion is proved. The non-five-colorability certificate is exhaustive computer-assisted finite reasoning, not a short traditional argument. A related paper mentions unspecified computational tests, so unpublished prior verification of this first case remains possible; no priority or independence certification is claimed.

## References

1. Carmen Arana, Penny Haxell, Tomáš Kaiser, and Matěj Stehlík, *The chromatic number of G-stable Kneser graphs*, arXiv:2610.17884, first submitted 2026-10-13, https://arxiv.org/abs/2610.17884. In particular Conjecture 1.3, Theorems 1.2 and 1.4.
2. A. Schrijver, *Vertex-critical subgraphs of Kneser-graphs*, Nieuw Archief voor Wiskunde 26 (1978), 454–461. Bibliographic record: https://research.tue.nl/en/publications/vertex-critical-subgraphs-of-kneser-graphs/.
3. C. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688, 2010, https://arxiv.org/abs/1003.5688 (context on the classical one-cycle family).
