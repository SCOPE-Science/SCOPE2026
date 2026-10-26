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

Run `python3 checker.py` with Python 3 and no external packages. Successful standard output ends in `ALL_CHECKS_OK 269746`.

Checks include direct truth-functional evaluation of the McKinsey schema over every valuation on each labelled symmetric adjacency matrix with 1–5 vertices, exact involution frame counts, exhaustive rooted counts for all loop-free labelled graphs through 6 vertices, and rational-probability inclusion-exclusion checks. Numerical sparse-limit diagnostics at five positive constants are approximate tests, not infinite certificates. The unrestricted local and global results are established in RESULT.md by proofs, and the Poisson limit by factorial moments. External independent validation has not been performed.
