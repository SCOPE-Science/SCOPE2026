# A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs

## Finding

**Theorem.** For every finite connected simple bipartite graph \(G=(V,E)\) with \(n=|V|\ge1\) and \(m=|E|\), let
\[K=I_3(G)=\{S\subseteq V:\alpha(G[S])\le2\},\quad b=m-n+1,\]
and write \(c_4(G)\) for the number of distinct unoriented simple four-cycles. Then
\[\boxed{|K|\simeq\bigvee^{\binom{b+1}{2}-c_4(G)}S^3.}\]
A wedge of zero spheres is interpreted as a point. In particular, \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{\binom{b+1}{2}-c_4(G)}\), every other reduced integral homology group is zero, and \(\pi_1(|K|)=0\). The theorem implies \(c_4(G)\le\binom{b+1}{2}\).

The claim determines **homotopy types**, not just Euler characteristics, and holds without degree, planarity, girth, or square-attachment restrictions. For an even cycle of length at least six, \(b=1\) and \(c_4=0\), giving \(S^3\); for \(K_{3,3}\), \(b=4\) and \(c_4=9\), again giving \(S^3\). For the cube, \(b=5\) and \(c_4=6\), giving nine three-spheres. For any tree the complex is contractible.

## Assumptions and scope

Graphs are finite, simple, undirected, connected, and bipartite, including the one-vertex graph. Independent sets are vertex sets containing no graph edge. The complex includes the empty simplex; geometric realization is the ordinary finite CW realization. Count an unoriented four-cycle only once, regardless of starting point and direction. Each bipartite four-vertex set carrying two perfect matchings is one and only one simple four-cycle. The graph \(K_{1}\) is a trivial base case; remaining arguments assume \(n\ge2\). No statement is made for nonbipartite graphs or for robust parameter greater than three.

## Proof

**1. Dimension and two-skeleton.** Fix bipartition \(V=A\sqcup B\). Any five vertices contain at least three vertices of one part, which are independent. Thus \(\dim K\le3\). Every pair of vertices is a face. A triple is a face exactly when it contains a graph edge, since a three-element independent set is the only prohibited triple. A four-element face has exactly two vertices in each part and has independence number at most two if and only if it supports a matching of size two, by the bipartite matching/vertex-cover theorem; equivalently two disjoint graph edges among its four vertices.

**2. Simple connectivity.** In the complete one-skeleton of \(K\), let \(x,y\) be any two vertices and choose an ordinary graph path \(x=v_0,v_1,\ldots,v_t=y\). For each successive path edge \(v_i v_{i+1}\), the triple \(\{x,v_i,v_{i+1}\}\) is a face whenever its vertices are distinct. The fan of these triangles gives a homotopy relative endpoints from the simplicial edge \(xy\) to the path. Each graph loop \(v_0,v_1,\ldots,v_t=v_0\) is similarly filled by triangles \(\{v_0,v_i,v_{i+1}\}\) containing graph edges. Therefore every edge loop in \(K\) contracts and \(\pi_1(|K|)=0\). This also handles the case of a graph consisting of one edge; the one-vertex case is immediate.

**3. Trees collapse.** Suppose \(H\) is a graph and \(H'\) adds a leaf \(t\) adjacent only to \(v\in V(H)\). For a simplex \(S\subseteq V(H)\), the face \(S\cup\{t\}\) is allowed exactly when \(S\setminus\{v\}\) is a clique in \(H-v\). Indeed \(t\) is nonadjacent to every other vertex, so any two independent vertices in \(S\setminus\{v\}\) would form an independent triple with \(t\); conversely that clique condition precludes such a triple and also prevents independent triples involving \(v\). Consequently
\[\operatorname{lk}_{I_3(H')}(t)=v*\operatorname{Cl}(H-v),\]
a cone. Hence \(t\) is a dominated vertex, and the usual elementary simplicial collapses delete its star without affecting \(I_3(H)\). Building a finite tree by leaves proves \(I_3(T)\) contractible for every tree, including \(K_1\).

**4. The integral edge-insertion lemma.** Let \(H\) be any connected spanning bipartite subgraph on \(V\), let \(a\in A,b\in B\) be nonadjacent in \(H\), and set \(H'=H+ab\). Put \(L=I_3(H)\subseteq L'=I_3(H')\) and
\[U=\{w\in V\setminus\{a,b\}:aw\notin E(H),\ bw\notin E(H)\}.\]
The newly admitted triangles are exactly \(\{a,b,u\}\) for \(u\in U\). By the two-disjoint-edge characterization, every newly admitted tetrahedron is \(\{a,b,x,y\}\), where \(xy\in E(H)\) avoids \(a,b\) and at least one of \(x,y\) lies in \(U\). To see the last criterion, the old graph already admitted this tetrahedron precisely when both alternative cross-edges \(ay\) and \(bx\) existed; since \(x,y\) lie in opposite bipartition classes, failure of that alternative is precisely \(x\in U\) or \(y\in U\). There are no new simplices in dimensions zero or one, nor above three.

Thus \(C_2(L',L;\mathbb Z)\) is the free group with basis \(U\). The relative boundary from new tetrahedra is, up to changing orientations of generators, the incidence map of the graph obtained from \(H-\{a,b\}\) by retaining exactly its edges incident with \(U\) and then treating vertices outside \(U\) as a zero/sink: for an edge \(xy\), its boundary is \(\pm(u_x-u_y)\) if both endpoints are in \(U\), and \(\pm u_x\) if just one endpoint is. The ordinary simplicial boundary formula gives these signs directly; triangles not containing both \(a,b\) disappear in relative chains.

Every component of the induced subgraph \(H[U]\) has an edge to \(V\setminus(U\cup\{a,b\})\). Otherwise it would be a component of the connected graph \(H\), because no vertex of \(U\) is adjacent to \(a\) or \(b\). A path within \(U\) leading to such a boundary edge expresses each basis vector \(u\) as an **integer** linear combination of these relative boundary columns (coefficients \(\pm1\)); therefore
\[\partial_3:C_3(L',L;\mathbb Z)\twoheadrightarrow C_2(L',L;\mathbb Z).\]
Hence \(H_2(L',L;\mathbb Z)=0\). The long exact sequence of \((L',L)\) gives the surjection \(H_2(L;\mathbb Z)\twoheadrightarrow H_2(L';\mathbb Z)\). Select a spanning tree \(T\subseteq G\) and add all remaining graph edges, preserving connectedness and the fixed bipartition. Starting with the collapsible complex \(I_3(T)\), the surjections prove \(H_2(K;\mathbb Z)=0\).

**5. Homotopy type.** The result is connected, simply connected, and has \(H_2(K;\mathbb Z)=0\). Hurewicz in degree two implies \(\pi_2(K)=0\), and Hurewicz in degree three gives \(\pi_3(K)\cong H_3(K;\mathbb Z)\). Since \(\dim K\le3\), the top integral homology \(H_3\) is a free abelian group. Choose maps of three-spheres representing a basis of \(H_3\). Their wedge induces an isomorphism on integral homology in all degrees; the homology version of Whitehead's theorem for simply connected CW complexes gives a homotopy equivalence \(\bigvee^{\operatorname{rank}H_3(K;\mathbb Z)}S^3\simeq K\). If the rank is zero, \(K\) is contractible by the same reasoning.

**6. Exact multiplicity.** Set \(d_v=\deg_G(v)\). The face counts are
\[f_0=n,\qquad f_1=\binom n2,\]
\[f_2=m(n-2)-\sum_{v\in V}\binom{d_v}{2},\]
\[f_3=\binom m2-\sum_{v\in V}\binom{d_v}{2}-c_4(G).\]
For \(f_2\), count graph edges together with third vertices; a triple with two graph edges is counted twice, and bipartite graphs have no triangles. For \(f_3\), count unordered pairs of disjoint graph edges; a four-vertex matching is counted twice instead of once precisely for a four-cycle. Substituting in \(\widetilde\chi(K)=-1+f_0-f_1+f_2-f_3\) gives
\[\widetilde\chi(K)=c_4(G)-\binom{m-n+2}{2}=c_4(G)-\binom{b+1}{2}.\]
Since reduced homology is free and occurs only in degree three, \(\widetilde\chi(K)=-\operatorname{rank}H_3(K;\mathbb Z)\), proving the displayed theorem. \(\square\)

## Verification

The standalone `verify.py` independently constructs all simplices through dimension three using the graph-edge characterization, computes signed boundary matrices modulo both \(2\) and \(3\), and checks vanishing of the first two reduced homology groups and the exact predicted top rank. It exhaustively tests all connected labeled bipartite graphs with part sizes \((1,1)\), \((2,2)\), \((2,3)\), \((3,3)\), and additionally tests even cycles, bicliques, the cube, a fourteen-vertex Fano-plane incidence graph and a joined-square graph: **240 connected graph instances**. It separately checks the surjectivity of the new relative boundary in **639 connected bipartite edge-insertion instances** over both characteristics. Replaying the delivered code prints `VERIFY_OK 240 connected graphs and 639 edge insertions; mod 2/3 exact ranks`. The finite tests do not prove integral surjectivity or general homotopy equivalence; those are established in Steps 2–5.

## Relationship to prior work

Filakovský [1, Theorems 1.1–1.2] computes sphere wedges for rectangular grids and **square-sequence** bipartite graphs; its square-sequence assumption excludes connected bipartite graphs with no four-cycles, such as long even cycles. Thus [1] is a genuine special case, not the unrestricted theorem. Kim and Lew [2] call the same object \(I_3(G)\) and prove collapsibility-number bounds, including Theorem 1.8, but do not determine unrestricted bipartite homotopy types. Carnero Bravo [3] proves special graph-family homotopy calculations, including complete multipartite graphs, trees, and cycle powers, not the general graph result. Even an exact face-polynomial or equivariant Euler-character calculation would establish only alternating homological data and cannot imply simple connectivity, vanishing integral \(H_2\), or the homotopy conclusion. This theorem's new contribution is the integral edge-insertion/homotopy argument for *all connected bipartite graphs*; the Euler-count identity is not claimed as novel.

## Limitations

The claim requires bipartiteness and \(k=3\). It does not classify the higher robust clique complexes, arbitrary nonbipartite cases, equivariant homotopy types, actions on \(H_3\), or homotopy types of the Alexander-dual total-cut complexes without further hypotheses. Finite verification over two finite fields is not an integral or infinite proof. The literature review cannot exclude unindexed or inaccessible equivalent treatments. Independent mathematical audit has not been conducted.

## References

[1] Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11, Theorems 1.1–1.2 and §3; https://arxiv.org/abs/2602.11365.

[2] Minki Kim and Alan Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605 (2019), *Israel Journal of Mathematics* 249 (2022), 83–120, especially Theorems 1.5–1.8; https://arxiv.org/abs/1912.12605.

[3] Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, especially §§4–5; https://arxiv.org/abs/2602.21427.
