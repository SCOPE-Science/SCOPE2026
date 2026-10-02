# Fresh audit — SCOPE-20260910-046

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

On the unit-length metric graph \(K_{3,3}\), the degree-three divisor consisting of the three matching-edge midpoints has Baker–Norine rank exactly zero.

## Correctness

**PASS** — The one witness point needed for the upper bound was independently reconstructed. On the once-subdivided 15-vertex model, Dhar burning from \(a_0\) for the divisor \(D-a_0\) burns all 15 vertices while the value at \(a_0\) is negative; hence the divisor is \(a_0\)-reduced and not equivalent to an effective divisor. Since \(D\) itself is effective, the rank is exactly zero. The archived verifier source gives the same burn certificate.

Residual risk: The package contains auxiliary finite-subdivision corroboration that is not needed for the decisive single-point rank upper bound.

## Originality

**PASS** — Resultary search returned the assigned record as the direct exact match. Luo gives the metric-graph reduced-divisor/rank-determining framework, and work on gonality-three and low-genus tropical curves gives the surrounding structural context, but no inspected source states or implies this exact symmetric midpoint-divisor rank on unit \(K_{3,3}\).

Residual risk: A specialized unpublished divisor table could exist; the literature search cannot prove universal absence.

### Originality checks

**equivalent_formulations**

Searches: Resultary semantic query: unit K3,3 matching midpoints Baker Norine rank; metric graph divisor rank matching edges K3,3.

Evidence: https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE046; Ye Luo, Rank-determining sets of metric graphs, https://arxiv.org/abs/0906.2807.

Reasoning: The reduced-divisor criterion is general; no equivalent exact statement for this divisor was found.

**broader_coverage**

Searches: gonality three graphs K3,3; low-genus trigonal tropical curves.

Evidence: https://arxiv.org/abs/1810.08665; https://arxiv.org/abs/2602.02257.

Reasoning: The structural papers concern gonality/trigonal geometry broadly and do not force the rank of this particular midpoint divisor.

**exact_database_or_table**

Searches: Resultary and literature search for exact divisor tables on unit K3,3.

Evidence: No exact external table containing this divisor/rank pair was located..

Reasoning: The assigned record was the only direct exact match found.

**claim_vs_prior_implication**

Searches: Luo reduced divisors and rank-determining sets; gonality-three classifications.

Evidence: https://arxiv.org/abs/0906.2807; https://arxiv.org/abs/1810.08665.

Reasoning: Those theorems provide tools and ambient gonality information but do not imply that this named degree-three divisor has rank zero.

### Source inspections

- **Assigned RESULT.md** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/046/RESULT.md. Trigger: Exact claim/proof. Material read: Full Dhar burning proof and limitations. Method: direct file inspection. Assessment: SUPPORTS. Evidence: The rank-zero inference from one unwinnable subtraction is correct.
- **verify_disproof.py** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/046/artifacts/verify_disproof.py. Trigger: Critical certificate. Material read: Full graph construction and burn loop. Method: direct source inspection plus independent reconstruction. Assessment: SUPPORTS. Evidence: The 15-vertex burn reaches the whole graph and leaves the sink negative.
- **Rank-determining sets of metric graphs** — https://arxiv.org/abs/0906.2807. Trigger: Reduced-divisor/rank framework. Material read: Relevant metric-graph rank-determining and reduced-divisor material. Method: primary-source search/inspection. Assessment: NOT_COVERING_EXACTLY. Evidence: Gives the general method, not this exact divisor.
- **Trigonal and embedded tropical curves of low genus** — https://arxiv.org/abs/2602.02257. Trigger: Same low-genus trigonal context. Material read: Abstract/relevant scope for genus-three/four trigonal tropical curves. Method: primary-source search/inspection. Assessment: NOT_COVERING_EXACTLY. Evidence: Does not state the matching-midpoint rank calculation.
- **Graphs of gonality three** — https://arxiv.org/abs/1810.08665. Trigger: Broader gonality coverage. Material read: Classification context for gonality-three graphs. Method: primary-source search/inspection. Assessment: NOT_COVERING_EXACTLY. Evidence: Graph gonality does not determine rank of this specific divisor.

## Value

**PASS** — The divisor is a natural symmetric degree-three divisor on the canonical genus-four trivalent graph \(K_{3,3}\), and its rank directly decides a proposed tropical Brill–Noether/lifting witness. A concrete rank-zero obstruction here is therefore a motivated boundary/counterexample, not an arbitrary finite calculation.

Residual risk: The value is localized to the named divisor and does not classify all degree-three divisors on the graph.

## Overall disposition

**PASSED**
