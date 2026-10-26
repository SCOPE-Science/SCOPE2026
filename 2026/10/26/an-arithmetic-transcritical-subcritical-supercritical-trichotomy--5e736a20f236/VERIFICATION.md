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

The script `check_fourier.py` runs under Python 3 without third-party packages and computes the exact rational coefficients of the normalized invariant-density perturbation after factoring powers of \(\pi\). It checks the Fourier pushforward recurrence through cubic order for degrees \(2,3,4,5,6,8,10,20\), including zero mean, mode symmetry, and all three first-moment cases. The accompanying `checker_output.txt` records actual execution.

The analytic proof extends the cubic cases from finite diagnostics to all integers \(b\ge4\) because no Fourier frequency above three is generated through third order, so \(P_b\) annihilates every nonzero input at those degrees. Analytic dependence and scalar-root exhaustion follow by strip-space implicit-function and strict quadratic curvature. No computer experiment claims to certify an infinite proof.

No independent scientific audit has been undertaken. The cited literature and precise limitations appear in `RESULT.md` and `AUDIT.json`.
