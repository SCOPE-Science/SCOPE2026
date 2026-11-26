# Degree-sharp total outer-independent coalitions in high-girth graphs

## Finding

**Theorem.** Let \(G\) be a finite simple graph of minimum degree at least two and girth at least five. Then
\[
C_t^{\mathrm{oi}}(G)=\Delta(G)+1.
\]
More generally, let \(\Delta(G)\ge1\). Suppose some maximum-degree vertex \(v\) has independent open neighborhood \(N(v)\), and each vertex outside \(N[v]=N(v)\cup\{v\}\) has a neighbor outside \(N(v)\). Then the same equality holds, with maximum partition
\[
\{V(G)\setminus N(v)\}\ \cup\ \{\{w\}:w\in N(v)\}.
\]
The girth threshold in the first assertion cannot be lowered to four: deleting two independent edges from \(K_{3,3}\) gives minimum degree two, girth four, maximum degree three, and coalition number three.

## Assumptions and scope

Graphs are undirected and need not be connected; forests have infinite girth. A *total outer-independent dominating set* (TOIDS) is a set \(D\) such that every vertex, including each vertex in \(D\), has a neighbor in \(D\), and \(V(G)\setminus D\) is independent. A pair of disjoint nonempty sets is a coalition if neither is a TOIDS but their union is. A coalition partition is a partition into nonempty blocks such that each block has a coalition partner among the other blocks; \(C_t^{\mathrm{oi}}\) is the maximum number of blocks. The local theorem requires positive maximum degree: without this restriction the single-vertex graph would satisfy both neighborhood predicates vacuously but have no coalition partition.

## Proof

**Upper bound.** Two disjoint sets cannot both be TOIDS, since the second would be contained in the independent complement of the first and thus fail to dominate its own vertices. In the graph on the blocks of a coalition partition, put an edge between each coalition pair. Its edges intersect pairwise and it has no isolated vertices. Such a graph is a star or a triangle: if two edges meet at a block \(X\), an edge not containing \(X\) must join their other endpoints, and in that case no edge can leave the resulting triangle. The one-edge case is also a star. Hence there is a block \(X\) with all \(k-1\) other blocks as partners, where \(k\) is the number of blocks.

If \(X\) fails total domination, a witness \(u\) having no neighbor in \(X\) needs a neighbor in each partner, so \(k-1\le\deg(u)\le\Delta(G)\). Otherwise, \(V(G)\setminus X\) contains an edge, and every partner must contain one of its endpoints, giving at most two partners. This proves the upper bound for \(\Delta(G)\ge2\). If \(\Delta(G)=1\) and there is a coalition partition, there can be no isolated vertices, so \(G\) is a nonempty matching. Each of its endpoints forces its unique neighbor into any totally dominating set. The only TOIDS is therefore \(V(G)\), and a coalition partition must have exactly two blocks, again giving the upper bound.

**Construction.** Under the local hypotheses put \(X=V(G)\setminus N(v)\). Every vertex other than \(v\) has a neighbor in \(X\): neighbors of \(v\) see \(v\), and vertices outside \(N[v]\) are covered by assumption. The block \(X\) fails total domination at \(v\), and no singleton is a TOIDS. For each \(w\in N(v)\), \(X\cup\{w\}\) supplies a neighbor to \(v\) and leaves independent complement \(N(v)\setminus\{w\}\). There is at least one partner since \(\deg(v)=\Delta(G)\ge1\). The displayed partition is a coalition partition and meets the upper bound.

**High girth.** Triangles are excluded, so \(N(v)\) is independent. A vertex outside \(N[v]\) cannot have two neighbors in \(N(v)\), since those neighbors and the two vertices would form a four-cycle. Minimum degree two then supplies a neighbor outside \(N(v)\). This applies to a maximum-degree vertex.

**Boundary at girth four.** Use bipartition \(A=\{0,1,2\}\), \(B=\{3,4,5\}\) and delete edges \(\{1,4\}\) and \(\{2,5\}\) from the complete bipartite graph. The degrees are \(3,2,2,3,2,2\) and there is a four-cycle \(0,4,2,3,0\). The partition \(A,\{3\},\{4,5\}\) is valid: all its blocks are independent and \(A\) with either other block forms a TOIDS. If a partition had four blocks, a hub \(X\) would have three partners, so it must fail total domination at a vertex \(u\) of degree three. Its three neighbors must be outside \(X\), one in each partner. Thus \(u\) is \(0\) or \(3\), and all of the opposite shore is outside \(X\). Either degree-two vertex on the shore of \(u\) has no neighbor in \(X\) and has neighbors in at most two of the partners, a contradiction. The coalition number is three.

## Verification

The supplied `verification/verify.py` directly tests total domination and independence. Its exact partition routine visits every partition and skips candidates having no more blocks than the incumbent valid maximum; this cannot remove a candidate that improves the maximum. The graph census considers 33,864 labeled graphs of orders three through six and finds 72 meeting the high-girth hypotheses. The supplied output also records constructive tests on larger graphs and exact small boundary checks, including the six-vertex graph above. The finite tests do not prove the unrestricted or the positive-degree local theorem; the proof above covers both and gives a separate mathematical boundary argument.

## Relationship to prior work

Buntina and Golmohammadi introduced the invariant in *Total outer-independent coalition in graphs*, arXiv:2607.23623v2, July 2026. Their Theorem 1 bounds each block's number of partners by the maximum degree, and Lemma 2 gives a universal hub in a maximum partition. Thus the degree ceiling is known. Their Theorem 2 gives the cycle value three; this is not a new case. The contribution here is the matching lower construction under a local condition and the resulting sharp equality for all finite graphs of minimum degree at least two and girth at least five.

## Limitations

The local condition is sufficient, not necessary; the result does not classify all extremal graphs or partitions. Other coalition predicates that omit outer independence are different invariants. Priority beyond the compared statements is not established.

## Reference

O. Buntina and H. Golmohammadi, *Total outer-independent coalition in graphs*, [arXiv:2607.23623v2](https://arxiv.org/abs/2607.23623v2), especially Theorem 1, Lemma 2, and Theorem 2(iv).
