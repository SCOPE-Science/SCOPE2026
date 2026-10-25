# Full leaf-symmetry homology of bidirected double-star multipath complexes

## Finding
Let \(a,b\ge3\), and let \(X_{a,b}\) be the simplicial multipath complex of the graph obtained by orienting each edge of the double star with \(a\) and \(b\) leaves at its adjacent hubs in both directions. Its arcs are simplicial vertices; an arc set is a face exactly when all connected components are directed vertex-simple paths or isolated vertices. The group \(G=S_a\times S_b\) acts by permuting the respective leaf sets.

Let \(V_t=\ker(\mathbb Z^t\xrightarrow{\sum}\mathbb Z)\) be the integral augmentation lattice of \(S_t\). Let \(C_t\) denote the bipartite crown graph with vertices \(u_1,\ldots,u_t,v_1,\ldots,v_t\) and edges \(u_iv_j\) for \(i\ne j\), acted on by simultaneous permutation of the labels; set \(A_t=H_1(C_t;\mathbb Z)\), its integral cycle lattice. With the exterior tensor-product action,
\[
\widetilde H_q(X_{a,b};\mathbb Z)\cong
\begin{cases}
(V_a\boxtimes V_b)^{\oplus2},&q=2,\\
A_a\boxtimes A_b,&q=3,\\
0,&q\notin\{2,3\}.
\end{cases}
\]
These are isomorphisms of actual integral \(G\)-modules, not merely equalities of ranks or rational characters.

Write \(f(\sigma)\) for the number of fixed points of a leaf permutation \(\sigma\), and \(p(f)=f^2-3f+1\). The complete rational characters on the two homology groups are
\[
\chi_2(\sigma,\tau)=2(f(\sigma)-1)(f(\tau)-1),\qquad
\chi_3(\sigma,\tau)=p(f(\sigma))p(f(\tau)).
\]
For \(a=b=t\), the full graph automorphism group is \((S_t\times S_t)\rtimes\langle h\rangle\), where \(h\) exchanges the hubs and their two identically indexed leaf sets. On the center-exchanging coset,
\[
\boxed{\chi_2((\sigma,\tau)h)=0,\qquad
\chi_3((\sigma,\tau)h)=p(f(\sigma\tau)).}
\]
The choice of whether the product is \(\sigma\tau\) or \(\tau\sigma\) does not affect fixed-point counts or this formula. For \(t\ge4\), \(A_t\otimes\mathbb Q\) decomposes as \(S^{(t-2,2)}\oplus S^{(t-2,1,1)}\); for \(t=3\) it is the one-dimensional sign representation.

## Assumptions and scope
Every graph is finite, with all oppositely oriented arrows present on every undirected edge. Opposite arrows on one edge cannot both lie in a multipath. A selected arc set must have indegree and outdegree at most one at each vertex. The graph is a bidirected tree, so those restrictions and exclusion of opposite pairs are sufficient: the only possible directed cycles would be two-cycles. All homology is reduced simplicial homology with integral coefficients unless a rational character is indicated. The formulas apply to all positive-dimensional reduced homology for every \(a,b\ge3\). For unequal leaf counts, the full automorphism group is \(S_a\times S_b\); for equal counts it has the additional hub exchange.

## Proof
**1. The invariant crown-graph core.** Delete both central arrows. The subcomplex \(Z\) is the join \(C_a*C_b\): at each center there is at most one incoming and one outgoing leaf arrow, with distinct leaves if both are present. Therefore the bidirected-star complex is exactly the one-dimensional crown graph \(C_t\). When \(t\ge3\), \(C_t\) is connected; its integral homology is free in degree one, canonically \(A_t\), with rank \(t(t-1)-2t+1=t^2-3t+1\). The reduced join homology theorem, natural under separate factor permutations, gives
\[
\widetilde H_3(Z;\mathbb Z)=A_a\boxtimes A_b,
\quad \widetilde H_q(Z;\mathbb Z)=0\quad(q\ne3).
\]
There are no torsion terms because both graph cycle lattices are free.

**2. The two invariant cone attachments.** Write the two central arrows as \(e_+\) and \(e_-\). They are incompatible. Faces containing exactly \(e_+\) are its cone over a link \(L_+\cong K_{a,b}\), because the chosen leaf arrows must point into one hub and out of the other, and at most one arrow from either collection can be chosen. Likewise \(L_-\cong K_{a,b}\), with the orientations interchanged. Both links are subcomplexes of \(Z\); no simplex contains both central arrows. Thus \(X_{a,b}=Z\cup(e_+*L_+)\cup(e_-*L_-)\), an equality of simplicial complexes natural under \(G\). The relative quotient is the wedge \(X_{a,b}/Z\cong\Sigma L_+\vee\Sigma L_-\) (cones with their bases collapsed).

**3. Integral link modules and exact sequence.** For a complete bipartite graph \(K_{a,b}\), orient every edge from the first part to the second. Its integral cycle lattice is exactly the collection of \(a\)-by-\(b\) integer matrices with zero row sums and zero column sums. The map \(V_a\otimes V_b\to H_1(K_{a,b};\mathbb Z)\) sending \((e_i-e_{i'})\otimes(e_j-e_{j'})\) to the corresponding signed four-edge cycle is an integral basis isomorphism: deleting one chosen row and one column provides independent integer coordinates, and the omitted entries are forced by the vanishing-sum conditions. This is \(S_a\times S_b\)-equivariant. Both link first-homology lattices are therefore \(V_a\boxtimes V_b\). Since their higher homology vanishes,
\[
H_q(X_{a,b},Z;\mathbb Z)\cong
\begin{cases}(V_a\boxtimes V_b)^{\oplus2},&q=2,\\0,&q\ne2.\end{cases}
\]
The long exact sequence for the pair, naturally equivariant with integral coefficients, now yields \(H_3(Z)\cong H_3(X_{a,b})\) and \(H_2(X_{a,b})\cong H_2(X_{a,b},Z)\); all other reduced groups vanish. No splitting of a nontrivial extension is needed: the isomorphisms occur in separate degrees.

**4. Rational characters of leaf permutations.** For \(\sigma\in S_t\), its trace on the augmentation lattice \(V_t\otimes\mathbb Q\) is \(f(\sigma)-1\). The equivariant augmented chain exact sequence of the connected crown graph gives \([A_t]=[\mathbb Q[E(C_t)]]-[\mathbb Q[V(C_t)]]+[\mathbb Q]\) in the representation ring. A fixed crown edge has two distinct fixed labels, giving \(f(\sigma)(f(\sigma)-1)\) fixed edges, while there are \(2f(\sigma)\) fixed vertices. Thus the trace on \(A_t\) is \(p(f(\sigma))\). Characters multiply under exterior tensor products and add under direct sums, establishing the two stated formulas. The symmetric-group decomposition follows from the standard ordered-distinct-pairs permutation representation: over \(\mathbb Q\), removing the two vertex permutation modules and restoring the trivial module yields \(S^{(t-2,2)}\oplus S^{(t-2,1,1)}\) for \(t\ge4\), and the sign module for \(t=3\).

**5. The full balanced automorphism group.** When \(a=b=t\), the hub swap \(h\) interchanges the two links and hence interchanges the two direct summands in \(H_2(X_{t,t})\). Every linear map interchanging two complementary summands has zero trace, also after leaf permutations. On \(H_3\), the swap exchanges the factors of \(C_t*C_t\); the symmetry sign in the join Künneth is \((-1)^{(1+1)(1+1)}=+1\) because both contributing cycles are one-dimensional. It therefore acts as the ordinary tensor-factor flip on \(A_t\otimes A_t\). The trace of \((\sigma\otimes\tau)\) followed by factor interchange equals \(\operatorname{tr}(\sigma\tau\mid A_t)\), by a basis calculation. Step 4 supplies this trace as \(p(f(\sigma\tau))\). These are the complete characters of the full group in both degrees. \(\square\)

## Verification
The standalone Python 3 file `verify_double_star_equivariance.py` independently enumerates every candidate arc subset, checks directed-path admissibility, and computes the signed augmented simplicial Lefschetz number for 72 elements of the full center-swapping group at \((a,b)=(3,3)\), and all 144 leaf permutations at \((3,4)\). The observed Lefschetz numbers agree with \(\chi_2-\chi_3\) element by element, including all balanced hub swaps. Independently, exact mod-two boundary-matrix ranks give reduced Betti ranks \((8,1)\) in degrees \((2,3)\) at \((3,3)\), and \((12,5)\) at \((3,4)\). The script prints `VERIFY_OK` after all checks. These finite computations are corroboration; the integral equivariant exact-sequence proof above establishes the statements for all parameters.

## Relationship to prior work
Caputi, Collari, and Smith (2026) introduce and calculate bidirectional-path and bidirectional-polygon multipath complexes, not the double-star leaf-permutation representations. The published *Homotopy classification of bidirected double-star multipath complexes* establishes the nonequivariant homotopy types of \(X_{a,b}\) and supplies a crown-graph and cone-attachment decomposition. Those constructions are used here and are not claimed to be new. The additional assertion is a complete integral homology-module classification and, in the balanced case, explicit characters for the previously unaccounted center-exchanging automorphisms. The 2024 multipath-homotopy paper treats different graph families, and the 2024 quiver-minor comparison concerns digraphs without oriented cycles; this bidirected family has two-cycles.

## Limitations
Only the natural graph automorphism action on reduced integral homology is classified; the theorem does not produce a \(G\)-equivariant wedge-of-spheres homotopy decomposition, determine equivariant stable homotopy groups, or classify arbitrary bidirected trees. Its novel representation calculation refines a published nonequivariant decomposition and uses that decomposition as an essential prerequisite. Equivalent representations in unindexed literature cannot be ruled out. Finite tests do not substitute for the universal proof; no independent external audit has been performed.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, publicly posted 2026-01-09, https://arxiv.org/abs/2601.05670.
2. *Homotopy classification of bidirected double-star multipath complexes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-homotopy-classification-of-bidirected-double-star-multipath-comp--9525e342e100.
3. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, Mathematika 70 (2024), e12235, preprint arXiv:2208.04656, https://arxiv.org/abs/2208.04656.
4. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248, https://arxiv.org/abs/2401.01248.
