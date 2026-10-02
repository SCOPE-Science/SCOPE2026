# Independent mathematical audit — SCOPE-20260920-dec63dd1eae1

Audited at: 2026-10-01T22:05:12.892464Z

Disposition: **passed**

## Correctness — PASS

On each conditioning atom the operator is rank one with norm \(c_n=E(|w|)(A_n)\|u\chi_{A_n}\|_\infty\), while the non-atomic block has norm \(\gamma\). Finite atomic truncations give the approximation upper bound, and disjoint almost norming vectors give the matching Bernstein lower bound both on atoms and on a partition of the non-atomic region. The resulting disjoint \(\ell_1\) witness is contractively complemented and forces the exact compact/FSS/SS distance. For nuclearity, the atomic rank-one series gives the upper bound and finite diagonal compression plus the nuclear trace inequality gives the reverse bound. The two counterexamples directly invalidate the cited average-based endpoint criteria.

### Correctness sources

- assigned RESULT.md
- Estaremi-Jabbarzadeh 2013 Theorem 2.7
- Al Ghafri-Shamsigamchi-Estaremi 2026 preprint

### Correctness risks

- The theorem is the same-space \(L^1\) endpoint and does not claim the corresponding theory for other exponent pairs.

## Originality — PASS

Primary text of the 2013 paper states an \(L^1\) compactness criterion using ambient-space atoms, and the 2026 preprint uses conditional averages in its atomic nuclearity series. The assigned trivial-conditioning and spiky-atom examples invalidate those statements as written. Searches found no prior corrected all-index profile using the essential-supremum block coefficient, no exact common compact/FSS/SS distance, and no exact nuclear norm with that coefficient.

### Equivalent formulations

The assigned theorem is not merely a reparameterization: replacing a conditional average by the true \(L^\infty\) norm on each conditioning atom changes both compactness and nuclearity conclusions.

Searches:
- Published-record semantic search: weighted conditional expectation L1 exact approximation Bernstein nuclear norm atomic block essential supremum
- Primary search of the 2013 compactness theorem and 2026 nuclearity preprint

Evidence:
- The earlier criteria use different invariants and are contradicted by explicit examples in the assigned proof.
- No exact corrected all-index theorem was located.

### Broader coverage

Broader representation theory does not mechanically supply the sharp block norm and all-index consequences without the audited endpoint calculation.

Searches:
- Grobler-de Pagter representation literature cited by the record
- Estaremi 2014 essential-norm literature
- 2026 nuclearity preprint

Evidence:
- General multiplication-conditional-expectation representation theory supplies structural background.
- The inspected endpoint criteria do not give the corrected coefficient or exact s-number/nuclear profile.

### Exact database or table

The invariant is derived from rank-one operator norms and a nuclear trace lower bound, not from a known table.

Searches:
- Published-record semantic query for the coefficient \(E(|w|)(A_n)\|u\chi_{A_n}\|_\infty\) and exact nuclear norm

Evidence:
- No earlier exact profile or table was found.

### Claim versus prior implication

The prior criteria cannot imply the corrected theorem because the assigned examples falsify their endpoint invariants.

Searches:
- Compared the assigned theorem with Estaremi-Jabbarzadeh 2013 Theorem 2.7 and the 2026 nuclearity theorem

Evidence:
- The trivial-conditioning example is rank one although the 2013 stated threshold set is nonatomic.
- The spiky atomic example has convergent average-based series but fixes an isometric \(\ell_1\), so it is not compact or nuclear.

### Sources inspected

- **Weighted Lambert type operators on Lp spaces** — https://doi.org/10.7153/oam-07-05
  - Trigger: Direct source of the endpoint compactness criterion challenged by the record.
  - Material read: Primary full-text material around Theorem 2.7 and its stated \(L^1\) criterion.
  - Method: Author-posted/public article text.
  - Assessment: CONTRADICTED_AT_ENDPOINT
  - Evidence: The theorem uses ambient-space atoms in a way refuted by conditional expectation onto the trivial sigma-algebra.
- **Weighted conditional expectation operators and nuclearity** — https://arxiv.org/abs/2602.19105
  - Trigger: Direct source of the average-based nuclearity criterion challenged by the record.
  - Material read: Primary preprint material covering the atomic nuclearity proposition/theorem and the use of conditional averages of \(|u|\).
  - Method: Primary preprint text.
  - Assessment: CONTRADICTED_AT_ENDPOINT
  - Evidence: The audited spiky-atom example separates the average of \(|u|\) from the true rank-one functional norm \(\|u\|_\infty\).

### Checked sources

- https://doi.org/10.7153/oam-07-05
- https://doi.org/10.1007/s11117-013-0229-5
- https://arxiv.org/abs/2602.19105
- published-record semantic search

### Residual risks

- Older Banach-lattice representation work may contain parts of the block decomposition under different terminology.
- The later 2026 Ommi-Estaremi nuclearity preprint was not needed for the decisive comparison and was not fully audited here.

## Value — PASS

The result corrects concrete published endpoint criteria, supplies explicit reusable counterexamples, and replaces them with exact finite-index, ideal-distance, and nuclear-norm formulas governed by the true atomic operator norm. This is a motivated repair of a natural operator class.

### Value sources

- Estaremi-Jabbarzadeh 2013
- Al Ghafri-Shamsigamchi-Estaremi 2026

### Value risks

- The theorem does not extend the correction beyond the stated same-space \(L^1\) setting.

## Limitations

- Same-space \(L^1\) endpoint only.
- The conditioning sigma-algebra is assumed sigma-finite.
- Older representation literature may contain partial structural overlap.
