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

# Reproducible checks

Run `python3 verify_weak_decay.py` with Python 3 and SciPy. The companion `verification_output.txt` records the expected output.

The script evaluates Yoshida's finite scale function with exact fractions and compares the hitting probability with an independently solved finite tridiagonal Dirichlet problem for rational probabilities, attenuation factors, and boundaries, passing 684 exact/range/root/quadrature assertions. The printed numerical values demonstrate agreement between small-attenuation integrals and the predicted limit at representative fixed heights, and print the upper-edge comparison; convergence at the slowly varying logarithmic edge is established by proof, not numerical sampling. The dilogarithm action is evaluated with SciPy's Spence function under its conventional definition.

The analytical theorem relies on the Riemann-sum limit, potential sign classification, subcritical geometric domination, bounded convergence and a singular endpoint expansion, as detailed in `RESULT.md`. These are proved mathematical assertions, not independently certified computational results. No independent audit was performed.
