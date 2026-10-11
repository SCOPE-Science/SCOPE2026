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

# Verification of the polygon circle-intersection theorem

Run `python verify.py` with Python 3, `sympy`, and `mpmath`. The script must terminate with `VERIFY_OK`. It symbolically reduces the squared gap using the identity \(\sin^2lpha+\cos^2lpha=1\) and enumerates all ordinary radius chambers for a finite, explicitly stated set of polygon orders and boundary-center parameters with 75-digit arithmetic. It independently constructs circle/segment roots and tests just-below/just-above six-window values, even-polygon endpoints, and odd-polygon edge midpoints. Orders up to 101 are tested for the six-point witness, but no finite test certifies an infinite claim.

The proof's actual nonstandard steps are the angular local-maximum criterion, two/three-peak upper bound, opposite-side projection identities, and the exact quadratic factorization. The quadratic factorization and selected roots are checked by the script; the global angular arc argument and critical-level counting are proved in RESULT.md and are not certified by finite numerical tests. The present review is not independent validation or an external certificate.
