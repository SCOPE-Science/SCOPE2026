# Review of the exact 35-class unary modality theorem

## Correctness — PASS

The first five equations in the proof are Lemma 5 of the cited full text; the sixth is Lemma 10(1). Lemmas 15–17 give the seventh and prove double-negation stability of the updownset used to derive the eighth. Monotonicity/antitonicity and the reflexive diamond inclusion complete that derivation. Since all eight equations hold in *every* permitted model, any contextual rewrite preserves operator semantics. The standalone program reduces every one of 105 generator/representative products to one of 35 representatives using these equations. By induction this is an all-word upper bound, not extrapolation from finite cases. The same program checks the five explicit models satisfy *all* frame conditions and have 35 distinct outcome vectors. Thus the sharp lower bound matches the upper bound. The checker was run from the exact file embedded in the new package.

## Originality — PASS (historical-priority risk noted)

Pacheco's Theorem 18 (arXiv:2609.00736, 2026) explicitly obtains only the upper bound 105 and no exact census. Its Lemmas 5, 10, 15–17 are credited as components of the proof, not claimed as new. Ciraulo's 2025 constructive Kuratowski work discusses different constructive-topological operators; Pacheco explicitly distinguishes it from these modal systems. Targeted searches for '35' together with the logic, its aliases, and unary modality reductions, as well as published research-record searches and prior-claim checks, found no stronger/equivalent 35-state theorem. Search absence alone is not a uniqueness proof; algebraic/pointfree formulations are a residual risk.

## Value — PASS

The exact cardinality is the natural outstanding invariant left bounded but undetermined by a specific recent paper. The result strengthens a 105-class upper bound to a sharp 35 and supplies a complete finite calculation of the unary modal composition monoid, with a reusable reduction algorithm and explicit separating structures. It settles a classification question, not an arbitrary low-dimensional slice or a mere numeric experiment.

## Limitations and closest literature

The main source is Pacheco, *Modalities in non-classical variations of S4*, arXiv:2609.00736. A secondary related source is Ciraulo, *Kuratowski's problem in constructive Topology* (2025). A first-order mathematical consequence of unrelated published mathematical research items about five modal-to-modal translations does not imply this exact 35-element unary word monoid. The external-priority risk remains; the five models are not certified size-minimal.

Self-review: passed. Independent audit: not yet performed.
