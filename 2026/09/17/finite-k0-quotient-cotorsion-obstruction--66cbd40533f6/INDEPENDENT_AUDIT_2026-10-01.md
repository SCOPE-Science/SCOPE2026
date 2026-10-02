# Independent mathematical audit — SCOPE-20260917-66cbd40533f6

Final disposition: **passed**.

## Correctness
**PASS.** The proof reconstructs in the semisimple split-exact setting. Euler classes are additive on conflations; complements of retractions remain in the kernel of the finite quotient, giving weak idempotent completeness; standard cone sequences give the Frobenius structure; semisimplicity gives the displayed Ext formula. Exponent-e direct sums make the truncation factorizations and simple test objects lie in the subcategory, proving the object-ideal identities, orthogonality, and ideal completeness. For the two stalk-pair witnesses, the long cohomology sequence forces a truncation object with nonzero quotient class, so the required special object approximation cannot lie in the subcategory. Every ambient complex is a summand of its e-fold direct sum, giving the stated idempotent completion.

## Originality
**PASS.** Ren–Wang v1 (2026-09-16) proves the parity case for bounded vector-space complexes. Their v2 (2026-09-29) says the main results are unchanged and interprets that example as the dense subcategory corresponding to 2Z in K0; it still does not state the arbitrary finite-quotient theorem. Classical K0 dense-subcategory results cover the density/idempotent-completion viewpoint but not the finite-quotient ideal-cotorsion obstruction theorem. Later public records dated 2026-09-19 and 2026-09-20 strictly generalize the finite-quotient mechanism, but they postdate this 2026-09-17 record and therefore are subsequent coverage rather than earlier prior art.

## Value
**PASS.** The finite quotient is a structural mechanism, not merely a renamed parity parameter: it replaces doubling by the quotient exponent, works for semisimple categories with several simple classes, and explains the correct signed Euler congruence controlling the exact subcategory. That is a reusable homological-algebra generalization of a newly exposed obstruction.

## Source inspections
- **Ren and Wang, A parity obstruction to completeness of object cotorsion pairs, arXiv:2609.18681v2** — Full arXiv HTML inspected, including the introduction, Theorem 1.2, and the stable-category/K0 interpretation. The paper treats the even-total-cohomology vector-space category and states that v2 leaves the main result unchanged. Consequence: Earlier source covers the mod-2 vector-space special case, not arbitrary finite Grothendieck quotients.
- **Finite Grothendieck quotients control object-cotorsion completeness (public research record, 2026-09-19)** — Full result text inspected. It gives exact quotient-valued defect classes and every finite abelian defect group. Consequence: Strictly broader subsequent coverage; dated after the audited record.
- **Finite-abelian Grothendieck obstructions to object cotorsion completeness (public research record, 2026-09-20)** — Full result text inspected. It adds exact direct-sum stabilization indices. Consequence: Strictly broader subsequent coverage; does not constitute earlier prior art.

## Originality comparison
- **Equivalent formulations.** Searches: finite Grothendieck quotient cotorsion obstruction; dense subcategory K0 exact category cotorsion pair. Evidence: Ren–Wang v2 identifies the parity example with the subgroup 2Z in K0 but states only that case. Reasoning: The audited theorem is equivalent to taking a finite-index kernel H=ker(phi) and imposing Euler class in H; that formulation was explicitly checked against the closest parity source.
- **Broader coverage.** Searches: finite abelian K0 cotorsion obstruction; quotient-valued truncation defect cotorsion. Evidence: Public 2026-09-19 and 2026-09-20 records give stronger quotient-valued defect theorems. Reasoning: Those records postdate the audited record, so they establish present-day broader coverage but not pre-existing coverage at the audited publication date.
- **Exact database or table.** Searches: exact title and theorem phrase searches; Resultary semantic search on finite K0 quotient and cotorsion completeness. Evidence: No earlier exact theorem was located; later records were found and inspected in full. Reasoning: Search failure is not used alone; the originality decision rests on direct comparison with the closest full-text parity theorem and the dated later broader records.
- **Claim versus prior implication.** Searches: Ren Wang theorem 1.2 parity; Matsui Grothendieck dense exact categories. Evidence: Parity implies only the quotient Z/2 example; dense-subcategory K0 classification does not provide the ideal cotorsion pair or object-completeness obstruction. Reasoning: Neither earlier source mechanically implies the full finite-quotient ideal-cotorsion theorem without the new construction.

## Residual risks
- A concurrent unpublished finite-quotient generalization could exist under different exact-category terminology.
- The theorem is elementary once the finite-index K0 viewpoint is identified; the value rests on identifying and proving that structural mechanism.

## Limitations
The theorem is restricted to bounded complexes over an essentially small Hom-finite semisimple category and to finite quotients of its Grothendieck group. Later public research records give stronger quotient-valued defect classifications, but they postdate this record. Older Grothendieck-group descriptions of dense subcategories remain prior background.
