# Vertex-degree distribution and connected simple stratum of complete-split graphical zonotopes

## Finding
Let \(r\ge2\) and \(s\ge1\) be integers, and let \(G_{r,s}=K_r\vee\overline{K_s}\), the join of a clique of \(r\) labeled vertices with an independent set of \(s\) labeled vertices. Write \(Z_{r,s}\) for its graphical zonotope in the standard edge-vector realization. Its one-skeleton has \(r!(r+1)^s\) vertices and dimension \(r+s-1\). If \(d(v)\) is the one-skeleton degree of vertex \(v\), its complete degree polynomial is
\[
D_{r,s}(z)=\sum_{v\in V(Z_{r,s})}z^{d(v)}=r!s!\,[x^s]e^{2xz}\bigl(z+e^{xz^2}-1\bigr)^{r-1}.
\]
Consequently, the number of *simple* vertices (those with degree equal to dimension) is
\[
S(r,s)=r!\sum_{j=0}^{\min(r-1,s)}\binom{r-1}{j}\frac{s!}{(s-j)!}\,2^{s-j}.
\]
The subgraph induced by **all** simple vertices is connected for every \(r\ge2,s\ge1\). If \(s\ge2\), the degree support is the full integer interval \([r+s-1,r+2s-2]\), with exactly \(r!(r-1)\) vertices of the maximum degree; if \(s=1\), every vertex is simple and has degree \(r\).

## Assumptions and scope
The join has every clique edge and every clique-independent edge, but no independent-independent edges. Orientations are acyclic and two zonotope vertices are adjacent precisely when their acyclic orientations differ by reversal of one edge that preserves acyclicity, equivalently a cover relation in their associated reachability posets. The term *simple vertex* refers to polytope incidence degree \(\dim Z_{r,s}=r+s-1\), not to a globally simple polytope. All vertices and graph elements are labeled; no quotient by automorphisms is taken. Parameters are exactly the integers specified above.

## Proof
**Canonical gap encoding.** In every acyclic orientation, the induced orientation on the clique is a transitive tournament, giving a unique order \(u_1<\cdots<u_r\). Each independent vertex \(x\) has all its edges pointing from earlier clique vertices into \(x\), and from \(x\) to later clique vertices, with a unique cut index \(i\in\{0,\ldots,r\}\). Otherwise two clique vertices ordered as \(u_i<u_j\) would have \(u_j\to x\to u_i\), making a directed cycle. Conversely any order of the clique together with an assignment of each independent vertex to a gap gives an acyclic orientation. Thus there are \(r!(r+1)^s\) orientations.

Write \(c_i\) for the count in gap \(i\), \(\sum_{i=0}^r c_i=s\). Within an interior gap \(i\in\{1,\ldots,r-1\}\), each independent vertex contributes two cover arcs, to the preceding and following clique vertices. At an end gap it contributes one cover arc. The clique arc \(u_i\to u_{i+1}\) is a cover precisely when \(c_i=0\); all nonconsecutive clique arcs are transitively implied. Since these are *all* cover arcs, and exactly cover arcs are reversibly flippable, the degree is
\[
d(c)=c_0+c_r+2\sum_{i=1}^{r-1}c_i+\sum_{i=1}^{r-1}\mathbf1_{c_i=0}.
\]

**Degree enumerator and simplicity.** For each gap-count vector the label assignments have multiplicity \(s!/(c_0!\cdots c_r!)\), independent of the \(r!\) clique orders. End gaps have exponential generating function \(e^{xz}\), and interior gaps have \(z+e^{xz^2}-1\), giving the stated coefficient formula. Subtracting the dimension and using \(\sum c_i=s\),
\[
d(c)-(r+s-1)=\sum_{i=1}^{r-1}\max(c_i-1,0).
\]
This is zero precisely when every interior gap contains at most one independent vertex. Choose the \(j\) singly occupied interior gaps, inject \(j\) distinct labeled independent vertices into them, and place each remaining label in either end gap. This gives the stated \(S(r,s)\).

The excess is between zero and \(s-1\) when \(s\ge1\), with equality at the upper bound exactly when all \(s\) vertices lie in one interior gap, provided \(s\ge2\). For each \(h\in\{1,\ldots,s-1\}\), placing \(h+1\) vertices in one interior gap and the other \(s-h-1\) at an end gap realizes excess \(h\); placing all independent vertices in end gaps realizes excess zero. Thus the entire interval occurs and the maximum multiplicity is \(r!(r-1)\) for \(s\ge2\). If \(s=1\), all interior gap counts automatically satisfy the simplicity criterion.

**Connected induced subgraph of simple vertices.** A cover reversal between an independent vertex \(x\) and a neighboring clique vertex moves \(x\) by one gap to the left or right without changing the clique order; it is an edge of the zonotope one-skeleton. Starting from any simple orientation, repeatedly choose the leftmost occupied interior gap and move its unique occupant one gap left. The preceding interior gap is empty, and the destination may be the unrestricted left end gap; hence every intermediate orientation remains simple. Once all interior gaps are empty, move independent vertices from the right end gap one at a time into the rightmost interior gap and consecutively toward the left end, always through currently empty interior gaps. Again every intermediate orientation is simple. All independent vertices now lie in the left end gap. At this stage each clique adjacency \(u_i,u_{i+1}\) is a cover, and reversing it swaps the two consecutive clique labels while preserving all gap assignments and simplicity. Adjacent swaps connect all clique orders. Thus any simple orientation can reach a canonical orientation with every independent vertex in the left end gap and an arbitrarily fixed clique order, by a path entirely among simple vertices. Reversing these paths connects every pair of simple orientations.

## Verification
Two reproducible, algorithmically distinct checks accompany the result. `verify_direct.py` enumerates *all edge directions*, filters by acyclicity, computes every cover arc via reachability, and compares observed degree histograms against the gap formula for five small parameter pairs. `verify_simple.py` independently uses gap-state coordinates and the exact local move rules to check counts and connectivity of the simple-vertex locus for all \(2\le r\le5\), \(1\le s\le4\). Exact finite checks corroborate, but do not replace, the above proof for every integer parameter.

## Relationship to prior work
Grujić's *Counting faces of graphical zonotopes* (2016, arXiv:1604.06931), Theorem 1.1 and Examples 5.1–5.4, establishes the *global face polynomial* of an arbitrary graphical zonotope. It does not provide the vertex-by-vertex one-skeleton degree distribution or connectivity of the simple-vertex induced subgraph of the complete-split family. Postnikov, Reiner and Williams' *Faces of generalized permutohedra* (2006 preprint, arXiv:math/0609184), Section 5, characterizes when an entire graphical zonotope is a simple polytope; that criterion does not classify its individual simple vertices when it is not globally simple. The local degree formula uses known correspondence between acyclic orientations, cover edges, and zonotope vertices, and makes no claim of inventing these tools. The result is about the nonbipartite split family, not the complete-bipartite family. A possible unindexed equivalent account under graphic-arrangement chamber terminology remains an originality risk.

## Limitations
These results apply only to complete-split graphs \(K_r\vee\overline{K_s}\) and do not classify all split graphs or the diameter of the induced simple-vertex graph. The proof shows connectivity, not a shortest path formula. The novelty assessment is literature-based and not a proof that no equivalent unpublished or unindexed result exists. Independent external review has not been performed.

## References
1. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, first posted 2016-04-23; Theorem 1.1, Sections 2 and 5.
2. A. Postnikov, V. Reiner and L. Williams, *Faces of generalized permutohedra*, arXiv:math/0609184, first posted 2006-09-06; Section 5, Proposition 5.2.
3. R. P. Stanley, *Acyclic orientations of graphs*, Discrete Mathematics **5** (1973), 171–178.
