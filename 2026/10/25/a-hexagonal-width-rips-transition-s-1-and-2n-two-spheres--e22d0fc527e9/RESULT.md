# A hexagonal-width Rips transition: \(S^1\) and \(2n\) two-spheres

## Finding
For every integer \(n\ge7\), endow the vertex set of the Cartesian graph \(C_6\square C_n\) with its shortest-path distance and let \(X_n\) be its *inclusive* Vietoris–Rips complex at distance \(2\). Then
\[
X_n\simeq S^1\vee\bigvee^{2n}S^2.
\]
The nonempty face vector, from dimension zero to four, is
\[
(6n,36n,62n,36n,6n).
\]
There are \(53n\) explicit elementary simplicial collapses to a two-complex that admits an acyclic discrete-Morse matching with precisely one critical vertex, one critical edge, and \(2n\) critical triangles. Consequently \(H_1(X_n;\mathbb Z)\cong\mathbb Z\), \(H_2(X_n;\mathbb Z)\cong\mathbb Z^{2n}\), and all other reduced integral homology groups vanish.

## Assumptions and scope
Write the vertices as \((x,y)\in\mathbb Z/6\mathbb Z\times\mathbb Z/n\mathbb Z\). For cyclic shortest distances \(d_6,d_n\), a nonempty vertex set \(\sigma\) is a simplex exactly when every distinct pair of its vertices satisfies
\[
d_6(x,x')+d_n(y,y')\le2.
\]
All assertions quantify over integers \(n\ge7\). A face orbit means an orbit under simultaneous translation \(y\mapsto y+1\). The exact, finitely many translation-orbit templates used below are specified in `artifacts/certificate.json`; each vertex is encoded by an integer first coordinate and a longitudinal offset in \(\{-1,0,1,2\}\), interpreted modulo \(n\).

## Proof
**1. Uniform face classification.** The longitudinal projection of a simplex is a clique in the second power of \(C_n\). For every \(n\ge7\), any such clique lies in three consecutive cyclic columns. Indeed the maximal cliques of the second power are precisely the consecutive triples; its other faces are their subsets. On such a three-column interval all longitudinal distances of projected vertices are their integer differences. Hence every face and every codimension-one face/coface incidence has a translation template in the width-two infinite strip \(\mathbb Z/6\mathbb Z\times\mathbb Z\); these templates, and their incidence multiplicities, do not depend on \(n\ge7\). The complete face orbit census gives respectively \(6,36,62,36,6\) translation orbits of nonempty faces of cardinality \(1,2,3,4,5\). Translation acts freely on every simplex: a nonempty set contained in at most three consecutive columns cannot be fixed by a nontrivial longitudinal shift when \(n\ge7\). Multiplication by \(n\) proves the face vector.

**2. Simplicial collapses.** The accompanying certificate lists \(53\) ordered orbit pairs \((\sigma_i,\tau_i)\), where \(\sigma_i\) is a codimension-one face of \(\tau_i\). At the \(i\)-th stage, after deleting all translates of the earlier pairs, each translate of \(\sigma_i\) is contained in exactly one surviving coface, its corresponding translate of \(\tau_i\), and \(\tau_i\) is maximal. Thus all \(n\) pairs in the orbit can be removed sequentially as elementary collapses. The preceding locality classification reduces each freeness assertion for every \(n\ge7\) to the finite incidence comparison of the displayed integer-offset templates, rather than extrapolation from finitely many periods. The certificate and standalone verifier expose all \(53\) pairs and independently reconstruct and check the full simplices and incidences in finite periods. Exactly \(53n\) elementary pairs are deleted, leaving a two-dimensional complex with face vector \((6n,19n,15n)\).

**3. A perfect acyclic discrete-Morse matching.** On the surviving complex, `certificate.json` lists \(13\) edge/triangle orbit pairs. Every triangle has at most one edge in a selected edge orbit, so translation gives \(13n\) disjoint matches. The certificate lists an order of the \(15\) triangle orbits. For every selected matched edge and every other triangle incident with that edge, the latter triangle's orbit precedes the matched triangle's orbit. Therefore every nontrivial alternating gradient step strictly increases the orbit order; no closed gradient path is possible. Two triangle orbits, hence \(2n\) triangles, remain critical.

The unmatched edges comprise six orbit types: five within-column edges connecting respectively the first-coordinate pairs \((0,4)\), \((1,3)\), \((2,4)\), \((3,5)\), and \((4,5)\), together with the longitudinal edges connecting \((5,y)\) to \((5,y+1)\). In each column the five transverse edges form a tree on all six vertices. Match their five nonroot vertices toward the root \((5,y)\), then match the longitudinal vertices \((5,y)\) for \(1\le y<n\) toward \((5,0)\) along a spanning path. This supplies \(6n-1\) additional vertex/edge pairs without closed gradient paths. It leaves one critical vertex and one critical edge. The two matching dimensions cannot combine to form a closed gradient path, since every discrete-Morse alternating path has a fixed pair of consecutive dimensions. Discrete Morse theory therefore yields a CW complex homotopy equivalent to \(X_n\) with one \(0\)-cell, one \(1\)-cell and \(2n\) \(2\)-cells.

**4. Every attaching degree is zero.** The projection
\[
p:X_n\longrightarrow\operatorname{VR}_{\le2}(C_n),\qquad (x,y)\longmapsto y
\]
is simplicial because longitudinal distance is at most product distance. For \(n\ge7\), the clique complex of the second power of \(C_n\) collapses onto the ordinary \(n\)-cycle: its only \(2\)-simplices are consecutive triples and every distance-two chord belongs to exactly one such triangle. The longitudinal rim \(y\mapsto(5,y)\) maps isomorphically to the cycle, and therefore gives an infinite-order element of \(H_1(X_n;\mathbb Z)\). In the Morse CW model the boundary homomorphism from its \(2n\) two-cells to its single one-cell must consequently be identically zero; any nonzero attaching degree would make \(H_1\) finite. An attaching map from \(S^1\) to the one-skeleton \(S^1\) is classified up to homotopy by its degree, so every \(2\)-cell is attached nullhomotopically. The model is therefore \(S^1\vee\bigvee^{2n}S^2\), proving the integral homotopy classification.

## Verification
The standalone standard-library program `artifacts/verify.py` uses `artifacts/certificate.json` and reconstructs every simplex directly from the product graph metric, rather than taking a stored face list as an axiom. It replays the \(53n\) elementary collapses, checks the orbit matching and its strictly monotone gradient order, and identifies the six residual edge orbits and their spanning-tree-plus-cycle form. Actual successful executions are recorded in `artifacts/verification_output.txt` for all periods \(7\le n\le20\), including both odd and even periods. The universal statement follows from the local three-column classification and orbit-incidence proof, not from the finite range of tests.

## Relationship to prior work
Adamaszek [1] classifies clique complexes of powers of cycles, including the cycle factor underlying the projection in step four. Adams and collaborators [2], Sections 5.1–5.2, classify square torus-grid Vietoris–Rips complexes, notably the threshold \(3k\)-by-\(3k\) case and the regime with both cycle lengths above \(3k\). Their results do not state or imply the present anisotropic \(6\)-by-\(n\) homotopy type for arbitrary \(n\ge7\). The closely related publicly indexed four-wide and five-wide strips have respectively \(S^1\vee\bigvee^n S^3\) and \(S^1\vee\bigvee^n S^2\) types; the hexagonal width has two independent \(2\)-sphere classes per longitudinal period. The present contribution is the exact boundary-width classification with a finite all-period Morse certificate, not the already-known square-grid or cycle-power formulas.

## Limitations
No result is asserted for \(n\le6\), for any other radius, or for all rectangular grids of other widths. All claims concern the graph shortest-path metric and inclusive threshold \(2\), not a Euclidean embedding metric. Although the source and indexed-record searches found no direct prior covering statement, an equivalent classification in unindexed literature or an unstated corollary of broader techniques cannot be ruled out. The computer replay tests finitely many periods; the all-period proof relies on the explicit width-two locality lemma. No independent external audit has been performed.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version 2011-04-03. https://arxiv.org/abs/1104.0433

[2] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first public version 2025-02-10, especially Sections 5.1–5.2 and Theorems 5.8 and 5.10. https://arxiv.org/abs/2502.07134
