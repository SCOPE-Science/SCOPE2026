# Independent audit — Projective-overlap budget for direct support tau-tilting induction

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/17/projective-overlap-budget-for-morita-context-tau-tilting--f1048adac53c`
**Audited tree:** `27c7fff931d06ee2c5966cb9e05bec67afe81cdf`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The projective-overlap count follows from Lambda=eLambda direct-sum fLambda, full faithfulness of the two corner inductions, Krull–Schmidt, and inclusion–exclusion. In the semisimple quotient, overlap classes are exactly mixed simple Artinian blocks, and such a block makes both eSfSe and fSeSf nonzero, yielding the zero-overlap/radical equivalence. For tau-rigid Z, adjunction identifies all induced projectives orthogonal to Z; inclusion–exclusion gives |Z|+|P_Z^perp|=|A|+|B|-Delta. The standard tau-rigid-pair summand bound then gives Delta>=omega, with equality exactly at support tau-tilting size. The M2(k) example attains the budget as stated.

### Independent checks

- Re-derived full faithfulness of corner induction via the (-⊗eLambda, (-)e) adjunction and eLambda e=A, and similarly for f.
- Re-derived omega=|A|+|B|-|Lambda| and the mixed-Wedderburn-block description.
- Checked the semisimple-product argument showing mixed blocks are exactly the obstruction to both connecting-map images being radical-valued.
- Re-derived the counts |P_Z^perp|=r_X+r_Y-d_P and |Z|=|X|+|Y|-d_Z, then the tau-rigid-pair inequality and equality criterion.
- Checked the strict M2(k) example and its one-unit beta_Y budget.

## Originality

Zhang’s arXiv:2609.18746 (submitted 2026-09-16) proves the direct-induction converse only for radical-valued connecting maps and gives non-radical examples; it does not state the six-term overlap budget or the resulting arbitrary-map equality criterion. Classical Morita-context radical facts and AIR tau-tilting counts are prior art and are not counted as new. Fresh searches through 2026-09-29 located no prior projective-overlap budget matching the submitted formula.

### Literature checked

- https://arxiv.org/abs/2609.18746 — Yingying Zhang, Support tau-tilting modules over Morita context algebras; closest direct-induction theorem and non-radical examples.
- https://arxiv.org/abs/1210.1036 — Adachi–Iyama–Reiten, tau-tilting theory; standard summand-count and torsion-class ingredients.
- https://doi.org/10.1515/math-2024-0009 — Asefa–Xu, silting over Morita rings; nearby Morita-context representation-theoretic literature.
- https://doi.org/10.1016/0021-8693(73)90143-9 — Sands, Radicals and Morita contexts, identified bibliographically as possible classical background; full text was not inspected and no originality claim is placed on the classical radical sublemma alone.

## Scientific value

The result converts the precise hypothesis where the closest new converse breaks into an exact quantitative obstruction and necessary-and-sufficient criterion. It explains the published M2(k) obstruction, recovers the radical theorem as zero budget, and gives a sharp family with arbitrary overlap count.

## Limitations

- The structural radical/overlap equivalence may admit older equivalent ring-theoretic formulations; the claimed novelty is the tau-tilting six-term budget and arbitrary-map criterion.
- Zhang’s source preprint is extremely recent, so concurrent revision risk remains.
- Computing the duplicate counts d_Z and d_P can itself require nontrivial module-isomorphism recognition; the theorem is exact rather than automatically algorithmic.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
