# Scientific review: square-one automorphisms of free class-two Lie algebras

## Correctness — PASS

The theorem explicitly fixes the free class-two Lie algebra \(L_d=V\oplus\bigwedge^2V\), the square-one convention (identity included), the generator dimension and all field-characteristic boundaries. The universal block description \(F_{G,f}\) is verified directly against the Lie bracket, and the square-one condition is equivalent to \(G^2=I\) and \(fG+(\bigwedge^2G)f=0\). In odd characteristic the eigenmodule decomposition yields the precise linear-solution dimension and Gaussian-binomial count; conjugation by a central shear eliminates the cocycle and provides the conjugacy classification and sharp quadratic fixed-space bound. In characteristic two, the wedge-square Jordan-module decomposition is checked block by block, with the Hom-space dimension and square-zero matrix orbit count completing the proof. The packaged Python checker independently implements finite matrix identities and matches all reported small-field totals, with full operator enumeration in three cases. Infinite-field and extension-field claims rely on the symbolic proof rather than finite tests.

## Originality — PASS with specified residual risk

Payne (arXiv:0809.3131v1) supplies the classical free-nilpotent automorphism setting and rational eigenvalue analysis, but not characteristic-two finite-field square-one counts. Benito–Roldán-López (arXiv:1911.01897v1) provide an explicit general automorphism description, which is a genuine structural antecedent; it does not itself give the involution strata, characteristic-two \(k[C_2]\)-Hom multiplicities, exact enumeration, or odd-characteristic conjugacy and sharp fixed-space formula. Publicly searchable nearby findings about fixed-point-free Heisenberg automorphisms and automorphism families concern different predicates or algebras; those findings do not imply the stated all-dimensional census. Actual searches are recorded in AUDIT.json. Residual risks include the possibility of an older unindexed enumeration or an indirect consequence of a more general finite-group involution-count theorem. Publication priority is not independently certified.

## Value — PASS

The entire order-two locus is a natural invariant of the automorphism group of a free nilpotent Lie algebra. The result gives a complete arithmetic census in every finite-field characteristic, identifies the modular obstruction to simply reusing the odd-characteristic semisimple argument, classifies conjugacy classes in the tame characteristic, and determines the least possible fixed-space dimension sharply. The characteristic-two count requires explicit tensor-product Jordan module calculations, not a single routine substitution into a known table. This provides structural data for finite automorphism groups and their fixed Lie subalgebras, rather than an arbitrary narrow numerical slice.

## Limits and literature comparison

For \(d\ge2\), characteristic-two conjugacy classes and fixed-space ranks are not classified; the even-characteristic claim is a complete count by the rank of the induced square-zero operator. The checker tests small prime fields only. The 2019 work was inspected at its automorphism propositions and group-structure remark, while the order-two Lie-ring literature could only be checked at the abstract level in this review. A broader theorem might imply some formulas after additional calculation; the checked sources do not state the present exact result.

Self-review: passed. Independent audit: not yet performed.
