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

# Reproduction and verification

The fully embedded standalone `check.py` requires only Python 3's standard library. Run `python check.py`. The script loops over the complete finite family of block-preserving maps for each specified small parameter pair, materializes the resulting transformation of the entire point set, tests idempotence and commutation directly on every point, and independently evaluates the proposed rank-polynomial sum. It verifies each coefficient and the predicted least rank and its coefficient. On the packaged source, all 15 cases passed and the final line was `ALL_EXACT_CHECKS_PASSED 15`.

This is finite-instance corroboration, not a substitute for the all-parameter proof. The proof in `RESULT.md` supplies the exact bijection needed for the infinite family. No external mathematical certification or independent audit is claimed.
