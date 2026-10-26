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
# Verification information

The independent audit is not yet performed. The analytical proof is in `RESULT.md`; the optional reproducibility script is `check.py` and requires Python, NumPy, SciPy, and SymPy. Run `python check.py` in the same directory as the other files. It checks the exact rational identities symbolically, tests the Zak normalization by a direct convergent time-domain sum, checks the two frequency-derivative squares and the quadratic-critical numeric behavior. A successful invocation emits `CHECK_OK` with the three exact-formula constants evaluated numerically.

The numerical tests check finite samples only: they do **not** establish that the Zak zero list is exhaustive, that the lower frame symbol is globally positive, or that the limiting quadratic law holds. Those three global conclusions are established by the exact algebra, compactness, and Taylor arguments in `RESULT.md`. A historical novelty check and an independent scientific audit remain outstanding.
