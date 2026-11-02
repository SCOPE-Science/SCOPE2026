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

# Verification and limits

Run `python3 checker.py` in the directory containing the research files. The checker requires only the Python 3 standard library. It constructs directed edges explicitly and forms the ordinary and non-backtracking transition matrices independently of the closed formulas; each matrix has exact rational entries and verified unit row and column sums. For eight specified bouquets it computes the fundamental-matrix trace with rational Gaussian elimination, compares to both analytic formulas, and checks the sign. It additionally tests the strict-classification statement on all bouquets with two through four cycles and each cycle length between three and seven. The recorded execution printed `CHECKS_OK 799 exact comparisons`.

The full infinite-size conclusion is supplied by the determinant identity and strict coordinate-derivative argument in `RESULT.md`, not by exhaustive or probabilistic numerical evidence. The reduction of the non-backtracking arc matrix to tour coordinates is justified algebraically and all relevant zero-denominator expressions are polynomial identities after cancellation. The comparison is strictly about edge-state hitting times. The work has no independent audit or computational certification beyond these ordinary exact checks.
