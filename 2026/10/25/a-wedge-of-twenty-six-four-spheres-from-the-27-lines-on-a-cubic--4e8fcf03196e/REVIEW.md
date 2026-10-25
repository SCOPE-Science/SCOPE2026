# Review of the 27-line skew-line complex

## Correctness (PASS)

The classical intersection classes reconstruct the Schläfli graph without relying on its name. The independent standalone verifier enumerates all 2,763 nonempty simplices and checks all 10,584 incidences. Its deterministic 1,368-pair matching has one critical vertex and 26 four-cells; complete directed-Hasse acyclicity is verified on all 2,763 face nodes. Forman's theorem yields the claimed wedge because there are no critical cells of intermediate positive dimension. The independent mod-two boundary ranks are \(26,190,530,550,72\). The exact output is in `verify_output.txt`.

## Originality (PASS)

The closest source inspecting the identical graph and simplicial construction is Cioabă and Mim (2026), Proposition 7.7(2b), which proves only first-homology vanishing over arbitrary fields. Dolgachev and Kapranov (1993) identify all 27 lines and the sixes but do not give the homotopy type of this disjointness complex. Cross-checks using the complementary generalized-quadrangle partial-ovoid formulation, plus the full graph name and numerical parameters, revealed no covering theorem. The 27-line open-neighborhood complex indexed elsewhere is a different functor, while the degree-four rank agreement with a snub-cubical independence complex does not imply equivalence of objects. An unindexed equivalent computation remains possible.

## Value (PASS)

This determines the complete integral homotopy type of a natural 27-line exceptional-curve compatibility complex associated with cubic surfaces, not just a Betti number. The complex is nonpure, with 72 six-line simplices and 216 inclusion-maximal five-line simplices, but nonetheless has a perfect Morse collapse to a pure four-sphere wedge. The concrete, reusable certificate can be checked without external computational packages.

## Limitations and remaining review

The statement is restricted to nonsingular complex cubic surfaces and their full line sets, and does not calculate the Weyl-group action on the degree-four homology. Literature indexing is incomplete and there has been no independent validation.

Self-review: passed. Independent audit: not yet performed.
