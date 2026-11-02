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

The general classification has a self-contained mathematical proof in RESULT.md. Exact finite checks were performed by running the embedded standalone `verify.py` with Python standard-library `fractions.Fraction` arithmetic.

Observed result: `VERIFY_OK rational_graph_parameter_cases=2555 graph_profiles=365 parameters=7`.

For every tested graph the checker verifies grand-coalition and deletion identities, negative-side contradictions when an arc has positive weight, stability of independently sampled graph-zonotope core allocations, and efficiency plus every coalition inequality for restricted games. It also independently checks the rank of the edge-difference matrix by rational elimination against the positive-support component count, and includes empty, single-edge, and zero-weight-arc boundary cases.

Finite rational samples cannot certify arbitrary real coefficients or arbitrary large networks. The proof supplies those quantifiers; there is no formal-system certification and no independent external validation.
