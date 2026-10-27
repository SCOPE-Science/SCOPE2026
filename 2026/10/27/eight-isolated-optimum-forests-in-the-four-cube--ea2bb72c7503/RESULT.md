# Eight isolated optimum forests in the four-cube

## Finding

Let \(Q_d\) denote the graph whose vertices are binary words of length \(d\), adjacent precisely when their Hamming distance is one. Write \(E_d\) and \(O_d\) for its even- and odd-parity vertex classes, and write \(\overline v\) for the bitwise complement of a word \(v\). An *induced forest* is a vertex subset whose induced graph is acyclic. Two maximum induced forests are *exchange-adjacent* if one is obtained from the other by removing one selected vertex and inserting one unselected vertex.

**Theorem.** The maximum induced forest of \(Q_4\) has ten vertices. Its complete family of maximum vertex sets is
\[
\mathcal F_4=\bigl\{E_4\cup\{v,\overline v\}:v\in O_4\bigr\}\ \cup\ \bigl\{O_4\cup\{v,\overline v\}:v\in E_4\bigr\},
\]
where repeated representations of an antipodal pair are identified. There are exactly eight such sets. Each induces two vertex-disjoint copies of \(K_{1,4}\), and **all eight vertices of the maximum-forest exchange graph are isolated**. Equivalently, all minimum feedback vertex sets in \(Q_4\) have six vertices and are precisely the complements of those eight forests.

For contrast, the maximum induced forests of \(Q_3\) have five vertices, there are exactly 32 of them, and their one-vertex exchange graph is connected. The same exchange graph for \(Q_2\) is \(K_4\), and \(Q_1\) has a single maximum forest. Thus \(Q_4\) is the first positive binary hypercube dimension with disconnected maximum-induced-forest exchange graph.

The numerical size of a maximum induced forest/decycling number in cubes is covered by earlier literature; the asserted contribution is the **exhaustive equality classification and optimal-exchange rigidity at the first disconnection dimension**.

## Assumptions and scope

Graphs are finite, undirected, and simple. The binary words are individually labelled by their coordinate positions. All induced subgraphs use all edges inherited from their ambient hypercube. An exchange always changes **exactly one selected and one unselected vertex** while keeping maximum cardinality and acyclicity; no intermediate nonoptimal set is allowed. The theorem treats positive dimensions one through four, and asserts no all-dimensional characterization.

## Proof

**1. Upper bound at dimension four.** The graph \(Q_4\) has sixteen vertices, thirty-two edges, and degree four. Let \(F\) be an induced forest with eleven vertices and let \(D=V(Q_4)\setminus F\), so \(|D|=5\). Counting edges incident with \(D\) gives
\[
 e(Q_4[F])=32-4|D|+e(Q_4[D])=12+e(Q_4[D])\ge12.
\]
But a forest on eleven vertices has at most ten edges, a contradiction. Every larger induced forest would contain an eleven-vertex induced forest. Hence \(|F|\le10\).

**2. Restrictions at equality.** Now let \(|F|=10\), \(|D|=6\). The analogous identity is
\[
 e(Q_4[F])=8+e(Q_4[D]).
\]
A forest on ten vertices has at most nine edges. Therefore \(e(Q_4[D])\le1\). Put \(a=|D\cap E_4|\), \(b=|D\cap O_4|\), so \(a+b=6\). We prove that \(a=0\) or \(b=0\).

If \((a,b)=(2,4)\), the two deleted even vertices are either at Hamming distance two or four. If they are antipodal, their neighborhoods partition all eight odd vertices, so the four deleted odd vertices create four edges in \(Q_4[D]\). If their distance is two, their eight odd vertices have incident-degree pattern \(2,2,1,1,1,1,0,0\) into the chosen two even vertices. Any four deleted odd vertices therefore create at least two edges in \(Q_4[D]\). Both contradict \(e(Q_4[D])\le1\). By parity symmetry \((4,2)\) is also impossible.

If \((a,b)=(3,3)\) and \(e(Q_4[D])\le1\), at least two distinct deleted even vertices have zero neighbors among the three deleted odd vertices. Yet any two distinct even vertices in \(Q_4\) have at most two *common nonneighbors* in \(O_4\): the number is two at Hamming distance two and zero at distance four. They cannot share three deleted odd nonneighbors. Thus \((3,3)\) is impossible.

If \((a,b)=(1,5)\), let \(x\) be the unique deleted even vertex. Since \(e(Q_4[D])\le1\), exactly one of its four odd neighbors lies in \(D\); the other three lie in \(F\). Every pair among these three surviving odd neighbors has, besides \(x\), one further common even neighbor. Those three additional even vertices are distinct and all survive, because \(x\) is the only deleted even vertex. They and the three surviving odd neighbors form an induced six-cycle in \(Q_4[F]\), a contradiction. The parity-reversed case \((5,1)\) is identical. Only \((0,6)\) and \((6,0)\) remain.

**3. Equality classification.** If all six deleted vertices are odd, \(F\) consists of every even vertex and two odd vertices \(u,v\). Distinct vertices of the same parity in \(Q_4\) have Hamming distance two or four. At distance two they share exactly two even neighbors, giving an induced four-cycle in \(F\). At distance four they are antipodal, their neighbor sets are disjoint, and \(F\) induces two disjoint copies of \(K_{1,4}\). The same holds with parities reversed. Each of the two parity classes contains four antipodal pairs, giving exactly eight ten-vertex forests. This simultaneously proves their existence and achieves the bound in step 1.

**4. Exchange isolation.** For a fixed fully included parity class, two different antipodal pairs are disjoint, so replacing one vertex cannot produce a different ten-vertex forest. Configurations with different fully included parity classes intersect in exactly four vertices, so they cannot differ in just one selected vertex. The exchange graph is therefore an edgeless graph on eight vertices.

**5. The three-cube comparison.** The graph \(Q_3\) has eight vertices, twelve edges, and two parity classes with four vertices each. If a putative forest has six vertices, the deleted pair has at most one edge and the remaining induced graph has at least \(12-6=6\) edges, whereas a six-vertex forest has at most five. Thus the maximum has at most five vertices. Conversely, deleting any three vertices of one parity leaves a forest: the other parity is independent, and the single retained vertex of the deleted parity supplies three star edges.

Every five-vertex forest has a three-vertex complement \(D\). The edge identity is \(e(Q_3[F])=3+e(Q_3[D])\). The successful deletion triples consist precisely of (i) the eight pure-parity triples, or (ii) triples containing two vertices of one parity and one of the other, with exactly one edge between the parities inside \(D\). Indeed, a mixed triple has one or two such edges, and the second possibility exceeds the four-edge forest bound. In the first possibility no square of \(Q_3\) can survive intact: if a four-cycle survived, the deleted triple would lie inside its complementary square, in which the odd deleted vertex would be adjacent to both deleted even vertices (or conversely), forcing two deleted edges. Since any cycle on five vertices in a bipartite graph would have to be a square, these triples do yield forests.

There are six choices of a same-parity pair and exactly two opposite-parity vertices adjacent to exactly one of those two. This gives twelve mixed triples of each majority parity, hence \(8+12+12=32\) maximum forests. Under single exchanges, the four pure even triples form a clique, and so do the four pure odd triples. Every mixed deletion triple is exchange-adjacent to a pure triple of its majority parity. Finally, the valid deleted triples
\[
\{0,3,5\}\;\longrightarrow\;\{2,3,5\}\;\longrightarrow\;\{1,2,5\}\;\longrightarrow\;\{1,2,4\}
\]
form an exchange path connecting a pure even triple to a pure odd triple, where binary words of length three are represented by their integer values. Thus the exchange graph is connected. For \(Q_2\), all four three-vertex subsets are induced paths and are pairwise exchange-adjacent. The graph \(Q_1\) is a single edge; its full two-vertex set is its unique maximum induced forest, making the optimum exchange graph a single vertex. This completes the transition claim.

## Verification

The complete standalone checker `verify.py` reconstructs \(Q_2,Q_3,Q_4\), independently tests each subset for acyclicity by both a depth-first search and a disjoint-set union edge scan, and reconstructs the optimum exchange graph without assuming the theorem. It exhausts \(2^{16}=65,536\) vertex subsets in dimension four, and checks that its eight maxima coincide **exactly** with the stated antipodal formula, that each has induced degree multiset \(1^8,4^2\), and that no exchanges are possible. At dimensions two and three it independently verifies maxima, components and all exchange edges. Run: `python3 verify.py`. The expected final output line is `ALL_VERIFY_OK`.

The finite enumeration is an exhaustive verification of the specific dimensions, not a numerical extrapolation to higher dimensions. The foregoing argument proves each assertion without relying on an unexamined search log.

## Relationship to prior work

Focardi, Luccio and Peleg study feedback vertex sets of hypercubes. Pike investigates hypercube decycling bounds and their relation to binary distance-four codes. Pike and Zou determine the **numerical** decycling number of every Cartesian product of two cycles; because \(Q_4\cong C_4\square C_4\), that published result includes the numerical invariant considered here. The value ten for the largest forest is **not** claimed as previously unknown. The additional assertions concern *all* equality sets, their two-star form, the absence of one-vertex exchanges, and the contrast with dimension three.

Gunderson, Meagher, Morris and Pantangi's Theorem 1.5 gives a general regular-graph forest bound, which also yields \(10\) as an upper bound for \(Q_4\). Their accessible full text treats structural equality questions for other specified families, without stating this eight-configuration four-cube result. The earlier directly relevant full texts by Focardi et al. and Pike–Zou were not accessible for complete statement-by-statement comparison; see the residual risk below.

## Limitations

The result is a complete finite classification for the naturally first disconnected dimension, **not** an infinite-dimensional extremal characterization. Earlier papers imply the scalar optimum and may contain unindexed or unpublished refinements; particularly the unavailable complete treatments of the four-cube and toroidal grids could conceivably state an equivalent equality classification. No independence, external audit, or universal novelty certification is asserted.

## References

1. R. Focardi, F. L. Luccio and D. Peleg, *Feedback vertex set in hypercubes*, Information Processing Letters **76** (2000), 1–5. DOI: `10.1016/S0020-0190(00)00127-7`. Dated public record: 20 November 2000.
2. D. A. Pike, *Decycling hypercubes*, Graphs and Combinatorics **19** (2003), 547–550. DOI: `10.1007/s00373-003-0529-9`.
3. D. A. Pike and Y. Zou, *Decycling Cartesian Products of Two Cycles*, SIAM Journal on Discrete Mathematics **19** (2005), 651–663. DOI: `10.1137/S089548010444016X`. Publisher records online availability from 1 August 2006.
4. K. Gunderson, K. Meagher, J. Morris and V. R. T. Pantangi, *Induced forests in some distance-regular graphs*, arXiv:`2301.05207`, initial release 12 January 2023; published in Discrete Applied Mathematics **346** (2024), 290–300.
