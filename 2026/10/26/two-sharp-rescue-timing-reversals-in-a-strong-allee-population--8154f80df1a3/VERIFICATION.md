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

The mathematical proof is in `RESULT.md`. The standalone numerical checker is `verify_allee.py` (Python with NumPy/SciPy as described in `requirements.txt`). Invoke `python verify_allee.py` in the directory containing the script; an expected successful run reports `VERIFICATION_OK`, 96 randomized parameter sets, and two roots near 0.145029705606619 and 0.654970294393381 in the soluble symmetric example.

The verifier integrates the scalar equation with absolute tolerance 2e-14 and relative tolerance 2e-12, locates two crossings independently in their analytically established brackets, and samples the sign pattern at 101 points for each test case. It is a non-exhaustive numerical cross-check, not an infinite-dimensional or universal proof. The proof's decisive ingredients are exact differentiation of the scalar flow, a single curvature sign change, and strict endpoint signs. The asymptotic limits are established analytically, not certified by finite-horizon plots.

No independently conducted mathematical audit has been performed.
