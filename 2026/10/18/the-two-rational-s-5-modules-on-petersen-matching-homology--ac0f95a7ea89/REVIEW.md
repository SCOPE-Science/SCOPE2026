# Review of the two rational \(S_5\)-modules on Petersen matching homology

## Correctness (PASS)

The claim concerns the *ordinary* matching complex of the Kneser realization \(P=KG(5,2)\) of the Petersen graph, and the natural action of \(S_5\) induced by the five symbols. Exhaustive matching enumeration yields face cardinalities (1,15,75,145,90,6), including the empty simplex. Exact rational ranks (1,14,61,79,6) of the augmented simplicial boundary maps prove rational Betti ranks five in degree two and five in degree three, with no other reduced homology.

For each conjugacy type, the invariants of the oriented simplicial chain complex are constructed by coherent signed orbit sums, and their exact rational boundary ranks give the invariant homology dimensions. Because taking invariants under a finite cyclic group is exact over \(\mathbb Q\), the fixed dimensions determine the two ordinary characters by the cyclic averaging identity. The resulting rows equal the sign-twisted five-point permutation character and the irreducible Specht \((3,2)\) character. The modular direct trace computation independently reproduces every row. All seven classes, including the order-six mixed cycle and both order-two classes, are covered. This is a proof for one fully enumerated finite complex, not an extrapolation from tests.

## Originality (PASS, subject to residual risk)

The closest previous graph-specific computation (record `80050a32-4367-4c54-9ae8-daf37b3378cd`) already establishes the mixed sphere-wedge homotopy type and the two Betti numbers. Those assertions are not new. Shareshian–Wachs, arXiv:math/0409054v1, examine complete-graph and chessboard matching complexes and present Bouc's representation theory, not this proper Petersen matching subcomplex. Zaslavsky (DOI:10.1016/j.disc.2011.12.010, §§3–3.2) classifies automorphism orbits of matchings in the Petersen graph, but does not identify its simplicial homology modules or the two boundary-image modules. Bate–Everitt–Ford–Ramos, arXiv:2312.13750v3, focus their explicit representation decompositions on complete-hypergraph matching complexes; the stated results do not specialize to \(\mathcal M(KG(5,2))\).

Exact-statement, equivalence, reduction, and stronger-coverage searches did not identify a covering published calculation. They also distinguished ordinary matching complexes from *two*-matching complexes and from the Morse complex of the Petersen graph, both different objects. Nonetheless, unindexed or differently named equivariant computations could exist. No absolute priority claim is made.

## Value (PASS)

The Petersen graph is a canonical highly symmetric graph with intrinsic \(S_5\)-action. Its equal degree-two and degree-three Betti ranks do not determine the two actions. This calculation finds a mathematically meaningful contrast: one rational module is reducible and a sign twist of a natural permutation representation, while the other is the irreducible five-dimensional \((3,2)\) Specht module. These characters can inform other equivariant constructions on the same graph and provide an exact comparison target; no dependent theorem is needed for the invariant itself to be of interest. This is neither a renamed homology rank nor a routine sign-only calculation.

## Remaining scientific limits

Only rational representations of the natural \(S_5\)-action are classified. Integral lattice structure, torsion, equivariant homotopy and generalizations to other graphs are not asserted. Bibliographic nonretrieval is not a proof of global priority. Computational inputs, complete boundary formula, invariant-orbit algorithm and executable checks are supplied.

Self-review: passed. Independent audit: not yet performed.
