# Twelve rank-three theories of finite rectangular grid graphs, with a sharp ten-vertex kernel

## Finding

Let \(P_t\) be the undirected simple path on \(t\geq 1\) vertices, including the one-vertex graph \(P_1\), and let \(G_{m,n}=P_m\square P_n\) denote the graph Cartesian product. Work in first-order logic with equality and a single undirected adjacency relation; no coordinate directions, boundary constants, vertex colours, or orders are named.

Write \(a=\min(m,n)\) and \(b=\max(m,n)\). Define the following twelve-valued key:

\[
\kappa(m,n)=\begin{cases}
\mathrm{path}_{\min(b,7)}, &a=1,\\
\mathrm{small}_{a,b}, &(a,b)\in\{(2,2),(2,3),(2,4),(3,3)\},\\
\mathrm{bulk}, &\text{otherwise}.
\end{cases}
\]

**Theorem.** For all positive integers \(m,n,r,s\),

\[
G_{m,n}\equiv_3 G_{r,s}\quad\Longleftrightarrow\quad \kappa(m,n)=\kappa(r,s).
\]

Thus the family has exactly **twelve** rank-three first-order theories. The least-order representatives, one per theory, are \(G_{1,1}\), \(G_{1,2}\), \(G_{1,3}\), \(G_{1,4}\), \(G_{2,2}\), \(G_{1,5}\), \(G_{1,6}\), \(G_{2,3}\), \(G_{1,7}\), \(G_{2,4}\), \(G_{3,3}\), and \(G_{2,5}\). Their orders are respectively \(1,2,3,4,4,5,6,6,7,8,9,10\). Every grid is rank-three-equivalent to a grid of at most **ten** vertices, and ten is sharp. In particular, the five-rung ladder \(G_{2,5}\) and the twelve-vertex rectangular grid \(G_{3,4}\) satisfy exactly the same rank-three sentences despite having different shapes and orders.

## Assumptions and scope

All parameters are positive integers. Adjacency in \(G_{m,n}\) holds for two vertices \((i,j)\) and \((k,l)\) precisely when their Manhattan distance equals one. The symbol \(\equiv_3\) denotes agreement on every first-order sentence of quantifier rank at most three, with arbitrary Boolean connectives and alternations. The result does not concern counting quantifiers, orders, coordinate predicates, higher quantifier ranks, toroidal grids, or products with more than two factors.

## Proof

**1. Exact finite-type recursion.** For any finite simple graph \(H=(V,E)\), let \(A(x,y,z)\) be the complete atomic diagram of the ordered triple, recording all equality and adjacency facts. The rank-one type of the ordered pair \((x,y)\) is exactly its atomic diagram together with the set

\[
\tau_1(x,y)=\bigl(\mathrm{atomic}(x,y),\ \{A(x,y,z):z\in V\}\bigr).
\]

The rank-two type of a distinguished vertex, and the rank-three sentence type of the graph, are then determined respectively by

\[
\tau_2(x)=\{\tau_1(x,y):y\in V\},\qquad
\tau_3(H)=\{\tau_2(x):x\in V\}.
\]

These are exact, not approximate, invariants: the atomic base and existential extension sets are the standard back-and-forth induction, while negation and Boolean combinations require no additional information. Hence \(H\equiv_3 H'\) if and only if \(\tau_3(H)=\tau_3(H')\). The implementation in `verify.py` encodes the complete triple diagrams in nine explicit bit positions and performs the above recurrence without relying on graph-isomorphism heuristics.

**2. Uniform path cutoff.** For all \(t\geq7\), \(P_t\equiv_3 P_7\). Here is a direct proof using the preceding types. In \(P_t\), with \(t\geq7\), every pair of vertices has a third vertex nonadjacent to both because the union of their closed neighborhoods has at most six vertices. For distinct \(x,y\), all remaining categories of triples \((x,y,z)\) depend only on whether \(x,y\) have distance one, two, or at least three; for distances one and two, the categories additionally depend on whether each selected vertex is an endpoint. For distance at least three, the categories do not depend on endpoint status. Indeed, distinct vertices have a common neighbor exactly at distance two; at distance one or two, an exclusive neighbor of \(x\) exists exactly when \(x\) has degree two; at distance at least three, an exclusive neighbor of either selected vertex always exists. Repeated-vertex triple diagrams are automatic, and the pair \((x,x)\) has the same rank-one type for every \(x\). It follows that \(\tau_2(x)\) depends only on the distance from \(x\) to the nearer endpoint, truncated at three. All four possible truncated distances \(0,1,2,3\) occur in every path with at least seven vertices, with the same rank-two types. Their rank-three sentence types therefore coincide.

**3. Cartesian-product preservation.** Suppose \(A\equiv_3 A'\) and \(B\equiv_3 B'\). Then \(A\square B\equiv_3 A'\square B'\). In the three-round Ehrenfeucht–Fraïssé game on the products, Duplicator plays the two factor games in parallel. The pairwise equality of selected coordinates and the pairwise adjacency of each coordinate are preserved. Since

\[
(a,b)\sim(a',b')\iff
\bigl(a=a'\ \land\ b\sim b'\bigr)
\ \lor\ \bigl(a\sim a'\ \land\ b=b'\bigr),
\]

the induced product graph on all chosen pairs is preserved. The same proof works with either product chosen by Spoiler at each round. It follows from Step 2 that each \(G_{m,n}\) is rank-three-equivalent to \(G_{\min(m,7),\min(n,7)}\).

**4. Exhaustive canonical classification.** After exchanging coordinates, there are precisely \(28\) canonical grids \(G_{m,n}\) with \(1\leq m\leq n\leq7\). Applying Step 1 to all twenty-eight gives exactly the twelve equivalence classes recorded in `canonical_table.json`. The first eleven classes are singleton sets of canonical dimension pairs \((1,1),(1,2),(1,3),(1,4),(2,2),(1,5),(1,6),(2,3),(1,7),(2,4),(3,3)\); the twelfth comprises the remaining seventeen canonical dimension pairs, beginning with \((2,5)\) and \((3,4)\). The program verifies all twenty-eight profiles, and an independently written alternating-game minimax recursion confirms inequivalence of all \(\binom{12}{2}=66\) distinct least-order representatives. Equality of the complete \(\tau_3\) invariants proves equivalence within each class. Steps 2 and 3 extend this exhaustive canonical computation to all positive dimensions.

**5. Sharpness.** The largest least-order representative is \(G_{2,5}\), of order ten. Its class contains no smaller canonical grid and, by Steps 2–4, no grid with either dimension exceeding seven can yield a smaller representative in that class. Thus ten is the smallest universal representative-size bound.

## Verification

Run `python3 verify.py` from this directory using Python 3.9 or later. The script uses only the standard library. It reads `canonical_table.json`, recomputes all canonical types and class memberships from their adjacency matrices, checks all 66 interclass representative comparisons using an independent direct three-round game, checks selected intraclass game comparisons, tests several dimension pairs beyond the cutoff as supplementary checks, and recomputes the global census of 18 pointed rank-two vertex types. The file `verification_output.txt` records a successful replay. The program's finite enumeration is exhaustive on the twenty-eight canonical grids; the mathematical path cutoff and product argument are necessary to conclude the infinite-family theorem.

## Relationship to prior work

Brown and Hoshino (2007) classify Ehrenfeucht–Fraïssé games on individual paths and cycles, including the exceptional seven-vertex cutoff for three rounds on paths. Their statement concerns pairs of paths or pairs of cycles, not Cartesian products, and does not specify the twelve grid classes or the cross-shape identification of \(G_{2,5}\) with \(G_{3,4}\). The Cartesian-product preservation lemma is a standard composition fact, noted for example as an exercise in *Logical Methods in Combinatorics* (2009/10, Lecture 5, p. 3); it only supplies the finite reduction and not the exact classification. Kopczyński (2019/2020), in a separate investigation of grid axiomatization and finite spectra, works with four directed neighbor relations and additional unary predicates, rather than the pure single-adjacency signature at rank three. These sources motivate the precise distinction between a factorwise bound and the finer grid classification.

## Limitations

The logical signature and quantifier-rank bound are essential. More expressive signatures can distinguish coordinate directions, and stronger logical ranks can separate structures merged here. The code independently checks the finite logical-type census but does not prove the infinite cutoff; the latter is established in Steps 2–3. The literature comparison is limited to the specifically examined sources and indexed searches; unindexed or inaccessible results could contain an equivalent classification. No independent scientific audit has been performed.

## References

1. Jason Brown and Richard Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212; publicly dated 30 April 2007. Full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. *Logical Methods in Combinatorics*, Lecture 5, 2009/10, p. 3 (Cartesian-product preservation posed as an exercise). https://janos.cs.technion.ac.il/COURSES/236605-09/lec05.pdf
3. Eryk Kopczyński, *Axiomatizing rectangular grids with no extra non-unary relations*, arXiv:1912.09797, first posted 20 December 2019; Fundamenta Informaticae **176** (2020), 129–138. https://arxiv.org/abs/1912.09797
