# Independent audit — SCOPE-20260917-001

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For every q at least 5 and t at least 3, a rainbow K_q with t otherwise vertex-disjoint six-cycles sharing one clique vertex is weakly C₄-rainbow saturated; consequently rwsat(n,C₄) is at most 6n/5 plus 126/5 for every n at least 20.

## Correctness

**PASS** — The eight-stage insertion proof was checked directly against the universal new-color quantifier. The switching lemma is valid because the old clique edge can be chosen with color different from the current new edge and the two switched cycles cannot both be spoiled by the same old/new collision under separate injectivity. Each later stage uses only edges inserted earlier. The construction ends at the complete graph and has exactly binomial(q,2)+6t initial edges. The inspected finite checker independently encodes the exact old/new collision predicate for representative small parameters, but the infinite theorem rests on the symbolic proof rather than those experiments.

Residual risks:
- The finite checker is supplementary and does not itself prove the infinite family; the symbolic witness argument is the theorem-grade evidence.

## Originality

**PASS** — The nearest cycle result of Bo, Lian and Liu gives leading coefficient 4/3 for C₄ via its general cycle construction. The audited six-cycle coupling yields 6/5 and is not a parameter substitution into that bound. Current published-results search found no other 6/5 C₄ construction.

### equivalent_formulations

Searches: Resultary semantic search: weak rainbow saturation C4 six-cycle construction asymptotic coefficient 6/5; Web search for rwsat C4 coefficient 1.2 and 6/5

Evidence: The exact search returns the audited record as the direct match.; Bo–Lian–Liu's abstract states the general cycle coefficient ell/(ell-1), which is 4/3 for ell=4.

Reasoning: Equivalent notation such as weak saturation with respect to rainbow copies does not produce another 6/5 statement in the inspected sources.

### broader_coverage

Searches: arXiv:2609.03823 Bo–Lian–Liu; arXiv:2401.11525 Li–Ma–Xie

Evidence: The general bound of Bo–Lian–Liu specializes only to 4/3 for C₄; Li–Ma–Xie establishes existence/general bounds but not 6/5.

Reasoning: No broader inspected theorem dominates the 6/5 upper bound.

### exact_database_or_table

Searches: Published-results search for weak rainbow C4, K2,2, 6/5, 1.2

Evidence: No exact table/database is relevant; no independent exact 6/5 record was found.

Reasoning: The claim is an infinite constructive theorem rather than a finite database entry.

### claim_vs_prior_implication

Searches: Compare six-cycle proof with Bo–Lian–Liu cycle coefficient 4/3

Evidence: The prior coefficient is strictly larger and therefore does not imply the audited upper bound.

Reasoning: The improvement requires a different gadget-coupling argument.

### Source inspections

- **Weak rainbow saturation numbers of paths, stars and cycles** — https://arxiv.org/abs/2609.03823
  - Trigger: Closest prior C₄ upper bound
  - Material read: ArXiv abstract and theorem summary available through current retrieval; full HTML endpoint was unavailable in this run
  - Method: primary-source abstract inspection plus failed full-text endpoint
  - Assessment: NOT_COVERING 6/5
  - Evidence: The abstract states coefficient ell/(ell-1), hence 4/3 for C₄.
- **Weak Rainbow Saturation Numbers of Graphs** — https://arxiv.org/abs/2401.11525v1
  - Trigger: Definition and general existence/bounds
  - Material read: Bibliographic record and theorem descriptions; full text was not retrievable through the current web endpoint
  - Method: primary-source metadata/abstract comparison
  - Assessment: NOT_COVERING 6/5
  - Evidence: General framework does not state the audited construction.
- **A six-cycle construction for weak rainbow saturation of C4** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE001
  - Trigger: Exact published-results hit
  - Material read: Title and summary
  - Method: semantic published-results search
  - Assessment: SELF_MATCH
  - Evidence: Exact same theorem.

Originality residual risks:
- The closest arXiv full text could not be fetched through the current web endpoint; comparison relies on the primary abstract plus the audited package's explicit construction and citations.
- A later or unindexed contemporaneous improvement could exist.

## Value

**PASS** — Reducing the asymptotic upper coefficient for a natural weak-rainbow-saturation problem from 4/3 to 6/5 is a substantive quantitative advance and narrows the known asymptotic interval. The construction is uniform for all n at least 20, not a tiny-instance computation.

Residual risks:
- The optimal coefficient remains undetermined.

## Scientific limitations

- The construction is an upper bound and does not determine the optimal coefficient.
- Finite checker results are supplementary to the symbolic proof.

## Disposition

**PASSED**

This audit is not peer review or external certification.
