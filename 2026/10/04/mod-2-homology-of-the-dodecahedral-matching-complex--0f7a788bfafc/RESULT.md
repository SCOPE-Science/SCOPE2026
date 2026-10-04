# Mod-\(2\) homology of the dodecahedral matching complex
## Finding
Let \(D=G(10,2)\) be the dodecahedral graph and \(\mathcal M(D)\) its ordinary matching complex. Then \(\widetilde H_5(\mathcal M(D);\mathbb F_2)\cong\mathbb F_2^5\), \(\widetilde H_6(\mathcal M(D);\mathbb F_2)\cong\mathbb F_2^{117}\), and \(\widetilde H_i(\mathcal M(D);\mathbb F_2)=0\) for every \(i\notin\{5,6\}\).

## Assumptions and scope
Let \(D\) be the generalized Petersen graph \(G(10,2)\), with vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), outer edges \(u_i u_{i+1}\), spokes \(u_i v_i\), and inner edges \(v_i v_{i+2}\). This is the dodecahedral graph. The ordinary matching complex \(\mathcal M(D)\) is the simplicial complex whose vertices are the 30 edges of \(D\) and whose simplices are pairwise vertex-disjoint edge sets. All homology in the finding is reduced simplicial homology with coefficients in \(\mathbb F_2\).

## Proof
For \(1\le k\le 10\), a \((k-1)\)-simplex of \(\mathcal M(D)\) is exactly a matching of size \(k\). Exhaustive enumeration gives the matching counts, including the empty matching,
\[
(1,30,375,2540,10155,24474,34805,27300,10260,1400,36).
\]
Use the augmented simplicial chain complex over \(\mathbb F_2\). For each \(k\ge1\), the boundary of a size-\(k\) matching is the sum of the \(k\) size-\((k-1)\) matchings obtained by deleting one edge; for \(k=1\) this is the augmentation to the empty simplex. Exact row reduction over \(\mathbb F_2\) gives the ranks
\[
(1,29,346,2194,7961,16513,18287,8896,1364,36)
\]
for these ten boundary maps. Therefore, in simplicial dimension \(k-1\),
\[
\dim_{\mathbb F_2}\widetilde H_{k-1}=c_k-r_k-r_{k+1},
\]
with \(r_{11}=0\). Substitution gives reduced Betti numbers in dimensions \(0,\ldots,9\)
\[
(0,0,0,0,0,5,117,0,0,0),
\]
which is exactly the stated claim. The identity \(\partial^2=0\) holds because every two-edge deletion occurs twice and therefore cancels over \(\mathbb F_2\).

## Verification
The standalone script `verify.py` reconstructs \(G(10,2)\) from its defining edge rule, checks that it has 20 vertices, 30 edges and degree three at every vertex, exhaustively enumerates every matching, reconstructs every augmented boundary matrix, performs exact bitset Gaussian elimination over \(\mathbb F_2\), and checks the reduced Euler characteristic independently. Its terminal line is `DODECAHEDRAL_MATCHING_F2_VERIFY_OK`.

## Relationship to prior work
Jelić Milutinović, Jenne, McDonough and Vega define graph matching complexes and emphasize that their topology is difficult outside a few established graph families; their 2019 work treats trees, polygonal line tilings and honeycomb connectivity, not the dodecahedral graph. Bayer, Goeckner and Jelić Milutinović give a broad structural classification of matching complexes that are homology manifolds and matching-complex preliminaries; the inspected full text contains no dodecahedral or generalized-Petersen instance. Exact searches for `dodecahedral graph matching complex`, `G(10,2) matching complex`, the equivalent line-graph independence-complex formulation, and the computed Betti pair \((5,117)\) found no source implying this calculation.

## Limitations
The claim is only about reduced homology over \(\mathbb F_2\). No integral homology, torsion statement, cup product, homotopy type, shellability, or discrete-Morse model is asserted. A literature search cannot exclude every unpublished or unindexed computation; the originality assessment is limited to the inspected sources and recorded database searches.

## References
1. M. Jelić Milutinović, H. Jenne, A. McDonough, J. Vega, *Matching complexes of trees and applications of the matching tree algorithm*, arXiv:1905.10560, first public 2019-05-25.
2. M. Bayer, B. Goeckner, M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, first public 2019-06-07; Mathematika 66 (2020), 973--1002.
3. MSC2020, 55U10, *Simplicial sets and complexes in algebraic topology*.
