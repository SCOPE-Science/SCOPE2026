---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The theorem has an explicit algebraic proof for all probability factors in the closed two-dimensional simplex. The key determinant identity is independently checked with the included `checker.py` by evaluating two degree-at-most-three-in-each-variable polynomials at all \(4^6=4096\) points in a degree-determining grid. The standard-library program also tests the exact equality interval on 101 rational parameter values, tests the full simplex inequality on rational-grid factor samples, and checks both dual-potential regimes with rational parameters.

Run: `python3 checker.py`. Observed outcome: `PASS 9469 exact checks including 4096 identity-grid points`.

The finite grid on normalized factor pairs is **not** a global optimization certificate by itself. The global result, including boundary cases and the equality classification, uses the inequalities in `RESULT.md`, the polynomial identity, and equality conditions for the elementary dual estimate. The 2026 lead preprint explicitly states the broader \(n\ge3\) bound as a conjecture; this result treats only \(n=3\). Scientific review is same-model only. Independent audit and independent validation have not been performed.
