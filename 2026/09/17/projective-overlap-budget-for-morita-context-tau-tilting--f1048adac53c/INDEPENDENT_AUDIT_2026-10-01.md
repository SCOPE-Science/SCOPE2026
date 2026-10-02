# Independent mathematical audit — Projective-overlap budget for direct support tau-tilting induction

Audit date: 2026-10-01 (UTC) UTC
Disposition: passed

## Correctness
the overlap identity follows by counting indecomposable projective classes induced from the two idempotent corners and using that every indecomposable projective of the Morita-context algebra occurs in at least one corner. Semisimple block analysis gives zero overlap exactly when both connecting images are radical. For the support tau-tilting criterion, adjunction identifies the corner projectives orthogonal to the induced module; inclusion-exclusion for duplicate induced modules and duplicate projectives gives the stated six-term deficit, and the standard summand bound for tau-rigid pairs gives the lower bound by the projective overlap, with equality exactly at support tau-tilting.

## Originality
Zhang's primary abstract says direct corner induction is characterized by two-sided compatibility conditions and that necessity is proved under radical-valued connecting maps. The present result identifies the missing general obstruction as projective overlap and gives an exact numerical budget outside the radical case. Resultary search found no prior equivalent overlap-budget formula; a later SCOPE record on full Morita corners is subsequent and does not constitute prior coverage.

### equivalent_formulations
No located source states the quantitative overlap budget in an equivalent form.

Searches: Resultary: Morita context support tau tilting projective overlap direct induction radical condition; Zhang arXiv:2609.18746; Adachi–Iyama–Reiten arXiv:1210.1036

Evidence: The zero-overlap condition is equivalent to radical-valued connecting maps; the six-term deficit equality is equivalent to saturating the τ-rigid-pair summand bound.

### broader_coverage
No prior broader theorem inspected subsumes the arbitrary-connecting-map budget.

Searches: Zhang arXiv:2609.18746; Asefa–Xu 2024; Green–Psaroudakis arXiv:1303.2083; Resultary projective overlap search

Evidence: Zhang's accessible abstract states direct induction and necessity under a radical hypothesis; later Resultary work is subsequent, not prior. Classical Morita-context sources concern structure rather than this τ-tilting equality criterion.

### exact_database_or_table
This is a structural theorem rather than table extraction.

Searches: Resultary support tau tilting Morita context overlap

Evidence: No database/table of overlap budgets is relevant or was found.

### claim_vs_prior_implication
Best-of-knowledge not mechanically implied by the statements actually inspected; full Zhang text was inaccessible, leaving explicit residual risk.

Searches: Zhang arXiv:2609.18746 abstract; AIR arXiv:1210.1036

Evidence: The standard summand bound and Zhang's τ-rigidity criterion are ingredients, but the inclusion–exclusion overlap identity and six defect accounting are additional deductions not stated in the accessible prior material.

### Source inspections
- **Yingying Zhang, Support tau-tilting modules over Morita context algebras: A bilateral approximation approach** — Primary abstract inspected. Full text could not be retrieved in this run; this access limitation is explicitly retained as a risk rather than treated as novelty evidence. Assessment: Compared against the final statement and implication scope.
- **Adachi, Iyama, Reiten, tau-tilting theory** — Primary foundational source for support tau-tilting summand counts and tau-rigid pairs. Assessment: Compared against the final statement and implication scope.
- **Resultary search** — Searched Morita context, support tau-tilting, projective overlap, direct induction, and radical-condition formulations. Assessment: Compared against the final statement and implication scope.

## Scientific value
the theorem explains precisely why the radical-valued hypothesis is the zero-overlap regime and supplies a general exact criterion for direct induction, a natural structural question in support tau-tilting theory.

## Reproducibility
The proof was reconstructed from the induced-projective union count, corner defect decomposition, adjunction for orthogonal projectives, and the tau-rigid pair summand inequality; the M2(k) example is consistent with one shared projective class.

## Limitations and residual risks
Originality is assessed to the best of current searches. The exact overlap-budget criterion was not found, while the zero-overlap/radical observation rests on standard semisimple-ring facts. The full text of the very recent Zhang preprint was not retrievable in this run, so the comparison used its primary abstract plus the precise theorem statements cited and reproduced in the record; this is retained as a residual originality risk.
- The full text of arXiv:2609.18746 was inaccessible during this run; the primary abstract and record's cited theorem statements were compared, leaving a nonzero risk that an uninspected passage already states an equivalent overlap formula.
- Computing duplicate isomorphism classes in applications can itself be nontrivial.
