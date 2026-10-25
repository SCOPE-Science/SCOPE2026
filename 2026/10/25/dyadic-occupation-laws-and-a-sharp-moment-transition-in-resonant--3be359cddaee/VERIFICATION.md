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

The standalone `verify.py` reconstructs orbit values directly with Python `fractions.Fraction`, independently computes \(\nu_2(k+1)\), and checks every even and odd index for 4,096 steps for nine rational parameter values. It verifies exact level counts and exceptional parameter cases. Critical-moment numerical ratios for \(d=-2,3,-3\) and dyadic horizons are printed as a diagnostic, without being used as proof. Execute `python verify.py` with Python 3. No external packages are required.

The universal, all-real-parameter and all-time claims are established analytically in RESULT.md. The verifier does not establish novelty or independent auditing.
