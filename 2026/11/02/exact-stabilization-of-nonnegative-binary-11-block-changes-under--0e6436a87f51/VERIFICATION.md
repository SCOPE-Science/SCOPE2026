---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The statistic counts overlapping adjacent 11 pairs, not runs. I reconstructed the eight states (previous input/output bit and carry), the exact 1/2-weight digit transitions, the zero-suffix carry expectation and F_a=e_000 M_1 M_0^(a-1) M_1 H. The characteristic identity det(lambda I-M_0)=lambda^6(lambda-1)(lambda-1/(2z)) makes later consecutive differences scale by 1/(2z) once a>=7. The explicitly factored F_8-F_7 has numerator degree 8 and denominator degree 9, so it has no nonnegative Laurent powers at infinity; the same is true for every later increment. Rational symbolic reconstruction of Q_1,...,Q_8 agrees with the six exceptions and the sharp plateau Q_a=(54+65z+44z^2+12z^3)/256 for all a>=7. The carry persistence probability O(2^-L) permits finite-cylinder approximation, proving natural density existence. Q_6 differs from Q_7 and all j>3 have zero mass, and any finite integer with larger change would give a positive-measure cylinder, ruling out pointwise j>3. Finite enumerations are corroboration, not a substitute for Cayley-Hamilton.

## originality

PASS

Qualified PASS: the broad published exact conditional recurrences for 11-block changes compute each individual shift in principle, and the many-one-block Gaussian theorem is prior work. I found no inspected statement fixing the precise uniform finite a=7 stabilization and four nonnegative masses for all a>=7. This is a mathematical statement stronger than isolated recurrence evaluation, but its derivability by a simple unreported specialization of prior recurrences is a substantive priority risk.

## value

PASS

The sparse-shift 11-block law is a natural sharp arithmetic stability invariant: it determines exactly when the nonnegative mass function stops depending on the separation of two changed bits, not merely an isolated finite table. It refines a pre-existing general recurrence to an all-separation structural threshold and exact four masses, likely useful to researchers of block-counting and generalized Cusick-type density phenomena.

The dated certificate retains the supplied scientific assessment, sources and limitations.
