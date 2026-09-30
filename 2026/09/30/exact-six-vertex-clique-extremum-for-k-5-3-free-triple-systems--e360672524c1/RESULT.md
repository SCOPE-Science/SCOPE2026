# Exact six-vertex clique extremum for \(K_5^{(3)}\)-free triple systems
## Finding
Let \(H\) be a simple \(3\)-uniform hypergraph on a six-element vertex set \(V\). A clique is a subset \(S\subseteq V\) such that either \(|S|<3\), or every three-element subset of \(S\) is an edge of \(H\). Assume that \(H\) contains no \(K_5^{(3)}\). Then
\[
k(H)\le 49.
\]
Equality holds if and only if there is a partition \(V=A\sqcup B\) with \(|A|=|B|=3\) such that
\[
E(H)=\binom{V}{3}\setminus\{A,B\}.
\]
Equivalently, \(H\cong B_6\), the balanced complete bipartite \(3\)-graph. Hence there is one extremal isomorphism type and exactly
\[
\frac12\binom{6}{3}=10
\]
labeled extremal hypergraphs.

## Assumptions and scope
Hypergraphs are finite, simple, and \(3\)-uniform. The forbidden configuration is the complete \(3\)-graph on five vertices. The quantity \(k(H)\) counts all clique subsets, including the empty set and subsets of size one or two. The statement is only for six vertices; it does not assert the corresponding exact result at any other order.

## Proof
Let
\[
\mathcal F=\binom{V}{3}\setminus E(H)
\]
be the family of missing triples and write \(f=|\mathcal F|\). The hypergraph \(H\) is \(K_5^{(3)}\)-free exactly when every five-element subset contains a missing triple. Since the five-element subsets are \(V\setminus\{v\}\), this is equivalent to
\[
\bigcap_{F\in\mathcal F}F=\varnothing.
\]
For each missing triple \(F\), take its complementary triple \(G=V\setminus F\), and let \(\mathcal G\) be the resulting family. Then \(|\mathcal G|=f\) and the preceding condition is equivalent to
\[
\bigcup_{G\in\mathcal G}G=V.
\]
Let \(\partial_2\mathcal G\) be the two-shadow, the set of pairs contained in at least one member of \(\mathcal G\), and put \(s=|\partial_2\mathcal G|\).

A four-set \(Q\subseteq V\) fails to be a clique of \(H\) exactly when it contains a missing triple \(F\). Writing \(P=V\setminus Q\), this is equivalent to \(P\subseteq V\setminus F\) for some \(F\in\mathcal F\), namely \(P\in\partial_2\mathcal G\). Therefore the number of four-vertex cliques is \(15-s\). Because there are no cliques on five or six vertices,
\[
\begin{aligned}
k(H)
&=1+6+\binom{6}{2}+|E(H)|+(15-s)\\
&=22+(20-f)+(15-s)\\
&=57-(f+s).
\end{aligned}
\]
It remains to prove \(f+s\ge 8\), with equality only for two disjoint triples in \(\mathcal G\).

If \(f=2\), the condition \(\bigcup\mathcal G=V\) forces the two triples to be disjoint. Their two-shadows are then disjoint triangles, so \(s=6\) and \(f+s=8\).

Suppose \(f=3\). Any two distinct triples have two-shadows whose union has at least five pairs. Equality at five occurs only when the two triples share two vertices; their shadow union is then two triangles sharing one edge. The only triangles contained entirely in that five-edge graph are the two original triangles, so a third distinct triple necessarily contributes a new pair. Hence \(s\ge6\), and \(f+s\ge9\).

If \(f=4\), two distinct triples already contribute at least five shadow pairs, so \(f+s\ge9\). If \(f=5\), the same observation gives \(f+s\ge10\). Finally, if \(f\ge6\), one triple alone contributes three pairs, so \(f+s\ge9\). Thus \(f+s\ge8\) always, with equality exactly in the case \(f=2\) of two disjoint complementary triples. Substituting into \(k(H)=57-(f+s)\) gives \(k(H)\le49\) and the stated equality classification.

## Verification
Two standalone exhaustive verifiers accompany this result. `artifacts/verify_direct.py` enumerates all \(2^{20}\) labeled six-vertex triple systems directly, tests the six possible \(K_5^{(3)}\) vertex sets, counts four-cliques, and canonicalizes extremizers under all \(6!\) vertex permutations. It returns maximum clique count \(49\), ten labeled extremizers, and one isomorphism class. `artifacts/verify_shadow.py` independently enumerates complementary triple families, uses the covering condition \(\bigcup\mathcal G=V\), and minimizes \(|\mathcal G|+|\partial_2\mathcal G|\). It returns minimum \(8\) with exactly ten labeled witnesses, all partitions into two disjoint triples.

## Relationship to prior work
Chen, Deng, Hou, Liu, and Zhang study the same clique-counting objective for \(K_5^{(3)}\)-free triple systems and prove that the balanced complete bipartite construction is uniquely extremal for all sufficiently large orders. Their source states the result only for sufficiently large \(n\), with no six-vertex exact statement in the theorem. The argument above gives the exact order-six value and equality classification by a short complement-and-shadow reduction. Their paper also identifies the problem as the \((r,\ell)=(3,4)\) instance of the clique-counting conjecture of Frankl, Gryaznov, and Talebanfard.

## Limitations
The proof uses special features of six vertices: complements of missing triples are again triples, and complements of four-sets are pairs. It does not extend verbatim to seven or more vertices. No claim is made here about the smallest order from which the general balanced-bipartite extremal theorem holds. The literature comparison is best-of-knowledge based on the cited current source, web searches for the exact six-vertex statement, and published-finding corpus searches; absence from those searches is not an absolute publication guarantee.

## References
1. W. Chen, J. Deng, J. Hou, X. Liu, and Y. Zhang, *Vertex-colored Turán theorems with applications in extremal hypergraph problems*, arXiv:2606.02210v1 (first public version 2026-06-01). The source lists MSC2020 classes 05C35, 05C65, 05D05.
2. P. Frankl, S. Gryaznov, and N. Talebanfard, *A Variant of the VC-Dimension with Applications to Depth-3 Circuits*, ITCS 2022, DOI 10.4230/LIPIcs.ITCS.2022.72. This is background for the general clique-counting conjecture; it is not used as the dated primary source of the present finding.
