# A two-torsion window in bidirected complete-bipartite multipath topology

## Finding
Let \(B_{2,n}\) be the directed graph with vertices \(u_0,u_1,v_1,\ldots,v_n\) and both arrows \(u_i\to v_j\) and \(v_j\to u_i\) for each \(i\in\{0,1\}\) and \(1\le j\le n\). Let \(X_n\) be its *multipath complex*: a set of arrows is a simplex precisely when every nontrivial component of its directed subgraph is a directed simple path. Write \(M(\mathbb Z/2,2)=S^2\cup_{\deg 2}e^3\) for the degree-two Moore space. Then the following are integral homotopy equivalences, for exactly the six specified integers:

\[
\begin{aligned}
X_3&\simeq S^1\vee\bigvee^{6}S^2,\\
X_4&\simeq \bigvee^{7}S^2\vee M(\mathbb Z/2,2),\\
X_5&\simeq M(\mathbb Z/2,2)\vee\bigvee^{31}S^3,\\
X_6&\simeq\bigvee^{169}S^3,\\
X_7&\simeq\bigvee^{491}S^3,\\
X_8&\simeq\bigvee^{1105}S^3.
\end{aligned}
\]

Thus the second integral homology has exactly one order-two summand at \(n=4,5\), but none at \(n=3,6,7,8\). In particular, the rational and mod-two Betti numbers alone do not determine the homotopy type at the two intermediate parameters.

## Assumptions and scope
All arrows are distinct, there are no loops, and antiparallel arrows may coexist in the ambient directed graph but not in a multipath. Every selected vertex has at most one incoming and one outgoing arrow; all selected directed cycles, including two-cycles and four-cycles, are forbidden. Every selected arrow is incident with one of the two vertices \(u_0,u_1\); hence a simplex contains at most four arrows and has dimension at most three. The assertion is **finite** and concerns only \(3\le n\le8\). It makes no claim at \(n=2\) or \(n\ge9\).

## Proof
The accompanying `CHECK.py` exhaustively constructs the face poset in two ways for each parameter, first by selecting up to four arrows and checking incoming/outgoing uniqueness and absence of directed cycles, then by recursively extending valid faces and checking the same condition. They agree exactly, and the face counts in ascending cardinality \(0,1,2,3,4\) are given below. No larger face is possible by the four available incoming/outgoing slots at the two vertices of the small bipartition class.

Order the arrows with the outgoing arrows from \(u_0\), then those from \(u_1\), followed by the arrows entering \(u_0\) and then those entering \(u_1\), each block increasing in \(j\). Starting with the *augmented* face poset, at each arrow in this order, match every still-unmatched face not containing the arrow with its one-arrow extension, if both are still unmatched. This is an acyclic discrete-Morse matching: the checker orients every unmatched codimension-one face incidence downwards and every matched incidence upwards, and proves the entire directed incidence graph acyclic by a complete topological sort. A matched empty-face/vertex pair is interpreted using reduced Morse theory; restoring a base point gives the ordinary homotopy type.

The critical-cell counts by simplex dimension are, in order, \((c_1,c_2,c_3)=(1,6,0),(0,9,2),(0,7,38),(0,13,182),(0,21,512),(0,31,1136)\) for \(n=3,4,5,6,7,8\). There are no other critical cells in positive dimensions. In particular, for \(n\ge4\) the resulting based Morse CW complex has only two-cells and three-cells, and its two-skeleton is a wedge of two-spheres.

The integral cellular differential is reconstructed with signs, not merely with field ranks. For a lower simplex \(a\) paired upwards with a higher simplex \(b\), the elementary cancellation relation substitutes \(a=-[a:b]\sum_{a'\ne a}[a':b]a'\), where \([a':b]\in\{0,1,-1\}\) is the oriented simplicial incidence coefficient. Recursing along the acyclic gradient graph until critical lower cells are reached gives each full integral Morse boundary column. Lower simplices paired downwards project to zero. This is precisely the integer algebraic-Morse cancellation formula, and the recursion terminates because the complete incidence orientation was checked acyclic.

For \(n=3\), the Morse boundary from the six two-cells to the single one-cell is exactly zero. Since maps from a circle into itself are classified by degree, each two-cell attaches nullhomotopically. For \(n=4\), the integer matrix from the two three-cells to nine two-cells has rank two with Smith factors \(1,2\). A unit entry, a two-by-two minor of determinant \(-2\), and rank one modulo two give these exact factors. For \(n=5\), the matrix from 38 three-cells to seven two-cells has rank seven and Smith factors \(1,1,1,1,1,1,2\): a seven-by-seven minor has determinant \(-2\), whereas the mod-two rank is six. In each case, the minors together with mod-two rank prove the Smith factors without assuming that a field computation determines integral torsion.

For \(n=6,7,8\), the respective Morse matrices have sizes \(13\times182\), \(21\times512\), and \(31\times1136\). In each case, the certificate gives specific columns forming a square integral minor of determinant \(\pm1\), checked using exact fraction-free integer arithmetic. Thus the differential is split surjective over \(\mathbb Z\), and all its nonzero Smith factors equal one. The remaining three-cell counts are exactly \(169,491,1105\). The complete signed matrices, critical simplex masks, minor witnesses, acyclicity witnesses and independent field-rank checks are reproducibly generated in `MORSE_CERTIFICATE.json` by `CHECK.py`.

Finally, the two-skeleton for \(n\ge4\) is a wedge of simply connected two-spheres, and maps from a two-sphere to that wedge are classified by their integral degree vector via the Hurewicz theorem. Integer changes of bases in the two- and three-cell groups can therefore be realized by homotopy equivalences and cellular attaching-map operations. The stated Smith normal forms give the displayed wedges of spheres and degree-two Moore spaces. This establishes actual integral *homotopy types*, not only integral homology groups.

## Verification
For the six parameters, the complete augmented face counts are respectively \(115,313,711,1417,2563,4305\), and the corresponding acyclic matching pairs number \(54,151,333,611,1015,1569\). The independent direct simplicial boundary calculation over \(\mathbb F_2\) agrees exactly with the mod-two homology implied by every integral Morse matrix: the reduced Betti vectors in dimensions zero through three are \((0,1,6,0)\), \((0,0,8,1)\), \((0,0,1,32)\), \((0,0,0,169)\), \((0,0,0,491)\), and \((0,0,0,1105)\).

Execute `python3 CHECK.py --verify MORSE_CERTIFICATE.json` using the Python standard library. The final success marker is `BIDIRECTED_K2N_INTEGRAL_MOORE_WINDOW_VERIFIED`. The certificate contains exact entries rather than floating-point approximations. It does not use any precomputed external log or mathematical table.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith [1] study multipath complexes and, in particular, compute the Euler characteristic of **one-way** oriented complete bipartite digraphs, whose complexes are matching/chessboard complexes. The present graph has both arrows on every bipartite edge and hence contains directed two-cycles and four-cycles in the ambient digraph; its face condition and homotopy conclusions are different. Caputi, Collari and Ramos [2] compare multipath and matching complexes for acyclic digraphs, so their matching-complex reduction does not apply here. The later bidirectional-graph paper [3] treats paths and polygons and does not state the present two-by-\(n\) complete-bipartite classification. The closest accessible online result on *bidirected double stars* concerns a tree, rather than the cyclic complete bipartite graph studied here. No covering result was found in the accessible records; this is not a proof that no unindexed or implicit equivalent exists.

## Limitations
The computation and homotopy classification are exhaustive only for the six stated values, not an induction over all \(n\). The observed disappearance of the Moore summand after \(n=5\) is not claimed to continue indefinitely. Other multipath graph conventions, particularly allowing directed cycles or orienting each edge only one way, give different complexes. No integral action of graph automorphisms or claim about higher homotopy groups is included. Public-literature and repository access do not guarantee bibliographic completeness; independent audit has not been performed.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first submitted 2022-08-09), especially Definition 2.2, Section 3.2 and Section 4. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (first submitted 2024-01-02), Theorem 4.20 and Section 4. https://arxiv.org/abs/2401.01248
3. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first submitted 2026-01-09), introduction and Section 2. https://arxiv.org/abs/2601.05670
