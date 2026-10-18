# Low-degree \(\Gamma\)-homology of finite simple graphs

## Finding
For every finite undirected simple graph \(G=(V,E)\) with no isolated vertices, let \(c(G)\) be its number of connected components and let \(|G|\) denote its ordinary one-dimensional CW realization. With the normalized integral \(\Gamma\)-cubical chains of Zaidi and Jamil [1],
\[
H_0^{\Gamma}(G;\mathbb Z)\cong\mathbb Z^{c(G)},\qquad
H_1^{\Gamma}(G;\mathbb Z)\cong H_1(|G|;\mathbb Z)\cong\mathbb Z^{|E|-|V|+c(G)},\qquad
H_2^{\Gamma}(G;\mathbb Z)=0.
\]
The first two identifications are natural under vertex maps taking an edge to an edge or collapsing its endpoints. The new structural conclusion is the integral degree-two vanishing for **every** graph, including graphs with triangles and squares. This is a low-degree theorem, not a claim about higher \(\Gamma\)-homology.

## Assumptions and scope
A graph is viewed as the \(2\)-uniform hypergraph whose hyperedges are its two-element edges. There are no loops, multiple edges, or isolated vertices; disconnected graphs are allowed.

For \(n\ge1\), the \(\Gamma\)-cube \(J_n^{\Gamma}\) has vertex set \(\{0,1\}^{n}\), and for each vertex \(a\) it has the hyperedge consisting of \(a\) and its \(n\) Hamming-distance-one neighbors. A singular \(n\)-cube is a hypergraph morphism \(\sigma:J_n^{\Gamma}\to G\): the image of every source hyperedge is contained in a target graph edge. For \(n=0\), a singular cube is a vertex supported by an edge. A cube independent of some coordinate is degenerate. The integral normalized chains \(C_n^{\Gamma}(G)\) are free on nondegenerate cubes, with
\[
\partial_n\sigma=\sum_{i=1}^{n}(-1)^i(A_i\sigma-B_i\sigma),
\]
where \(A_i\) and \(B_i\) insert \(0\) and \(1\), respectively, in coordinate \(i\). This fixes all sign conventions.

## Proof
**1. All singular squares live on one graph edge.** The four radius-one hyperedges of \(J_2^{\Gamma}\) are precisely the four three-element subsets of its four vertices. Were a singular square to have three distinct image vertices, some three source corners would map to these three vertices. Those three corners form a source hyperedge, whose image cannot fit in a two-element target edge. Therefore every square has at most two distinct values. A *nondegenerate* square must have two, which must be adjacent because a source triple contains both. Consequently, with \(e\) running over the undirected edges,
\[
C_2^{\Gamma}(G)=\bigoplus_{e\in E}C_2^{\Gamma}(e),\qquad
C_1^{\Gamma}(G)=\bigoplus_{e\in E}C_1^{\Gamma}(e),
\]
and \(\partial_2\) preserves the edge summands. The normalization causes no shared generators: nondegenerate cubes have a unique two-element image.

**2. A single edge has no positive-dimensional \(\Gamma\)-homology.** Write \(e=\{u,v\}\), fix \(u\), and use the full normalized \(\Gamma\)-chain complex of the one-edge hypergraph. Every vertex map from any \(J_n^{\Gamma}\) to \(e\) is a hypergraph morphism. For every singular cube \(\sigma\), form the cone cube
\[
T_n\sigma(x,0)=\sigma(x),\qquad T_n\sigma(x,1)=u.
\]
It is valid for all \(n\), and if \(\sigma\) is degenerate then \(T_n\sigma\) is degenerate. Put \(K_n=(-1)^{n+1}T_n\). Direct expansion of the normalized cubical boundary (the first \(n\) faces cancel, while the final pair is \(\sigma\) minus the constant cube) gives
\[
\partial_{n+1}K_n+K_{n-1}\partial_n=\mathrm{id}-c_u,
\]
where \(c_u\) sends degree-zero vertices to \(u\) and vanishes in positive normalized degrees. Hence \(H_k^{\Gamma}(e;\mathbb Z)=0\) for all \(k\ge1\). This is an **integral chain contraction**, not a rational-rank argument.

**3. Vanishing of the second group.** Let \(z\in C_2^{\Gamma}(G)\) have \(\partial_2z=0\). By Step 1 write \(z=\sum_{e\in E}z_e\) uniquely. Since \(\partial_2\) stays inside the direct sum \(C_1^{\Gamma}(e)\), each \(\partial_2z_e=0\). Step 2 supplies \(w_e\in C_3^{\Gamma}(e)\) such that \(\partial_3w_e=z_e\). Regard these edge-supported cubes as cubes in \(G\); then \(\partial_3(\sum_e w_e)=z\). Thus every integral two-cycle is a boundary, so \(H_2^{\Gamma}(G;\mathbb Z)=0\). The presence of additional three-cubes spanning several edges cannot invalidate this explicit bounding chain.

**4. First and zeroth groups.** For each edge \(e=\{a,b\}\), the group \(C_1^{\Gamma}(e)\) has two generators, the ordered arcs \((a,b)\) and \((b,a)\), whose one-boundaries are opposite. Hence every degree-two boundary supported on \(e\) lies in \(\mathbb Z((a,b)+(b,a))\). Conversely the square with ordered corner images \((a,b,a,a)\), in corner order \((0,0),(1,0),(0,1),(1,1)\), has boundary exactly \((a,b)+(b,a)\). Thus
\[
\mathrm{im}\,\partial_2=\bigoplus_{\{a,b\}\in E}\mathbb Z((a,b)+(b,a)).
\]
Quotienting the degree-one chain group by this image identifies \((b,a)=-(a,b)\), giving the ordinary integral oriented graph edge-chain group with its usual incidence boundary. The resulting degree-one homology is the graph cycle lattice and has rank \(|E|-|V|+c(G)\). Every vertex supports a degree-zero cube, and \(\partial_1\) is the graph incidence map, so \(H_0^{\Gamma}(G;\mathbb Z)=\mathbb Z^{c(G)}\). These identifications respect graph maps that may collapse edges.

## Verification
The proof is uniform over all finite simple graphs. A standalone standard-library Python checker in `verify.py` independently generates normalized cubes from the radius-one hyperedge rule, evaluates **signed** cubical boundaries, checks the integral cone-chain identity on every one-edge cube in dimensions zero through three, and calculates mod-two boundary ranks for seven finite graphs. It verifies the predicted low-degree Betti numbers and that all nondegenerate squares have a unique supporting graph edge. Reproduce with `python3 verify.py`.

The verifier corroborates but does not replace the universal chain-contraction proof. Its finite checks do not address higher-degree homology for arbitrary graphs.

## Relationship to prior work
Zaidi and Jamil [1, §3] introduce \(\Gamma\)-homology and calculate its first group for individual graphs and a chain-of-triangles family (their Proposition 3.10); that calculation provides part of the degree-one insight used here. The present theorem extends the low-degree graph comparison to every finite simple graph and adds a uniform **integral degree-two vanishing** statement, which is not stated by the source's examples or its excision results.

The earlier *discrete cubical homology of graphs* studied by Barcelo, Greene, Jarrah, and Welker [2, 3] uses graph maps from ordinary one-skeleton hypercubes, not morphisms from the \(\Gamma\)-hypercubes whose square hyperedges are three-element sets. Its higher homology can be nonzero, so its vanishing and comparison theorems do not imply the present claim. This distinction is essential: the proof here uses the **three-corner** constraint absent from ordinary cubical graph homology.

## Limitations
The graph must be simple, \(2\)-uniform, and without isolated vertices (the last condition ensures that degree-zero singular cubes include every graph vertex in the conventions of [1]). No computation of \(H_k^{\Gamma}\) for \(k\ge3\), no uniform-hypergraph extension, and no equivalence of entire chain complexes with ordinary graph chains is asserted. The literature comparison does not exclude unindexed equivalent work.

## References
[1] S. H. A. Zaidi and S. S. Jamil, *A cubical approach to homology theories for hypergraphs*, arXiv:2610.08196v1, first public 2026-10-06. https://arxiv.org/html/2610.08196v1

[2] H. Barcelo, C. Greene, A. S. Jarrah, and V. Welker, *Discrete cubical and path homologies of graphs*, Algebraic Combinatorics 2 (2019), 417–437. https://doi.org/10.5802/alco.49

[3] H. Barcelo, C. Greene, A. S. Jarrah, and V. Welker, *On the vanishing of discrete singular cubical homology for graphs*, SIAM Journal on Discrete Mathematics (2021). https://doi.org/10.1137/20M1338484
