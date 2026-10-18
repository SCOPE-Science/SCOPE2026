# Seven minimal induced homology spines of \(GP(7,2)\)

## Finding
Let \(G=GP(7,2)\), with outer vertices \(u_i\) and inner vertices \(v_i\) indexed by \(i\in\mathbb Z/7\mathbb Z\). Put \(K=\operatorname{Ind}(G)\). For every vertex subset \(W\), the inclusion \(K[W]\hookrightarrow K\) induces a nonzero homomorphism on integral third homology **if and only if** there exists \(i\in\mathbb Z/7\mathbb Z\) for which
\[
W_i=V(G)\setminus\{v_i,v_{i+1},v_{i+2}\}\subseteq W.
\]
Each of these **exactly seven** vertex-minimal supports contains eleven vertices, and \(K\) simplicially collapses onto each \(K[W_i]\). Every \(K[W_i]\) is homotopy equivalent to \(S^3\), so every inclusion \(K[W_i]\hookrightarrow K\) is a simple-homotopy equivalence. In particular \(K\simeq S^3\), and the seven smallest integral third-homology carriers are all collapse spines. There are no other vertex-minimal supports carrying nonzero ambient third homology.

## Assumptions and scope
The generalized Petersen graph has edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with indices modulo seven. Its independence complex is the **ordinary** simplicial complex of independent vertex sets; \(K[W]\) is the full induced subcomplex on \(W\). Homology is unreduced in degree three and has integer coefficients unless another coefficient ring is displayed. A *carrier* means a subset with nonzero inclusion-induced map into ambient homology. The theorem concerns this specific graph; no claim is made for all generalized Petersen graphs.

## Proof
Enumerating independent sets with the explicit 21-edge graph gives the face vector \((14,70,154,147,49)\) in dimensions zero through four. The attached `certificate.json` lists 134 ordered elementary collapses from \(K\) to \(K[W_0]\). Every pair consists of a codimension-one free face and its unique surviving coface, and the final remaining complex is exactly \(K[W_0]\). Cyclic rotation sends this sequence to an equally valid 134-pair collapse onto every \(K[W_i]\).

The same certificate gives 82 matched adjacent-dimensional face pairs of \(K[W_0]\), leaving precisely one critical vertex and one critical three-simplex. Directing unmatched Hasse arrows downwards and matched arrows upwards gives an acyclic digraph, as independently checked in `verify.py`. Discrete Morse theory produces a CW complex with one zero-cell and one three-cell, and no cells in dimensions one or two. Its attaching map is constant, hence it is \(S^3\). Cyclic rotation proves the analogous conclusion for all seven carriers. The ambient collapse proves \(H_3(K;\mathbb Z)\cong\mathbb Z\) and that each carrier inclusion is an integral isomorphism.

It remains to rule out every other support, without assuming monotonicity of homology under induced inclusions. If \(W\) excludes an outer vertex, then \(K[W]\) lies in an induced subcomplex of the form \(K-u_i\). The seven graphs are rotationally isomorphic; exact degree-three and degree-four boundary ranks over \(\mathbb F_2\) for \(K-u_0\) are respectively \(73\) and \(32\), while it has \(105\) three-simplices. Therefore its \(H_3(-;\mathbb F_2)\) vanishes.

Suppose instead that \(W\) contains all seven outer vertices, and let \(S\subseteq\mathbb Z/7\mathbb Z\) be the missing inner indices. If \(S\) has a pair of indices at cyclic distance three, then \(K[W]\) lies in a rotation of \(K-\{v_0,v_3\}\). For this latter induced complex the corresponding ranks are \(55\) and \(23\), and there are \(78\) three-simplices; its degree-three mod-two homology also vanishes.

Finally, every subset \(S\) of the seven cyclic indices with **no** pair at cyclic distance three is contained in some three-consecutive-index set \(\{i,i+1,i+2\}\). This is the explicit seven-cycle-square clique fact; the verifier also checks all \(128\) such index subsets independently. Consequently, unless \(W\) contains one of the seven \(W_i\), it lies in one of the fourteen just-described mod-two-acyclic barriers. If a map \(H_3(K[W];\mathbb Z)\to H_3(K;\mathbb Z)\cong\mathbb Z\) were nonzero, its rationalization would be nonzero; the mod-two vanishing of the containing barrier forces its rational degree-three homology to vanish by the universal coefficient theorem. This contradiction proves necessity.

Conversely, if \(W_i\subseteq W\), the inclusion through \(K[W]\) composes to the already proved integral homology isomorphism \(H_3(K[W_i];\mathbb Z)\to H_3(K;\mathbb Z)\); hence the intermediate map is nonzero (indeed surjective). Every proper subset of \(W_i\) cannot contain any \(W_j\), since both have eleven vertices, proving minimality and the exact count.

## Verification
From the directory containing `verify.py` and `certificate.json`, execute `python3 verify.py`. It reconstructs all simplices independently of the certificate, checks every stated free-face condition for the 134-pair collapse and its seven rotations, checks all 82 Morse pairs plus acyclicity, reconstructs the two obstruction complexes and their mod-two boundary ranks, and checks the elementary seven-index covering lemma. Expected final line: `VERIFY_OK GP7_2 FACE_VECTOR_14_70_154_147_49 SEVEN_COLLAPSE_SPINES_134 EACH_S3 MORSE_82 BARRIERS_2_RANK_TESTS`. Exact finite checks are exhaustive for the declared fourteen-vertex graph, not experiments extrapolated to larger graphs.

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418v1) develops homotopy tools for graph independence complexes, including cycle and forest examples, but its inspected treatment does not give the induced-support dichotomy above. Besharati, Ebrahimi and Azadi's *Independence number of generalized Petersen graphs* (arXiv:1008.2583v1) studies the same graph family and determines the maximum independent-set size, rather than inclusion-induced simplicial homology, its seven carriers, or elementary collapses. The present claim is a complete induced-support classification, not merely a rank calculation. It is distinct from analyses of \(GP(6,2)\), \(GP(8,3)\), and graph-metric Rips complexes of generalized Petersen graphs.

## Limitations
No formula for \(GP(n,2)\) with variable \(n\), or a classification of the homology of *all* induced subcomplexes in degrees other than the inclusion-induced third-homology image, is asserted. The result does not establish publication priority in all unindexed literature. The displayed Morse matching is non-equivariant; the seven carrier collapses are related by rotations, not one simultaneous equivariant collapse. Independent external review has not been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first submitted 2 July 2010, https://arxiv.org/abs/1007.0418.
2. N. Besharati, J. B. Ebrahimi, A. Azadi, *Independence number of generalized Petersen graphs*, arXiv:1008.2583v1, first submitted 16 August 2010, https://arxiv.org/abs/1008.2583.
