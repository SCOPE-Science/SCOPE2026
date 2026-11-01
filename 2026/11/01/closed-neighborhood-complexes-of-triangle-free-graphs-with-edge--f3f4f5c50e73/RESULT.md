# Closed-neighborhood complexes of triangle-free graphs with edge-disjoint squares

## Finding

Let \(G\) be a finite connected simple graph with no triangles. Suppose distinct simple four-cycles of \(G\) share no edge. Write \(v=|V(G)|\), \(e=|E(G)|\), and \(s=|C_4(G)|\), counting unoriented cycles on four distinct vertices. Let the **closed-neighborhood complex** be
\[
\mathcal N[G]=\{\sigma\subseteq V(G):\text{some }z\in V(G)\text{ satisfies }\sigma\subseteq N_G[z]\}.
\]
The empty face is included by convention.

**Theorem.** There is a finite explicit sequence of elementary simplicial collapses
\[
\mathcal N[G]\searrow K(G),\qquad K(G)=G\cup\bigcup_{Q\in C_4(G)}\partial\Delta^3_Q,
\]
where \(\partial\Delta^3_Q\) is the four-triangle boundary of a tetrahedron on the four vertices of \(Q\), and \(G\) is viewed as a one-dimensional simplicial complex. Furthermore,
\[
|\mathcal N[G]|\simeq\bigvee^{e-v+1-s}S^1\vee\bigvee^{s}S^2.
\]
A zero-fold wedge contributes no summand. The one-vertex graph gives a point. The vertex inclusion \(G\hookrightarrow\mathcal N[G]\) induces a surjection in integral first homology whose kernel is the free primitive sublattice with basis the oriented boundaries of the four-cycles. Hence the only possibly nonzero reduced integral homology groups are
\[
\widetilde H_1(\mathcal N[G];\mathbb Z)\cong\mathbb Z^{e-v+1-s},\qquad
\widetilde H_2(\mathcal N[G];\mathbb Z)\cong\mathbb Z^{s}.
\]

## Assumptions and scope

Graphs are finite, nonempty, undirected and simple. A four-cycle means a simple (not necessarily induced) cycle on four vertices. The hypothesis is **edge-disjointness of all distinct four-cycles**, not merely of a selected family. In a triangle-free graph every four-cycle is induced. No bound on vertex degree or number of longer cycles is imposed. The complex uses vertex-centered, closed graph-neighborhood sets \(N_G[z]=\{z\}\cup N_G(z)\); it is not the Lovász open-neighborhood complex. The exact simplicial-collapse statement is stronger than the subsequent homotopy classification.

## Proof

**Step 1: matching structure at each vertex.** Fix \(z\in V(G)\). Form a graph \(D_z\) on the neighbors of \(z\), joining two neighbors \(a,b\) exactly when they have a common neighbor distinct from \(z\). In a triangle-free graph, such a pair and the two common neighbors give a four-cycle \(z-a-w-b-z\). Conversely every four-cycle through \(z\) determines an edge \(\{a,b\}\) of \(D_z\). Since two distinct four-cycles sharing a neighbor-edge of \(z\) would share an edge of \(G\), the graph \(D_z\) is a **matching** (plus isolated vertices).

**Step 2: enumerate free faces.** For each \(z\), and for each subset \(F\subseteq N_G(z)\) of size at least two that is **not** an edge of \(D_z\), pair the faces \(F\) and \(F\cup\{z\}\). Process these pairs in decreasing order of \(|F|\) for each \(z\), and process the centers in any order. The order within any cardinality is irrelevant.

To show that every pair is a legal elementary collapse, observe that \(F\), being of size at least two and not an edge of the matching \(D_z\), contains neighbors \(a,b\) without another common neighbor. Triangle-freeness ensures \(a\) and \(b\) are nonadjacent. Hence a closed neighborhood containing \(F\) must be centered at a common neighbor of \(a,b\), which is **uniquely** \(z\): neither \(a\) nor \(b\) can serve as a center because they are nonadjacent. Thus every coface of \(F\) lies in the simplex on \(N_G[z]\). All cofaces of \(F\) other than \(F\cup\{z\}\) are removed earlier: those with additional neighbors are removed at higher \(|F|\), either as the lower or upper face of their own pair. Therefore at this step \(F\) has unique coface \(F\cup\{z\}\), which is maximal, and the removal is an elementary simplicial collapse. The unique-center argument also prevents collisions between different choices of \(z\).

After the indicated collapses, the surviving faces in each neighborhood simplex consist exactly of the center, its neighbor vertices and edges, and the triangles \(\{z,a,b\}\) with \(\{a,b\}\in E(D_z)\). For each four-cycle \(z-a-w-b-z\), these triangles supply the four boundary triangles of the tetrahedron on \(\{z,a,w,b\}\), together with all their edges. Conversely no other triangles remain. Thus the residual complex is precisely \(K(G)\), proving the displayed collapse.

**Step 3: two disks per square.** For each four-cycle with cyclic vertices \(z,a,w,b\), its tetrahedron boundary splits into two triangulated disks spanning its square loop: the disk made of triangles \(\{z,a,b\}\) and \(\{w,a,b\}\) along diagonal \(\{a,b\}\), and the complementary disk with triangles \(\{a,z,w\}\) and \(\{b,z,w\}\) along diagonal \(\{z,w\}\). First attach one disk for every square to the graph \(G\). Because the square loops are edge-disjoint, one boundary edge of each disk is not used in any other first disk. Each first disk can be collapsed across that boundary edge, then across its internal diagonal, leaving a connected graph \(G'\) with the same vertices and exactly \(e-s\) edges. In particular \(\beta_1(G')=e-v+1-s\), and this number is nonnegative.

Now attach the remaining disk of each tetrahedral boundary. Its boundary is the same four-edge loop, which already bounds the first disk and is therefore nullhomotopic in the intermediate complex. Attaching \(s\) two-cells along nullhomotopic loops produces the wedge of \(s\) two-spheres with the intermediate graph, giving the homotopy formula. The first disks impose exactly the four-cycle relations on \(H_1(G;\mathbb Z)\); the unique original edge in each square makes these relations primitive and independent. The remaining disks create the \(s\) independent two-sphere classes. This proves the integral homology and inclusion statements. \(\square\)

## Verification

The included standalone `checker.py` reconstructs the closed-neighborhood simplices and the proposed tetrahedron-boundary core independently. It checks every prescribed elementary pair as a genuine free-face/maximal-coface deletion and recomputes mod-two Betti numbers by boundary-matrix elimination. The executed test suite covered 3,430 qualifying graphs (including all connected labeled triangle-free graphs with pairwise edge-disjoint squares on at most six vertices), 95,179 input nonempty faces, 23,172 legal collapse pairs, and 1,430 total square instances; every comparison passed. These finite tests are not a proof of the unbounded theorem; the complete argument is the free-face and disk-attachment proof above. Execute `python checker.py` with standard Python 3.

## Relationship to prior work

Matsushita's *Closed neighborhood complexes of graphs* (arXiv:2511.12608; first public November 16, 2025) defines this vertex-centered closed-neighborhood complex and proves general relationships with graph fundamental groups, categorical products and Alexander duality. Its relevant definitions, results, examples and proof sections do not state the sparse-square collapse or its two-dimensional integral homotopy decomposition. In particular, a determination of the fundamental group does not determine the two-sphere summands or a simplicial collapse.

The known *Graph-like neighborhood complexes with edge-disjoint four-cycles* considers the **open Lovász** neighborhood complex; its circle-wedge calculation does not classify the closed complex. The known high-girth **prism** graph Čech classification concerns product graphs with interacting four-cycles, not the edge-disjoint-square class except in trivial intersections. Adams–Shukla–Singh's *Čech complexes of hypercube graphs* (arXiv:2212.05871) treats hypercubes, whose many squares share edges, and uses geometric-graph balls rather than solely vertex-neighborhood sets. No direct covering implication was established from those results.

## Limitations

The theorem applies only to triangle-free graphs with **all** distinct squares pairwise edge-disjoint. It does not classify square grids, hypercubes or other graphs with intersecting squares; nor does it describe automorphism representations, higher-radius nerves, integral chain-level persistence beyond the stated inclusion, or metric geometric-ball Čech variants. The literature comparison cannot rule out equivalent unindexed work. Independent mathematical validation has not been performed.

## References

1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first public 2025-11-16, https://arxiv.org/abs/2511.12608.
2. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public 2022-12-12, https://arxiv.org/abs/2212.05871.
3. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, existing research result concerning the **open** neighborhood construction (distinct from the present closed construction).
4. *A high-girth prism Čech collapse and its integral symmetry modules*, existing research result for prism graph Čech nerves (different graph class).
