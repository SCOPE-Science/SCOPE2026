# Scientific review: integral torsion in folded-cube three-cut complexes

## Correctness — PASS

The proof uses the explicit quotient \(\mathbb F_2^d/\langle\mathbf1\rangle\) and derives all short-cycle properties for every \(d\ge5\). The Alexander dual has a complete one-skeleton, two-edge-path triangles and square tetrahedra, with no larger faces. Each square contributes two genuine free-face collapses, leaving its square-filling disk. All distant pairs contribute separate one-cycles. The square complex is a free two-fold quotient of the simply connected cubical two-skeleton, so \(H_1\cong\mathbb Z/2\); its Euler characteristic determines the free \(H_2\) rank. Integral universal coefficients and combinatorial Alexander duality supply the displayed groups. The standalone code reproduces independent finite checks for \(d=5,6\), not a purported infinite certification.

## Originality — PASS with residual risk

The foundational ordinary cut-complex paper (arXiv:2304.13675) provides the definition, unrelated constructed torsion examples and a triangle-free **two-cut** theorem. Its sequel (arXiv:2407.08158) treats disjoint unions, paths and grids. A closer prior general reduction expresses three-cut homology for graphs with at most two common neighbors using the associated square-completion homology; it does **not** compute that homology for folded hypercubes. The present antipodal-cover calculation supplies the missing integral invariants and a complete explicit infinite-family formula. The published edge-disjoint-square result does not apply because each folded-cube edge lies in at least four squares. A matching result outside inspected indexes remains possible; the rectagraph paper was only examined by abstract.

## Value — PASS

Folded cubes are a canonical family with unusually rigid four-cycle geometry. The result exhibits integral \(\mathbb Z/2\) torsion in every ordinary three-cut complex, gives exact free ranks, and proves failure of shellability and Cohen–Macaulayness over every field. The distinction between ordinary and total cut complexes is maintained, and no homotopy type of the cut complexes is claimed.

## Limits of verification

The exact infinite-family proof is mathematical; the executable checker independently verifies its finite local instances, integral degree-two Morse certificate in the Clebsch case, and small prime boundary ranks. It does not establish exhaustiveness of the scientific literature or independent validation.

Self-review: passed. Independent audit: not yet performed.
