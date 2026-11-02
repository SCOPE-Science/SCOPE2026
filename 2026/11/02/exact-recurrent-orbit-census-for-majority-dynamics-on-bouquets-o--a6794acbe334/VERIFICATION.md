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

# Reproducible checks

Run `python3 verify.py` in a directory containing `verify.py`; Python's standard library is sufficient. The script builds the adjacency matrix for each square bouquet, directly applies the update to every binary configuration for \(1\le k\le6\), and checks both the exact fixed-state count and the number of unordered primitive two-cycles against the closed formulas. It independently checks the eight local words and the equivalent binomial sum through \(k=150\). The output of the actual execution is preserved in `verify_output.txt`.

These computations do not prove the all-parameter theorem. The algebraic proof in `RESULT.md` supplies that. The original 1980 general convergence theorem is not reproduced; the paper gives a self-contained finite Lyapunov argument instead. Independent external review is not included.
