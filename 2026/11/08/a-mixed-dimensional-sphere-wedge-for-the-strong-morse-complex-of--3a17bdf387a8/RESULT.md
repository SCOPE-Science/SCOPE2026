# A mixed-dimensional sphere wedge for the strong Morse complex of \(\Theta_{2,2,3}\)

## Finding
For the unfilled theta graph \(\Theta_{2,2,3}\) consisting of three internally disjoint pole-to-pole paths of lengths \(2,2,3\), the **full** strong discrete-Morse matching complex satisfies
\[
|\mathcal{SM}(\Theta_{2,2,3})|\simeq S^1\vee\bigvee^5 S^2.
\]
Its reduced integral homology is \(\widetilde H_1\cong\mathbb Z\), \(\widetilde H_2\cong\mathbb Z^5\), and zero in other degrees. The assertion is about integral homotopy type, not merely homology.

## Assumptions and scope
The graph is the **one-dimensional, unfilled** simplicial complex with vertex set \(\{0,1,2,3,4,5\}\) and edge set
\[
\{\{0,2\},\{0,3\},\{0,4\},\{1,2\},\{1,3\},\{1,5\},\{4,5\}\}.
\]
The distinguished poles are \(0\) and \(1\). The two short paths pass through \(2,3\), and the long path passes through \(4,5\). This is the first uneven theta obtained by subdividing a single edge of \(K_{2,3}\).

We use the definition of Knudson and Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (publicly posted September 6, 2026): \(\mathcal{SM}(G)\) is the downward closure of all strong matchings produced by injective vertex filtrations. In a one-dimensional graph the descending link of a vertex is a discrete set; it is a cone exactly when that vertex has **one** earlier neighbor. Therefore, for any ordering, the generating strong matching consists of the vertex-edge pairs \((v,\{v,a\})\) precisely when \(a\) is the unique neighbor of \(v\) appearing earlier. All \(6!=720\) orderings are included; no other generating matchings occur.

## Proof
Index the \(14\) possible oriented vertex-edge pairings \((v,a)\) lexicographically:
`(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,0),(2,1),(3,0),(3,1),(4,0),(4,5),(5,1),(5,4)`.
A simplex is encoded by a nonzero \(14\)-bit mask. Exhaustively generating the strong matchings from the \(720\) vertex orders yields \(91\) distinct generators, \(36\) maximal faces and the full face vector
\[
(f_0,f_1,f_2,f_3)=(14,57,58,10).
\]
This is an exact finite enumeration, not a random sample; the complete constructive algorithm is in `verify.py`.

Define an elementary face-poset matching by processing the coordinates in the order
`11,12,0,2,13,3,10,5,6,9,4,1,7,8`. At coordinate `j`, traverse every nonempty simplex mask by increasing `(number_of_bits,mask)` and pair every still-unmatched mask lacking bit `j` with its union with bit `j`, provided both masks are faces and currently unmatched. This produces exactly \(66\) incidence pairs, hence \(7\) critical cells. Their masks are `1096,1168,1296,1538,1664,2048,4160`, with dimensions \((2,2,2,2,2,0,1)\). The critical vector is therefore
\[
(c_0,c_1,c_2,c_3)=(1,1,5,0).
\]

The complete directed Hasse diagram has \(139\) nodes and \(328\) cover incidences. Reverse exactly the \(66\) matching incidences, leaving all others directed downward. A complete topological sort visits all \(139\) nodes, proving that the matching is **globally acyclic**. By finite discrete-Morse theory this supplies a CW model with precisely one zero-cell, one one-cell and five two-cells.

For the attaching degrees, use the signed simplicial incidence convention
\[
\partial[v_0,\ldots,v_q]=\sum_{i=0}^q(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_q],
\]
where vertex indices are in increasing order. Cancel the \(66\) matched lower/upper cells algebraically over \(\mathbb Z\), with incidence pivots \(\pm1\). For each pivot, subtract the signed boundary of the upper cell from the boundaries of all other current co-dimension-compatible upper cells to eliminate its lower-cell coefficient, then delete that matched pair. Each of the \(66\) pivots is exactly a unit; the resulting differential on the seven unmatched cells is identically zero. The supplied verifier reconstructs and checks all these integer operations.

The one-skeleton of the Morse CW model is a circle because there is one vertex and one edge. Each two-cell is attached along a loop in this circle. Its degree is its coefficient in the integral cellular boundary, which the calculation proves to be zero. As \(\pi_1(S^1)\cong\mathbb Z\), a degree-zero loop is nullhomotopic. Attaching all five such disks yields a wedge of five two-spheres on the circle, proving the displayed equivalence.

## Verification
Run `python3 verify.py` using Python 3 with no third-party packages. It independently reconstructs the graph, all orderings, the complete face poset, the matching, the reversed Hasse digraph and every exact integral cancellation. Its expected terminal marker is `ALL_VERIFY_OK`; the full output is in `verify_output.txt`. Important checks are \(91\) generators, \(36\) facets, face vector \((14,57,58,10)\), \(66\) matched pairs, \(139\) Hasse vertices and \(328\) incidences, complete acyclicity, and seven critical cells with zero integer differential. The exact enumeration constitutes a reproducible finite certificate. No randomized search or external solver is required by the final verification.

## Relationship to prior work
Knudson and Owens-White define this precise full strong matching complex and compute homotopy types for paths, stars, simplices and their boundaries, alongside results on cycles. Their paper does not treat uneven theta graphs, as verified by inspecting the text and its listed graph families. The current graph is a natural first edge subdivision outside the complete-bipartite family, allowing two short cycles of length five and one of length four; its mixed-dimensional homotopy is not obtained by substituting a parameter into the published path/cycle/star formulas. Ordinary Morse-matching complexes and ordinary graph matching complexes use different definitions and do not settle this claim. Prior calculations for complete bipartite graphs supply context but do not imply a homotopy equivalence after edge subdivision.

## Limitations
This theorem applies only to the specified six-vertex graph and the **full** strong matching complex. It does not classify general theta graphs, the pure strong matching subcomplex, arbitrary edge subdivisions, automorphism representations, or stronger equivariant homotopy types. An equivalent result in unindexed literature cannot be ruled out solely by search.

## References
Knudson, K. P. and Owens-White, A., *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, September 6, 2026, https://arxiv.org/html/2609.06844v1 (Sections 3–4, 6–10).

Forman, R., *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (discrete-Morse CW theorem).
