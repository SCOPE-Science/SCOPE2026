# Octagon flips connect all Möbius–Kantor perfect matchings despite frozen hexagon states

## Finding
Let \(G=GP(8,3)\) be the sixteen-vertex Möbius–Kantor graph. On its perfect matchings, let \(F_6\) and \(F_8\) join two matchings when their symmetric difference is one simple alternating cycle of length six and eight, respectively. The exact claims are:

1. \(G\) has \(33\) perfect matchings, \(F_6\) has \(96\) edges and component sizes \(30,1,1,1\), and \(F_8\) has \(36\) edges and is connected.
2. \(F_8\) is the following explicit \(33\)-vertex graph \(T\): take three hubs; attach eight pendant leaves to each hub; and for each pair of hubs, install two internally disjoint paths of length two. Its three hubs are exactly the matchings isolated in \(F_6\).
3. \(F_8\) has radius \(3\), diameter \(4\), and degree multiset \(\{12^3,2^6,1^{24}\}\). Thus octagon flips **alone** transform any perfect matching into any other in at most four steps, while all hexagon flips together fail to connect the state space. The least upper bound on the lengths of permitted simple-cycle flips giving connectivity is exactly \(8\).
4. Allowing both lengths yields \(132\) edges, vertex degrees \(7\) (24 matchings), \(10\) (six matchings), and \(12\) (three matchings); all vertices then have eccentricity \(3\).

The three hexagon-frozen matchings are the all-spoke matching and two complementary-phase no-spoke matchings. The \(30\)-vertex nontrivial component of \(F_6\) has radius \(3\), diameter \(4\), with \(24\) vertices of degree \(6\) and six of degree \(8\).

## Assumptions and scope
The graph has outer vertices \(u_i\) and inner vertices \(v_i\), where \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_i u_{i+1}\), \(v_i v_{i+3}\), and \(u_i v_i\), all indices modulo eight. These are undirected simple edges. The computer-readable labeling is \(u_i=i\), \(v_i=8+i\).

A perfect matching covers every vertex exactly once. A legal \(\ell\)-flip, where \(\ell\in\{6,8\}\), replaces the \(\ell/2\) matching edges of a **simple** alternating \(\ell\)-cycle by its other \(\ell/2\) edges. Every simple cycle of the specified length is permitted; the move is **not** restricted to cycles that bound a face in any chosen surface embedding. Paths in \(F_6\) and \(F_8\) have unit edge lengths.

## Proof
**Matching enumeration.** The graph is bipartite with classes \(\{u_0,u_2,u_4,u_6,v_1,v_3,v_5,v_7\}\) and its complement. A perfect matching is exactly a bijection between these eight-vertex classes that follows the listed edges. Consequently, checking all \(8!=40320\) bijections is exhaustive. The independent second method recursively matches the least uncovered vertex to one of its three neighbors; the two methods give the identical sorted list of exactly \(33\) edge sets in `certificate.json`. The distribution by number of spokes is \(4,16,12,1\) for respectively \(0,2,4,8\) spokes, with no other spoke counts.

**Flip equivalence.** For any two distinct perfect matchings \(M,N\), the symmetric difference \(M\triangle N\) is a vertex-disjoint union of simple even alternating cycles. Therefore \(M,N\) are joined by one \(\ell\)-flip if and only if their symmetric difference itself is one simple cycle with exactly \(\ell\) edges. This criterion is both necessary and sufficient and does not assume a planar embedding.

**Complete finite adjacency certificate.** There are precisely \(\binom{33}{2}=528\) unordered pairs to check. The first independent program tests each pair with the preceding criterion; it finds \(96\) hexagon pairs and \(36\) octagon pairs. The second independent program instead enumerates **all** graph simple cycles of length six and eight (respectively \(24\) and \(30\) edge sets), checks every matching's alternating occupancy, performs the symmetric-difference replacement, and obtains the **same** pairs. Both compare the complete labeled matching list and pair lists to the embedded `certificate.json`. This checks exhaustion of the matching space, legal moves, and adjacency rather than merely numerical totals.

**Structural isomorphism.** In the octagon adjacency list, exactly three vertices have degree \(12\), six have degree \(2\), and \(24\) have degree \(1\). Every edge has a degree-12 endpoint. Each degree-12 vertex has exactly eight degree-one neighbors and four degree-two neighbors; for each unordered pair of degree-12 vertices, exactly two degree-two vertices have precisely those hubs as neighbors. These verified incidence conditions construct the claimed isomorphism with \(T\) directly. The three hubs coincide with the three degree-zero vertices in the hexagon adjacency list. Explicitly, one hub uses all eight spokes, while the other two have no spokes. The other \(30\) vertices form one hexagon-connected component, as exhaustive breadth-first searches verify.

**Distances and sharpness.** In \(T\), each hub has eccentricity \(3\). A pendant leaf has eccentricity \(4\), attained by a pendant leaf at a different hub, and each degree-two vertex has eccentricity \(4\). Hence \(F_8\) has radius \(3\) and diameter \(4\). Any legal flip shorter than length eight must, since the girth is six, have length six. Such flips leave three matchings isolated, so the minimum successful maximum permitted cycle length is eight. Exhaustive breadth-first searches on the union of the two certified edge lists give eccentricity exactly three at each of its \(33\) vertices. The respective degree counts and \(132\) total edges follow from those edge lists.

## Verification
With Python 3 standard library and the three standalone files in one directory, run:

```
python3 verify_bipartite.py certificate.json
python3 verify_cycles.py certificate.json
```

Each script independently constructs all matchings and all required adjacency pairs, checks the full embedded certificate, and asserts the claimed structures and distances. The captured outputs are `bipartite_output.txt` and `cycles_output.txt`. The two methods compute the same canonical certificate fingerprint:

`7594df583189eabc5ab8acb6feff960f57f872dfbeca09e3c79888614b332a33`

This digest identifies the complete ordered data and is a reproducibility aid, not an independent proof without inspection of the algorithms and their run conditions. All loops run over explicitly finite spaces, so there is no unproved infinite extrapolation.

## Relationship to prior work
Marušič and Pisanski (2000) identify \(GP(8,3)\) with the Möbius–Kantor graph and document its bipartite Cayley structure and toroidal hexagonal and octagonal embeddings. Their graph-structure results do not specify the perfect-matching flip graphs. Lijnen and Ceulemans (2004) study symmetry-distinct embeddings of the same graph, a different object. De Carvalho, Lucchesi, and Murty (2013) develop lower bounds on perfect-matching counts for bipartite matching-covered graphs, not adjacency under prescribed alternating-cycle flips.

Balasubramanian (2025) explicitly gives the number \(33\) as the coefficient of the perfect-matching term in the graph's matching polynomial; this number is **not claimed as a new previously unknown invariant**. Its knowledge does not imply which matchings are connected by given cycles. Bošković (2026) studies general flip-connectedness under bounded cycle lengths; the inspected full text concerns decorated graph families and does not identify the octagon-only graph \(T\) for \(GP(8,3)\). In particular the acceptable decorations with more than two distinguished vertices in that framework are non-bipartite, while \(GP(8,3)\) is bipartite.

The novel content asserted here is the sharp local-move threshold and the complete three-hub structural classification of the octagon-only dynamics, together with its contrast to hexagon-only dynamics. It is not an embedding census, an enumeration of matchings alone, or a homotopy calculation for the matching complex.

## Limitations
This is an exact theorem for one finite graph, not a statement about all generalized Petersen graphs or all toroidal bipartite graphs. All moves use **all** simple cycles of the designated lengths, not embedding-dependent facial moves. No mixing-time estimate is claimed. Relevant published graph-embedding and matching-polynomial material was not uniformly accessible in complete text; unseen equivalent results remain a priority risk. An older, year-dated graph-structure paper predates the earliest day-resolved publication record used for chronological classification; no unverified day has been invented. The finding has undergone self-review only; no independent audit has been performed.

## References
1. D. Marušič and T. Pisanski, “The remarkable generalized Petersen graph \(G(8,3)\),” *Mathematica Slovaca* 50 (2000), 117–121, full OA text: https://dml.cz/dmlcz/133137.
2. E. Lijnen and A. Ceulemans, “Oriented 2-cell embeddings of a graph and their symmetry classification: generating algorithms and case study of the Möbius–Kantor graph,” *Journal of Chemical Information and Computer Sciences* 44 (2004), 1552–1564, DOI: 10.1021/ci049865c.
3. K. Kutnar and D. Marušič, “A complete classification of cubic symmetric graphs of girth 6,” *Journal of Combinatorial Theory B* 99 (2009), 162–184, DOI: 10.1016/j.jctb.2008.06.001.
4. M. H. de Carvalho, C. L. Lucchesi, and U. S. R. Murty, “On the Number of Perfect Matchings in a Bipartite Graph,” *SIAM Journal on Discrete Mathematics* 27 (2013), 940–958, DOI: 10.1137/120865938.
5. K. Balasubramanian, “Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions,” *Symmetry* 17 (2025), 133, DOI: 10.3390/sym17010133.
6. V. Bošković, “Flip dynamics on perfect matchings beyond bipartite and planar graphs,” arXiv:2607.16101 (2026), https://arxiv.org/abs/2607.16101.
