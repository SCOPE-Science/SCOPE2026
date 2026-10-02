# Fresh audit — SCOPE-20260910-050

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the stated Markoff-type K3 surface at parameter \(k=3\), the affine integral model has no points modulo 8 and therefore no \(2\)-adic or integral points; the displayed \(z=1\) fibre also has no rational point, so the proposed elliptic-curve rank certificate is inapplicable.

## Correctness

**PASS** — The finite local obstruction was independently exhausted over all residue classes modulo 8 and has zero solutions. Therefore an integral or \(2\)-adic point cannot exist. For the fibre, writing a rational coordinate as a reduced fraction yields two coprime quadratic forms whose product must be a square; the parity and square classes modulo 8 rule out both sign branches, while the projective boundary would require a nonsquare rational ratio. This supports rational-point emptiness of the fibre as stated.

Residual risk: The result is parameter-specific and does not establish other geometric invariants of the surface.

## Originality

**PASS** — The highly relevant Dao paper on Brauer–Manin obstructions for the same Markoff-type Wehler family was inspected; its main explicit obstruction family uses negative parameters of a special form and its local-solubility hypotheses do not cover \(k=3\). Resultary search returned the assigned record as the direct exact match. No source inspected states the modulo-8 emptiness or rational-fibre emptiness for this parameter.

Residual risk: Best-of-knowledge originality remains subject to obscure parameter-specific computations not indexed in the searched sources.

### Originality checks

**equivalent_formulations**

Searches: Resultary Markoff K3 k=3 mod 8 empty rational fibre; same-family parameter k=3 integral points.

Evidence: https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE050; Quang-Duc Dao, https://arxiv.org/abs/2302.11515.

Reasoning: The exact parameter-three congruence obstruction and fibre statement were not found outside the assigned record.

**broader_coverage**

Searches: Dao Markoff-type Wehler K3 Brauer-Manin theorem; later rational/integral points Markoff-type K3.

Evidence: https://arxiv.org/abs/2302.11515; https://arxiv.org/abs/2504.10992.

Reasoning: The inspected theorem in the 2023 paper treats a special negative-parameter family and does not dominate the positive parameter-three case.

**exact_database_or_table**

Searches: parameter k=3 local-solubility tables Markoff-type K3; Resultary exact k=3 query.

Evidence: No external exact modulo-8 table or rational-fibre table for this parameter was located..

Reasoning: No database/table found supplied the claimed emptiness.

**claim_vs_prior_implication**

Searches: same-family Brauer theorem hypotheses and local-solubility propositions.

Evidence: Dao 2023 requires parameter hypotheses not satisfied by k=3..

Reasoning: The main prior theorem does not imply this case; the elementary mod-8 obstruction is separate and stronger than a height-window sieve for the parameter at hand.

### Source inspections

- **Assigned RESULT.md** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/050/RESULT.md. Trigger: Exact arithmetic claims. Material read: Full rational-fibre proof, mod-8 proof, scope limits. Method: direct file inspection. Assessment: SUPPORTS. Evidence: The local obstruction is sufficient for integral emptiness, and the fibre parity argument is coherent.
- **mod8_emptiness_proof.py** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/050/artifacts/mod8_emptiness_proof.py. Trigger: Critical finite local certificate. Material read: Entire 512-class and 64-class exhaustive checker. Method: direct source inspection plus independent enumeration. Assessment: SUPPORTS. Evidence: Independent recount also found zero solutions in both residue searches.
- **Brauer-Manin obstruction for Wehler K3 surfaces of Markoff type** — https://arxiv.org/abs/2302.11515. Trigger: Same family and closest prior theorem. Material read: Full theorem region and parameter hypotheses, including the explicit negative-parameter obstruction family. Method: primary PDF inspection. Assessment: NOT_COVERING_EXACTLY. Evidence: The theorem region inspected does not include k=3.
- **Rational and integral points on Markoff-type K3 surfaces** — https://arxiv.org/abs/2504.10992. Trigger: Plausible later broader source. Material read: Abstract/scope for rational and integral points in related Markoff-type families. Method: primary-source search/inspection. Assessment: NOT_DECISIVE_COVERAGE. Evidence: No exact implication of the k=3 congruence/fibre claim was found.

## Value

**PASS** — The parameter \(k=3\) is a concrete case in an active Markoff-type K3 arithmetic family that is not covered by the inspected obstruction theorem. An unconditional elementary local obstruction eliminates the entire integral-point problem for this case and simultaneously exposes an ill-posed rank-certificate premise on a natural fibre, making the result a motivated boundary/correction rather than a random congruence check.

Residual risk: The contribution is a single parameter and does not generalize the Brauer–Manin analysis.

## Overall disposition

**PASSED**
