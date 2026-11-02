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

Run `python3 verification/verify.py` with Python 3 and SymPy installed. The program performs exact-rational comparisons of the actual grounded path Laplacian inverse square against the derived formula. It also enumerates the objective at every possible single-leader location and tests the sharp phase boundaries, including exact ties. Its printed output, recorded verbatim in `verification/checks.txt`, reports 2,296 exact grounded-inverse checks and 16,519 exact optimizer-set checks. The claims for arbitrary path sizes and arbitrary real positive exceptional resistance follow from the detailed algebraic proof in `RESULT.md`, not finite enumeration. Only the specified path model and ideal grounding are tested.
