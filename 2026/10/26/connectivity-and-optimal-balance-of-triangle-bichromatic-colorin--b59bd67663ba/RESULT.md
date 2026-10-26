# Connectivity and optimal balance of triangle-bichromatic colorings at degeneracy two

## Finding

Let \(G\) be any finite simple \(2\)-degenerate graph. Give each vertex one of two named colors, red or blue, subject only to the condition that no triangle is monochromatic. Define the **reconfiguration graph** \(\mathcal R(G)\) to have one vertex for each valid coloring, with two such vertices adjacent exactly when they differ at one graph vertex.

**Theorem.** The reconfiguration graph \(\mathcal R(G)\) is nonempty and connected. In particular, if \(n=|V(G)|\), a valid coloring always exists with \(\lfloor n/2\rfloor\) red and \(\lceil n/2\rceil\) blue vertices (or vice versa). Its minimum color-class discrepancy is exactly \(n\bmod 2\), the parity lower bound.

Both assertions are sharp with respect to degeneracy. For every integer \(m\ge1\), the \(3\)-degenerate graph \(A_m=K_3\vee\overline{K_m}\) has precisely six valid two-colorings, all isolated in \(\mathcal R(A_m)\). Every such coloring has class sizes \(2\) and \(m+1\), and therefore minimum discrepancy \(m-1\); the balanced conclusion fails for \(m\ge3\).

A complementary exact finite-state classification is available for the triangle-book graph \(B_m=K_2\vee\overline{K_m}\), which is \(2\)-degenerate. Its reconfiguration graph comprises two \(m\)-dimensional hypercubes, joined by two distinct length-two paths: one joins their all-red-leaf corners and the other their all-blue-leaf corners. Consequently its number of states and diameter are, exactly,
\[
|V(\mathcal R(B_m))|=2^{m+1}+2,
\qquad
\operatorname{diam}\mathcal R(B_m)=m+2.
\]
The exact generating polynomial of its valid colorings by the number of red vertices is
\[
P_{B_m}(z)=2z(1+z)^m+z^2+z^m.
\]

## Assumptions and scope

Graphs are finite, undirected, simple, and may be disconnected or empty. A graph is \(2\)-degenerate when **every nonempty induced subgraph** contains a vertex of degree at most two. A triangle means three pairwise adjacent distinct vertices; triangles need not be faces of an embedding. Every vertex is colored exactly once with one of two named colors. A valid coloring makes each triangle meet both color classes; this is also called a no-monochromatic-triangle coloring or a Property-B coloring of the triangle hypergraph. A legal reconfiguration step changes one vertex's color and retains validity. The discrepancy is the absolute difference between the two color-class sizes.

The join \(H\vee J\) connects every vertex of \(H\) to every vertex of \(J\). The graph \(\overline{K_m}\) consists of \(m\) pairwise nonadjacent vertices. All family statements range over **every** integer \(m\ge1\); the connectivity statement ranges over **every** finite simple \(2\)-degenerate graph, without a size bound.

## Proof

**1. Fiber lemma and connectivity.** Proceed by induction on \(n=|V(G)|\). For \(n=0\), the sole empty coloring is valid. For \(n>0\), degeneracy supplies \(v\in V(G)\) of degree at most two. Put \(H=G-v\). Every triangle of \(G\) containing \(v\) must use both its neighbors, and those neighbors must be adjacent. Thus \(v\) belongs to **at most one triangle**, \(\{v,u,w\}\).

Fix a valid coloring \(c\) of \(H\), and let \(F_c\subseteq\{\mathrm{red},\mathrm{blue}\}\) be the colors admissible at \(v\). When \(v\) is in no triangle, \(F_c\) has both colors. Otherwise, if \(c(u)\ne c(w)\), both choices are admissible; if \(c(u)=c(w)\), exactly the opposite color is admissible. In all cases \(F_c\ne\varnothing\), and its one- or two-vertex flip graph is connected.

Moreover, whenever \(c,c'\) are adjacent in \(\mathcal R(H)\), their fibers intersect. If they were disjoint, the only possibility would be two opposite singletons: one base coloring would have \(c(u)=c(w)=\mathrm{red}\), the other \(c'(u)=c'(w)=\mathrm{blue}\), or the reverse. Changing both neighbor colors, however, requires **two** base-vertex changes, contrary to adjacency. Therefore \(F_c\cap F_{c'}\ne\varnothing\).

By induction \(\mathcal R(H)\) is nonempty and connected. Each coloring of \(H\) has at least one extension over \(v\). Given a base path \(c_0,c_1,\ldots,c_s\) in \(\mathcal R(H)\), choose for each base edge a common permissible color for \(v\); within each connected fiber, move to that permissible color if necessary, then perform the corresponding base-vertex flip while keeping \(v\) fixed. This lifts the base path and connects any two extended colorings. Hence \(\mathcal R(G)\) is nonempty and connected, completing induction.

**2. Optimal balance.** Swapping red and blue globally preserves the no-monochromatic-triangle condition. Therefore, for any valid coloring \(c\), its complementary coloring \(\bar c\) is also valid. By connectedness there is a legal single-vertex path from \(c\) to \(\bar c\). If the first coloring has \(r\) red vertices, their red counts at the endpoints are \(r\) and \(n-r\), while each reconfiguration move changes this count by exactly one. The discrete intermediate-value property guarantees that the path contains a state with \(\lfloor n/2\rfloor\) red vertices, and one with \(\lceil n/2\rceil\). Thus the minimum discrepancy is \(0\) when \(n\) is even and \(1\) when \(n\) is odd. No integer bipartition can achieve a smaller absolute difference.

**3. A sharp degeneracy-three obstruction.** In \(A_m=K_3\vee\overline{K_m}\), the three vertices of the central triangle cannot all have the same color. Suppose they have two red vertices and one blue vertex. Each independent vertex is adjacent to the two red vertices, so must be blue to avoid a monochromatic triangle. Conversely this forced assignment is valid, since any triangle has two central vertices and at most one independent vertex. There are three ways to choose the singleton blue central vertex and two ways to assign the named colors, so there are exactly six valid colorings. No independent vertex can flip (it would form a monochromatic triangle with the red central pair), the singleton central vertex cannot flip (the central triangle would become monochromatic), and a paired central vertex cannot flip (it would form a monochromatic triangle with another blue central/independent pair). Hence all six reconfiguration states are isolated. Their class sizes are \(2\) and \(m+1\). The graph has degeneracy exactly \(3\): deleting its independent vertices leaves a triangle, every independent vertex has degree three, and a central triangle plus any independent vertex induces \(K_4\).

**4. Complete book-graph census.** Let the two adjacent hubs of \(B_m\) be \(u,v\). If the hub colors differ, the \(m\) independent leaf colors may be chosen arbitrarily. Each of the two hub orientations therefore yields the \(m\)-cube of all leaf-color assignments. If the hubs are both red, every leaf must be blue; if both are blue, every leaf must be red. These are the only two additional states. The all-blue-leaf equal-red-hub state is adjacent to the all-blue-leaf corner in each hub-orientation cube, giving one length-two inter-cube path, and similarly for the all-red-leaf state. No other inter-cube edges exist, proving the complete claimed graph structure and state count.

Within one cube the distance is the Hamming distance, at most \(m\). An inter-cube path can traverse either two-edge connection; reaching the corresponding all-one corner costs the number of opposite leaf bits, and the alternative connection costs the complementary number. Thus inter-cube distances are at most \(m+2\). A connector state lies at distance at most \(m+1\) from any cube vertex, and its distance from the other connector is exactly \(m+2\), since changing all \(m\) leaves and both hub colors is necessary, and a path attaining that bound exists through either cube. Therefore the diameter is exactly \(m+2\). Counting red vertices in the two cubes gives \(2z(1+z)^m\); the two connectors contribute \(z^2\) and \(z^m\). These terms sum to the displayed polynomial, including multiplicities when degrees coincide.

## Verification

The standalone exact-integer program `verify.py` independently enumerates all labelled simple graphs on at most six vertices (\(33{,}868\) graphs) and filters by the defining degeneracy test. For all \(26{,}342\) qualifying graphs it independently computes the triangles, all valid named two-colorings, every permitted one-vertex flip, reachability, and the exact minimum discrepancy. It also directly builds the book and degeneracy-three examples: books for \(1\le m\le8\), with full all-pairs graph distances and coefficient counts, and obstructions for \(1\le m\le9\), checking that all six configurations are isolated. It completes with:

`VERIFY_OK labelled_graphs=33868 2_degenerate_graphs=26342 books=8 book_states=1036 rigid_examples=9`

Run using Python 3, standard library only, with `python verify.py`. The finite experiment corroborates but does not substitute for the four infinite proofs above; the proof applies to all allowed parameters.

## Relationship to prior work

Arevalo Loyola, Biniaz, Bose and Shermer (2026), **Polychromatic 2-colorings with Bounded Discrepancy for Triangulations**, establish general discrepancy bounds for triangulations. The present statement is deliberately different: it gives the **parity-optimal** discrepancy for all \(2\)-degenerate graphs and proves **connectivity of every legal single-vertex recoloring state**. In particular, every maximal outerplanar graph admits a perfectly balanced (up to parity) polychromatic two-coloring of its triangular faces; no outerplanarity or embedding is required for the stronger theorem.

Karpiński and Piecuch (2017, 2021) study two-coloring without monochromatic triangles, including algorithms establishing existence for outerplanar and planar graph classes. Asayama and Matsumoto (2022) already prove balanced polychromatic two-colorability for three-colorable triangulations. **The balance conclusion alone is not claimed as new:** indeed, any properly three-colorable graph admits a balanced two-coloring without monochromatic triangles, simply by coloring two of the three independent proper color classes in opposite colors and allocating members of the third class to meet the target size. In particular, the new assertion is the much stronger **connectedness of the entire legal recoloring space** on every two-degenerate graph, together with the sharp degenerate obstruction and the exact book-state classification. Existence or a balanced output alone cannot imply connectedness of all valid states. Proper-coloring reconfiguration and equitable **proper** coloring use different feasibility constraints. The 2026 work on reconfiguration of triangulations under diagonal flips changes the triangulation rather than recoloring one vertex of a fixed graph.

The originality comparison was limited to the sources named below and research-record searches for equivalent formulations, single-vertex-flip connectivity, balanced Property-B coloring, degeneracy bounds, and the sharp book and apex examples. This is not a claim that every older equivalent theorem has been excluded.

## Limitations

The unconditional connectivity and optimal-balance theorem is limited to finite simple \(2\)-degenerate graphs. The six-isolated-state example demonstrates that both conclusions can fail at degeneracy three, but does not classify all \(3\)-degenerate graphs. The exact polynomial and diameter concern only the joined-edge book family. No universal mixing-time, shortest-path algorithm, or upper bound on the diameter for arbitrary \(2\)-degenerate graphs is claimed. The computational certificate covers only the stated finite ranges. Independent review and a complete historical-priority assessment remain outstanding.

## References

1. A. Arevalo Loyola, A. Biniaz, P. Bose, T. Shermer, *Polychromatic 2-Colorings with Bounded Discrepancy for Triangulations*, SWAT 2026, LIPIcs 370, paper 33, DOI:10.4230/LIPIcs.SWAT.2026.33 (public 2026-06-08). https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SWAT.2026.33
2. A. Arevalo Loyola et al., same title, arXiv:2609.31574v1 (posted 2026-09-25; a later public version). https://arxiv.org/html/2609.31574v1
3. M. Karpiński, K. Piecuch, *On vertex coloring without monochromatic triangles*, arXiv:1710.07132 (2017). https://arxiv.org/abs/1710.07132
4. M. Karpiński, K. Piecuch, *Linear-time algorithm for vertex 2-coloring without monochromatic triangles on planar graphs*, arXiv:2110.04606 (2021). https://arxiv.org/html/2110.04606
5. Y. Asayama, N. Matsumoto, *Balanced Polychromatic 2-Coloring of Triangulations*, Graphs and Combinatorics 38, article 16 (2022), DOI:10.1007/s00373-021-02420-8. The abstract explicitly states balanced coloring for three-colorable triangulations. https://doi.org/10.1007/s00373-021-02420-8
6. V. Bartier, N. Bousquet, M. Heinrich, *Recoloring graphs of treewidth 2*, arXiv:2012.11459 (2020). https://arxiv.org/abs/2012.11459 (proper-coloring reconfiguration, a different notion).
7. D. W. Cranston, R. Mahmoud, *Equitably Coloring Planar and Outerplanar Graphs*, arXiv:2509.16123 (2025). https://arxiv.org/abs/2509.16123 (equitable proper coloring, a different constraint).
