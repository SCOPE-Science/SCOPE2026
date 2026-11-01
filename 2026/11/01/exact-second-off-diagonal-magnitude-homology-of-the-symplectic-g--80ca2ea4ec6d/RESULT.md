# Exact second-off-diagonal magnitude homology of the symplectic generalized quadrangle of order three

## Finding
Let \(G\) be the point–line incidence graph of the symplectic generalized quadrangle \(W(3,3)\), built from totally isotropic two-dimensional subspaces of \(\mathbb F_3^4\) with the standard nondegenerate alternating form. It has 40 point vertices, 40 line vertices, and 160 incidence edges. For ordered opposite-class endpoints \((x,y)\), the magnitude homology at bidegree \((3,5)\) over \(\mathbb F_2\) has dimension
\[
\dim_{\mathbb F_2}\operatorname{MH}_{3,5}^{x,y}(G;\mathbb F_2)=\begin{cases}0,&d(x,y)=1,\\9,&d(x,y)=3.\end{cases}
\]
Same-class endpoints contribute zero because total length five is odd in a bipartite graph. Therefore the **complete global rank** is
\[
\boxed{\dim_{\mathbb F_2}\operatorname{MH}_{3,5}(G;\mathbb F_2)=25920.}
\]
This is the first thick symplectic generalized-quadrangle order above the previously computed order-two example; no all-order formula is asserted.

## Assumptions and scope
Vertices are the 40 projective one-spaces and 40 totally isotropic two-spaces over \(\mathbb F_3\), with adjacency by inclusion and metric the shortest-path metric. Each point or line has degree four. For fixed \(x,y\), \(C_k^{x,y}\) is the \(\mathbb F_2\)-vector space on tuples of \(k+1\) consecutive-distinct vertices beginning at \(x\), ending at \(y\), with sum of consecutive graph distances exactly five. Its boundary deletes an internal vertex when the triangle distance equality holds, the standard magnitude differential. Homological degrees two, three and four determine \(H_3\), and no assertion is made in other bidegrees or over other characteristics.

## Proof
The provided exhaustive construction independently enumerates the 40 normalized projective vectors over \(\mathbb F_3\), the 40 isotropic 2-spaces, and incidence, checks the defining unique-neighbor generalized-quadrangle axiom, and computes every shortest-path distance. Fix one point \(x\) and one incident line \(y\). In degrees \((2,3,4)\), the length-five chain-group dimensions are \((18,81,120)\). Exact bit-vector elimination finds ranks \((18,63)\) for \(\partial_3\) and \(\partial_4\), respectively. The rank formula gives \(81-18-63=0\). For a point \(x\) and nonincident line \(y\), the corresponding chain dimensions are \((28,87,72)\); the two boundary ranks are \((28,50)\), so \(87-28-50=9\). The verifier tests \(\partial_3\partial_4=0\) for every chain basis column in each block, and the ranks are computed with exact Gaussian elimination over \(\mathbb F_2\).

It remains to establish that these two representative calculations exhaust all endpoint pairs. The program explicitly constructs the 40 symplectic transvections \(T_v(w)=w+\omega(w,v)v\), on projective points and isotropic lines, and checks their induced permutations. Their generated orbit of any incident point-line pair contains all 160 such ordered pairs; their generated orbit of any nonincident point-line pair contains all 1440 such ordered pairs. Graph automorphisms preserve the magnitude boundary and bidegree. Reversing the vertex order in each magnitude chain gives an isomorphism for the opposite line-to-point ordered pairs. Finally, bipartiteness forces any length-five chain with same-class endpoints to be absent. There are \(2\cdot1440=2880\) ordered distance-three opposite-class pairs, each contributing nine, proving the global rank \(25920\). This is a finite but **exhaustive proof**, rather than an extrapolation from sampling or an assumed automorphism transitivity.

## Verification
Run `python3 verify.py` in the directory containing `gq_constructor.py`. Both scripts use only Python 3 standard-library modules. The verifier independently constructs all generating symplectic transvections, exhaustively checks both endpoint-pair orbit sizes, enumerates every length-five basis tuple in the two local cases, verifies all boundary compositions vanish, and eliminates the exact mod-two boundary matrices. `verification_output.txt` contains the observed counts and terminal marker `GQ33_MAGNITUDE_EXACT_MOD2_VERIFIED`. The finite proof covers all ordered endpoints by certified orbits and chain reversal, not only two unverified representative pairs.

## Relationship to prior work
Asao, Hiraoka and Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044 (first public 2021-01-22), establish near-diagonal magnitude-homology vanishing under stronger girth assumptions; the girth-eight generalized quadrangle lies at the unforced second-off-diagonal boundary. A previously published calculation for the Tutte–Coxeter incidence graph \(W(3,2)\) determines the analogous mod-two group at order two (local rank four, global rank 1440). That different order is already known and not claimed as a new result. Neither result implies the exact order-three chain ranks and the new global value 25920. The parameter search included symplectic/dual generalized-quadrangle aliases and the exact bidegree and numeric fingerprints.

## Limitations
The rank is over \(\mathbb F_2\) only; integral torsion, rational rank and an all-parameter formula for \(W(3,q)\) are not established. The two representative boundary matrices are verified exhaustively for one graph; transvection-orbit enumeration ensures the asserted global coverage. Equivalent unindexed magnitude-homology tables remain an originality risk.

## References
1. Y. Asao, Y. Hiraoka, S. Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044, first public 2021-01-22. https://arxiv.org/abs/2101.09044
2. R. Hepworth and S. Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125 (definition and differential).
3. *Second off-diagonal magnitude homology of the Tutte–Coxeter graph*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-second-off-diagonal-magnitude-homology-of-the-tutte-coxeter-grap--4b0a76652329
