# Optimal paired domination and connected reconfiguration in \(\mathrm{KG}(n,2)\)

## Finding

For each integer \(n\ge 6\), let \(G_n=\mathrm{KG}(n,2)\) have the two-element subsets of \([n]\) as vertices, with adjacency defined by disjointness. A paired dominating set is a dominating vertex set whose induced subgraph admits a perfect matching. Then
\[
\gamma_{\mathrm{pr}}(G_n)=4.
\]

Under the identification of vertices of \(G_n\) with edges of the complete graph on \([n]\), a four-vertex set is paired dominating **if and only if** its four ground edges contain a matching of size three. The four-edge ground graph therefore has exactly one of the following three shapes: \(P_4\sqcup K_2\), \(P_3\sqcup 2K_2\), or \(4K_2\), together with unused ground vertices. Consequently, the number of minimum paired dominating sets is
\[
N_n=180\binom n6+315\binom n7+105\binom n8.
\]
Here \(\binom nk=0\) whenever \(k>n\). The corresponding classes have respectively \(180\binom n6\), \(315\binom n7\), and \(105\binom n8\) sets. Their induced subgraphs in \(G_n\) have respectively one, two, and three perfect matchings.

Define the token-jumping reconfiguration graph \(\mathcal R_n\) whose vertices are these minimum paired dominating sets and in which two are adjacent when their symmetric difference has exactly two vertices of \(G_n\). Then **\(\mathcal R_n\) is connected for every \(n\ge 6\)**.

## Assumptions and scope

All graphs are finite, simple, and undirected. A selected vertex dominates itself in the ordinary (closed-neighborhood) domination convention. A perfect matching in the induced selected graph is not required to be induced. The ground edges are unordered two-element subsets, and the counted selected sets are unordered sets of graph vertices on the fixed labeled ground set \([n]\). This result treats all integers \(n\ge6\), with no assertion about smaller Kneser graphs. Token jumping changes one selected graph vertex at a time while preserving cardinality four and paired domination at every intermediate configuration.

## Proof

**The transversal lemma.** Let \(F\) be a nonempty family of ground edges, considered as selected vertices of \(G_n\), and let \(H=([n],F)\). Write \(\tau(H)\) for the minimum number of ground vertices meeting every edge of \(F\), and \(\nu(H)\) for the maximum number of pairwise disjoint edges of \(F\). For every two-element ground set \(X\), the corresponding vertex of \(G_n\) has a selected neighbor exactly when some edge of \(F\) avoids \(X\). It follows, with the selected vertices included in the quantifier, that \(F\) is a **total dominating** set of \(G_n\) if and only if \(\tau(H)\ge3\). Every paired dominating set is total dominating because every selected vertex belongs to an edge of the induced perfect matching. Thus every paired dominating \(F\) satisfies \(\tau(H)\ge3\).

**Classification for four selected vertices.** Suppose \(|F|=4\) and \(F\) is paired dominating. If \(H\) contains a triangle, its fourth edge either meets that triangle, in which case two ground vertices cover all four edges and \(\tau(H)\le2\), or is disjoint from the triangle. In the latter case the disjointness graph induced on these four selected edges is the three-leaf star \(K_{1,3}\), which has no perfect matching. Both cases contradict paired domination. Hence \(H\) is triangle-free. Because \(H\) has only four edges, no other odd cycle is possible; therefore \(H\) is bipartite. König's equality \(\nu(H)=\tau(H)\) now implies \(\nu(H)\ge3\).

Conversely, suppose \(F\) contains three pairwise disjoint ground edges \(a,b,c\), with fourth edge \(e\). A two-element set meets at most two of \(a,b,c\), so every graph vertex has a selected neighbor; indeed \(\tau(H)\ge3\). The fourth edge \(e\) is disjoint from at least one of \(a,b,c\). Pair \(e\) with such an edge and pair the other two selected edges with each other. Both pairs are adjacent in \(G_n\), yielding a perfect matching on the four selected vertices. Thus \(F\) is paired dominating. This proves the classification.

**Minimum and multiplicities.** Any two-element paired dominating set consists of two disjoint ground edges, say \(\{a,b\}\) and \(\{c,d\}\). The graph vertex \(\{a,c\}\) meets both and is not selected, so it is undominated. A paired dominating set must have even cardinality, hence its minimum cardinality is at least four. For \(n\ge6\), a matching of three ground edges exists and can be augmented with any distinct fourth ground edge. By the classification this is paired dominating, so \(\gamma_{\mathrm{pr}}(G_n)=4\).

The union of the four ground edges contains exactly six, seven, or eight ground vertices. With six, its shape is \(P_4\sqcup K_2\): choose the two vertices of the isolated edge in \(\binom62=15\) ways, and arrange the four others as a nonoriented four-vertex path in \(4!/2=12\) ways, giving \(180\) per six-set. With seven, the shape is \(P_3\sqcup2K_2\): choose the middle vertex in \(7\) ways, the two endpoints in \(\binom62=15\) ways, and pair the remaining four vertices in \(3\) ways, giving \(315\) per seven-set. With eight, the shape is \(4K_2\), with \((8-1)!!=105\) choices per eight-set. These cases are disjoint and exhaustive, proving the displayed census. In the disjointness graph on the four selected edges the three shapes become, respectively, a triangle with one pendant vertex, \(K_4\) minus one edge, and \(K_4\); direct matching inspection gives respectively one, two, and three perfect matchings.

**Reconfiguration.** For every three-edge matching \(M\) of the ground complete graph, define
\[
\mathcal S_M=\{M\cup\{e\}:e\in\tbinom{[n]}2\setminus M\}.
\]
Every state in \(\mathcal S_M\) is a minimum paired dominating set, and any two states in this family differ by one selected graph vertex. Thus \(\mathcal S_M\) is a clique in \(\mathcal R_n\), and the classification shows that the families \(\mathcal S_M\) cover all vertices of \(\mathcal R_n\).

We connect these cliques via two elementary transformations of three-edge matchings. If \(M'\) replaces one edge of \(M\) with another edge disjoint from its other two edges, the common four-edge state \(M\cup M'\) belongs to both cliques. If \(M=\{ab,cd,ef\}\) and \(M'=\{ac,bd,ef\}\) differ by a two-edge flip on four distinct ground vertices, the states \(M\cup\{ac\}\) and \(M'\cup\{ab\}\) are adjacent in \(\mathcal R_n\): each contains its own matching triple and their intersection consists of the three edges \(ab,ac,ef\). The alternative flip orientation is identical after renaming.

Any two three-edge matchings of the complete graph can be joined by a sequence of these transformations. First equalize their six-vertex supports: replace an edge \(yz\) at a currently used ground vertex \(y\) outside the desired support by \(xz\), where \(x\) is currently unused but belongs to the desired support. The result is a three-edge matching and improves support agreement. Once the support is fixed, two perfect matchings of these six vertices are connected by two-edge flips: to create a required pair \(uv\), replace the current edges \(ua\) and \(vb\) by \(uv\) and \(ab\), leaving already corrected pairs intact, and repeat. Each elementary transformation links the corresponding cliques in \(\mathcal R_n\). Since their union covers all states, \(\mathcal R_n\) is connected.

## Verification

The included independent graph-theoretic verifier constructs the disjointness adjacency relation directly, exhaustively checks every four-vertex candidate for ordinary domination and an induced perfect matching, and compares its result with the three-matching characterization. Over \(6\le n\le10\), it checks \(235{,}725\) candidates and reproduces both the total count and the separate ground-support class counts. A second verifier constructs the token-jumping adjacency among predicted optimal configurations and confirms connectivity for \(6\le n\le9\). The exact messages are in `verification_output.txt`; both scripts use only the Python standard library. The infinite-family statements rely on the foregoing proofs, not finite experimentation.

## Relationship to prior work

Cornet and Torres [1] investigate domination and multiple domination in Kneser graphs and characterize the minimum ordinary dominating configurations, with specific incidence descriptions for two-subset Kneser graphs. Brešar, Cornet, Dravec, and Henning [2] study total and multiple domination in the same graph family and establish that, in the relevant large-ground-set regime, minimum total dominating sets form disjoint families. These earlier results concern different extremal requirements: they do not enumerate the four-vertex paired-dominating configurations nor establish token-jumping connectivity under preservation of the induced perfect matching. The present proof explicitly supplies those further statements; it does not claim the known three-vertex total-domination or ordinary-domination results as new.

## Limitations

The theorem is for \(n\ge6\); no claim is made about the Petersen-graph boundary \(n=5\). Counts are for labeled ground sets and distinguish vertex subsets, not selections of a particular perfect matching inside each subset. Independent mathematical review has not been performed. Although the cited accessible primary works and targeted related-record searches did not yield the same paired-domination census or reconfiguration theorem, an equivalent unindexed result cannot be excluded.

## References

[1] M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603, first submitted 29 August 2023, https://arxiv.org/abs/2308.15603; freely available complete text https://arxiv.org/html/2308.15603v2.

[2] B. Brešar, M. G. Cornet, T. Dravec, and M. A. Henning, *\(k\)-Domination invariants on Kneser graphs*, arXiv:2312.15464, first submitted 24 December 2023, https://arxiv.org/abs/2312.15464; freely available complete text https://arxiv.org/html/2312.15464v1.
