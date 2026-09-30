# Independent Audit — 2026/09/21/novikov-three-step-nilpotent-dimension-12--bd312a6bbfdc

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8acd4e5446a7746233fce0dad9c334d2d62e09fd`
- Disposition: **PASSED**

## Correctness

**PASS** — The displayed algebra is exactly the stated one-dimensional central quotient of the Burde-Dekimpe-Vercammen 13-dimensional example: substituting x13=-2x9-2x10+2x11 into the original brackets reproduces the new table, so Jacobi is inherited. The lower central layers remain gamma2=<x5,...,x12>, gamma3=<x9,...,x12>, gamma4=0. The repository's exact-rational verifier was inspected: it encodes the standard lower-central ideal restrictions, commutator relation, cyclic Novikov identity, and the operator identity from the 2008 obstruction; its exact echelon ranks are asserted as 1088,1376,1504,1678, leaving 50 free left-multiplication entries. Independently simplifying the compact certificate in RESULT.md gives [R2,R3]_(11,2)=-1/4 identically in its four remaining parameters. Since Novikov right multiplications commute, this is a contradiction.

## Originality

**PASS** — Burde-Dekimpe-Vercammen's open 2008 preprint states the known 13-dimensional four-generated three-step nilpotent counterexample and the positive theorem for at most three generators. The checked original bracket table confirms the central quotient used here. Targeted searches for 12-dimensional Novikov-free three-step nilpotent Lie algebras and later citations of the 2008 example found no prior 12-dimensional construction. The novelty is therefore the dimension-lowering central quotient plus its independent obstruction, not the general necessary identities or the 13-dimensional example.

## Scientific value

**PASS** — Lowering the explicit four-generated three-step counterexample from dimension 13 to 12 sharpens a concrete boundary in the Novikov-structure problem and comes with a compact exact obstruction certificate. The result is meaningful incremental progress while correctly making no minimality claim.

## Sources

- **Novikov algebras and Novikov structures on Lie algebras** — D. Burde; K. Dekimpe; K. Vercammen. https://arxiv.org/abs/0705.1316 — Open primary source for the 13-dimensional counterexample, the relevant necessary identities, and the three-generator positive theorem.
- **Novikov structures on solvable Lie algebras** — D. Burde; K. Dekimpe. https://arxiv.org/abs/math-ph/0502008 — Earlier Novikov-structure background.
- **Novikov, LR- and post-Lie algebra structures, and their relation to NIL-affine crystallographic actions** — K. Vercammen. https://www.kuleuven.be/doctoraatsverdediging/fiches/3E07/3E070097.htm — Later dissertation context continuing this line of examples.

## Limitations

- No minimality is proved; counterexamples of dimension at most 11 are not ruled out.
- The theorem is characteristic-zero only.
- The full 1678-row elimination was inspected in source form rather than independently reimplemented from scratch; the final compact contradiction was independently simplified.

## Independent checks

```json
{
  "central_quotient_bracket_substitution_checked": true,
  "lower_central_series_checked": true,
  "exact_verifier_source_inspected": true,
  "compact_commutator_certificate_independently_simplified": "-1/4",
  "original_13d_open_source_checked": true,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory snapshot and the checked commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first, with authorized institutional retrieval used only where a directly relevant full text remained unavailable.
