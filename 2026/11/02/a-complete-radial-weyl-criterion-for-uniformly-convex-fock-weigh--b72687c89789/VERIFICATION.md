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

# Analytical and computational verification

The proof uses four independently checkable ingredients: exact monomial diagonalization and multiplicity \(\binom{n+d-1}{d-1}\); the uniform strong-concavity localization of the radial moment density; the saddle equation \(r_n\phi'(r_n)=n+d-1/2\) with radial-slope derivative bound \(|h'(r)|\le C/r\); and the threshold bracketing \(n_t=r_t\phi'(r_t)+O(r_t)\). Their combination implies the asserted profile and its necessary-and-sufficient consequence without numerical extrapolation.

The included `check.py` was executed using scipy and passed 162 finite tests of radial eigenvalue-integral asymptotics and degree-multiplicity scaling, covering Gaussian, oscillatory-Hessian-but-convergent-slope, and log-oscillating-slope examples. Representative diagnostics (dimension two, decay exponent two, degrees 40/160/640) trend to the instantaneous predicted profiles. The exact outputs are reproducible with `python check.py` after installing `requirements.txt`.

The computation is only a finite diagnostic. It does not certify the analytic asymptotic uniformity, the full cluster intervals, novelty, or the claim's relationship to inaccessible papers. No independent audit was conducted.
