# Degree-sharp total outer-independent coalitions in high-girth graphs

## Finding

**Theorem.** Let \(G\) be any finite simple graph of minimum degree \(\delta(G)\ge2\) and girth at least \(5\), allowing disconnected graphs and taking the girth of a forest to be infinite. Its total outer-independent coalition number satisfies

\[
\boxed{C_t^{\mathrm{oi}}(G)=\Delta(G)+1.}
\]

More generally, the same equality holds when some maximum-degree vertex \(v\) has an independent open neighborhood \(N(v)\), and every vertex \(u\notin N[v]\) has a neighbor outside \(N(v)\). In either case, a maximum coalition partition is explicit:

\[
\mathcal P_v=\{V(G)\setminus N(v)\}\ \cup\ \{\{w\}:w\in N(v)\}.
\]

The girth hypothesis cannot simply be replaced by girth at least \(4\): the graph obtained from \(K_{3,3}\) by deleting a two-edge matching has minimum degree \(2\), maximum degree \(3\), girth \(4\), and coalition number \(3<4\). This finite boundary instance is separately checked by exhaustive partition enumeration; it is not used to prove the unrestricted theorem.

## Assumptions and scope

All graphs are finite, undirected, loopless, and without parallel edges. For a graph \(G\), \(N(u)\) denotes the open neighborhood of \(u\), \(\delta(G)\) and \(\Delta(G)\) its minimum and maximum degrees, and girth the length of its shortest cycle. A vertex set \(D\) is a *total outer-independent dominating set* (TOIDS) when (i) each vertex, including each vertex in \(D\), has a neighbor in \(D\), and (ii) \(V(G)\setminus D\) is independent. Two disjoint nonempty sets form a TOI-coalition if neither is a TOIDS but their union is. A *TOI-coalition partition* partitions all vertices into nonempty sets, each having a distinct coalition partner among the other parts. The maximum number of parts is \(C_t^{\mathrm{oi}}(G)\).

No connectedness or regularity assumption is needed. The lower-bound construction uses only one suitable vertex. The statement does not characterize all extremal partitions or all graphs attaining the maximum-degree upper bound.

## Proof

**1. Universal degree upper bound when \(\Delta\ge2\).** No two disjoint vertex subsets \(D,E\) can both be TOIDS. Indeed, if \(D\) is a TOIDS then \(V\setminus D\) is independent; since \(E\subseteq V\setminus D\), \(E\) is independent, contradicting the total-domination requirement inside the nonempty set \(E\).

Take any TOI-coalition partition with \(k\) parts. Its coalition graph has the parts as vertices and an edge for every valid coalition pair. It has no isolated vertices. The preceding observation says two edges of this graph cannot be disjoint, so its edge set is pairwise intersecting; such a simple graph with no isolated vertices is a star or a triangle (with the one-edge case included as a star). Consequently, some part \(X\) has all \(k-1\) other parts as coalition partners.

If \(X\) fails total domination, choose \(u\) having no neighbor in \(X\). Every partner of \(X\) must contain a neighbor of \(u\). Different partner parts are disjoint, whence \(k-1\le\deg(u)\le\Delta\). Otherwise \(X\) totally dominates but is not outer-independent; choose an edge \(ab\) in \(G[V\setminus X]\). Every partner must contain at least one of \(a,b\), so there are at most two partners and \(k-1\le2\le\Delta\). In either case \(k\le\Delta+1\).

**2. Local construction.** Suppose \(v\) has degree \(\Delta\), \(N(v)\) is independent, and every \(u\notin N[v]\) has a neighbor outside \(N(v)\). Write \(X=V\setminus N(v)\). Every vertex except \(v\) has a neighbor in \(X\): a neighbor of \(v\) is adjacent to \(v\in X\), while a vertex outside \(N[v]\) is covered by the second local assumption. The vertex \(v\) itself has no neighbor in \(X\), so \(X\) is not a TOIDS. No singleton is a TOIDS in a loopless graph. For every \(w\in N(v)\), the set \(X\cup\{w\}\) totally dominates every vertex and has independent complement \(N(v)\setminus\{w\}\). Thus every singleton \(\{w\}\) forms a TOI-coalition with \(X\). The displayed \(\Delta+1\)-part partition is valid. The upper bound yields equality.

**3. Girth reduction.** If \(\delta(G)\ge2\) and the girth is at least \(5\), then \(N(v)\) is independent for every vertex \(v\), since a neighboring pair inside \(N(v)\) would create a triangle. For any \(u\notin N[v]\), at most one neighbor of \(u\) lies in \(N(v)\), since two would form the four-cycle \(v,a,u,b,v\). Since \(\deg(u)\ge2\), there is a neighbor outside \(N(v)\). Thus every vertex satisfies the local criterion, in particular a maximum-degree vertex. The theorem follows.

**4. Boundary at girth four.** Label the bipartition \(A=\{0,1,2\}\), \(B=\{3,4,5\}\), and take all nine cross edges except \(\{1,4\}\) and \(\{2,5\}\). This graph has the stated degree sequence and a four-cycle. The included exhaustive verifier enumerates every one of the \(203\) set partitions of its six labeled vertices, evaluates the TOIDS predicate directly for each pair union, and establishes that the maximum valid number of parts is \(3\). This finite certificate shows the girth threshold in this sufficient theorem cannot be weakened to \(4\) without extra assumptions.

## Verification

The standalone standard-library program `verification/verify.py` constructs graphs from edge lists and implements the TOIDS predicate directly from neighborhoods and complements. For each constructed partition it checks nonemptiness, coverage, non-TOIDS parts, and coalition validity. It also enumerates every unlabeled set partition using the canonical operation of inserting the next vertex in one existing block or creating a new block; this is exhaustive and has no isomorphism or search-pruning assumptions.

The program exhaustively considers all \(33{,}864\) labeled simple graphs on \(3\) through \(6\) vertices, and finds \(72\) meeting the minimum-degree and girth assumptions. It checks their optimal coalition numbers by exhaustive vertex-partition enumeration. Further exhaustive coalition checks cover \(C_7\), \(C_8\), the wedge of two \(5\)-cycles, and the Petersen graph. Explicit partitions are also checked for the Heawood graph and the \(3\)- and \(4\)-dimensional hypercubes (the latter fall under the local criterion despite having four-cycles). Finally, the \(K_4\), \(P_4\), and six-vertex bipartite boundary instances have their strict deficits checked exhaustively. The run output ends with `VERIFY_OK`.

The unrestricted proof does not rely on the finite tests. The packaged files `verification/verify.py` and `verification/verify_output.txt` are reproducible with a standard Python 3 interpreter and require no external dependencies.

## Relationship to prior work

Buntina and Golmohammadi introduced total outer-independent coalitions in *Total outer-independent coalition in graphs* (arXiv:2607.23623, first submitted 26 July 2026). Their Section 3 Theorem 1 bounds the number of partners of each partition block by \(\Delta(G)\), and their Section 4 Lemma 2 supplies a universal hub in a maximum partition; together these yield the general upper bound used above. Their Section 4 determines the invariant for complete graphs, complete bipartite graphs, paths, and cycles. In particular, the cycle case \(C_t^{\mathrm{oi}}(C_n)=3\) is already published and is not claimed independently.

The contribution here is the matching *degree-sharp lower construction* under a radius-two neighborhood condition and its application to **every** finite graph of girth at least five and minimum degree at least two. It applies to unbounded nonregular high-girth graph families, including wedges of long cycles, beyond the separately treated classes in the source. The source's concluding questions explicitly ask for degree-based bounds. A universal upper bound, or a result about TOIDS without coalitions, does not imply this equality unless the partner construction is also supplied.

## Limitations

The local criterion and the girth/minimum-degree assumptions are sufficient, not necessary. The theorem neither determines coalition numbers for all triangle-free graphs nor classifies all extremal partitions. The six-vertex boundary relies on exhaustive finite enumeration, whose correctness is inspectable in the supplied code; the infinite equality is entirely mathematical. Results about ordinary coalitions or total outer-independent domination alone need not transfer to this hybrid partition invariant. Literature searches cannot exclude an unindexed equivalent theorem; priority has not been independently adjudicated.

## References

1. O. Buntina and H. Golmohammadi, *Total outer-independent coalition in graphs*, arXiv:2607.23623v1, submitted 26 July 2026; revised version arXiv:2607.23623v2, 29 July 2026. https://arxiv.org/abs/2607.23623v1 . The revised full text was inspected in Sections 1, 3, 4, and 6, including Theorem 1, Lemma 2, Theorem 2, and the concluding questions.
