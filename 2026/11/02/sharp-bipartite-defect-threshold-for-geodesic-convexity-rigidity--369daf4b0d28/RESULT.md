# Sharp bipartite defect threshold for geodesic-convexity rigidity and online shattering

## Finding
Let \(G=(L\sqcup R,E)\) be a finite simple bipartite graph. Assume an integer \(t\ge1\), \(|L|,|R|\ge2t+3\), and that every vertex has at most \(t\) nonneighbors on the opposite side. Then all geodesically convex vertex subsets of \(G\) are exactly
\[
\mathcal C(G)=\{\varnothing,V(G)\}\cup\{\{v\}:v\in V(G)\}\cup\{\{u,v\}:uv\in E(G)\}.
\]
In particular, writing \(N=|V(G)|\),
\[
|\mathcal C(G)|=N+|E(G)|+2,\qquad
\Phi_G(z)=1+Nz+\binom N2 z^2,
\qquad \operatorname{VCdim}(\mathcal C(G))=2,\qquad
\operatorname{Ldim}(\mathcal C(G))=3.
\]
The side-size condition is **sharp uniformly in the defect bound**: for every \(t\ge1\), a graph with both sides of size \(2t+2\), at most \(t\) missing neighbors per vertex, and a proper geodesically convex four-vertex set exists. The assertion that the only convex sets are the displayed ones is called *g-minimality* in earlier literature; the newly assessed assertion is the sharp quantitative defect threshold, with its learning-dimension consequences, not the definition of g-minimality.

## Assumptions and scope
Graph geodesic convexity requires a set to contain **every** vertex of **every shortest path** between any two of its vertices. In the concept class, instances are vertices and hypotheses are indicator functions of convex vertex sets. An \(s\)-element support is VC-shattered when all \(2^s\) traces occur. Littlestone shattering means that a complete binary decision tree of depth \(d\), with a vertex query at each internal node, is realized by hypotheses along every root-to-leaf labeled path. These definitions include empty and full convex sets. No regularity or transitivity is assumed; the bipartition can be unbalanced.

## Proof
**(1) Common-neighbor forcing.** Any pair of vertices on the same side, say in \(L\), has at least \(|R|-2t\ge3\) common neighbors in \(R\). Their distance is two, so every such common neighbor belongs to any convex set containing the pair. The symmetric statement holds on the other side. Every opposite-side nonedge has distance exactly three: for such a pair \(a_0\in L\), \(b_0\in R\), choose a neighbor \(r\in N(a_0)\subseteq R\), then choose a vertex \(\ell\in N(r)\cap N(b_0)\subseteq L\). The intersection has at least \(|L|-2t\ge3\) elements, and \(a_0-r-\ell-b_0\) is a shortest path of length three. In particular, the whole graph is connected.

**(2) No proper convex set has two vertices on one side.** Suppose \(S\subsetneq V(G)\) is convex and contains at least two vertices in \(L\). Put \(A=S\cap L\), \(B=S\cap R\), \(a=|A|\) and \(b=|B|\). By (1), \(b\ge3\), and applying (1) to two members of \(B\) gives \(a\ge3\). If \(A=L\), each \(r\in R\) has at least \(|L|-t\ge2\) neighbors in \(A\), hence is forced into \(S\); this makes \(S=V(G)\), contrary to properness. Similarly \(B\ne R\). Therefore \(L\setminus A\) and \(R\setminus B\) are nonempty.

For any \(r\in R\setminus B\), at most one vertex of \(A\) is adjacent to \(r\); otherwise a length-two geodesic with midpoint \(r\) contradicts convexity. Thus at least \(a-1\) edges from \(A\) to this \(r\) are missing. The total number of missing edges incident to \(A\) is at most \(at\), giving
\[
(q-b)(a-1)\le at, \qquad q=|R|.
\]
Interchanging the sides gives \((p-a)(b-1)\le bt\), where \(p=|L|\). As each outside vertex has at most \(t\) nonneighbors, the existence of vertices outside \(S\) also forces \(a-1\le t\) and \(b-1\le t\). Consequently \(q-b\ge(2t+3)-(t+1)=t+2\), so
\[
(t+2)(a-1)\le at,\qquad 2a\le t+2.
\]
Therefore \(a\le(t+2)/2\), and the first missing-edge bound and \(a\ge3\) imply
\[
q-b\le\frac{at}{a-1}=t+\frac{t}{a-1}\le\frac{3t}{2}.
\]
But \(b\le(t+2)/2\) symmetrically, and hence
\[
q-b\ge(2t+3)-\frac{t+2}{2}=\frac{3t}{2}+2,
\]
a contradiction. Thus a proper convex set contains at most one vertex from \(L\) and at most one from \(R\).

**(3) Classification.** An opposite-side pair which is a nonedge has a shortest path of length three, and cannot itself be convex. Each edge endpoint set is convex since its endpoints have distance one. Empty set, full set and every singleton are convex. These exhaust the possibilities by (2).

**(4) Static shattering.** Any two distinct vertices \(x,y\) are shattered: the empty set, their individual singletons and the full set realize the four traces. For a three-vertex support to be shattered, each of its three two-element traces must be realized without the third vertex; by (3), the three pairs must all be edges. This would form a triangle, impossible in a bipartite graph. Thus every singleton and pair, but no larger support, is shattered, proving the polynomial and VC dimension.

**(5) Online shattering.** The following explicit depth-three complete tree gives the lower bound. Choose \(v\in L\), two distinct neighbors \(w_1,w_2\in R\), and an edge \(xy\) disjoint from \(v\) (all exist from the lower degree condition). At the root query \(v\). After answer one, query \(w_1\) and then \(w_2\) on both second-level branches. The four binary answer strings on this branch are realized respectively by \(\{v\}\), \(\{v,w_2\}\), \(\{v,w_1\}\), and \(V(G)\). After answer zero at the root, query \(x\), then \(y\); the four answer strings are realized by \(\varnothing\), \(\{y\}\), \(\{x\}\), and \(\{x,y\}\). Hence \(\operatorname{Ldim}\ge3\).

For the upper bound, fix any first query \(v\). Hypotheses giving answer one are exactly \(V(G)\), \(\{v\}\), and \(\{v,u\}\) for neighbors \(u\) of \(v\). At every subsequent vertex query \(u\ne v\), at most two such hypotheses answer one, namely \(V(G)\) and possibly \(\{u,v\}\); a repeated query \(v\) gives only the constant answer one. No complete depth-three continuation is possible after positive root answer: a depth-three tree would require at least four hypotheses in the positive branch after *either* second query, while the positive branch of any informative second query has at most two. Thus the positive-root version space has Littlestone dimension at most two; the full class has Littlestone dimension at most three.

**(6) Sharpness construction.** Let \(p=q=2t+2\). Choose distinct \(u,v\in L\) and \(x,y\in R\). Split the \(2t\) remaining right vertices into disjoint \(t\)-sets \(R_u,R_v\), and make \(u\) nonadjacent exactly to \(R_u\) and \(v\) exactly to \(R_v\). Split the \(2t\) remaining left vertices into disjoint \(t\)-sets \(L_x,L_y\), and make \(x\) nonadjacent exactly to \(L_x\) and \(y\) exactly to \(L_y\). Retain all other possible bipartite edges. Every vertex has at most \(t\) missing neighbors. The common neighbors of \(u,v\) are precisely \(x,y\), and the common neighbors of \(x,y\) are precisely \(u,v\). All other pairs in \(S=\{u,v,x,y\}\) are adjacent. Therefore \(S\) induces a geodesically convex \(K_{2,2}\), and \(S\subsetneq V(G)\). This disproves a universal statement with \(2t+2\) substituted for \(2t+3\).

## Verification
The accompanying standard-library Python program `check_rigidity.py` independently builds shortest-path intervals and enumerates convex sets. It exhausts all isomorphism classes of deleted matchings for equal side orders five and six; checks the extremal boundary construction for defect parameters one through five; tests 185 deterministic sampled near-complete bipartite graphs at or above the proved threshold; and computes the VC and Littlestone dimensions of the five-by-five crown instance by direct finite version-space recursion. Its terminal success marker is `ALL_DENSE_BIPARTITE_RIGIDITY_CHECKS_PASS randomized_graphs=185`. The all-parameter assertions rely on the preceding proof, not experimental extrapolation.

## Relationship to prior work
Brown and Oellermann introduced **g-minimal graphs** and proved that a graph has precisely the trivial convex sets if and only if it is triangle-free and every nonadjacent pair has full geodesic convex hull [1]. This known classification, and the elementary hypothesis enumeration conditional on g-minimality, are **not** claimed as new. The proposed contribution is the **uniform, sharp** sufficient threshold \(|L|,|R|\ge2t+3\) under maximum cross-nonneighbor degree \(t\), together with an explicit all-parameter boundary counterexample and exact VC/Littlestone consequences. The graph-convexity survey [2] gives broader background. Thiessen and Gärtner [3] study general online learning of graph-convex sets and halving-type mistake bounds, rather than, in its accessible abstract, this particular sharp dense-bipartite rigidity threshold. Another published result studies geodesic subpath numbers of bicliques with a deleted matching [4], a different numerical invariant. These distinctions compare mathematical claims, not titles alone.

## Limitations
The full text of Brown and Oellermann [1] and Thiessen and Gärtner [3] was not accessible in the present comparison, so a prior specialized corollary or theorem hidden in either paper remains a genuine historical-priority risk. A complete priority search under older terminology is not claimed. The theorem is specific to bipartite graphs with the **maximum missing-neighbor degree** restriction; it is not a statement about arbitrary dense graphs or average-degree conditions. External independent mathematical validation has not been performed.

## References
[1] Jason I. Brown and Ortrud R. Oellermann, *Graphs with a Minimal Number of Convex Sets*, Graphs and Combinatorics 30 (2014), 1383–1397, doi:10.1007/s00373-013-1356-2.

[2] Mitre C. Dourado, Marisa Gutierrez, Fábio Protti, Rudini Sampaio and Silvia Tondato, *Characterizations of graph classes via convex geometries: a survey*, arXiv:2203.15878 (first public 2022-03-29).

[3] Maximilian Thiessen and Thomas Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, pp. 349–364, doi:10.1007/978-3-031-26412-2_22.

[4] *Geodesic subpath numbers of bicliques with a deleted matching*, published published-finding corpus mathematical research record, 2026-10-04, identifier: 525c4067322f.
