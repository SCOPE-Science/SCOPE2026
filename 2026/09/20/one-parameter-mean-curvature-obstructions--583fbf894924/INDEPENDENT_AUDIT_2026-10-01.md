# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-583fbf894924`

## Correctness — PASS

The hyperbolic normalization is exact: writing the inputs as \(m e^{-u}\) and \(m e^u\) expresses the logarithm of the mean as a difference of the even analytic function \(\phi(z)=\log(\sinh(z)/z)\). At the reflection center \(r=-\alpha/2\), the logarithmic second derivative vanishes while the logarithmic first derivative is nonzero, so ordinary curvature is strictly positive. For the symmetric product, differentiating the even formula and expanding \(\phi\) gives \((\log P)''=-(2\alpha/15)u^4+O(u^6)\), uniformly for \(r\) on compact sets. The inspected symbolic verifier reproduces both leading coefficients and direct sample signs.

### Correctness sources

- assigned RESULT.md
- Cheung–Qi 2007 primary paper, DOI 10.11650/twjm/1500404648
- artifacts/verify_curvature_obstructions.py

### Correctness risks

- The result does not classify the full curvature sign diagrams.
- The near-diagonal transition for ordinary curvature is asymptotic, not a global exact inflection point.

## Originality — PASS

The 2007 primary paper was inspected at the definition and explicit Open Problems 1 and 2. It poses the two curvature claims that the audited theorem refutes. The 2009 follow-up treats monotonicity and logarithmic-convexity properties rather than these counterexamples, and the 2025 survey revisits the established one-parameter theory without an identified resolution of the two questions. Current semantic search found no other theorem giving the midpoint obstruction or the near-diagonal product-curvature expansion.

### equivalent_formulations

Searches:
- Resultary query: generalized one-parameter mean Cheung Qi concavity Open Problem 1 J_alpha product logarithmic convexity
- Cheung–Qi 2007 full text
- searches for the reflection center and the coefficient -2 alpha / 15

Evidence:
- The source explicitly states strict concavity as Open Problem 1 and the exterior log-convexity clause in Open Problem 2.
- No separate published counterexample was found.

Reasoning:
Equivalent formulations through the generalized one-parameter mean, Stolarsky terminology, reflection symmetry, and product logarithmic curvature were checked.

### broader_coverage

Searches:
- Qi–Cerone–Dragomir–Srivastava 2009
- Yang–Qi 2025 survey

Evidence:
- The 2009 work provides alternative proofs of known monotonic/logarithmic-convex properties.
- The later survey discusses the established theory but no matching resolution was located.

Reasoning:
The inspected broader literature does not dominate the audited counterexamples.

### exact_database_or_table

Searches:
- current Resultary mean-inequality findings

Evidence:
- The only exact semantic match was the audited finding; no table/database encodes these curvature signs.

Reasoning:
This is an analytic counterexample theorem, so exact-database coverage is not the natural prior-art route.

### claim_vs_prior_implication

Searches:
- Cheung–Qi proven log-concavity versus audited ordinary convexity
- product monotonicity versus product log-curvature

Evidence:
- A positive log-concave function can still have positive ordinary second derivative, so the midpoint obstruction does not contradict the source theorem.
- Monotonicity of the symmetric product does not imply its second logarithmic derivative has the conjectured sign.

Reasoning:
The audited claims are logically distinct from the prior proven properties.

### source_inspections

- **Logarithmic Convexity of the One-Parameter Mean Values** — https://doi.org/10.11650/twjm/1500404648. Trigger: Primary source of both open problems. Material read: Author-posted full text, including the generalized definition and the explicit final open problems. Method: Primary full-text theorem/problem comparison. Assessment: The source poses rather than solves the audited questions. Evidence: Open Problem 1 asserts ordinary strict concavity and Open Problem 2 asserts exterior logarithmic convexity of the symmetric product.
- **Alternative proofs for monotonic and logarithmically convex properties of one-parameter mean values** — https://doi.org/10.1016/j.amc.2008.11.023. Trigger: Direct citation-chain follow-up. Material read: Accessible author-posted abstract/introduction and stated theorem scope. Method: Scope and implication comparison. Assessment: Not covering the audited curvature obstructions. Evidence: Its stated focus is alternative proofs of monotonicity and logarithmic-convexity properties.
- **Bivariate homogeneous functions of two parameters** — https://doi.org/10.1016/j.jmaa.2024.129091. Trigger: Recent survey/review source in the citation chain. Material read: Accessible discussion of the one-parameter mean and its established curvature/monotonicity properties. Method: Recent-literature comparison. Assessment: No matching resolution was located. Evidence: The discussion records known one-parameter results and product monotonicity without the audited counterexamples.

### checked_sources

- Cheung–Qi 2007 primary text
- Qi et al. 2009
- Yang–Qi 2025
- current Resultary exact semantic search
- assigned symbolic verifier

### residual_risks

- The midpoint argument is short and may have appeared informally or in poorly indexed literature.

## Scientific value — PASS

The theorem gives universal counterexamples to a published open problem for every parameter and unequal input pair and refutes a second conjectured exterior regime by a robust asymptotic mechanism. It also identifies the structural reflection reason for the first failure.

### Value sources

- Cheung–Qi Open Problems 1 and 2
- audited exact midpoint and near-diagonal calculations

### Value risks

- The central clauses of Open Problem 2 remain unresolved.

## Limitations

- The full ordinary-curvature sign diagram is not classified.
- The full symmetric-product log-curvature diagram is not classified.
- The central clauses of Open Problem 2 remain open.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
