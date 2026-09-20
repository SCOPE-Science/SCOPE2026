# Review: Isolated-unit criterion for isotropy embeddings in Steinberg algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The main obstruction follows directly from the defining topology of a Steinberg algebra. If the identity isotropy singleton has a characteristic function in the algebra, local constancy forces the unit singleton to be open. Conversely, if the unit is isolated, intersecting any open bisection containing an isotropy arrow with the source fibre over that unit produces the singleton arrow; Hausdorffness makes it compact. Thus the singleton embedding exists exactly for isolated units.

The corner computation was checked separately. Multiplication by `e_x=1_{\{x\}}` on both sides cuts support to arrows with source and range equal to `x`. Under isolation those arrows form a discrete subset, and compact support is finite, giving exactly the isotropy group algebra. Likewise `A e_x` is the finitely supported module on the source fibre. The right isotropy action on that fibre is free, so choosing orbit representatives decomposes `A e_x` as a direct sum of copies of the isotropy group algebra. This proves freeness, the corrected corner adjunction, and exactness of induction over arbitrary coefficient rings.

The two-loop graph counterexample was checked against the boundary-path topology. The periodic path `a^∞` has isotropy `Z` but is not isolated because every prefix cylinder `Z(a^n)` contains paths that branch through the other loop. Hence even the identity singleton characteristic function is absent from the Steinberg algebra.

A second issue was checked independently of topology. When `x` is isolated, the identity of the isotropy group algebra maps to the corner idempotent `e_x`, not generally to an identity acting as one on an arbitrary unital `A`-module. Therefore restriction of the whole `M` does not land in the stated category of unital isotropy modules unless `e_x M=M`; the correct corner object is `e_x M`. The disjoint union of two one-loop graphs gives a concrete witness.

## Originality

PASS, qualified to the best of our knowledge.

The full text of arXiv:2609.20230v1 was inspected at its Steinberg-algebra definition and Sections 4.1--4.2. It explicitly defines `iota_x(u^p)=1_{\{(x,p,x)\}}` for arbitrary infinite paths and asserts in Proposition 4.1 that this is an injective algebra homomorphism; Definition 4.2 then restricts the whole module along this map. The source does not impose isolation at this point.

Prior Steinberg-algebra literature already supplies the correct general mechanism: induction from isotropy via the free module on the source fibre. In particular, arXiv:2006.09931 by Q. L. Nguyen and B. V. Nguyen describes Steinberg's induction/restriction theory for isotropy, and Demeneghi's arXiv:1710.09723 develops compatible isotropy induction. Those results are treated as prior art, not as new contributions here.

Targeted searches for isolated units, isotropy corners, singleton characteristic functions, and isotropy group-algebra embeddings did not locate a prior notice of the specific error in arXiv:2609.20230v1 or the combined sharp repair stated here. The exact isolated-unit criterion is elementary enough that an equivalent observation may be implicit in foundational definitions. The originality claim is therefore limited to identifying and sharply correcting the recent unrestricted embedding and separating the topological obstruction from the unital corner obstruction.

No inaccessible source was identified whose title or abstract gives concrete evidence of already containing this correction. The residual risk is instead terminology-level: an older groupoid-algebra source may state the same corner fact without using the phrases searched here.

## Value

PASS.

The affected embedding is the foundation of the source paper's Section 4 restriction construction. The result gives both a minimal rank-one counterexample and an exact criterion for when the proposed singleton inclusion exists. It also shows that isolation alone does not make the stated restriction functor correct in the category of unital modules; replacing `M` by `e_x M` yields the standard corner adjunction. Finally, it distinguishes this defect from established source-fibre isotropy induction, which remains available for nonisolated units.

## Limitations

This record does not claim that every theorem later in arXiv:2609.20230v1 is false. Results depending on the unrestricted singleton inclusion require re-examination or reformulation, while independent parts of the paper are outside the scope of this finding. The general nonisolated restriction theory is not redeveloped here; established Steinberg isotropy theory should be used for that purpose. No independent validation is asserted.
