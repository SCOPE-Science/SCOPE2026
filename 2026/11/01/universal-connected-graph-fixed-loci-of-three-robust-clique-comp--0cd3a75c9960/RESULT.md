# Universal connected graph fixed loci of three-robust clique complexes

## Finding

Let \(G=A\sqcup B\) be a finite connected simple bipartite graph with an involutive graph automorphism \(\sigma\) interchanging the color classes. Write its vertex orbits as \(O_i=\{a_i,b_i\}\), where \(a_i\in A\), \(b_i=\sigma(a_i)\in B\), for \(1\le i\le n\). Define the simple graph \(Q\) on \(\{1,\ldots,n\}\) by
\[
 ij\in E(Q)\quad\Longleftrightarrow\quad i\ne j\ \text{and}\ a_i b_j\in E(G),
\]
and put \(L=\{i:a_i b_i\in E(G)\}\). The graph \(Q\) is connected. Let \(Q^\sharp\) be the *one-dimensional graph* obtained from \(Q\) by adding all edges between distinct vertices of \(L\); in particular, triangles of \(Q^\sharp\) are **not** filled.

**Theorem (exact geometric fixed locus).** For the three-robust clique complex
\[
I_3(G)=\{S\subseteq V(G):\alpha(G[S])\le2\},
\]
there is a canonical piecewise-linear homeomorphism
\[
 \boxed{\ |I_3(G)|^{\langle\sigma\rangle}\ \cong_{\mathrm{PL}}\ |Q^\sharp|\ }.
\]
The homeomorphism sends graph vertex \(i\) to the midpoint of the edge joining \(a_i\) and \(b_i\) in the geometric realization. Consequently the fixed space is connected and has free fundamental group of rank
\[
\boxed{\ |E(Q)|+\binom{|L|}{2}-|E(Q[L])|-n+1\ },
\]
with torsion-free reduced integral homology only in degree one, of the same rank (or a contractible fixed space if the rank is zero).

**Universality within connected bipartite graphs.** Conversely, every finite connected nonempty simple graph \(H\) is realized *exactly*, up to the indicated PL identification, as such a fixed-point space. Given \(r\in V(H)\), take two sets \(V(H)\times\{+,-\}\), put an edge between \((u,+)\) and \((v,-)\) and between \((v,+)\) and \((u,-)\) for every edge \(uv\in E(H)\), and add the single bridge \((r,+)(r,-)\). The resulting simple bipartite graph \(G_H\) is connected, and sheet exchange is a color-reversing involution with
\[
\boxed{\ |I_3(G_H)|^{\mathbb Z/2}\ \cong_{\mathrm{PL}}\ |H|\ }.
\]
In all these realizations the ambient complex \(I_3(G_H)\) is simply connected. Thus an arbitrary connected graph, and an arbitrary finitely generated free fundamental group, can occur as a geometric involution fixed locus inside a simply connected three-robust clique complex.

## Assumptions and scope

All graphs are finite, simple, and undirected. Connected includes the one-vertex graph. The independence number \(\alpha(F)\) counts the largest vertex set spanning no edges in \(F\). The geometric fixed space means points fixed by the induced *linear* action on the ordinary geometric realization of the simplicial complex; it is not the simplicial complex of fixed original vertices, which is empty for this color-exchanging action. Graphs on the right-hand sides are taken as **one-dimensional CW/simplicial complexes**, never as clique or flag complexes. The notation \(Q[L]\) means the induced subgraph of \(Q\) on \(L\). The theorem requires the involution to interchange the two color classes and not merely preserve their union. No planarity, girth, or degree conditions are imposed.

## Proof

**1. Orbit-barycenter realization of fixed points.** Because \(\sigma(A)=B\) and \(\sigma(B)=A\), every vertex orbit consists of exactly two vertices \(O_i=\{a_i,b_i\}\). Consider any fixed point \(p\) of the geometric realization \(|I_3(G)|\). There is a unique simplex whose relative interior contains \(p\); as \(\sigma(p)=p\), that simplex is preserved setwise by \(\sigma\). Hence its vertex set is a disjoint union of full orbits \(O_i\). In its barycentric coordinates, the weights on \(a_i\) and \(b_i\) coincide for every present orbit. Thus its fixed subset is exactly the simplex spanned by the orbit midpoints \(m_i=(a_i+b_i)/2\). Conversely, a union of orbit-pair midpoints forms such a fixed simplex whenever the union of the original orbit vertices is a face of \(I_3(G)\). This gives an exact canonical triangulation of the geometric fixed locus by orbit midpoints, with no appeal to homological fixed-point theorems.

**2. The fixed triangulation is one-dimensional.** Every subset of three vertices in \(A\) or three in \(B\) is an independent triple of \(G\). Therefore a face of \(I_3(G)\) meets either bipartition class in at most two vertices. An invariant face containing \(k\) full vertex orbits contains exactly \(k\) vertices from each class; thus \(k\le2\). In particular, the orbit-barycenter fixed triangulation has vertices and edges only, even when its one-skeleton contains triangles.

**3. Exact edge criterion.** For distinct orbits \(i,j\), the four vertices \(a_i,b_i,a_j,b_j\) support a face of \(I_3(G)\) if and only if their induced bipartite graph has independence number at most two. König's matching–vertex-cover theorem and \(\alpha=|V|-\nu\) for bipartite graphs show that this is equivalent to a perfect matching of size two. Such a matching has precisely two possible pairings: the two diagonal edges \(a_i b_i\) and \(a_j b_j\), or the two off-diagonal edges \(a_i b_j\) and \(a_j b_i\). The latter exist together because \(\sigma\) is a graph automorphism. The diagonal pairing exists precisely when \(i,j\in L\); the off-diagonal pairing exists precisely when \(ij\in E(Q)\). Therefore orbit-midpoint edges are exactly those in \(E(Q)\cup\binom{L}{2}\). Steps 1–3 furnish the claimed PL homeomorphism to the one-dimensional \(Q^\sharp\).

**4. Connectivity and integral homotopy.** If \(Q\) were disconnected, no edge of \(G\) could connect orbit vertices belonging to distinct components of \(Q\), because edges inside a single orbit do not change orbit, and every cross-orbit edge is recorded in \(Q\). This contradicts connectedness of \(G\). Thus \(Q\) and \(Q^\sharp\) are connected. A connected graph with \(n\) vertices and \(e\) edges is homotopy equivalent to a wedge of \(e-n+1\) circles. Since \(Q^\sharp\) adds exactly \(\binom{|L|}{2}-|E(Q[L])|\) edges to \(Q\), the formula for fundamental group and reduced integral homology follows, including the rank-zero and \(n=1\) boundary cases.

**5. Universal realization.** Let \(H\) be any finite nonempty connected simple graph and fix \(r\in V(H)\). Build \(G_H\) exactly as in the theorem. It is a simple bipartite graph whose sheet-exchange involution interchanges its color classes. Every vertex \((u,\pm)\) can be joined to one of \((r,+)\) or \((r,-)\) by lifting a path in \(H\) from \(u\) to \(r\), alternating sheets at each step. The single edge \((r,+)(r,-)\) joins these two root vertices. Thus \(G_H\) is connected (also for \(H\) a single vertex). In the notation of the theorem its off-diagonal quotient graph is exactly \(H\), and its diagonal-edge set is the singleton \(\{r\}\). Therefore \(Q^\sharp=H\), proving the exact PL universality assertion.

**6. Simply connected ambient complex.** For any connected graph \(G\), the complex \(I_3(G)\) has a complete one-skeleton: no pair contains an independent triple. Every triangle of vertices containing at least one edge of \(G\) belongs to \(I_3(G)\). Fix \(x,y\in V(G)\) and a graph path \(x=v_0,\ldots,v_s=y\). The fan of triangles \(\{x,v_i,v_{i+1}\}\), ignoring degenerate terms, gives a relative-endpoint homotopy of the complete-one-skeleton edge \(xy\) to that path. Thus every edge loop in the complex can be replaced by a loop using only graph edges. Any graph-edge loop \(v_0,v_1,\ldots,v_t=v_0\) is filled by the analogous fan of triangles \(\{v_0,v_i,v_{i+1}\}\), each containing the graph edge \(v_iv_{i+1}\). Hence \(\pi_1(I_3(G))=0\). Apply this to the connected \(G_H\). \(\square\)

For illustration, take \(H=C_3\). Its rooted bipartite double cover has six vertices and seven edges. The geometric fixed locus is \(S^1\), although a direct enumeration of the ambient complex gives reduced mod-two Betti vector \((0,0,0,1)\). The conclusion of the theorem, however, is integral and PL, not merely this finite homology example.

## Verification

The standalone `verify.py` reconstructs the original bipartite graphs and enumerates invariant faces directly by searching for independent triples; it never uses the perfect-matching edge criterion to decide admissibility. It compares the resulting fixed-complex face sets with the proposed one-dimensional orbit graphs for **all 1,098 symmetric binary adjacency matrices of order at most four**, including diagonal edges and disconnected graphs for this local test. It also checks **all 772 labeled connected graphs on one through five vertices**, builds their rooted bipartite double covers with one diagonal bridge, independently verifies lift connectivity and equality of every fixed simplex with the original graph. For the triangle realization it calculates the ambient mod-two reduced Betti vector and complete face vector independently. Successful execution prints:

`VERIFY_OK symmetric_matrices=1098 connected_lifts=772 triangle_lift_fvector=[6, 15, 18, 9] reduced_mod2_betti=[0, 0, 0, 1]`

These finite tests do not prove universality for arbitrarily large graphs or integral/PL equivalence; Steps 1–6 above prove those statements directly.

## Relationship to prior work

Kim and Lew [1] introduce the complexes \(I_k(G)\) and investigate collapsibility bounds, not geometric automorphism fixed sets. Filakovský [2], first publicly available on February 11, 2026, establishes sphere-wedge homotopy for three-robust clique complexes on square-sequence bipartite graphs and grid graphs; the inspected complete paper does not identify color-exchange fixed loci or the universality construction. Carnero Bravo [3] studies total-cut duals and related homotopy calculations, including simple connectivity, but not the fixed-locus classification.

A broader existing connected-bipartite sphere-wedge theorem determines the *ambient* homotopy type; it cannot by itself recover the geometric fixed subspace, even when the latter has nontrivial fundamental group. A known general equivariant alternating-character formula gives Lefschetz numbers and Euler characteristics of quotients, not the exact PL graph structure of the fixed set. Previously examined graph-prism layer swaps produce complete one-skeleta in certain cases; these are special choices where every orbit has a diagonal edge, and neither cover arbitrary color-exchanging bipartite graphs nor realize a prescribed connected graph with a single diagonal bridge. The present theorem determines the fixed locus for every color-exchanging bipartite involution and proves exact graph universality, rather than asserting only Betti numbers or Euler characteristics.

## Limitations

The classification concerns the threshold-three robust clique complex and involutions that exchange the two bipartition classes. It does not classify color-preserving involutions, higher-order automorphisms, general \(k\)-robust complexes, or the full equivariant homotopy type. The universality statement realizes finite connected one-dimensional graph spaces, not arbitrary higher-dimensional complexes. Literature searches and source inspection cannot rule out unindexed equivalent formulations; no independent external mathematical audit has been performed.

## References

[1] Minki Kim and Alan Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, first posted 2019-12-29; https://arxiv.org/abs/1912.12605.

[2] Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11; https://arxiv.org/abs/2602.11365.

[3] Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, posted 2026; https://arxiv.org/abs/2602.21427.
