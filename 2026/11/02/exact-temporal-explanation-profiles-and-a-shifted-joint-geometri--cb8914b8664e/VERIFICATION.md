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

Run `python3 checker.py` with Python 3.9 or newer. The script contains all of its dependencies (Python standard library only) and checks the formula directly by truth evaluation on independently enumerated completions. For lengths \(1\) through \(4\), it compares the complete sets of subset-minimal AXps and CXps with the proposed structural formulas for all \(4^n\) traces. For lengths \(1\) through \(7\), it exhaustively counts the joint \((A_n,C_n)\) distribution and compares exact integer counts with the two finite probability formulas, computed as rational numbers. Expected final line: `ALL_CHECKS_OK`.

All finite tests are cross-checks, not independent formal verification of an infinite theorem. Total-variation convergence and all-parameter exactness require the symbolic proof in `RESULT.md`. No independent audit has been performed.
