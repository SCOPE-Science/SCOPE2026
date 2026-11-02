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
# Verification details

The accompanying `verify.py` is standalone source code for recomputing finite examples and checking a symbolic characteristic polynomial. Run with Python 3 and dependencies listed in `requirements.txt`.

The program constructs the genuine \((m+2)\)-dimensional shift Jacobian. It compares the direct characteristic polynomial for \(m=3\) with the stated exact formula using symbolic algebra, then checks residuals and spectral locations for several memory lengths and a grid of \(\kappa\)-values. It separately evaluates the double-root boundary and the parameter point \((m,\tau,\mu)=(150,70,0.001)\). These runs passed when packaged.

The proof for arbitrary \(m\) uses the explicit Jacobian/characteristic identity, real-root sign changes, analytic perturbation of simple roots, and a second-order expansion of the double fast root. The finite checks are diagnostic and not a substitute for any of these arguments. No independent mathematical or computational audit has been performed, and no global fixed-gain assertion is certified.
