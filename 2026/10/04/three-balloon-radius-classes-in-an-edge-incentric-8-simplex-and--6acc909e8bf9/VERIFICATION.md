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
# Verification

The accompanying `verify.py` uses only Python's standard library and exact rational arithmetic for the certificate identities. It checks:

- exact signs isolating the selected zero \(b\) of \(P\);
- exact substitution/factorization certificates for \(H_1\) and \(H_2\);
- the exact remainder formula for \(M^2-7N\) modulo \(P\);
- the zero-linear-coefficient auxiliary-root identity and coefficient matching;
- positivity and distinctness bounds sufficient for the construction.

The analytic Vieta argument proves that four positive classes are impossible. The checker does not claim an exhaustive classification of three-class examples or minimality of dimension \(8\). Decimal values printed by the checker are diagnostics and are not used to establish the theorem.
