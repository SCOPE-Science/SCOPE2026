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

# Reproducible verification

Run `python3 verify.py` using Python 3 with the standard library only.

The program (i) builds all sixteen linear subspaces of \(\mathbb F_2^3\) and computes exact rational expected first-recovery times by a subspace Markov chain for seven sample distributions; (ii) compares those times with the closed access functional; (iii) checks the thirteen-column witness value \(167/60\) and its strict separation from \(279/100\); (iv) derives all Bernstein coefficients by exact rational conversion on sixteen subintervals for three boundary polynomials and verifies positive minima; (v) checks the transformed-polynomial identities at rational points; and (vi) checks the rational gradient residual and the stated global strong-convexity constant used for the optimizer enclosure.

Expected output begins with `localization_center` and then `VERIFY_OK`. The three boundary certificate minima printed are \(8873/12288\), \(24521/512\), and \(1557633/2048\), respectively.

The subspace tail identity, the exact Hessian matrix domination, the denominator signs and the compactness argument are established in `RESULT.md`; computation checks are supporting finite certificates and do not alone prove an all-distribution statement. No independent audit or external validation is claimed.
