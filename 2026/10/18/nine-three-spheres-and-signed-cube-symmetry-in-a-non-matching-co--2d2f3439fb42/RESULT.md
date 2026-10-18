# Nine three-spheres and signed cube symmetry in a non-matching complex

## Finding
Let \(Q_3\) be the graph of the three-dimensional Boolean cube, with vertices \(\{0,1\}^3\) and edges joining words at Hamming distance one. Let
\[
K=\operatorname{NM}_3(Q_3)
=\{F\subseteq E(Q_3):F\text{ contains no three pairwise vertex-disjoint edges}\}.
\]
Then the integral homotopy type is
\[
K\simeq\bigvee^9 S^3.
\]
More precisely, write its full graph-automorphism group as \(B_3=(C_2)^3\rtimes S_3\), acting by signed coordinate permutations. Let \(P\) be the rational permutation representation on the three coordinate directions, with the translation subgroup acting trivially. Let \(U\) be the signed three-dimensional coordinate representation, and let \(\epsilon\) be the sign of the coordinate-permutation factor (trivial on translations). Then
\[
\widetilde H_3(K;\mathbb Q)
\cong P\oplus(\epsilon\otimes U)\oplus
(\epsilon\otimes\bigwedge^2 U)
\]
as rational \(B_3\)-representations. Every other reduced integral homology group vanishes; in degree three it is free of rank nine.

The cube is also the crown graph \(K_{4,4}\) with one perfect matching removed. Its non-matching complex therefore has the same nonequivariant homotopy type as the complete bipartite \(K_{4,4}\) non-matching complex, despite the deletion of four graph edges. No general theorem for all crown graphs is asserted.

## Assumptions and scope
The graph is exactly the simple eight-vertex cube \(Q_3\). The integer threshold is exactly three, and the complex is formed on the *twelve graph edges*, not on the eight graph vertices. This is not the ordinary matching complex, the degree-at-most-two matching complex, or a cut complex. The automorphism group acts simplicially by permuting the twelve edge-vertices. Integral homotopy and rational equivariant homology are different claims; no integral decomposition of the automorphism lattice is asserted.

Fix the graph-vertex encoding \(v\in\{0,\ldots,7\}\), with three bits. Index graph edges in the order obtained from the pairs \((v,v\mathbin{\mathrm{xor}}2^j)\), for \(v<v\mathbin{\mathrm{xor}}2^j\), scanning \(v=0,1,\ldots,7\) and \(j=0,1,2\). This gives the twelve edges
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),
(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
Here the integer bit operation is an implementation convention, not an additional mathematical hypothesis.

## Proof
**1. An exhaustive finite discrete-Morse certificate.** A minimal nonface of \(K\) is precisely a three-edge matching of \(Q_3\). Exhaustively choose three distinct members of its twelve-edge list and retain exactly those whose six endpoints are distinct. There are exactly \(44\) such triples. Test all \(2^{12}=4096\) edge masks against these \(44\) triples. Precisely \(601\) masks are faces, including the empty face, with augmented face vector
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)
=(1,12,66,176,222,108,16).
\]
This is a complete finite enumeration, not a sample.

In the indicated graph-edge order, use the fixed pivot permutation of edge indices
\[
(2,10,11,5,0,4,9,6,7,3,8,1).
\]
At each successive pivot \(j\), pair every currently unpaired lower face \(F\) not containing edge \(j\) with its coface \(F\cup\{j\}\), provided both are still unpaired. The resulting matching has \(296\) pairs and nine unpaired three-dimensional faces; one pair is the augmented pair between the empty face and the vertex indexed \(2\). Discard that augmented pair. On the ordinary nonempty face poset there are \(295\) pairs, a single critical vertex (edge index \(2\)), and nine critical three-simplices; there are no other critical nonempty cells. In integer mask encoding, the nine critical three-simplices are
\[
51,105,177,1186,1289,1314,2569,2577,2720.
\]

Orient the entire ordinary Hasse diagram upward across unmatched cover relations and downward across matched relations. The packaged verifier constructs all arrows between the \(600\) nonempty faces and performs complete topological sorting, visiting all \(600\) vertices. Thus there is no closed gradient path; acyclicity is verified for the actual specified matching, not assumed from the greedy algorithm. Discrete Morse theory produces a CW model with precisely one zero-cell and nine three-cells, and no cells in other positive dimensions. Every three-cell therefore attaches to the single zero-cell, yielding exactly \(\bigvee^9 S^3\). This proves the integral homotopy assertion and excludes torsion.

**2. The complete symmetry character.** The cube automorphisms consist of the \(48\) maps
\[
g_{\sigma,b}: (x_0,x_1,x_2)\longmapsto
(x_{\sigma(0)}+b_0,\ x_{\sigma(1)}+b_1,\ x_{\sigma(2)}+b_2),
\]
where addition is modulo two, \(\sigma\in S_3\), and \(b\in\{0,1\}^3\). Every cube automorphism has this form, since the image of one vertex and the permutation of its three incident edges determine it.

Since reduced homology is concentrated in degree three, the reduced simplicial Lefschetz formula gives, for every graph automorphism \(g\),
\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=\sum_{F\in K,\ gF=F}(-1)^{|F|}\operatorname{sgn}(g\mid_F),
\]
where the empty face contributes one and the sign refers to the induced permutation of the ordered edge-vertices of the face. The independent exhaustive calculation in `verify.py` evaluates this integer for all \(48\) automorphisms.

For the proposed rational module \(P\oplus(\epsilon\otimes U)\oplus(\epsilon\otimes\bigwedge^2 U)\), the character is
\[
\chi(g_{\sigma,b})
=\#\operatorname{Fix}(\sigma)
+\operatorname{sgn}(\sigma)
\bigl(\operatorname{tr}U(g_{\sigma,b})
+\operatorname{tr}\bigwedge^2U(g_{\sigma,b})\bigr).
\]
The signed coordinate module \(U\) has \(Ue_i=(-1)^{b_j}e_j\) whenever \(\sigma(j)=i\). Hence both traces on the right are computed by elementary signed-permutation matrices, independently of simplicial chain calculations. The verifier confirms exact equality with the Lefschetz character for every one of the \(48\) group elements; the character histogram (character value : number of elements) is
\[
-1:6,\qquad 0:16,\qquad 1:15,\qquad 3:10,\qquad 9:1.
\]
As rational representations of a finite group are semisimple and their characters distinguish isomorphism classes, the stated representation follows.

## Verification
Run `python3 verify.py` using the provided standalone standard-library script. Its exact observed output is embedded as `verification_output.json`. It reconstructs the edge set and all \(44\) minimal nonfaces, enumerates all \(601\) augmented faces, checks the complete ordinary Hasse matching and its acyclicity, cross-checks the mod-two boundary ranks in dimensions one through five as \((11,55,121,92,16)\), and checks all \(48\) automorphism characters. The finite checks are exhaustive over the stated exact graph; no conjectural extrapolation is used.

## Relationship to prior work
Linusson, Shareshian and Welker determined the non-matching complex of the *complete* bipartite graph \(K_{4,4}\), which has the homotopy type \(\bigvee^9S^3\). Their theorem alone cannot determine the homotopy type of the proper edge-restricted complex on \(Q_3\), nor its complete \(B_3\)-representation. Holmsen and Lee prove broad Leray-number vanishing, not this exact classification. Shan and Wang (first posted September 2, 2026) prove that adding edges while preserving bipartiteness injects the relevant top-degree homology; their result bounds the cube's top-degree rank above by nine but does not establish its equality, full homotopy type, or character. The cube's ordinary matching, discrete-Morse, and cut complexes are distinct constructions, even though they share the underlying graph. The present calculation identifies a sparse graph attaining the complete-bipartite top-homology rank and resolves its natural full cube symmetry action.

## Limitations
This is an exact result for \(Q_3\) only, not a theorem for higher-dimensional hypercubes or crown graphs on larger parts. The proof of homotopy uses a complete finite certificate rather than a symbolic formula in a size parameter. The representation is determined over \(\mathbb Q\); integral module extensions and integral equivariant homotopy are not classified. The documented literature comparisons do not prove global uniqueness of the statement; unindexed equivalent work remains a residual risk.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621 (initial public submission September 2, 2026), especially Theorems 2.1 and 2.3. https://arxiv.org/abs/2609.02621
2. S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (2004), Journal of Algebraic Combinatorics 27 (2008), 331–349, especially Theorem 1.4 and Conjecture 1.15. https://arxiv.org/abs/math/0410345
3. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (2020), especially the bipartite Leray bound. https://arxiv.org/abs/2003.11270
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
