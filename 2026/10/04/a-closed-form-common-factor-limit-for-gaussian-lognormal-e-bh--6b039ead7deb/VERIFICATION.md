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

`verifier.py` uses only the Python standard library. It verifies the Gaussian-hazard root equation by bisection, confirms the sign change of the derivative and the scalar minimum independently on a dense grid, checks the tangency equation, and verifies opposite sides of the common-factor boundary.

For \(\alpha=0.05\), \(\delta=3\), and \(\rho=1/2\), the expected output begins with `VERIFY_OK` and reports
\[
t_*=0.0433882935110755,\qquad
w_*=3.29993272728449,\qquad
\bar\Phi(w_*)=0.000483540037137713.
\]
The script is a numerical check of the scalar calculus. The large-\(K\) limit itself is justified analytically by conditional empirical-tail convergence and binomial concentration, not by simulation.
