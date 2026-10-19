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

# Reproduction and analytical limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier checks the \(Q=\begin{psmallmatrix}3&1\\1&1\end{psmallmatrix}\), \(\sigma^2=1\), \(\beta=3\) witness using exact arithmetic in \(\mathbb Q(\sqrt3)\), including the active budget, optimal gain, complete covariance matrix, equality in Cauchy–Schwarz, and objective. It also uses fixed-seed finite parameter trials on both sides of the threshold and checks the claimed optimum against a 100-point feasible scalar grid in each case.

Expected output is `VERIFY_OK exact_quadratic_surd_witness_identities=13 dual_boundary_checks=320 grid_global_inequalities=32000 phase_cases=320`.

The grid is a numerical diagnostic only; it cannot establish an infinite-parametric claim, a uniqueness assertion, or originality. Those mathematical conclusions rest on the explicit moment reduction, strict concavity, equality conditions, and closed-form ellipse maximization in RESULT.md. The verifier does not check arbitrary histories, dimensions, noise distributions, or hardware implementations. An independent audit has not been performed.
