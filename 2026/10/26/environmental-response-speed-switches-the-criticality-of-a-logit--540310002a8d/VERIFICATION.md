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
# Verification of the logit feedback Hopf coefficient

Execute `python verification/verify_hopf_criticality.py` using packages from `verification/requirements.txt`. The script performs three independently specified checks. First, symbolic Taylor differentiation and the exact planar Hopf formula simplify identically to the stated coefficient, using the identities \(k^2=1-4q\) and \(\tau=-\chi\omega/k\). Second, a finite rational series and a rigorous geometric tail bound for \(\log10\) imply \(23/10<\log10<231/100\), yielding exact strict Lyapunov-sign inequalities for speeds \(1\) and \(40\). Third, accurate integrations compute Poincaré-section drifts at two radii at each speed, confirming their signs.

The symbolic calculation is an exact algebraic identity, while the rational inequalities strictly certify the example's sign separation. The numerical experiments do not establish the result for every possible parameter. The analytical proof of the general sign theorem is in `RESULT.md`. No independent review or validation has been performed.
