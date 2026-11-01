# Integral two-independence homotopy separates the dodecahedral and Desargues graphs

## Finding
For the generalized Petersen graphs on twenty vertices, two natural cubic instances have different integral homotopy types at the first higher-independence level:
\[
\operatorname{Ind}_2(\operatorname{GP}(10,2))\simeq S^6,
\qquad
\operatorname{Ind}_2(\operatorname{GP}(10,3))\simeq \bigvee^{41}S^7.
\]
Here the first graph is the dodecahedral graph and the second is the Desargues graph. Both equivalences are based on complete acyclic discrete-Morse matchings and explicit primitive integral attaching-degree matrices, not on Betti numbers alone.

## Assumptions and scope
For \(k\in\{2,3\}\), let \(\operatorname{GP}(10,k)\) have vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\). The vertex ordering is \(u_0,\dots,u_9,v_0,\dots,v_9\). Define \(\operatorname{Ind}_2(G)\) to be the abstract simplicial complex consisting of all vertex subsets \(A\) such that every connected component of the induced subgraph \(G[A]\) has at most two vertices. Equivalently, the induced maximum degree is at most one. Homotopy equivalences are ordinary nonequivariant homotopy equivalences of finite geometric realizations. Homology is integral unless otherwise specified. Graphs are simple and every index is reduced modulo ten.

## Proof
**Complete finite face construction.** Enumerate every subset of the twenty vertices, accepting exactly the subsets in which each selected vertex has at most one selected neighbor. This yields 63,142 nonempty faces for \(k=2\) and 62,048 for \(k=3\). The respective complete face vectors (dimensions zero to eleven) are
\[
(20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5)
\]
and
\[
(20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5).
\]

**Acyclic matching.** Starting with the entire face poset including the empty face, process vertex labels \(0,1,\dots,19\) in increasing order. At stage \(j\), simultaneously pair each still-unmatched face \(\sigma\) not containing \(j\) with \(\sigma\cup\{j\}\) when the latter is still unmatched. Reverse the pair involving the empty face and its singleton partner, leaving the latter as the basepoint critical zero-cell. Direct every nonempty face-poset incidence downwards, except that paired incidences point upwards. A full topological sort, including every incidence, visits every nonempty face: 410,500 incidences in the dodecahedral case and 400,760 in the Desargues case. Thus the matchings are globally acyclic, not merely dimensionwise acyclic. They have 31,565 and 31,000 pairs respectively. Their critical cell counts are, in dimensions \((0,5,6,7)\), respectively \((1,1,6,4)\), and, in dimensions \((0,6,7)\), respectively \((1,3,44)\). Forman's discrete Morse theorem supplies CW models with these cell counts.

**Exact signed Morse differential.** Orient a simplex by increasing vertex order. A critical face contributes the corresponding generator. A noncritical lower face paired with an upper face is reduced recursively by solving the upper cellular boundary equation, using its incidence sign and recursively reducing the other codimension-one faces. A complete executable implementation is provided in `verify_gp10_twoind.py`. Because the matching is acyclic, this recursion terminates and computes integral attaching-degree matrices.

For \(k=2\), in increasing critical-face order the only nonzero-degree differential matrices are
\[
\partial_6=(0,0,-1,0,1,0),\qquad
\partial_7=\begin{pmatrix}
1&1&0&0\\
0&0&0&-1\\
0&1&0&0\\
0&-1&1&0\\
0&1&0&0\\
0&0&-1&0
\end{pmatrix}.
\]
The product \(\partial_6\partial_7\) is identically zero. The matrix \(\partial_6\) contains the unit entry \(-1\); the \(4\times4\) submatrix of \(\partial_7\) from its first four rows has determinant \(-1\). Hence the two differentials have primitive images of ranks one and four. The reduced integral cellular homology is concentrated in degree six and is \(\mathbb Z\).

For \(k=3\), \(\partial_7\) is a \(3\times44\) integer matrix with a \(3\times3\) minor of determinant \(-1\), using zero-based column indices \((0,3,14)\) and all three rows. Thus its image is all of \(\mathbb Z^3\), its kernel is free of rank 41, and the reduced integral homology is concentrated in degree seven and is \(\mathbb Z^{41}\). The executable checker constructs the entire matrix rather than relying on the stated minor alone.

**From cellular homology to homotopy.** The Morse CW complex for \(k=2\) has one five-cell, six six-cells and four seven-cells over a basepoint. Each six-cell attaches to \(S^5\) by its integer degree, because \(\pi_5(S^5)\cong\mathbb Z\). The primitive unit row permits elementary changes of the six-cell basis and cancellation of a five/six-cell pair, leaving five six-cells and four seven-cells. The latter attach to \(\bigvee^5S^6\) through maps classified by their degree vectors, since \(\pi_6(\bigvee^5S^6)\cong\mathbb Z^5\); the primitive rank-four attaching matrix cancels four further six/seven-cell pairs. The result is \(S^6\). The \(k=3\) model has three six-cells and 44 seven-cells over a point, with primitive rank-three attaching matrix; the identical degree classification gives \(\bigvee^{41}S^7\). These are genuine integral homotopy equivalences, not conclusions from finite-field rank computations.

## Verification
Running `python3 verify_gp10_twoind.py` from this package reconstructs all graphs, faces, Hasse incidences, matching orientations, full acyclicity topological sorts, signed Morse differentials and integer unimodular minors. An independent bitset Gaussian-elimination computation of the original simplicial boundary ranks over \(\mathbb F_2\) reproduces the two reduced Betti vectors: \(1\) in degree six for \(k=2\), and \(41\) in degree seven for \(k=3\). This is a consistency check, not the source of the integral proof. The script ends with `GP10_TWO_INDEPENDENCE_INTEGRAL_HOMOTOPY_CERTIFICATE_OK` only after all assertions pass.

## Relationship to prior work
Deshpande and Singh's 2020 higher-independence framework introduces the underlying construction and discrete-Morse methods; their inspected examples and the subsequent 2020 distance-domination work do not determine these two generalized Petersen complexes. The 2021 work of Abdelmalek and collaborators treats, among other things, chordal and caterpillar cases, which do not imply the present nonchordal cubic-graph results. Previously documented ordinary independence homotopy types for these two graphs concern \(\operatorname{Ind}_1\), not \(\operatorname{Ind}_2\). Similarly, Kim and Lew's homology calculation for an independence-number-filtered complex on the dodecahedral graph uses a different simplicial face condition. Comparing the actual face predicates rules out deductions from those results. This calculation is a comparative classification for the two specified graphs; no general statement for all generalized Petersen graphs is asserted.

## Limitations
The classification is nonequivariant. It does not determine the automorphism representations on homology, persistent behavior under graph changes, or higher-independence levels beyond two. The computable proof is exhaustive for exactly these twenty-vertex graphs; it makes no claim of an infinite-parameter classification. Originality is based on inspected accessible sources and indexed research, so a less discoverable equivalent computation remains a bibliographic possibility. No independent external audit has been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first posted 2020-01-15), https://arxiv.org/abs/2001.05448.
2. P. Deshpande, A. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775v1 (2020), https://arxiv.org/abs/2001.06775.
3. A. Abdelmalek and collaborators, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (2021), https://arxiv.org/abs/2106.10863.
4. D. Kim and A. Lew, *Complexes of graphs with bounded independence number*, FPSAC 2020; the dodecahedral calculation there uses a different independence-number bound, not the induced-degree-one complex.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
