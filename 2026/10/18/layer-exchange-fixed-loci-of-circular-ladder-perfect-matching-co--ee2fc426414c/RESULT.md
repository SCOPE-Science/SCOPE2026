# Layer-exchange fixed loci of circular-ladder perfect-matching complexes

## Finding
For every integer \(n\geq3\), let \(L_n=C_n\square K_2\), let \(\mathcal M_p(L_n)\) be the simplicial complex of all subsets of perfect matchings of \(L_n\), and let \(\tau\) exchange its two cycle layers. The geometric fixed-point set has homotopy type
\[
|\mathcal M_p(L_n)|^{\tau}\simeq
\begin{cases}
\{\mathrm{point}\},&n\text{ odd},\\
\bigvee^2 S^{n/2-1},&n\text{ even}.
\end{cases}
\]
In particular, for every even \(n\geq4\) the fixed set has precisely two independent integral homology classes in degree \(n/2-1\), and has no other nonzero reduced integral homology.

## Assumptions and scope
The cycle \(C_n\) is a simple cycle with vertices indexed by \(\mathbb Z/n\mathbb Z\); \(n\geq3\). The ladder has vertices \((i,a)\) for \(a\in\{0,1\}\), horizontal edges \(\{(i,a),(i+1,a)\}\), and rungs \(\{(i,0),(i,1)\}\). A face of \(\mathcal M_p(L_n)\) is a collection of graph edges contained in some perfect matching, with the empty face allowed. The involution \(\tau\) exchanges \(a=0\) and \(a=1\). Its fixed-point set is taken on the geometric realization; it is not the induced subcomplex on individually fixed edge-vertices.

For a finite simple graph \(G\), let \(W(G)\) be obtained by attaching exactly one new pendant edge to every vertex of \(G\), and write \(\mathcal M(W(G))\) for the ordinary matching complex (all pairwise disjoint edge sets). The central identification is a homeomorphism of the fixed space with \(|\mathcal M(W(C_n))|\).

## Proof
**1. Orbit-simplex identification.** The involution fixes each rung edge and exchanges the two horizontal edges in each same-position pair. Call the resulting edge orbits \(r_i\) and \(h_i\), respectively. A fixed point in the realization assigns equal barycentric coordinates to both edges of each two-element orbit. By summing coordinates in each orbit, its fixed simplex is linearly homeomorphic to the simplex on the orbit set, provided the union of those orbits is an admissible face.

A union of edge orbits is a partial matching exactly when the chosen \(h_i\) form a matching of the core cycle, and no chosen \(r_i\) meets a chosen \(h_i\) or \(h_{i-1}\). Every such invariant partial matching extends to a perfect matching of \(L_n\): insert each rung at every core index left uncovered. Conversely every face of the perfect-matching complex is a partial matching. Consequently the allowed orbit sets are precisely the matchings of \(W(C_n)\), after identifying \(h_i\) with the core edge \(\{i,i+1\}\) and \(r_i\) with its pendant edge. The barycentric-coordinate maps agree on intersections and yield
\[
|\mathcal M_p(L_n)|^{\tau}\cong |\mathcal M(W(C_n))|.
\]

**2. A general whisker-toggle Morse matching.** Fix any finite simple \(G\) on \(m\geq2\) labeled vertices, and consider nonempty faces \(F\) of \(\mathcal M(W(G))\). Project \(F\) onto its set \(S\) of core edges. Necessarily \(S\) is a matching of \(G\). For each fixed \(S\), the possible pendant-edge subsets are *all* subsets of the pendant edges at vertices not incident with \(S\). If an uncovered vertex exists, choose the least one \(j\) and pair each face omitting its pendant edge with the face obtained by adding it. In the fiber \(S=\varnothing\), omit the pair involving the empty face; this leaves the single pendant-edge vertex at the least core index unpaired. Every fiber with \(S\ne\varnothing\) and an uncovered vertex is completely paired. A fiber with no uncovered vertex consists of a single unpaired face \(S\), where \(S\) is a perfect matching of \(G\).

This is an acyclic face-poset matching: on each fiber, the fixed-pendant-edge toggle is acyclic; across fibers, every directed unmatched downward face relation can only decrease the set of selected core edges, whereas matched upward relations leave it unchanged. Hence no directed cycle can cross fibers and no cycle occurs in a fiber. Thus there is one critical vertex and precisely one additional critical face for each perfect matching of \(G\), of dimension \(m/2-1\). In particular, when \(m\) is even the associated Morse CW complex has only one \(0\)-cell and \(p(G)\) cells in dimension \(m/2-1\), where \(p(G)\) denotes the number of perfect matchings of \(G\). If \(m\) is odd there are no additional cells. For \(m=2\) the single degree-zero case is the standard wedge-of-zero-spheres convention. The stated CW complexes are a point or a wedge of \(p(G)\) spheres in the indicated dimension; all higher attaching maps are constant because there are no intervening cells.

**3. Apply to cycles.** An odd cycle has no perfect matching. Every even cycle has exactly two perfect matchings, the alternating edge subsets starting at even and odd indices. In step 2 take \(G=C_n\): for odd \(n\) only the critical vertex survives, and for even \(n\geq4\) exactly two critical faces, each of size \(n/2\), survive. Combining with step 1 gives the displayed classification for all \(n\geq3\).

## Verification
The independent, standard-library-only script `verify.py` independently enumerates the original circular-ladder perfect matchings and checks the orbit-face identification against the whiskered-cycle incidence model, constructs the displayed acyclic matching, checks its unmatched faces and absence of directed cycles, and independently computes all mod-two reduced Betti numbers by boundary-matrix elimination. The command `python3 verify.py` passes for every \(n\) from \(3\) through \(9\). Its exact outputs are preserved in `verification_output.txt`. In particular, the computed nonzero reduced Betti numbers are two in degrees \(1,2,3\) for \(n=4,6,8\), respectively, with vanishing for odd \(n=3,5,7,9\). These finite checks corroborate the all-parameter combinatorial proof; they are not used in place of that proof.

## Relationship to prior work
Agarwal and Basak (arXiv:2608.30601, initially public August 31, 2026; revised September 2026) determine ordinary, nonequivariant homotopy types of independence and perfect-matching complexes of Möbius and circular ladders. The present object is instead the *geometric layer-exchange fixed-point space* of the circular-ladder perfect-matching complex. Their publicly accessible abstracts do not give this fixed-locus classification. Singh (arXiv:2101.05534, Corollary 3.3) established vertex decomposability of ordinary matching complexes of fully whiskered graphs; this implies a sphere-wedge alternative but does not provide the present exact multiplicity or fixed-locus identification. Vega's arXiv:1909.10406 studies **two-matching** complexes of whiskered cycles, a different degree constraint. The proof here supplies the explicit ordinary-matching multiplicity needed for the fixed-set classification, rather than claiming novelty for the broader pre-existing shellability result.

## Limitations
The theorem determines the geometric fixed-point space under **one specified involution**, not all subgroup-fixed spaces or the full equivariant homotopy type of the original perfect-matching complex. It does not calculate the complete rational representation on homology or assert an equivariant simplicial collapse. The full text of the motivating September 2026 revision could not be inspected through the available lawful routes; a previously unindexed or incidental equivalent fixed-locus calculation remains an originality risk. The provided proof is an internal mathematical argument and has not undergone independent peer review.

## References
1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first submitted August 31, 2026; revised September 2026), https://arxiv.org/abs/2608.30601.
2. Anurag Singh, *Vertex decomposability of complexes associated to forests*, arXiv:2101.05534, Corollary 3.3, https://arxiv.org/html/2101.05534v1.
3. Julianne Vega, *2-matching complexes*, arXiv:1909.10406, https://arxiv.org/html/1909.10406v2.
4. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
