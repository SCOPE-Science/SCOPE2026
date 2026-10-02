# Independent mathematical audit — SCOPE-20260930-f09137092e5f
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
For every \(n\geq2\) and \(m\geq1\), the generalized windmill \(W_{n,m}=K_1ee nK_m\) has general-position polynomial \(\psi(W_{n,m};x)=(1+x)^{nm}+x+n x((1+x)^m-1)\), and its coefficient sequence is unimodal.

## Correctness
Status: **PASS**.

The general-position sets are characterized exactly: without the hub every subset of the outer vertices is in general position, while a set containing the hub may use outer vertices from only one petal. This gives the displayed polynomial and coefficients. The symbolic proof then treats the exhaustive regimes \(m=1\), \(n=2,m\ge2\), and \(n\ge3,m\ge2\), controlling the only possible negative petal correction and the transition where that correction vanishes. A fresh finite sweep of the exact coefficient formula for \(2\le n\le30\), \(1\le m\le30\) found no failure; that experiment is only support for the all-parameter symbolic inequalities.

## Originality
Status: **PASS**.

The exact polynomial is not new: it is a specialization of the published join formula of Iršič–Klavžar–Rus–Tuite. The audited novelty is only the all-parameter unimodality theorem. Full inspection of that paper and the relevant portions of Rather’s 2026 explicit-formula/unimodality paper found no generalized-windmill, friendship, or equivalent \(K_1ee nK_m\) unimodality theorem. Published-record semantic search returned this record and no prior equivalent or stronger theorem.

### Equivalent formulations
- Search/source: V. Iršič, S. Klavžar, G. Rus, J. Tuite, General position polynomials, arXiv:2401.05696
- Search/source: B. A. Rather, Explicit Formulas and Unimodality Phenomena for General Position Polynomials, arXiv:2603.06930
- Search/source: Published-record semantic query: generalized windmill general position polynomial unimodal K1 join n Km friendship
- Evidence: The join formula specializes to the displayed polynomial, but no inspected source states the all-parameter windmill unimodality theorem.
- Reasoning: The formula is prior; the unimodality theorem is the final claim being assessed for novelty.

### Broader coverage
- Search/source: arXiv:2401.05696
- Search/source: arXiv:2603.06930
- Evidence: The primary sources discuss joins and unimodality phenomena in other structured families but do not furnish a theorem that implies unimodality for every \(K_1ee nK_m\).
- Reasoning: No broader theorem located dominates the audited family.

### Exact database or table
- Search/source: Published-record semantic corpus
- Search/source: Targeted literature search under windmill, friendship, clique-star, block-graph, and general-position-polynomial terminology
- Evidence: No exact table or family classification stating the theorem was found.
- Reasoning: This is a parametric graph-family theorem rather than a finite lookup invariant; exact-family literature and theorem corpus were searched.

### Claim versus prior implication
- Search/source: Iršič–Klavžar–Rus–Tuite 2024 join formula
- Search/source: Rather 2026 unimodality study
- Evidence: The join formula determines coefficients but does not itself imply unimodality; the audited proof supplies nontrivial coefficient inequalities over all parameter ranges.
- Reasoning: The known polynomial formula is an input, not a stronger theorem covering the unimodality conclusion.

### Source inspections
- **General position polynomials** (arXiv:2401.05696): trigger — primary source of the general join formula from which the polynomial specializes; material read — full accessible text around the join formula and the paper’s unimodality discussion; method — lawful arXiv full-text inspection; assessment — FORMULA_COVERED_UNIMODALITY_NOT_COVERED; evidence — The join framework yields the exact polynomial, but no generalized-windmill unimodality theorem was found.
- **Explicit Formulas and Unimodality Phenomena for General Position Polynomials** (arXiv:2603.06930): trigger — closest recent paper focused explicitly on formulas and unimodality; material read — full accessible text around its principal structured-family formulas, unimodality statements, and open questions; method — lawful arXiv full-text inspection; assessment — NEARBY_FAMILIES_NOT_COVERING; evidence — The inspected text treats other families such as complete multipartite and corona constructions; no windmill/friendship all-parameter theorem was located.

## Value
Status: **PASS**.

Unimodality is an active structural question for general-position polynomials and is not automatic even for simple graph families. Generalized windmills are a natural infinite block/chordal family simultaneously containing all stars and friendship graphs, so an all-parameter theorem with an exact coefficient-transition proof is a motivated structural result.

## Checked sources
- V. Iršič, S. Klavžar, G. Rus, J. Tuite, General position polynomials, arXiv:2401.05696; Results in Mathematics (2024).
- B. A. Rather, Explicit Formulas and Unimodality Phenomena for General Position Polynomials, arXiv:2603.06930 (2026).
- Published-record semantic query: generalized windmill general position polynomial unimodal K1 join n Km friendship.

## Residual risks
- The polynomial formula itself is prior and is not treated as an originality contribution.
- An equivalent unimodality observation could exist in block-graph literature under different terminology; no such source was located.

The audit distinguishes finite reproducibility checks from proofs of infinite statements and makes no claim beyond the final claim above.
