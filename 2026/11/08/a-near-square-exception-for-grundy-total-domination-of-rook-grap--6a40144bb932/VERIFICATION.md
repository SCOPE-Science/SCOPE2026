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

# Reproducibility and scope

Run `python3 check_coverage.py` and `python3 check_selected.py` with Python 3 (standard library only). Their exact expected textual outputs are embedded in `coverage_output.txt` and `selected_output.txt`. One program performs state recursion indexed by vertices already dominated; the other recurses over the selected vertices and recomputes dominance from scratch. The first additionally verifies the two constructive families for each enumerated board.

The enumeration checks \(2\le m\le6\), \(m\le n\le8\), \(mn\le42\) for the first method and nine cases up to \(4\times5\) for the second. Exhaustion is complete within these finite instances only. The general theorem is proved by the untouched-vertex/isolated-edge lemma, the forest property, and an upper/lower bound match; there is no computational extrapolation to arbitrary graph sizes.

No independent validation has been performed.
