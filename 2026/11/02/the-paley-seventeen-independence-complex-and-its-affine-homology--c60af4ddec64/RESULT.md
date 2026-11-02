# The Paley-seventeen independence complex and its affine homology representation

## Finding
Let \(P_{17}\) be the Paley graph on \(\mathbb F_{17}\), where distinct elements \(x,y\) are adjacent exactly when \(x-y\) is a nonzero square. Write \(X=\operatorname{Ind}(P_{17})\). Then
\[
X\simeq\bigvee^{16}S^2,\qquad \widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{16}.
\]
For the order-136 affine automorphism group \(G=\mathbb F_{17}\rtimes(\mathbb F_{17}^{\times})^2\), acting by \(x\mapsto ax+b\), the entire rational representation is
\[
\widetilde H_2(X;\mathbb Q)\cong\mathbb Q[\mathbb F_{17}]/\mathbb Q\mathbf1.
\]
In particular, its character is \(16\) at the identity, \(-1\) at the 16 nonzero translations, and \(0\) at the remaining 119 group elements. Its affine symmetry quotient satisfies \(\widetilde H_j(X/G;\mathbb Q)=0\) for all \(j\ge0\).

## Assumptions and scope
All graph and simplicial-complex conventions are ordinary, undirected and non-augmented for cell matching. The 17 labels are the integers \(0,\ldots,16\) modulo 17. The nonzero quadratic residues are \(\{1,2,4,8,9,13,15,16\}\). An independent set is a set without adjacent pairs, and the empty face is present abstractly but is excluded from the nonempty face-poset matching. The assertion concerns the natural affine subgroup only; it does not require identifying the full graph automorphism group. The quotient conclusion is over \(\mathbb Q\), not an assertion about integral torsion of the quotient.

## Proof
**Exact homotopy model.** The accompanying dependency-free `checker.py` constructs every independent subset by checking all pairs. It exhaustively certifies that there are no independent four-sets, and that the numbers of nonempty faces in sizes one, two and three are respectively \(17,68,68\). The absence of a four-set also excludes all larger faces.

Here is an explicit deterministic partial matching on the 153 nonempty faces. Maintain a set of unmatched faces. For the vertices \(v=0,1,\ldots,16\), in that order, inspect current unmatched faces \(\sigma\) not containing \(v\), sorted first by cardinality and then lexicographically. If \(\sigma\) and \(\sigma\cup\{v\}\) are both still unmatched, pair those two faces and remove them. This process produces precisely 68 disjoint covering pairs, leaving one singleton face and sixteen three-element faces. It is an *acyclic* matching: the checker constructs all 340 cover relations of the nonempty face poset, orients matched relations upward and every other relation downward, and topologically sorts the entire 153-vertex directed graph. Every face is removed by the topological sort, proving there is no directed cycle. This exhaustive finite certificate verifies all pairs and all possible gradient cycles, not merely sampled cases.

The elementary discrete-Morse theorem gives a CW homotopy model with one zero-cell, no one-cells and sixteen two-cells, and no other cells. Each two-cell attaches to the unique point, hence this CW complex is \(\bigvee^{16}S^2\). In particular the integral homology is torsion-free and is nonzero only in reduced degree two. Independently, the checker obtains mod-two boundary ranks 16 and 52 in dimensions one and two, consistent with the CW calculation.

**Affine symmetry.** Multiplication by a quadratic residue preserves adjacency, so the maps \(x\mapsto ax+b\) form a group of \(17\cdot8=136\) simplicial automorphisms. Since the complex has reduced rational homology only in degree two, the simplicial Lefschetz formula reads \(L(g)=1+\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))\). The checker computes the trace on every oriented simplex by counting setwise fixed simplices with their exact vertex-permutation signs, for all 136 automorphisms, then subtracts 1. It finds the character values \(16,-1,0\) with multiplicities \(1,16,119\), respectively.

There is also a structural verification: a nontrivial translation fixes no face of cardinality at most three, so \(L(g)=0\). A nonidentity multiplier is conjugate by a translation to multiplication about its unique fixed point. Unless the multiplier is \(-1\), it cannot setwise preserve any nonsingleton face of cardinality at most three, and \(L(g)=1\). The involution \(x\mapsto-x\) fixes one vertex and four edges and four triangles setwise; the latter eight simplices each have orientation sign \(-1\), giving \(L(g)=1-(-4)+(-4)=1\). Hence the claimed character holds for every affine map.

The 17-dimensional permutation representation on graph vertices has character equal to the number of fixed vertices. Its augmentation module has character equal to this number minus one, precisely the character just derived. Semisimplicity and equality of rational characters of finite-group representations establish the asserted rational module isomorphism. The augmentation module has no \(G\)-invariants because \(G\) acts transitively on vertices. Rational cellular chains of a finite-group quotient, after barycentric subdivision, identify with the invariant chain complex; averaging is exact in characteristic zero. Thus the quotient has no positive-dimensional reduced rational homology; it is connected, so reduced degree-zero homology also vanishes.

## Verification
Run `python3 checker.py` from the extracted package. The program uses only Python's standard library and checks the quadratic residues, an explicit nonresidue complement isomorphism, the exact 153 faces, absence of larger faces, all 68 pairs and 340 cover incidences, complete acyclicity, independent mod-two boundary ranks, and all 136 oriented Lefschetz traces. Its terminal success marker is `PALEY17_INDEPENDENCE_MORSE_68_PAIRS_AFFINE_136_CHARACTER_OK`. Finite enumeration is logically sufficient here because the theorem concerns one fixed finite graph, and the code exhausts its complete face poset and finite group.

## Relationship to prior work
Deshpande and Singh (2020) develop discrete-Morse classifications for higher independence complexes of complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees. Berghoff (2020) gives a general independence-complex spectral-sequence method. Neither inspected full text treats the Paley graph of order 17 or supplies this equivariant classification. A publicly indexed finding on the Paley-17 **open-neighborhood** complex has different simplices and does not imply the independence-complex statement; a Paley-29 independence-complex calculation concerns a different field order. The self-complementarity of the Paley-17 graph means this result also describes its clique complex: multiplication by any nonsquare, for example \(3\), identifies one with the other. This equivalence was included in the originality search rather than treated as a separate result.

## Limitations
The homotopy equivalence and affine-group representation are proved for this particular 17-vertex graph; no general theorem for other Paley orders is implied. The stated group is the explicitly verified affine subgroup; the character is not asserted for an unverified larger automorphism group. The rational quotient homology conclusion does not determine the integral quotient torsion. Bibliographic searching cannot exclude unindexed prior results, and the indexed neighborhood-complex document could not be inspected in full.

## References
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, submitted 2020-01-15, especially Sections 1–3.
- M. Berghoff, *On the Homology of Independence Complexes*, arXiv:2008.06267, submitted 2020-08-14, especially Sections 1–2.
- Public research record, *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, indexed 2026 (different complex; abstract-level comparison only).
- Public research record, *The Paley-29 independence complex is a wedge of 28 two-spheres and a mod-two Moore space*, indexed 2026 (different graph order).
