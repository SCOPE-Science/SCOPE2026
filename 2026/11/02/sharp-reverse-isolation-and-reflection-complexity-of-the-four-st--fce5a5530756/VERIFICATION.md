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

# Reproducibility and verification

Run `python3 verify.py` from the directory containing both `verify.py` and `factors8.txt`; the verifier uses no third-party libraries. The observed success output ended with `VERIFY_OK`. It checked that the eight adjacent pairs all occur by substitution depth four, generated exact factor sets up through length eight by depth-three two-block windows, compared those sets to an independently generated 8192-symbol prefix, verified all reversible and palindromic factors through length eight, and recomputed the factor-complexity formula through length 256 using exhaustive depth-eight block images. It also checked the sorted 56-factor `factors8.txt` list against the generated set and its SHA-256 `2aa97abe490366aad190ec88b638589d77046f871f0d6b69982810e4a6ec0fb4`.

The infinite statement is justified by the mathematical lemmas in `RESULT.md`: classwise injectivity establishes the global factor count, and the two-block decomposition makes the finite length-eight certificate exhaustive in the infinite fixed point. Finite computations alone would not prove the statement for unbounded factor lengths. No independent scientific audit, Lean formalization, external certificate review, or other independent validation is asserted.
