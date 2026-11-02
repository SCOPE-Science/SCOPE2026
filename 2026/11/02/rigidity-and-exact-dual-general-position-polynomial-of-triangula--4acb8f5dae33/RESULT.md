# Rigidity and exact dual-general-position polynomial of triangular graphs

## Finding
For each integer \(n\ge3\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph whose vertices are the two-element subsets of \([n]\), adjacent exactly when they intersect. A subset \(S\subseteq V(T_n)\) is *dual general position* when no shortest path between two vertices of \(S\), and no shortest path between two vertices outside \(S\), has an internal vertex in \(S\). In particular, all geodesics—not merely one chosen geodesic—are quantified over.

Define its entire cardinality enumerator, including the empty set, by
\[
D_n(z)=\sum_{S\subseteq V(T_n),\ S\text{ dual general position}}z^{|S|}.
\]
Then
\[
\boxed{D_n(z)=\begin{cases}
(1+z)^3,&n=3,\\
1+8z^3,&n=4,\\
1+n z^{n-1},&n\ge5.
\end{cases}}
\]
More precisely: when \(n=3\), all subsets qualify; when \(n=4\), the only nonempty qualifying sets are the eight triangles of \(T_4\) (four root-vertex stars and four root triangles); when \(n\ge5\), the only nonempty qualifying sets are the \(n\) full root-vertex stars
\[
S_a=\bigl\{\{a,b\}:b\in[n]\setminus\{a\}\bigr\},\qquad a\in[n].
\]
Consequently, \(\operatorname{gp}_{\mathrm d}(T_n)=3\) for \(n=3,4\), and \(\operatorname{gp}_{\mathrm d}(T_n)=n-1\) for \(n\ge5\). In every case \(n\ge5\), the nonempty dual-general-position sets are all maximum and there are no such sets of sizes \(1,\ldots,n-2\).

Using the previously proved ordinary general-position formula, the comparison is exact: \(\operatorname{gp}(T_n)-\operatorname{gp}_{\mathrm d}(T_n)=1\) precisely when \(n\ge6\) and \(3\mid n\); it is zero at every other \(n\ge3\). The formula for ordinary general position is credited to Ghorbani and collaborators, not claimed as new.

## Assumptions and scope
All graphs are finite, simple, undirected, and distances are graph shortest-path distances. The parameter \(n\) ranges over every integer \(n\ge3\). The empty subset satisfies the definition vacuously and is counted once. A triangular graph vertex \(\{a,b\}\) denotes the edge \(ab\) of the root complete graph. A root-vertex star consists of all such edges incident to one root vertex; a root triangle consists of the three edges on a chosen triple of root vertices. The dual definition requires *every* shortest path to avoid internal selected vertices for both within-selected and within-unselected endpoint pairs; mixed endpoint pairs are unrestricted.

## Proof
**1. A local obstruction in diameter two.** For \(n\ge4\), every two intersecting root edges are adjacent in \(T_n\), and two disjoint root edges have distance two (via any crossing root edge). Thus \(\operatorname{diam}(T_n)=2\). Fix a dual-general-position subset \(S\) and a selected vertex \(v\in S\). If two nonadjacent vertices of \(N(v)\cap S\) existed, their length-two path through \(v\) would contradict general position. If two nonadjacent vertices of \(N(v)\setminus S\) existed, their length-two path through \(v\) would contradict convexity of the unselected complement. Hence **both** \(N(v)\cap S\) and \(N(v)\setminus S\) induce cliques.

**2. The local triangular-graph neighborhood.** Fix \(v=\{a,b\}\). Its \(2(n-2)\) neighbors split into
\[
A=\{\{a,c\}:c\notin\{a,b\}\},\qquad
B=\{\{b,c\}:c\notin\{a,b\}\}.
\]
Both \(A\) and \(B\) are cliques of order \(n-2\); the only cross-edges join \(\{a,c\}\) to \(\{b,c\}\) with the same \(c\). Therefore the neighborhood is isomorphic to \(K_{n-2}\square K_2\). For \(n\ge5\), its clique number is \(n-2\), and its only cliques of that maximum size are \(A\) and \(B\): any clique using both sides contains at most two vertices.

**3. Forced full stars when \(n\ge5\).** The two clique subsets \(N(v)\cap S\) and \(N(v)\setminus S\) partition \(2(n-2)\) vertices. By Step 2, each has at most \(n-2\) members; both must have exactly \(n-2\). They must therefore be \(A\) and \(B\), in some order. In particular, since \(v\in S\), all the root edges incident to one endpoint, say \(a\), belong to \(S\). If an additional root edge \(\{c,d\}\in S\) avoided \(a\), choose \(t\notin\{a,c,d\}\). Such a \(t\) exists because \(n\ge5\). Then the three selected graph vertices
\[
\{a,t\},\quad\{a,c\},\quad\{c,d\}
\]
form a geodesic of length two in \(T_n\), because the outer two root edges are disjoint. This contradicts general position. Thus \(S=S_a\).

Conversely, \(S_a\) is a clique in \(T_n\), so it is in general position. Its complement consists of all root edges within \([n]\setminus\{a\}\). Every length-two geodesic between two of these edges uses a crossing edge whose endpoints also avoid \(a\), so the complement is convex. Therefore every \(S_a\) qualifies. Distinct root-vertex stars are distinct for \(n\ge3\), giving exactly \(n\) nonempty sets for \(n\ge5\).

**4. The four-root exception.** For \(n=4\), the neighborhood of each selected vertex is \(K_2\square K_2=C_4\), with clique number two. The two clique subsets from Step 1 partition its four vertices and therefore each have two members. Consequently every vertex in the induced selected graph \(T_4[S]\) has exactly two selected neighbors, which themselves are adjacent. Every nonempty connected component of \(T_4[S]\) is thus a triangle. There cannot be two such components because that would select all six vertices of \(T_4\) and give selected degree four instead of two. Thus \(S\) is one triangle. A triangle in \(L(K_4)\) is exactly a root-vertex star or a root triangle, giving four of each. In either case the complementary three graph vertices form the opposite triangle, so both endpoint classes are cliques and the dual condition holds. Hence exactly eight nonempty sets occur, all of cardinality three.

**5. The complete-graph boundary.** The graph \(T_3=L(K_3)\) is \(K_3\), so there are no internal vertices on shortest paths; every one of its eight subsets qualifies. The polynomial and dual-general-position-number formulas follow in every case.

**6. Comparison with ordinary general position.** Ghorbani et al. proved \(\operatorname{gp}(L(K_n))=n\) when \(3\mid n\) and \(n-1\) otherwise (their Theorem 4.4, for all \(n\ge3\)). Subtracting the established dual values gives the stated exact equality/deficit criterion. This step uses an existing theorem; the new contribution is the dual all-set classification.

## Verification
The standalone source `dual_triangular_verify.cpp` constructs the vertices and adjacency of \(T_n\) afresh and calculates all-pairs shortest-path distances by Floyd–Warshall. It enumerates all \(2^{\binom n2}\) candidate subsets for each \(3\le n\le7\). For every selected intermediate vertex, it checks all pairs for which the distance equality for a shortest path holds, rejecting subsets violating the original two endpoint-class requirements; it then checks that each survivor belongs to the claimed root-star/root-triangle family. The exact observed cardinality profiles are:

| \(n\) | subsets tested | accepted cardinalities and counts |
| --- | ---: | --- |
| 3 | 8 | \(0:1,\ 1:3,\ 2:3,\ 3:1\) |
| 4 | 64 | \(0:1,\ 3:8\) |
| 5 | 1,024 | \(0:1,\ 4:5\) |
| 6 | 32,768 | \(0:1,\ 5:6\) |
| 7 | 2,097,152 | \(0:1,\ 6:7\) |

The program exits successfully with `VERIFY_OK`. This finite exhaustive check is auxiliary: Steps 1–5 prove the infinite formula for every integer in scope.

## Relationship to prior work
Tian and Klavžar introduced dual general position and established the equivalence with general position plus convex unselected complement in their first arXiv version on 2024-02-27. Their general theorems concern arbitrary graphs and Cartesian products, rather than an all-set classification of triangular graphs. Ghorbani, Klavžar, Maimani, Momeni, Mahid, and Rus established the ordinary general-position number of \(L(K_n)\) in arXiv:1903.04286, Theorem 4.4 (first posted 2019-03-11); this result is used only for the final comparison. Di Stefano and collaborators studied *lower* ordinary general-position sets of the same line-graph family in arXiv:2306.09965, Theorem 5.2, a different invariant. Dokyeesun and collaborators studied dual general position in strong and lexicographic graph products in arXiv:2408.15951; their product results do not imply this classification for all triangular graphs.

The main new information is that **all** nonempty dual sets are maximum and, except for the four-root boundary, are precisely full root-vertex stars. This is not implied by knowing the ordinary general-position maximum or the smallest maximal ordinary general-position size, because those conditions do not impose convexity of the complement. Priority against all possible unindexed literature is not certified.

## Limitations
The theorem covers only triangular graphs \(L(K_n)\) and makes no claim for general line graphs, other Johnson graphs, or Kneser graphs. The accompanying enumeration checks only \(3\le n\le7\); larger orders are covered by proof rather than computation. The published-context comparison checks the closest available full texts and targeted searches but cannot exclude unpublished or unindexed prior equivalent formulations. No independent mathematical audit has been performed.

## References
1. J. Tian and S. Klavžar, *Variety of general position problems in graphs*, arXiv:2402.17338 (v1 posted 2024-02-27), especially Definition in Section 2, Theorem 3.1, Section 4, and concluding remarks. https://arxiv.org/abs/2402.17338 ; published version https://doi.org/10.1007/s40840-024-01788-z
2. M. Ghorbani, S. Klavžar, H. R. Maimani, M. Momeni, F. R. Mahid, and G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286 (v1 posted 2019-03-11), Theorem 4.4. https://arxiv.org/abs/1903.04286
3. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, *Lower general position sets in graphs*, arXiv:2306.09965 (v1 posted 2023-06-16), Section 5, Theorem 5.2. https://arxiv.org/abs/2306.09965
4. P. Dokyeesun, S. Klavžar, D. Kuziak, and J. Tian, *General position problems in strong and lexicographic products of graphs*, arXiv:2408.15951 (v1 posted 2024-08-28), Sections 4–5. https://arxiv.org/abs/2408.15951
