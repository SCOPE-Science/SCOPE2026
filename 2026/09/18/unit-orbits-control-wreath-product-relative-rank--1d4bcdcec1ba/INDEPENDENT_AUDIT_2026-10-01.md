# Independent mathematical audit — 2026-10-01

## Final claim

Unit orbits control relative rank in finite monoid wreath products

## Correctness — PASS

PASS. The two-factor formula was reconstructed from first principles. Projection to the top monoid forces the top relative-rank contribution. For unit-top generators, the singular support of a base tuple can only move inside unit-group orbits and singular defects cannot cancel, because a product in a finite monoid is a unit exactly when all factors are units. Producing a base element with one singular coordinate therefore requires at least the relative rank of the base monoid separately on each unit-group orbit. The matching upper bound is obtained from top lifts and local generators at orbit representatives. The iterated formula follows because unit-group orbit counts multiply. Independently, exhaustive enumeration of the supplied 12-element example gives exact relative rank four.

## Originality — PASS

PASS to the best of current knowledge. The current full text of Lu's preprint treats the transitive-unit-group case and the advertised full-transformation/symmetric-group iteration, but it does not state the exact arbitrary-orbit formula. The closest partition-rank literature concerns special full transformation monoids. A published-record semantic search returned the audited formula as the exact match and no earlier equivalent statement. The version-specific correction claim retains a bibliographic risk because the exact version-one text was not recovered in full.

### equivalent_formulations

Searches: relative rank wreath product group of units orbit formula; finite transformation monoid wreath product relative generation

Evidence: Published-record search found the audited result as the exact semantic match; the current Lu source gives only the transitive-unit-group special case.

Reasoning: Orbitwise transport by units is the natural equivalent formulation of the lower-bound obstruction; no inspected prior source states the resulting exact sum.

### broader_coverage

Searches: Lu 2026 iterated wreath products full text; Araújo-Schneider uniform partition wreath rank; Araújo-Bentz-Mitchell-Schneider arbitrary partition rank

Evidence: Lu's current Lemma 3.2 assumes the unit group is transitive, and the older partition papers work in more specialized transformation settings.

Reasoning: Those results do not mechanically determine the contribution from several unit-group orbits.

### exact_database_or_table

Searches: published mathematical record semantic search for exact unit-orbit relative-rank formula

Evidence: No earlier exact record or table entry was located.

Reasoning: This is a theorem-level generation formula rather than a standard tabulated invariant.

### claim_vs_prior_implication

Searches: Lu current Lemma 3.2 and Lemma 3.8; partition-semigroup relative-rank literature

Evidence: The current source proves the one-orbit upper bound and its restricted iteration, not the arbitrary-orbit lower bound or exact equality.

Reasoning: Additional singular-support analysis is required to obtain the exact orbit-weighted formula.

## Scientific value — PASS

PASS. The result replaces a fragile transitivity heuristic by the exact transport invariant, gives a sharp relative-rank formula for arbitrary finite transformation monoids, and explains when the motivating iterated calculation remains valid. The explicit small counterexample makes the boundary operationally clear.

## Source inspections

- **Jiaping Lu, Generation of Iterated Wreath Products Constructed from Full Transformation Monoids and Symmetric Groups** — https://arxiv.org/abs/2609.20521. Material read: Full current preprint, including Lemmas 2.1, 3.2, 3.4, 3.7 and 3.8 and the main theorem. Assessment: SPECIAL_CASE_NOT_GENERAL_COVERAGE. Evidence: The current text assumes unit-group transitivity for the relevant upper-bound lemma and treats the restricted iterated setting; it does not give the arbitrary unit-orbit formula audited here.
- **João Araújo and Csaba Schneider, The Rank of the Endomorphism Monoid of a Partition** — https://arxiv.org/abs/0807.1214. Material read: Published bibliographic and theorem context used by the motivating source. Assessment: SPECIALIZED_BACKGROUND. Evidence: The cited work concerns the special partition-preserving full-transformation setting rather than arbitrary finite transformation monoids with multiple unit orbits.

## Limitations and residual risks

Originality is to the best of current knowledge. The exact September 2026 version-one wording of the motivating preprint was not recovered in verified full text during this audit; the current version already assumes transitivity of the unit group in its two-factor upper-bound lemma. Older semigroup-generation literature under different terminology remains a residual risk.

- The exact version-one preprint text was not recovered; the current revision already uses unit-group transitivity, so the historical correction wording cannot be independently certified here.
- Differently phrased older semigroup-generation literature remains a residual originality risk.

## Disposition

**passed**
