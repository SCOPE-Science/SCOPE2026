# The Paley-\(11\) neighborhood complex: \(21\) two-spheres and hidden \(660\)-element symmetry

## Finding
Let \(T\) be the quadratic-residue tournament on \(\mathbb F_{11}\), oriented by \(a\longrightarrow b\) exactly when \(b-a\in Q=\{1,3,4,5,9\}\) modulo \(11\). Let \(K=\mathcal N^{+}(T)\) be its out-neighborhood simplicial complex: a nonempty set \(\sigma\) is a face exactly when some vertex of \(T\) sends an arc to every vertex of \(\sigma\). Then
\[
|K|\simeq\bigvee^{21}S^2.
\]
In particular \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{21}\), with other reduced integral homology zero.

The eleven maximal faces \(a+Q\) form the classical \(2\)-\((11,5,2)\) biplane. Accordingly the *full simplicial automorphism group* \(G=\operatorname{Aut}(K)\), not merely the tournament automorphism group, has \(660\) elements and is isomorphic to \(\operatorname{PSL}_2(11)\) (the abstract identification is independently recorded in Brown's biplane account). Its trace on \(\widetilde H_2(K;\mathbb Q)\) is as follows:

| Element order | Number of elements | Degree-two trace |
| ---: | ---: | ---: |
| 1 | 1 | 21 |
| 2 | 55 | -3 |
| 3 | 110 | 0 |
| 5 | 264 | 1 |
| 6 | 110 | 0 |
| 11 | 120 | -1 |

The character has average \(0\) and self-inner-product \(2\). On complexification, the degree-\(21\) representation is the multiplicity-free direct sum \(V_{10}^{\mathrm{other}}\oplus V_{11}\), where \(V_{11}\) is the unique complex irreducible representation of dimension \(11\) of \(G\), and \(V_{10}^{\mathrm{other}}\) is the ten-dimensional irreducible **other than** the augmentation constituent of the natural eleven-point permutation module.

By contrast, the natural orientation-preserving affine tournament subgroup \(H=\mathbb F_{11}\rtimes Q\) has order \(55\) and fixes exactly one rational degree-two homology class. Thus, for geometric quotients,
\[
\widetilde H_j(|K|/G;\mathbb Q)=0\quad\text{for all }j\geq0,
\qquad
\dim_{\mathbb Q}\widetilde H_2(|K|/H;\mathbb Q)=1.
\]
All other reduced rational homology groups of \(|K|/H\) vanish.

## Assumptions and scope
All faces are ordinary **unordered** subsets of the eleven residues; the empty face is excluded from the geometric complex and included only implicitly in reduced homology. The out-neighborhood convention is explicitly \(a+Q\); reversing all tournament arcs produces an isomorphic complex by relabeling \(a\mapsto-a\). The group \(G\) is the full group of vertex permutations preserving the *simplicial complex*, which is larger than the tournament automorphism group \(H\). Character statements use ordinary rational simplicial homology and its complexification, and quotient statements use geometric orbit spaces with rational coefficients, not orbit sets of individual simplices.

The classification belongs to simplicial/algebraic topology (MSC2020 \(55U10\)); its anchor is the directed-neighborhood/Hom-complex program first publicly posted on 2021-08-24 (Dochtermann--Singh, arXiv:2108.10948v1). Older biplane design theory is supporting background, not the dated topical anchor.

## Proof
**1. Faces and integral homotopy.** The facets are precisely \(F_a=a+Q\), for \(a=0,\ldots,10\). Direct complete enumeration of their downward closure gives the face vector \((11,55,110,55,11)\), hence \(242\) nonempty faces. Form a discrete-Morse matching as follows. Start with all faces unmatched; for pivots \(v=0,1,\ldots,10\), in increasing face dimension and then lexicographic order, match any currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both remain unmatched. The resulting matching has exactly \(110\) pairs and exactly \(22\) critical faces: the vertex \(\{0\}\) and \(21\) triangles.

For the complete Hasse graph of \(K\), orient each incidence from a larger face to a codimension-one smaller face, except reverse each matched incidence. There are exactly \(715\) oriented incidences. The supplied standalone checker performs a complete topological-sort traversal of all \(242\) face nodes and finds no directed cycle. This proves the matching is acyclic, rather than merely a numerical Morse count. The simplicial discrete-Morse theorem therefore gives a CW model with one zero-cell, no one-cells, \(21\) two-cells and no other cells. Since each two-cell must attach to the point, this CW model is a wedge of \(21\) two-spheres. This also proves integrality and the claimed absence of torsion.

**2. Full group.** A simplicial automorphism must preserve the eleven maximal five-element faces, and conversely any vertex permutation preserving those blocks is a simplicial automorphism. An exhaustive backtracking enumeration assigns images to the vertices in order \(0,1,\ldots,10\), pruning any partial injection that changes membership of a completed face of size at most five. Its surviving counts at depths \(0\) through \(11\) are exactly \((1,11,110,660,660,660,660,660,660,660,660,660)\). All \(660\) terminal maps are distinct block-preserving permutations, establishing the full order without relying on a black-box graph-isomorphism package. Brown identifies this familiar biplane group as \(\operatorname{PSL}_2(11)\).

**3. Degree-two character.** For each \(g\in G\), take the signed trace on oriented simplicial chains. If \(g\) preserves a face setwise, its contribution to the Lefschetz number is \((-1)^{\dim\sigma}\) times the sign of its permutation of that face's ordered vertices; otherwise its contribution is zero. Because step 1 leaves only \(H_0\cong\mathbb Q\) and \(H_2\cong\mathbb Q^{21}\), the degree-two homology character equals the simplicial Lefschetz number minus \(1\). This finite signed computation is carried out for **all** \(660\) enumerated automorphisms, returning the complete element-order table above.

The character sum is \(21-165+264-120=0\). Its squared sum is \(441+495+264+120=1320\), and hence its character inner product is \(2\). The ordinary character-orthogonality theorem implies precisely two distinct irreducible complex constituents, each of multiplicity one. The known irreducible degrees of \(\operatorname{PSL}_2(11)\) are \(1,5,5,10,10,11,12,12\); with zero trivial multiplicity and total dimension \(21\), the two dimensions must be \(10\) and \(11\). The inner product with the eleven-point permutation augmentation character \(g\mapsto\#\operatorname{Fix}_{\{0,\ldots,10\}}(g)-1\) is **zero**, so the ten-dimensional constituent is the other irreducible. This proves the stated decomposition without assuming it from a matching of numerical dimensions.

**4. Quotient comparison.** The affine maps \(x\mapsto a+bx\), \(a\in\mathbb F_{11}\), \(b\in Q\), form a subgroup \(H\) of order \(55\) preserving the tournament and each family of neighborhood facets. Restricted to \(H\), the degree-two character is \(21\) at the identity, \(-1\) at the ten nonidentity translations, and \(1\) at the forty-four remaining elements. Its average is \((21-10+44)/55=1\), whereas the full \(G\)-average is \(0\). For a finite simplicial group action, barycentric subdivision removes inversions and the rational transfer/averaging argument identifies quotient rational homology with the invariant homology. Since \(K\) is connected and has reduced rational homology only in degree two, these averages give exactly the quotient claims.

## Verification
Execute `python3 verify_paley11.py` from this package. The program uses only the Python standard library and checks the downward-closed faces, block intersections, the explicit discrete-Morse matching, complete directed-Hasse acyclicity, independent mod-two boundary ranks \((10,45,44,11)\), exhaustive full-group enumeration, all signed Lefschetz traces, character inner products, and the affine subgroup's trace distribution. Its terminal marker is `PALEY11_BIPLANE_21S2_FULL660_EQUIVARIANT_CHECKS_OK`. All required assertions must pass before that marker appears.

## Relationship to prior work
Dochtermann and Singh (arXiv:2108.10948v1, August 24, 2021; Sections 4--5 of the readable later text) introduced the relevant directed out-neighborhood complex, proved its equivalence to a directed Hom complex, and obtained general vanishing/connectivity results. Their text does not specify this eleven-vertex Paley complex or its homology representation; the general bounds do not imply its integral wedge type or the full-group character. Côté (arXiv:2301.03739v1) treats Dowker complexes and equivalences of finite relations, not this exact invariant. Brown (2004) supplies the blocks and full \(660\)-element symmetry group of the \((11,5,2)\) biplane; that combinatorial result is taken as known and is **not** claimed as new. Govc--Levi--Smith (2021) study directed flag/tournament complexes, a different construction.

A directed flag simplex requires a transitive subtournament, whereas an out-neighborhood simplex requires a common predecessor; for example, \(\{0,1,2\}\) is a cyclic triple contained in \(F_8\), and \(\{0,1,3\}\) is a transitive triple not contained in any \(F_a\). Thus published directed-flag invariants cannot be substituted for the present complex's results. Public indexed calculations of tournament neighborhood complexes through seven vertices do not cover the eleven-vertex instance. No exact homotopy-and-full-character statement for this complex was identified in the inspected primary full texts, public mathematical research records, or targeted literature searches. This negative search is not a claim of exhaustive novelty.

## Limitations
The Morse equivalence is an ordinary, not an equivariant, wedge decomposition. The irreducible decomposition is stated over \(\mathbb C\) after complexifying rational homology; no integral lattice decomposition, equivariant homotopy equivalence, or integral quotient homology is asserted. The quotient conclusions concern rational coefficients only. An unindexed equivalent computation or a non-obvious deduction from design-theoretic literature remains possible; independent mathematical audit has not been performed.

## References
- A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948v1 (first submitted 2021-08-24), Section 4 and Theorem 4.3. https://arxiv.org/abs/2108.10948
- E. Brown, *The Fabulous (11, 5, 2) Biplane*, Mathematics Magazine **77** (2004), 87--100; block construction and full automorphism group. https://paperzz.com/doc/8964847/the-fabulous--11-5-2--biplane
- D. Desjardins Côté, *Dowker Complexes and filtrations on self-relations*, arXiv:2301.03739v1 (2023-01-10). https://arxiv.org/abs/2301.03739
- D. Govc, R. Levi and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, Journal of Applied and Computational Topology **5** (2021), 313--337. https://doi.org/10.1007/s41468-021-00068-0
- OEIS A003882, irreducible complex-character degrees of \(\operatorname{PSL}_2(11)\), with ATLAS reference. https://oeis.org/A003882
