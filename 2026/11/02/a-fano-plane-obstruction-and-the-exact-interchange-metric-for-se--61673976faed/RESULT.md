# A Fano-plane obstruction and the exact interchange metric for seven-player regular tournaments

## Finding

Let \(V=\{0,1,\ldots,6\}\). A tournament is an orientation of every pair of distinct elements of \(V\), and it is *regular* if every vertex has outdegree three. Form the simple interchange graph \(\mathcal I_7\) whose vertices are all **labelled** regular tournaments on \(V\). A single interchange reverses all three arcs of a cyclically directed triangle. The following finite classification holds:

1. \(\mathcal I_7\) has exactly \(2640\) vertices and \(18480\) edges; it is connected, bipartite and \(14\)-regular, with radius \(8\) and diameter \(9\).
2. The relabelling action of \(S_7\) has three vertex orbits, of sizes \(240\), \(1680\) and \(720\), respectively. The complete number of configurations at each interchange distance from a representative is as follows (entries list distances \(0,1,\ldots\)):

   | Size of relabelling orbit | Distance-sphere sizes | Eccentricity |
   | ---: | --- | ---: |
   | \(240\) | \((1,14,91,343,749,871,476,92,3)\) | \(8\) |
   | \(1680\) | \((1,14,91,340,739,853,483,113,6)\) | \(8\) |
   | \(720\) | \((1,14,91,336,721,822,485,147,22,1)\) | \(9\) |

3. Write \(\overline T\) for the **converse** of a tournament \(T\), obtained by reversing every arc. The distances \(d_{\mathcal I_7}(T,\overline T)\) in the three orbits are respectively \(7,7,9\). Every tournament in the \(720\)-element orbit has exactly one vertex at distance \(9\), its converse. Thus the graph has precisely \(360\) unordered pairs at diameter distance, all converse pairs.
4. A *cyclic Fano decomposition* of \(T\) is a partition of the \(21\) pairs of \(V\) into seven triples, each a directed triangle of \(T\). The three relabelling orbits have respectively exactly \(2,2,0\) such decompositions. Moreover, for any regular seven-player tournament, converse distance \(7\) is equivalent to the existence of a cyclic Fano decomposition. This supplies a combinatorial obstruction to a shortest route in the exceptional \(720\)-element orbit.

In particular, the order-seven case has interchange diameter \((7-1)^2/4=9\), as anticipated by the classical Brualdi–Li diameter prediction reported in McShine (2000); the finer distance and Fano-decomposition classifications are not consequences of that prediction.

## Assumptions and scope

There are precisely seven fixed, distinct, labelled vertices. The tournament is a simple complete orientation without ties, and outdegree is exactly three **at every vertex**. An interchange is allowed only on a directed \(3\)-cycle; reversing that triangle preserves the score vector. No quotient by graph isomorphism is taken when defining the \(2640\) states. Distances refer to a minimum number of interchanges, not to simultaneous reversals or to relabellings. The relabelling-orbit sizes classify states but do not redefine adjacency.

A Fano decomposition is a labelled Steiner triple system \(2\text{-}(7,3,1)\) whose seven blocks are cyclic in the particular tournament. There are thirty Steiner triple systems on the fixed seven-element vertex set; these systems are distinguished by their labelled block collections.

## Proof

**Step 1: exhaustive, nonredundant state representation.** Order the \(21\) unordered pairs \((u,v)\) lexicographically with \(u<v\). Write a binary word \(w\) of length \(21\), whose bit for \((u,v)\) is \(1\) when \(u\to v\), and \(0\) when \(v\to u\). Every tournament has exactly one such word. Enumerate these words successively, keeping each vertex's current win count \(p_u\) and unassigned-pair count \(r_u\). A partial word is extendible only if \(p_u\le3\le p_u+r_u\) for every vertex. Branch into both possible orientations whenever that condition remains true, and accept a word only when every win count is exactly three. This is a complete binary decision tree with a sound pruning rule: no discarded prefix can have a regular extension, and every regular tournament survives its unique branch. The first verifier implements these precise steps and returns \(2640\) distinct words.

**Step 2: exact legal edges.** For \(a<b<c\), let the triple's bits be ordered \((ab,ac,bc)\). It is a directed cycle precisely for \((1,0,1)\) or \((0,1,0)\), so an interchange toggles exactly those three bits. The three orientation changes cancel at each involved vertex, and hence preserve regularity. Conversely, every single permitted interchange arises uniquely this way. A noncyclic triple has a unique vertex beating its two companions, so the number of noncyclic triples in any regular tournament is \(\sum_{u\in V}\binom{3}{2}=21\). Out of \(\binom{7}{3}=35\) triples, exactly \(14\) are directed cycles. Therefore \(\mathcal I_7\) is \(14\)-regular and has \(2640\cdot14/2=18480\) edges. Every interchange flips three bits, changing their sum modulo two, so the graph is bipartite.

**Step 3: all metric spheres.** Construct the fourteen neighbors of every enumerated state using the preceding bit rule, and perform breadth-first search from each of the \(2640\) sources. Each BFS assigns the minimum interchange distance to every reachable state, by induction on BFS layers. The exhaustive result is that each source reaches all \(2640\) vertices, and the only three distance profiles are the rows displayed above, attained \(240,1680,720\) times. Hence the radius is \(8\), the diameter is \(9\), and the stated eccentricity distribution follows. The class profiles are independently reconstructed by permuting the seven labels in the three canonical regular-tournament representatives of McKay's catalogue; their orbit sizes are \(240,1680,720\), and a BFS from one representative of each suffices because relabelling is a graph automorphism.

**Step 4: why the Fano geometry controls minimum converse paths.** Each of the \(21\) arcs differs between \(T\) and \(\overline T\). Since a single triangle interchange changes exactly three arcs, at least seven moves are required. If seven moves suffice, they comprise exactly \(21\) arc-reversals, so each arc must be reversed once and no arc can be repeated. Their seven triangles therefore partition the \(21\) unordered pairs, giving a Fano triple system, all of whose blocks were directed cycles in the initial tournament. Conversely, any seven edge-disjoint cyclic triangles can be reversed in any order, since they share no arcs, producing \(\overline T\) after exactly seven moves. Thus \(d(T,\overline T)=7\) if and only if \(T\) has a cyclic Fano decomposition.

To check the number of such decompositions, enumerate the \(35\) three-subsets and represent each by its three unordered-pair incidences. A recursive exact cover chooses the first still-uncovered pair and one of its containing triples; deleting those three pair incidences continues until all \(21\) pairs are covered. This enumerates all \(30\) labelled Fano systems once each. For every tournament, retain only those systems whose seven blocks are cyclic. The counts are exactly \(2\) for each of the \(240+1680\) states in the first two isomorphism orbits and \(0\) for the \(720\) states in the third orbit. In the third orbit, the converse cannot be reached in seven moves. The number of moves to reverse all arcs is odd, because each move changes the parity of the \(21\)-bit word; therefore eight moves cannot work either. The BFS supplies a nine-move route, proving converse distance nine for that orbit.

**Step 5: unique antipodes.** The exact BFS profiles show that only the \(720\)-element orbit contains vertices with eccentricity nine, and each of its sources has just one vertex at distance nine. Step 4 puts its converse at that distance, proving uniqueness. The \(720\) ordered diameter pairs correspond to \(360\) unordered pairs.

These steps prove every assertion without assuming the truth of the catalogue's completeness statement: the independent decision-tree enumeration establishes all \(2640\) labelled states, while the catalogue-derived permutation construction provides a second description of the same set.

## Verification

Both standalone Python 3 programs use only the standard library and are included with this document. Run:

```text
python3 verify_tournament_interchange_dynamic.py
python3 verify_tournament_interchange_orbits.py
```

The dynamic program enumerates regular orientations by score-pruned binary recursion, builds the complete legal-exchange graph and every all-source distance profile, enumerates thirty Fano exact covers, and tests converse distances and the complete diameter-pair census. The other program starts from the three independent public catalogue rows, generates their \(S_7\)-orbits, constructs directed arcs as seven per-vertex outgoing-neighbor masks, and calculates orbit-representative metrics and Fano covers. The two methods use different state encodings and enumeration strategies. All assertions pass when run directly from the enclosed paths. The finite nature of the problem is essential; no extension to larger tournament orders is claimed.

## Relationship to prior work

Brualdi and Li (1984) introduced this *same* triangle-reversal interchange graph for tournaments with a fixed score vector; connectivity and degree regularity are prior results, not new here. Kannan, Tetali and Vempala (1999) studied rapidly mixing walks on such fixed-score state spaces. McShine's complete 2000 paper proves general connectivity and rapid sampling, and in Remark 2 reports Brualdi and Li's proposed exact regular-tournament diameter \((n-1)^2/4\). It does not give the order-seven distance-sphere profiles, orbitwise converse distances, or cyclic-Fano obstruction. The precise degree and connectedness statements also appear in Kolesnik, Mitchell and Przybyłowski's later general discussion of the type-A interchange graph, but that article develops Coxeter-type extensions rather than these particular seven-vertex metrics. McKay's published combinatorial-data page lists the three regular seven-vertex isomorphism types, which serve as independent input for one verification program; the listing is not a distance table. Chen, Chang and Wang (2009) classify hypercube interchange graphs for *minimum* score vectors, not the central regular score vector used here.

In particular, this result confirms the numerical \(n=7\) case of the previously proposed diameter while also determining exactly which orientations have a geodesic converse path of length seven. The two-decomposition versus zero-decomposition distinction is an additional geometric classification, not implied by known global connectivity or uniform degree.

## Limitations

The theorem is a finite, exhaustive seven-vertex result. It neither proves the diameter prediction for arbitrary odd orders nor establishes a general criterion for all tournament score vectors. The exact shortest-path distributions rely on complete graph search, whereas the degree formula, bipartiteness, converse lower bound, and Fano equivalence have short conceptual proofs. The Brualdi–Li (1984) book chapter could not be inspected in full: it is directly relevant prior work and might contain an unlocated equivalent order-seven computation. This priority risk remains, and independent scholarly audit has not taken place. No claim of absolute historical priority is made.

## References

1. R. A. Brualdi and Q. Li, *The interchange graph of tournaments with the same score vector*, in *Progress in Graph Theory*, Academic Press, 1984, pp. 129–151. No fully accessible manuscript located in the literature check.
2. R. Kannan, P. Tetali and S. Vempala, *Simple Markov-chain algorithms for generating bipartite graphs and tournaments*, *Random Structures & Algorithms* **14** (1999), 293–308, doi:10.1002/(SICI)1098-2418(199907)14:4<293::AID-RSA1>3.0.CO;2-G. Publisher records first public publication on June 11, 1999.
3. L. McShine, *Random Sampling of Labeled Tournaments*, *Electronic Journal of Combinatorics* **7** (2000), #R8, doi:10.37236/1486. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r8/pdf.
4. B. Kolesnik, R. Mitchell and T. Przybyłowski, *Coxeter Interchange Graphs*, *Annals of Combinatorics* (2025), doi:10.1007/s00026-025-00768-9. Full HTML text: https://link.springer.com/article/10.1007/s00026-025-00768-9.
5. B. D. McKay, *Combinatorial Data: Regular and Semi-regular Tournaments*, https://users.cecs.anu.edu.au/~bdm/data/digraphs.html. Canonical seven-vertex strings: https://users.cecs.anu.edu.au/~bdm/data/rt7.txt.
6. A.-H. Chen, J.-M. Chang and Y.-L. Wang, *The Interchange Graphs of Tournaments with Minimum Score Vectors Are Exactly Hypercubes*, *Graphs and Combinatorics* **25** (2009), 27–34, doi:10.1007/s00373-008-0818-4.
