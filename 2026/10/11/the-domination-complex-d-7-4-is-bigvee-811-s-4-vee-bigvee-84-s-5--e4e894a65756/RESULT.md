# The domination complex \(D_{7,4}\) is \(\bigvee^{811}S^4\vee\bigvee^{84}S^5\)
## Finding
Let \(D_{7,4}\) be the simplicial complex on the \(21\) edges of \(K_7\) in which an edge set \(E\) is a simplex exactly when the labeled graph \(([7],E)\) has domination number at least \(4\). Then
\[
D_{7,4}\simeq \bigvee^{811}S^4\vee\bigvee^{84}S^5.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and labeled on \([7]=\{1,\ldots,7\}\). A vertex set \(A\) dominates a graph when every vertex outside \(A\) has a neighbor in \(A\). The domination number is the minimum size of such a set. The claim is only for the specific complex \(D_{7,4}\); no all-\(n\) formula for \(D_{n,n-3}\) is asserted.

## Proof
Exhaustive enumeration of all \(2^{21}\) labeled graphs on seven vertices gives the face counts by edge-set size
\[
(1,21,210,1330,4515,7077,3605,630),
\]
where the initial \(1\) is the empty face. In particular, there are \(17{,}388\) nonempty faces and no face with more than seven edges.

Order the \(21\) edge-vertices lexicographically. Starting with the full nonempty face poset, for each edge-vertex in order pair every still-unmatched face not containing that edge with the face obtained by adding it, whenever both are still unmatched. This yields \(8{,}210\) pairs. The complete modified Hasse diagram has \(83{,}895\) cover relations and is acyclic by a full topological sort. The unmatched faces consist of one \(0\)-simplex, \(847\) \(4\)-simplices, and \(120\) \(5\)-simplices.

Thus Forman reduction gives a CW complex with one \(0\)-cell, \(847\) \(4\)-cells, and \(120\) \(5\)-cells. Using the standard simplex incidences and the verified gradient paths, the integral Morse boundary \(\partial_5\colon\mathbb Z^{120}\to\mathbb Z^{847}\) has rank \(36\). A \(36\times36\) full-rank minor has determinant \(-1\), so every nonzero Smith invariant is \(1\). Hence the boundary is integrally equivalent to a diagonal block with \(36\) unit entries and zeros elsewhere.

The \(4\)-skeleton is \(\bigvee^{847}S^4\). Since it is \(3\)-connected, Hurewicz identifies \(\pi_4\) with \(H_4\), so each \(5\)-cell attaching map is determined by its degree vector. Integral changes of bases in the \(4\)- and \(5\)-cells reduce the attaching matrix to Smith form. The \(36\) unit cell pairs cancel, leaving \(811\) unattached \(4\)-cells and \(84\) trivially attached \(5\)-cells. This proves the stated wedge decomposition.

## Verification
The standalone verifier `artifacts/verify.py` reconstructs all \(2^{21}\) graphs, checks the face predicate from the domination definition, rebuilds the toggle matching, topologically sorts the full modified Hasse diagram, reconstructs the signed Morse boundary, verifies its exact rational rank \(36\), and checks a determinant-\(-1\) full-rank minor. Independently, it computes the mod-\(2\) simplicial boundary ranks
\[
(20,190,1140,3375,2891,630),
\]
which give reduced Betti numbers \(811\) in degree \(4\), \(84\) in degree \(5\), and zero otherwise. The Euler characteristic is \(728\), consistent with the wedge.

## Relationship to prior work
González and Hoekstra-Mendoza introduced and studied these bounded-domination graph complexes. Their Theorem 1.1 determines \(D_{n,n-2}\), and their Section 8 treats \(D_{5,2}\); they explicitly identify the range \(n-3\ge k\ge2\) as generally unknown and use \(D_{6,3}\) only as evidence that the earlier equidimensional pattern breaks. The inspected paper contains no \(D_{7,4}\) computation. A separate published published-finding corpus finding determines \(D_{6,3}\) as a mixed-dimensional sphere wedge, but that statement neither contains nor implies the seven-vertex case. Exact searches for \(D_{7,4}\), the seven-vertex domination-number-at-least-four formulation, and the numerical pair \((811,84)\) did not locate a covering statement.

## Limitations
This is a finite exact classification, not a formula for all \(D_{n,n-3}\). The novelty assessment is based on the inspected primary paper, exact web searches, published-finding corpus semantic searches, and the existing ledger; an unindexed result under substantially different terminology remains a residual bibliographic risk. The proof itself is finite and independently replayable from the definition.

## References
1. J. González and T. I. Hoekstra-Mendoza, “On the homotopy type of complexes of graphs with bounded domination number,” arXiv:1901.07130, first version 2019-01-22; Contributions to Discrete Mathematics 16(3), 2021, DOI 10.55016/ojs/cdm.v16i3.72114.
2. published-finding corpus record `2026/10/4/SCOPE-a-mixed-dimensional-sphere-wedge-for-d-6-3--55d89ec4bab2`, used only for overlap comparison with the adjacent case \(D_{6,3}\).
