# The scale-\(3\) Rips complex of the Tutte–Coxeter graph is a wedge of \(256\) three-spheres
## Finding
Let \(T\) be the Tutte–Coxeter graph in its duad–syntheme model, with the shortest-path metric. For every real \(r\) with \(3\le r<4\), the inclusive Vietoris–Rips complex satisfies \(\operatorname{VR}_{\le r}(T)\simeq\bigvee^{256}S^3\). More precisely, at this scale it is the simplicial join of two 15-vertex complexes, each of which simplicially collapses to \(\bigvee^{16}S^1\).

The two join factors arise canonically from the two parts of the standard duad–syntheme incidence model: the 15 duads are the edges of \(K_6\), and the 15 synthemes are its perfect matchings.

## Assumptions and scope
Let \(U=\{1,2,3,4,5,6\}\). A **duad** is a two-element subset of \(U\), and a **syntheme** is a partition of \(U\) into three duads. The Tutte–Coxeter graph \(T\) has the 15 duads and 15 synthemes as its two vertex classes, with a duad adjacent to a syntheme exactly when it belongs to that syntheme. This gives a cubic bipartite graph on 30 vertices. Distances are shortest-path distances in this graph. The inclusive complex \(\operatorname{VR}_{\le r}(T)\) contains a finite vertex set exactly when its graph-metric diameter is at most \(r\).

Because all graph distances are integers, the complex is constant for \(3\le r<4\). The statement concerns ordinary homotopy type.

## Proof
Write \(D\) for the duad vertices and \(S\) for the syntheme vertices. Two distinct duads have distance \(2\) exactly when they are disjoint: disjoint duads extend uniquely to a syntheme, whereas intersecting duads cannot lie in a common syntheme and have distance \(4\). Two distinct synthemes have distance \(2\) exactly when they share a duad, and otherwise have distance \(4\). Finally, a duad \(e\) and syntheme \(M\) have distance \(1\) when \(e\in M\), and distance \(3\) otherwise. Indeed, if \(e\notin M\), exactly one duad \(f\in M\) is disjoint from \(e\); the pair \(e,f\) extends to a syntheme \(M'\), giving the length-three path \(e-M'-f-M\).

Thus at threshold \(3\) every duad is joined to every syntheme. Inside \(D\), adjacency means disjointness; inside \(S\), adjacency means sharing a duad. Since a Vietoris–Rips complex is the clique complex of its threshold graph,
\[
\operatorname{VR}_{\le3}(T)=K_D*K_S,
\]
where \(K_D\) is the matching complex of \(K_6\), and \(K_S\) is the clique complex on synthemes with common-duad adjacency.

For \(K_D\), there are 15 vertices, 45 edges, and 15 triangles. Every edge of \(K_D\)—a two-edge matching in \(K_6\)—extends uniquely to a perfect matching, so every edge lies in exactly one triangle. Choose one edge from each triangle and perform the corresponding elementary collapse. The 15 chosen edges are distinct and free, so the result is a connected graph with 15 vertices and 30 edges. Hence
\[
K_D\simeq\bigvee^{16}S^1.
\]

For \(K_S\), each syntheme contains three duads and each duad lies in exactly three synthemes, so the 1-skeleton is 6-regular on 15 vertices and has 45 edges. Its triangles are exactly the 15 triples of synthemes containing a fixed duad. To see this, suppose three synthemes are pairwise adjacent but their three shared duads were distinct. Each syntheme would contain two of those duads, forcing the three duads to be pairwise disjoint; they would themselves form a syntheme, forcing all three synthemes to be equal, a contradiction. Hence every edge again lies in exactly one triangle. There is no clique of four synthemes: if four were pairwise adjacent, any three would share one duad, and the uniqueness of the shared duad for a fixed pair would force all four to contain that same duad, impossible because a duad belongs to exactly three synthemes. Thus \(K_S\) has no simplices above dimension \(2\). Collapsing one free edge in each triangle leaves a connected graph with 15 vertices and 30 edges, so
\[
K_S\simeq\bigvee^{16}S^1.
\]
Connectivity can be checked directly: if two perfect matchings share no duad, choose a duad in the first; exactly one duad of the second is disjoint from it, and those two extend to a perfect matching adjacent to both.

Finally, for connected based finite CW complexes, \(X*Y\simeq\Sigma(X\wedge Y)\). Therefore
\[
K_D*K_S\simeq
\Sigma\!\left(\left(\bigvee^{16}S^1\right)\wedge\left(\bigvee^{16}S^1\right)\right)
\simeq\bigvee^{256}S^3.
\]
This proves the claim.

## Verification
The bundled `verify.py` uses only the Python standard library. It constructs all 15 duads and 15 synthemes, rebuilds the 30-vertex incidence graph, and checks every pairwise distance. It then independently reconstructs both join factors and verifies that each has face vector \((15,45,15)\), with every edge in exactly one triangle and a connected 1-skeleton.

As an algebraic cross-check, it enumerates every simplex of the full threshold-3 Rips complex. The face vector is
\[
(30,315,1380,2475,1350,225),
\]
and exact row reduction over \(\mathbb F_2\) gives Betti vector
\[
(1,0,0,256,0,0).
\]
The finite computation is a cross-check; the homotopy conclusion itself comes from the explicit join decomposition and elementary collapses above.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine Vietoris–Rips complexes of Platonic-solid vertex sets and explicitly identify spherical buildings as a natural direction for extension. Their paper does not treat the Tutte–Coxeter graph or generalized-quadrangle incidence graphs.

McCabe later uses incidence graphs of generalized polygons, including generalized quadrangles, to prove lower bounds for approximating Vietoris–Rips filtrations. His girth-stability lemma states that the graph and its \(j\)-th power have homotopy-equivalent clique complexes when the girth is at least \(3j+1\). For the order-\((2,2)\) generalized quadrangle, whose incidence graph has girth \(8\), this controls \(j=2\) but not \(j=3\). The present computation therefore identifies the first scale beyond that stability range and gives its exact homotopy type.

Exact-name, alias, object-model, parameter, and implication searches under “Tutte–Coxeter”, “Tutte 8-cage”, “Cremona–Richmond”, “GQ(2,2)”, and the duad–syntheme model did not locate a published statement implying the displayed \(256\)-sphere wedge.

## Limitations
The theorem is specific to the Tutte–Coxeter graph and the interval \(3\le r<4\); no uniform formula for all generalized quadrangles is claimed. The originality assessment is based on the checked literature and indexed searches and cannot exclude inaccessible or poorly indexed prior work. The standard join identity is used after the two explicit elementary-collapse arguments; the verifier checks the concrete finite complexes but is not a substitute for that topological argument.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris-Rips complexes of Platonic solids*, arXiv:2302.14388, first posted 2023-02-28.
2. K. McCabe, *Lower Bounds for Approximating the Vietoris-Rips Filtration*, arXiv:2607.06524, first posted 2026-07-07.
