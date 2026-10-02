---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"passed"}
---

# Independent mathematical audit

## Final claim

In dimension four, isolated rank-zero Poisson germs with rank two off the origin and vanishing first jet need not have the same unimodularity behavior: the displayed conformal germ is non-unimodular, while the displayed Jacobian germ is unimodular.

## Correctness — PASS

The two germs were reconstructed from their formulas. For the conformal germ, the Schouten bracket vanishes, the modular field is (-2 x_2, 2 x_1, 0, 0), and every Hamiltonian vector field vanishes to order at least two, so the nonzero linear modular term cannot be Hamiltonian. For the Jacobian germ, the two displayed quadrics are Casimirs, the identity pi_13 + pi_24 = |x|^2 isolates the zero, the rank is exactly two off the origin, the modular field vanishes identically, and every coefficient has zero first jet. These checks agree with the exact symbolic verifier.

Checked sources: artifacts/verify.py (blob 39ca0dc07251fdd4d286ceed314eca502697d4c0)

Residual risks: The statement is local and germ-level; it does not supply a compact global example.

## Originality — PASS

The closest inspected literature provides general formulas and classifications for Poisson structures and modular classes in four dimensions, but no source located states or implies that the particular shared local data in the final claim admit both unimodular and non-unimodular realizations. The paired examples therefore establish a structural boundary not supplied by the general formulas alone.

### Equivalent formulations

The comparison was made at the level of shared hypotheses and the implication they fail to determine. Evidence: The literature describes modular vector fields and Jacobian/conformal constructions but did not identify this exact paired counterexample.

### Broader coverage

The audited dichotomy is not a corollary of the general framework found. Evidence: General R4 formulas are broader in object class but do not force a common unimodularity verdict from isolated zero, off-origin rank two, and vanishing first jet.

### Exact database or table

No tabulated prior result was located. Evidence: No exact example table with both displayed germs or the same hypothesis package was found.

### Claim versus prior implication

The final claim is a counterexample to an implication rather than a routine parameter substitution into a theorem. Evidence: The general formulas permit direct verification of each example, but they do not state the negative implication that the shared local data fail to determine unimodularity.

### Source inspections

- **On Poisson structures on R4** — https://arxiv.org/abs/1306.5254. Trigger: Same dimension and explicit Poisson/unimodularity formulas. Material read: Abstract and relevant formulas/classification context for four-dimensional Poisson structures and modular behavior. Method: Primary full-text inspection. Assessment: NOT_COVERING. Evidence: The paper supplies general machinery but not the paired local dichotomy under the audited common hypotheses.
- **Modular classes of Poisson structures** — https://arxiv.org/abs/1103.4267. Trigger: General modular-class framework. Material read: Definitions and structural context for modular classes and unimodularity. Method: Primary literature inspection. Assessment: NOT_COVERING. Evidence: The framework does not settle the audited local-data implication.

Checked sources: https://arxiv.org/abs/1306.5254; https://arxiv.org/abs/1103.4267; https://www.esi.ac.at/preprints/esi1973.pdf

Residual risks: The examples are elementary enough that an older unindexed source could contain an equivalent pair; no such source was located.

## Scientific value — PASS

The result is a motivated boundary statement: it shows that isolated rank-zero behavior, off-origin rank two, and an abelian linearization are insufficient local data to determine unimodularity. Such counterexamples directly constrain what a local criterion can use, even though the examples themselves are explicit and low-degree.

Checked sources: general modular-class literature; package constructions

Residual risks: Its value is as a local obstruction/boundary; it does not resolve the compact global problem that motivated the investigation.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and scientific value.
