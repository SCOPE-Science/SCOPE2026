# Full 144-symmetry homology of a triple complete-graph product

## Finding

For the categorical graph product \(G=K_2\times K_3\times K_3\), let \(X=\operatorname{Ind}(G)\). The full graph automorphism group is
\[\operatorname{Aut}(G)\cong C_2^{\ell}\times(S_3\wr C_2^{\kappa}),\qquad |\operatorname{Aut}(G)|=144.\]
The first involution interchanges the two bipartition layers; the second interchanges the two three-element coordinates. Put \(H=\widetilde H_3(X;\mathbb Q)\). Let \(\mathbf1\), \(\varepsilon\), and \(W\) denote the trivial, sign, and standard two-dimensional rational representations of \(S_3\). If \(U\) is one of these representations, write \(D_-(U)\) for the extension of \(U\boxtimes U\) in which factor interchange acts as minus the ordinary tensor flip. For distinct irreducibles \(U,V\), write \(I(U,V)=\operatorname{Ind}_{S_3\times S_3}^{S_3\wr C_2}(U\boxtimes V)\).

The complete decomposition, including all factor interchange signs, is
\[
H^{\ell=+1}\cong D_-(\mathbf1)\oplus I(\mathbf1,W)\oplus D_-(W),\qquad
H^{\ell=-1}\cong D_-(\varepsilon)\oplus I(\varepsilon,W).
\]
The respective dimensions are 9 and 5. The subgroup \(C_2^{\ell}\times S_3\times S_3\) fixes exactly one dimension of \(H\), but its factor-interchange extension \(\kappa\) negates that line. Thus the full graph-automorphism quotient is rationally acyclic in all positive degrees, even though \(H\) has dimension 14.

## Assumptions and scope

Vertices are \((a,i,j)\) with \(a\in\{0,1\}\) and \(i,j\in\{0,1,2\}\). Distinct vertices are adjacent exactly when all three coordinates differ. The independence complex consists of all subsets containing no such adjacent pair. The result concerns its ordinary simplicial action, not an orientation-twisted action artificially imposed on homology. Statements about the quotient are over \(\mathbb Q\) only; no integral homology of the quotient is asserted. The nonequivariant integral homotopy type \(X\simeq\bigvee^{14}S^3\) follows from Proposition 25 of [1].

## Proof

**Full automorphism group.** The graph is connected and bipartite with two 9-vertex layers. Every automorphism either preserves or exchanges the layers. Within one layer, two distinct grid cells have two common neighbors in the other layer precisely when they share a row or a column; otherwise they have one. The resulting intrinsic relation is the \(3\)-by-\(3\) rook graph. Its automorphism group is \(S_3\wr C_2\): its six maximal three-vertex cliques are the three rows and three columns, and their intersections recover the grid coordinates. A vertex in the opposite layer is uniquely determined by its four-neighbor set, so an automorphism preserving layers is uniquely specified by its action on one layer. All 72 rook-grid automorphisms extend to the original graph, and layer exchange doubles their number to 144.

**Homology concentration.** By Proposition 25 of [1] with the last two complete-graph factors both of order three, the complex is homotopy equivalent to a wedge of 14 three-spheres. Hence rational homology is concentrated in reduced degree three and has dimension 14. No novelty is claimed for this step.

**Exact character.** Fix any of the 144 graph automorphisms \(g\). Partition the 18 vertices into its permutation orbits. Discard any orbit containing adjacent vertices, and form a finite incompatibility graph whose remaining vertices represent the permitted orbits, with an edge between two orbits if their union contains an adjacent pair of original vertices. Let \(F_g\) denote the alternating independent-set sum of this auxiliary graph, including its empty face:
\[F_g=\sum_{A\text{ independent}}(-1)^{|A|}.\]
Each \(g\)-fixed simplicial face is a union of permitted vertex orbits. If it comprises \(k\) orbits and \(s\) original vertices, the sign of the induced permutation on its oriented face is \((-1)^{s-k}\), while its simplicial degree contributes \((-1)^{s-1}\). The combined signed contribution is \((-1)^{k+1}\). Including the empty face in reduced degree minus one gives reduced Lefschetz number \(-F_g\). Since all reduced rational homology lies in degree three, the Lefschetz formula yields \(\operatorname{tr}(g\mid H)=F_g\). This is an exact finite enumeration of the entire character, not a numerical approximation. The attached standard-library checker constructs all 144 permutations, verifies graph adjacency, evaluates every \(F_g\) using exact recursive deletion–contraction, and applies exact rational character orthogonality.

**Restriction and exchange signs.** Under the index-two subgroup without coordinate exchange, the layer-even restriction decomposes as \(\mathbf1\boxtimes\mathbf1\oplus\mathbf1\boxtimes W\oplus W\boxtimes\mathbf1\oplus W\boxtimes W\), and the layer-odd restriction as \(\varepsilon\boxtimes\varepsilon\oplus\varepsilon\boxtimes W\oplus W\boxtimes\varepsilon\), with multiplicity one for each term. Projecting the full 144-element character to the three diagonal isotypic components yields factor-exchange traces \(-1\), \(-2\), and \(-1\) on, respectively, the layer-even \(\mathbf1\boxtimes\mathbf1\), layer-even \(W\boxtimes W\), and layer-odd \(\varepsilon\boxtimes\varepsilon\). Those traces force minus-factor-flip extensions. Each off-diagonal pair induces a single irreducible module of dimension four, giving the stated complete decomposition.

**Quotient.** The only vector fixed by the layer involution and both separate \(S_3\) factors lies in the \(D_-(\mathbf1)\) summand. Factor exchange negates it. Averaging over the finite automorphism group, equivalently using rational transfer for a finite group action, gives \(\widetilde H_j(X/\operatorname{Aut}(G);\mathbb Q)=0\) in all nonnegative degrees. The complex and its orbit space are connected.

## Verification

Execute `python3 verify_triple_product.py` with Python 3.9 or newer. The checker uses the standard library only and enumerates 1,649 nonempty simplices, distributed over dimensions zero through eight as 18, 117, 348, 504, 378, 192, 72, 18, and 2. It independently checks reduced mod-two homology (rank 14 in degree three and zero elsewhere), 144 distinct adjacency-preserving permutations, the full signed rational Lefschetz character, seven nonzero irreducible restriction multiplicities, and the three factor-interchange projector traces. Successful output includes `TRIPLE_PRODUCT_144_EXACT_CHARACTER_AND_PROJECTORS_OK`. The finite-field calculation corroborates, but does not by itself establish, the published integral homotopy equivalence.

## Relationship to prior work

Antolín Camarena and Carnero Bravo [1], Proposition 25 and its proof, give \(\operatorname{Ind}(K_2\times K_n\times K_m)\simeq\bigvee^{f(2,n,m)}S^3\). Specializing their formula gives the 14-sphere nonequivariant homotopy type here. Their theorem does not provide the induced full automorphism character or the difference between separate-coordinate and exchanged-coordinate invariants. The earlier categorical-product work of Goyal, Shukla, and Singh [2] motivates the family without supplying this equivariant answer. Searches for the specific 144-element action, equivalent categorical-product and six-cycle formulations, and quotient invariants located no theorem implying this decomposition; bibliographic incompleteness remains possible.

## Limitations

The representation is over rational coefficients. No new assertion is made about the integral homotopy type, integral symmetry lattice, integral quotient homology, or analogous products with larger factors. The exact finite enumeration proves the stated representation for this 18-vertex graph only; it does not establish a parameter-uniform character theorem. Possible unindexed equivalent calculations have not been excluded by a mathematical uniqueness proof, and independent external validation has not occurred.

## References

[1] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v2 (first posted July 23, 2023), Section 4, Proposition 25. https://arxiv.org/html/2307.12401v2

[2] S. Goyal, S. Shukla, and A. Singh, *Homotopy type of independence complexes of certain families of graphs*, Contributions to Discrete Mathematics 16 (2021), 74–92; arXiv:1905.06926. https://arxiv.org/abs/1905.06926
