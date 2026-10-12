# Four mutual-visibility parameters of square-page book graphs
## Finding
For every integer \(r\ge2\), let \(B_r\) be the book graph formed from \(r\) copies of \(C_4\) sharing a common edge \(xy\), with page \(i\) equal to \(x a_i b_i y x\). Then
\[
\mu(B_r)=\mu_o(B_r)=\mu_d(B_r)=\mu_t(B_r)=2r.
\]
Moreover, for each of the four variants the unique maximum visibility set is
\[
I=\{a_i,b_i:1\le i\le r\},
\]
the set of all non-spine page vertices.

## Assumptions and scope
All graphs are finite, simple, and connected. For \(X\subseteq V(G)\), two vertices are \(X\)-visible if some shortest path between them has no internal vertex in \(X\). A mutual set requires this for pairs in \(X\); outer additionally requires mixed inside/outside pairs; dual additionally requires outside/outside pairs; total requires every pair.

## Proof
Let \(I=\{a_i,b_i:1\le i\le r\}\). It is total mutual-visible. Choose the edge itself for adjacent pairs, choose \(x-y-b_i\) for \(x,b_i\), \(y-x-a_i\) for \(y,a_i\), choose \(a_i-x-a_j\) and \(b_i-y-b_j\) for same-side pairs with distinct indices, and choose \(a_i-x-y-b_j\) for \(i\ne j\). Every internal vertex on these selected geodesics is a spine vertex and hence lies outside \(I\). Therefore all four parameters are at least \(2r\).

Let \(X\) be a mutual-visibility set. If \(x\in X\), then at most one of \(a_1,\ldots,a_r\) belongs to \(X\), because for distinct \(i,j\) the unique geodesic from \(a_i\) to \(a_j\) is \(a_i-x-a_j\). Symmetrically, if \(y\in X\), then at most one \(b_i\) belongs to \(X\).

If exactly one spine vertex is in \(X\), then \(|X|\le r+2\); if both are in \(X\), then \(|X|\le4\). Thus for \(r\ge3\), no spine-containing mutual set has size \(2r\), while a spine-free set has at most the \(2r\) internal vertices. Hence \(I\) is the unique maximum mutual set for \(r\ge3\).

For \(r=2\), a four-vertex set containing exactly one spine vertex must, up to symmetry, be \(\{x,a_k,b_1,b_2\}\). If \(j\ne k\), the three shortest \(a_k,b_j\)-paths are
\[
a_k-x-y-b_j,\qquad a_k-x-a_j-b_j,\qquad a_k-b_k-y-b_j,
\]
and each has an internal selected vertex. A four-vertex set containing both spine vertices has the form \(\{x,y,a_i,b_j\}\). If \(i=j\), both shortest \(x,b_i\)-paths are blocked internally by \(y\) or \(a_i\); if \(i\ne j\), every shortest \(a_i,b_j\)-path contains \(x\) or \(y\) internally. Hence no size-four mutual set contains a spine vertex, and \(I\) is unique also for \(r=2\).

Therefore \(\mu(B_r)=2r\) with unique maximum set \(I\). Every outer, dual, or total visibility set is in particular mutual-visible, while \(I\) is total-visible. Hence all four parameters equal \(2r\), and \(I\) is the unique maximum set for every variant.

## Verification
The included checker constructs \(B_r\), computes all-pairs distances and all shortest-path internal masks, and tests the four definitions directly. For every \(2\le r\le7\), it enumerates every vertex subset and verifies both the value \(2r\) and the common unique maximum set.

## Relationship to prior work
Mutual visibility was introduced in 2021. The 2023 paper introducing the total, outer, and dual variants used a closely related family built from \(C_5\) pages sharing one edge to exhibit strong separation among the parameters. A later correction reduced the dual value for that pentagonal-page family, but the profile remains separated. The square-page family behaves oppositely: all four parameters coincide and share one unique maximizer.

Targeted searches under book-graph, shared-edge-cycle, square-page, and generalized-theta terminology did not locate this formula or unique-maximizer statement.

## Limitations
The theorem covers square-page books only. It does not determine the four parameters for longer-cycle books or arbitrary generalized theta graphs. The finite computation is corroborative only.

## References
1. G. Di Stefano, “Mutual Visibility in Graphs,” arXiv:2105.02722v1, 6 May 2021; Applied Mathematics and Computation 419 (2022), 126850, DOI 10.1016/j.amc.2021.126850.
2. S. Cicerone, G. Di Stefano, S. Klavžar, “On the mutual visibility in Cartesian products and triangle-free graphs,” arXiv:2112.13024v1, 24 December 2021; Applied Mathematics and Computation 438 (2023), 127619, DOI 10.1016/j.amc.2022.127619.
3. S. Cicerone, G. Di Stefano, L. Drožđek, J. Hedžet, S. Klavžar, I. G. Yero, “Variety of mutual-visibility problems in graphs,” arXiv:2304.00864v1, 3 April 2023; Theoretical Computer Science 974 (2023), 114096, DOI 10.1016/j.tcs.2023.114096.
4. “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” Aequationes Mathematicae (2025), DOI 10.1007/s00010-025-01197-y.
