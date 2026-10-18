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
The file `verify.py` uses only the Python 3 standard library. Run `python3 verify.py` after extraction. It checks the exact fourth-moment quotients at character orders \(3\), \(4\), and sample orders at least \(5\) using exact rational arithmetic, verifies the sharp quadratic deficit identities on rational samples, and checks the fourth-root phase family by Gaussian-integer correlations.

The analytic proof in `RESULT.md` establishes the theorem for every compact Abelian group carrying a character of each stated order. The finite checker is not an exhaustive search for all coefficients or a proof for infinitely many orders; it verifies separately derived algebraic identities and extremal witnesses. All source comparisons are historical research checks, not mathematical certification of uniqueness. Independent audit has not been performed.
