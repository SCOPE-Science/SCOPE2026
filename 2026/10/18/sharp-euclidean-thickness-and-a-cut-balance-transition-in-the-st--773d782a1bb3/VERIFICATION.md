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

The accompanying `checker.py` independently enumerates all nontrivial cuts for every cycle with 3 through 10 vertices. It builds cyclic tubes directly rather than substituting the symbolic run formula, compares exact normalized-width squares using integer fractions, and checks the claimed minimizing cuts and their complement-equivalent normal lines. It additionally evaluates 4,800 explicit mean-zero test directions from the full coordinate-simplex support-range definition and compares against the predicted minimum; these are numerical corroborations only.

Expected checker output: `VERIFY_OK sizes=3..10 cuts=2024 direct_directions=4800`.

The all-dimensional correctness argument is the three-step analytic proof in `RESULT.md`. No finite test exhausts uncountably many directions in unbounded dimension. Source inspections and potential under-indexing risks are documented in `REVIEW.md` and `AUDIT.json`. Independent validation has not been performed.
