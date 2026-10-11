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

# Reproducibility and limits

Run `python checker.py` with SymPy installed in the same directory as `RESULT.md`. The script requires no input files and prints `VERIFY_OK` after asserting the Jacobian identities, exact variable transformation, trigonometric resonant projections, bifurcation-amplitude coefficient, nonlinear frequency/period coefficient, and both sign-change locations. The exact symbolic checks do not amount to a finite-data proof of the analytic Hopf bifurcation theorem; the latter follows from the documented transverse crossing and the strictly positive cubic saturation coefficient. The asymptotic expansion is local in \(\mu\) and pointwise in fixed \(K\in(0,1)\). No independent audit or external certification has been undertaken.
