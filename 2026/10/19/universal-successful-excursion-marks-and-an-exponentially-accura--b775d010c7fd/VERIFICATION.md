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

# Verification and reproducibility

The analytical argument in `RESULT.md` proves the high-rate joint transform using the absorbing-interval boundary-value solution, renewal conditioning, endpoint Laplace asymptotics, and a coupling to a half-line process. The explicit finite-rate upper bound is independent of any numerical experiment and holds for every real shape \(\beta>0\) once \(x\ge2\beta+2\). Every limiting assertion quantifies over fixed physical size and diffusion parameters and fixed local-power coefficients; the limit is \(r\to\infty\).

Running `python CHECK.py` with Python 3 and no third-party packages returned `PASS: 219 deterministic tests; no analytical limit inferred from these checks.` It independently integrates the exact two-endpoint first-passage transform, compares uniform resetting with the hyperbolic-tangent identity, checks the predicted transforms at multiple density powers and high but finite reset rates, and checks the finite-circle versus half-line mass discrepancy against the coupling upper bound for integer shapes. The code uses composite-Simpson quadrature, so its tests establish numerical consistency only and are not exhaustive proof.

No independent external scientific audit has been performed. Prior general formulas for the last reset position, mean passage time, and unmarked exponential limit are cited and not represented as newly proved discoveries.
