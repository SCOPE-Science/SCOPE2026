# Independent-domination spectra of central graphs of triangle-free graphs

## Finding

Let \(G=(V,E)\) be any finite connected simple triangle-free graph with \(n=|V|\ge3\), \(m=|E|\), and \(d(u)=\deg_G(u)\). Its central graph \(\mathsf C(G)\) is obtained by subdividing every edge once and joining the original vertices that were nonadjacent in \(G\). A support vertex is one adjacent to a degree-one vertex; let \(S\subseteq V\) be the support set. Write \(D_i(H;z)=\sum_{I}z^{|I|}\), where the sum is over all independent dominating vertex sets of \(H\), equivalently all inclusion-maximal independent sets.

**Theorem.** The exact independent-domination polynomial is
\[
D_i(\mathsf C(G);z)=z^m+\sum_{u\in V\setminus S}z^{m+1-d(u)}+\sum_{uv\in E}z^{m+3-d(u)-d(v)}.\tag{1}
\]
All contributions enumerate distinct sets even where their exponents coincide. In particular, the **total number** of independent dominating sets is
\[
D_i(\mathsf C(G);1)=m+n+1-|S|.\tag{2}
\]
Define \(Q=\max_{uv\in E}(d(u)+d(v))\) and \(e_Q=|\{uv\in E:d(u)+d(v)=Q\}|\). Then
\[
i(\mathsf C(G))=m+3-Q,\qquad
[z^{i(\mathsf C(G))}]D_i(\mathsf C(G);z)=e_Q+|\{u\in V\setminus S:d(u)=Q-2\}|+\mathbf 1_{Q=3}.\tag{3}
\]
For a connected \(d\)-regular triangle-free graph with \(d\ge2\), this simplifies to \(z^m+n z^{m+1-d}+m z^{m+3-2d}\); optimal multiplicity is \(2n\) for \(d=2\) and \(m\) for \(d\ge3\). For every nontrivial tree on \(n\ge3\) vertices, the total number is \(2n-|S|\). The polynomial need not be determined by the degree sequence alone: on vertices \(0,\ldots,5\), the two trees with edge sets \(\{01,12,13,04,45\}\) and \(\{01,12,03,05,34\}\) both have degree multiset \(\{3,2,2,1,1,1\}\), but their central-graph polynomials are respectively \(z^3+4z^4+5z^5\) and \(2z^3+z^4+6z^5\).

## Assumptions and scope

Graphs are finite, simple, connected, and triangle-free; \(n\ge3\), so \(m\ge2\). Each original vertex of \(G\) remains individually distinguished in \(\mathsf C(G)\), and the subdividing vertex of edge \(uv\) is uniquely attached to that original edge. The polynomial counts labelled vertex subsets, without quotienting by automorphisms. The term independent dominating means a vertex subset simultaneously independent and dominating; it does not mean the different independence-domination parameter that maximizes a domination demand over independent subsets.

## Proof

Write \(V(\mathsf C(G))=V\sqcup\{x_e:e\in E\}\). The vertices \(x_e\) are pairwise nonadjacent; each has exactly its two original endpoints as neighbours. For original vertices \(u,v\), adjacency in \(\mathsf C(G)\) holds precisely when \(uv\notin E(G)\).

Take any independent dominating set \(I\) and write \(U=I\cap V\). Independence of \(U\) means it is a clique in \(G\), so triangle-freeness forces \(|U|\le2\). Independence also forbids selecting \(x_e\) if \(e\) meets \(U\). Conversely, if \(e\) is disjoint from \(U\), then both neighbours of \(x_e\) lie outside \(I\), and domination forces \(x_e\in I\). Hence the entire set is uniquely forced by \(U\):
\[
I=U\cup\{x_e:e\in E(G-U)\}.\tag{4}
\]
There are precisely three possible types of \(U\).

If \(U=\varnothing\), all \(m\) subdividing vertices are selected. They dominate all originals because a connected graph with \(n\ge3\) has no isolated vertex. This contributes \(z^m\).

If \(U=\{u\}\), every original \(v\ne u\) with \(uv\notin E\) is dominated by \(u\) in the central graph. An original neighbour \(v\) of \(u\) is dominated by the subdivision vertex of an edge incident with \(v\) and not \(u\) precisely when \(d(v)\ge2\). Thus (4) is dominating exactly when \(u\notin S\). It contains \(1+m-d(u)\) vertices, producing the middle sum of (1).

If \(U=\{u,v\}\) with \(uv\in E\), any other original vertex \(w\) fails to be adjacent in \(G\) to at least one of \(u\) and \(v\): otherwise \(u,v,w\) form a triangle. Therefore \(w\) is adjacent in \(\mathsf C(G)\) to a selected original vertex. Every unchosen \(x_e\) meets \(U\), so is also dominated. This construction is always valid and has \(2+m-d(u)-d(v)+1=m+3-d(u)-d(v)\) vertices. Each edge \(uv\) contributes one distinct set. Equation (1) follows by exhaustion; setting \(z=1\) proves (2).

For the optimal-size assertion, connectedness and \(n\ge3\) imply \(Q\ge3\). Edge-generated sets have minimum size exactly \(m+3-Q\). The empty-type set has size \(m\ge m+3-Q\). If \(u\notin S\), each neighbour \(v\) has \(d(v)\ge2\), so \(Q\ge d(u)+2\); hence its singleton-generated size \(m+1-d(u)\ge m+3-Q\). Equality among the three types holds exactly for edges with degree sum \(Q\), eligible vertices with degree \(Q-2\), and the empty type when \(Q=3\). This proves (3).

## Verification

The standalone `verify.py` constructs the central graph from each input graph, independently enumerates all maximal cliques of its complement (equivalently all maximal independent sets of the central graph), and compares every weight coefficient with (1). It checks every connected labelled triangle-free simple graph on \(2\) through \(6\) vertices: \(3801\) graphs, including the small boundary \(K_2\), where only (1) and (2) are asserted in the code. Three larger samples check an eight-cycle, \(K_{4,4}\), and a ten-cycle. It separately verifies the minimum formula (3) whenever \(n\ge3\). Execute `python3 verify.py` from the directory containing that file; only the Python standard library is required. Finite computations corroborate but do not establish the infinite theorem, which follows from the proof above.

## Relationship to prior work

Cabrera-Martínez, López-Carmona, Rios-Villamar, and Serrano-Díaz (2026, Theorems 2.1--2.2) provide a clique-minimization formula for the independent domination **number** of central graphs and the minimum value \(m+3-Q\) for connected triangle-free graphs. These minimum-value results are prior work, not presented here as novel. Formula (1) instead classifies **every** independent dominating set by cardinality; (2) and the optimal-set multiplicity in (3) are distinct enumerative conclusions. Their full text and proof of the minimization formula were compared. Their structural construction motivates the enumeration but does not state its exact full polynomial or multiplicities.

Shivaswamy, Soner, and Alwardi (2014) define the independent-domination polynomial and evaluate it for several standard graph families. Their published formulas do not address central graphs of arbitrary connected triangle-free graphs. A related mathematical research record concerns higher iterates \(\mathsf C^k(G)\), not the first central graph enumerator in (1).

## Limitations

The formula requires triangle-freeness and connectedness. In a graph with triangles, the original-vertex subset may have three or more vertices, and pair-generated sets can fail domination. The statement does not extend without changes to disconnected graphs with isolated vertices, nor to labelled-set counting modulo automorphisms. Its originality is specifically the full enumerator and minimum multiplicity, not the independent domination number already proved in 2026. A general earlier maximal-independent-set theorem might imply the enumerator implicitly; comprehensive historical-priority confirmation remains open.

## References

1. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, A. Serrano-Díaz, *Independent domination in central graphs*, arXiv:2609.16357v1 (first public 2026-09-14), Sections 1--2, especially Theorems 2.1--2.2. https://arxiv.org/abs/2609.16357 . Accessible full text: https://www.researchgate.net/publication/414357442_Independent_domination_in_central_graphs .
2. P. M. Shivaswamy, N. D. Soner, A. Alwardi, *Independent Dominating Polynomial in Graphs*, International Journal of Scientific and Innovative Mathematical Research **2** (2014), 757--763. https://www.researchgate.net/publication/366503721_Independent_Dominating_Polynomial_in_Graphs .
