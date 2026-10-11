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

`verification/verify_lqr_signs.py` uses only the Python standard library. All matrix entries are parsed as exact rational numbers from the decimals printed in the source.

The replay checks:

1. the standard CARE residual \(A^{\mathsf T}P+PA-P^2+100I_4\) has max norm exactly \(1789/2000000\);
2. the printed-sign residual \(A^{\mathsf T}P+PA+P^2-100I_4\) has max norm exactly \(5532161073/25000000\);
3. the Faddeev–LeVerrier characteristic polynomial of \(A-P\) satisfies the strict quartic Routh–Hurwitz inequalities;
4. the characteristic polynomial of \(-(A+P)\) satisfies the same strict inequalities.

Consequently \(A-P\) is Hurwitz and \(A+P\) has all eigenvalues in the open right half-plane. The verifier does not simulate the nonlinear master/slave system and makes no claim about an unprinted higher-precision gain.
