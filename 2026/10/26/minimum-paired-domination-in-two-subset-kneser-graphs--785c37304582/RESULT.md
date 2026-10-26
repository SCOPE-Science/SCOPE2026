# Minimum paired domination in two-subset Kneser graphs

## Finding
Let \(G_n=\operatorname{KG}(n,2)\) for each integer \(n\geq4\). Its vertices are the unordered pairs from \([n]\), adjacent exactly when disjoint. A paired-dominating set is a dominating vertex set whose induced graph admits a perfect matching. Then
\[
\gamma_{\mathrm{pr}}(G_n)=
\begin{cases}
6,&n=4,5,\\
4,&n\geq6.
\end{cases}
\]
For \(n\geq6\), **every** minimum paired-dominating set, when regarded as a family of four edges of the complete graph on \([n]\), is isomorphic to exactly one of
\[
P_4\sqcup K_2,\qquad P_3\sqcup 2K_2,\qquad 4K_2,
\]
with any remaining symbols isolated. Conversely, each such four-edge family is a minimum paired-dominating set. Their respective labeled multiplicities are
\[
180\binom n6,\qquad315\binom n7,\qquad105\binom n8.
\]
Consequently the full number of minimum paired-dominating sets for \(n\geq6\) is
\[
180\binom n6+315\binom n7+105\binom n8.
\]
In the Petersen boundary case \(n=5\), exactly \(125\) six-element sets are minimum, in three automorphism orbits of sizes \(5,60,60\). Their complements (four vertices of \(G_5\)) induce respectively \(4K_1\), \(P_3\sqcup K_1\), and \(P_4\). At \(n=4\), the only minimum set is the whole six-vertex graph.

## Assumptions and scope
All graphs are finite, simple, undirected, unweighted and labeled on the ground set \([n]\). A set \(S\subseteq V(G)\) dominates when every vertex outside \(S\) has a neighbor in \(S\); \(S\) is paired-dominating when in addition \(G[S]\) has a perfect matching. Isomorphism types refer to the graph \(H_S=([n],S)\), in which the chosen two-subsets serve as edges, **not** to the induced graph \(G_n[S]\). Thus \(P_4\) has three edges and \(P_3\) has two. The class \(n\geq6\) is classified uniformly, not only checked for small \(n\).

## Proof
**Reduction to a two-vertex cover.** Given four selected edges \(S\) of the complete graph, let \(H=H_S\). An unselected vertex \(\{a,b\}\) of \(G_n\) has no neighbor in \(S\) precisely when \(\{a,b\}\) meets every edge of \(H\), i.e. it is a two-vertex cover of \(H\). If a two-vertex cover \(\{a,b\}\) is itself selected, it intersects every selected edge, so the corresponding vertex is isolated in \(G_n[S]\). This contradicts the existence of a perfect matching. Hence a four-set with a perfect matching is dominating **if and only if** \(H\) has vertex-cover number at least three.

**Four-edge structural classification.** A connected simple graph having four edges has a vertex cover of size at most two: it is one of the three five-vertex tree types or one of the two four-vertex unicyclic types, and the assertion is immediate in each case. Decompose an arbitrary four-edge graph without isolated vertices by component edge counts. A component with three edges is \(P_4\), \(K_{1,3}\), or \(K_3\); a two-edge component is \(P_3\). The only possibilities having vertex-cover number at least three are
\[
P_4\sqcup K_2,\quad K_3\sqcup K_2,\quad
P_3\sqcup 2K_2,\quad 4K_2.
\]
For \(K_3\sqcup K_2\), the three triangle edges mutually intersect; they are adjacent in \(G_n[S]\) only to the separate \(K_2\) edge. Thus \(G_n[S]\cong K_{1,3}\) has no perfect matching. The other three types each have an explicit perfect matching in their disjointness graph: in \(P_4\sqcup K_2\), pair the two terminal path edges and pair the middle path edge with the separate edge; for \(P_3\sqcup2K_2\), pair the two adjacent path edges individually with the two separate edges; for \(4K_2\), pair any four selected edges two by two. By the reduction, precisely these three types are four-element paired-dominating sets. No two-element paired-dominating set exists: the selected pair must be disjoint, and an edge joining one endpoint of each is unselected and meets both. A \(P_4\sqcup K_2\) configuration exists for every \(n\geq6\), giving minimum four.

**Enumeration and orbits.** The three edge families have support orders \(6,7,8\) and automorphism-group sizes \(4,16,384\), respectively. Thus their labeled embedding counts are \(\binom n6(6!/4)\), \(\binom n7(7!/16)\), and \(\binom n8(8!/384)\). This yields the formulas. For each type the symmetric group on \([n]\) acts transitively on labeled copies; hence there are precisely three natural symmetry orbits when \(n\geq8\), two when \(n=7\), and one when \(n=6\).

**Small boundaries.** The three types require at least six ground symbols, so no four-set qualifies for \(n=4,5\). The graph \(G_4\cong3K_2\) requires both endpoints of every component, giving its unique six-set. In \(G_5\), selecting the six two-subsets of a fixed four-symbol subset supplies a paired-dominating six-set (their induced graph is \(3K_2\)). For exact enumeration, let \(T\) be the complementary four-set in the Petersen graph \(G_5\). Because that graph has girth five and automorphism group \(S_5\), its induced four-vertex configurations have the following complete table. Here “paired” asks whether \(G_5[V\setminus T]\) has a perfect matching.

| Induced \(G_5[T]\) | Number of \(T\) | Complement dominating? | Complement paired? |
|---|---:|:---:|:---:|
| \(4K_1\) | 5 | yes | yes |
| \(K_2\sqcup2K_1\) | 60 | yes | no |
| \(P_3\sqcup K_1\) | 60 | yes | yes |
| \(2K_2\) | 15 | yes | no |
| \(P_4\) | 60 | yes | yes |
| \(K_{1,3}\) | 10 | no | yes |

The counts follow from elementary Petersen graph incidence: there are five independent four-sets (the stars of the five symbols), ten degree-three stars, \(10\cdot3\cdot2\cdot2/2=60\) induced four-vertex paths, and \(10\binom32\cdot2=60\) induced \(P_3\sqcup K_1\) configurations. Each of the fifteen Petersen edges has two partners in an induced \(2K_2\), yielding fifteen such sets; subtraction from \(\binom{10}{4}=210\) gives the remaining sixty \(K_2\sqcup2K_1\). A four-set violates domination exactly when it contains the entire neighborhood of one of its vertices, the \(K_{1,3}\) case. The six entries in the last column follow by checking a representative for each of the six \(S_5\)-orbits (the standalone verifier tests every labeled configuration independently). Therefore \(5+60+60=125\) minimum six-sets, with the asserted orbit sizes.

## Verification
Run `python3 verify.py` with standard Python 3. The verifier constructs every vertex and edge of \(G_n\) from disjoint two-subsets; exhaustively tests all even subset sizes for \(n=4,5\), all four-subsets for \(4\leq n\leq10\), and compares direct domination and induced perfect-matching tests against an independent two-vertex-cover criterion. It checks the three structural types and their exact multiplicities, and checks the three Petersen optimum orbits under all \(120\) permutations of its five ground symbols. The run reports `VERIFY_OK`; this exhaustive check supports, but does not replace, the all-\(n\) structural proof above.

## Relationship to prior work
Paired domination was introduced by Haynes and Slater in 1998, imposing a perfect matching on an ordinary dominating set. Ivančo and Zelinka (1993) and Östergård, Shao, and Xu (2015) studied ordinary domination in Kneser graphs. Cornet and Torres (arXiv:2308.15603, first posted 2023; Section 4, Lemma 18) give an incidence-degree characterization of \(k\)-tuple domination in \(\operatorname{KG}(n,2)\), and explicitly cite the known ordinary domination number three. Their results concern domination multiplicity rather than the perfect-matching constraint on the chosen set. In particular, an ordinary three-vertex dominating family is never a paired-dominating set (its size is odd), and the previously known ordinary minimum of three does not determine the classification or the count of four-vertex paired minima. The present theorem refines the domination question by a genuine matching constraint and determines all equality cases for every \(n\).

## Limitations
The result is restricted to the second Kneser parameter equal to two; it gives no analogous classification for larger subset size. It does not classify nonminimum paired-dominating sets. The five-symbol orbit count is a fully finite enumeration plus elementary type counting, while the infinite-family theorem is proved by the four-edge structural argument. No priority or independent expert verification is asserted; some earlier unindexed calculation or inaccessible full text could contain the same classification.

## References
- T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206. DOI: `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F`. Public online date: 1998-12-07 (publisher record).
- J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica 118 (1993), 147–152. DOI: `10.21136/MB.1993.126050`.
- P. R. J. Östergård, Z. Shao, and X. Xu, *Bounds on the domination number of Kneser graphs*, Ars Mathematica Contemporanea 9 (2015), 187–195. DOI: `10.26493/1855-3974.491.b02`.
- M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603 (2023; revised 2024), especially Sections 1, 3–5 and Appendix B.
