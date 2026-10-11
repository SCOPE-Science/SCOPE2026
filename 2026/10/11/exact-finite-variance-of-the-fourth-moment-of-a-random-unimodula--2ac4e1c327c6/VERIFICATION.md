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

The analytic verification uses three exact ingredients.

1. Parseval gives \(X_n=n^2+2E_n\).
2. Haar character orthogonality reduces \(\operatorname{Var}(E_n)\) to a sum of squared multiplicities of nontrivial exponent vectors.
3. Every such vector has multiplicity \(1\) when the two positive offsets coincide and multiplicity \(2\) otherwise; the only collision is the interchange of the two positive offsets.

The accompanying `verify.py` constructs the exponent vectors directly for every \(2\le n\le40\), checks the number of constant terms, checks that all nonconstant multiplicities lie in \(\{1,2\}\), and verifies the exact parity formula for the sum of squared multiplicities.

The finite replay is not an exhaustive proof for arbitrary \(n\); the all-\(n\) conclusion rests on the explicit character classification and closed-form counts in `RESULT.md`.
