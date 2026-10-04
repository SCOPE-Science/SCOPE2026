# The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge
## Finding
Let \(G\) be the Möbius–Kantor graph, realized as the generalized Petersen graph \(G(8,3)\). Its ordinary matching complex \(M(G)\), whose vertices are edges of \(G\) and whose simplices are pairwise vertex-disjoint edge sets, has homotopy type
\[
M(G)\simeq \bigvee^{8} S^{4} \vee \bigvee^{4} S^{5}.
\]
Thus this canonical cubic symmetric graph already exhibits a matching complex whose sphere-wedge decomposition occurs in two adjacent dimensions.

## Assumptions and scope
Write the vertices of \(G(8,3)\) as \(u_i,v_i\) for \(i\in\mathbb{Z}/8\mathbb{Z}\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), with indices modulo \(8\). This gives \(16\) graph vertices and \(24\) graph edges. The claim concerns the ordinary matching complex, not a perfect-matching complex and not a matching complex on a barycentric subdivision. No claim is made for other generalized Petersen graphs or for all cubic symmetric graphs.

## Proof
Index the \(24\) graph edges in lexicographic order on their endpoint pairs, exactly as reconstructed by `verify_mobius_kantor_matching.py`. Exhaustive enumeration gives \(11{,}068\) graph matchings including the empty matching, hence \(11{,}067\) nonempty simplices of \(M(G)\), with face vector
\[
(24,228,1096,2826,3816,2444,600,33).
\]

On the face poset of \(M(G)\), apply the deterministic staged matching that toggles graph-edge indices in the order
\[
20,22,7,0,3,15,6,21,13,23,8,17,10,12,16,18,11,4,5,9,2,1,14,19.
\]
At each stage, an unmatched simplex not containing the indicated graph edge is paired with its union with that edge whenever both remain unmatched. This produces \(5{,}525\) matched face-poset covers. Reversing precisely those covers in the full Hasse diagram gives a directed acyclic graph on all \(11{,}067\) nonempty simplices and all \(53{,}256\) face-poset covers. The critical simplices are exactly one in dimension \(0\), ten in dimension \(4\), and six in dimension \(5\).

Forman's theorem therefore gives a CW model with one \(0\)-cell, ten \(4\)-cells, and six \(5\)-cells. The signed gradient-path Morse boundary from the six critical \(5\)-cells to the ten critical \(4\)-cells has Smith normal form
\[
\operatorname{diag}(1,1,0,0,0,0).
\]
The \(4\)-skeleton is \(\bigvee^{10}S^4\). Since it is \(3\)-connected, Hurewicz gives
\[
\pi_4\!\left(\bigvee^{10}S^4\right)\cong H_4\!\left(\bigvee^{10}S^4;\mathbb{Z}\right)\cong\mathbb{Z}^{10},
\]
so the six attaching maps are determined by the integer degree matrix of the Morse boundary. Unimodular changes of basis put that matrix in Smith form. Two unit entries split off two contractible \(4\)-/\(5\)-cell pairs, while four zero columns attach trivially. The remaining CW complex is therefore \(\bigvee^8 S^4\vee\bigvee^4 S^5\).

## Verification
The standalone verifier reconstructs \(G(8,3)\), enumerates every matching, reconstructs every face-poset cover, checks the full directed acyclicity certificate, recomputes the signed Morse boundary, and verifies its Smith invariants from exact integer minors. Independently, it computes simplicial homology over \(\mathbb{F}_2\), obtaining Betti vector
\[
(1,0,0,0,8,4,0,0),
\]
consistent with the integral wedge decomposition. The verifier terminates with `VERIFY_OK`.

## Relationship to prior work
Donovan and Scoville define the ordinary matching complex and use discrete Morse methods to compute homotopy types for paths, cycles, and Dutch windmill graphs; their published paper has primary MSC \(57Q70\). Their listed families do not include the Möbius–Kantor graph. Exact searches under the aliases “Möbius–Kantor”, “Mobius-Kantor”, and \(G(8,3)\) did not locate a prior statement of the displayed homotopy type.

Broader literature checked for implication does not subsume the claim. The classification of manifold matching complexes determines when a matching complex is a homology manifold, rather than the exact homotopy type here. Results for outerplanar graphs do not apply because the Möbius–Kantor graph is nonplanar. A 2026 paper on Möbius ladder graphs studies independence complexes and perfect-matching complexes; both the graph family and the simplicial-complex functor differ from the ordinary matching complex of the Möbius–Kantor graph.

## Limitations
Originality is assessed relative to the inspected indexed literature and exact database searches; an unindexed computation or alternate terminology could still exist. The proof is a finite exact certificate for this single graph and does not provide a uniform formula for generalized Petersen graphs. The wedge decomposition relies on the explicitly verified discrete Morse matching and signed Morse differential; the \(\mathbb{F}_2\) homology calculation is a cross-check, not a substitute for the homotopy argument.

## References
1. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, arXiv:2207.13780 (first public version 2022-07-27); New York J. Math. 29 (2023), 1393–1412.
2. M. Bayer, B. Goeckner, and M. Jelić Milutinović, *Manifold Matching Complexes*, Mathematika 66 (2020), 973–1002, DOI 10.1112/mtk.12049.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601.
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601.
