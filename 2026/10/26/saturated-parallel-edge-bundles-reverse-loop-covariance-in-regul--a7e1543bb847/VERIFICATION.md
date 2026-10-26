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

Run `python3 verify.py` with Python 3 standard library. The program exhaustively generates each perfect matching of distinguishable half-edges when the total count is at most twelve for the listed test pairs, then independently computes loop counts and all parallel-edge bundle counts by direct enumeration. It compares exact rational covariances with the closed expression. It also checks the sign formula across additional admissible parameter values, and explicitly exercises the excluded two-vertex case. A successful execution ends with `VERIFY_OK`.

No random seed or external packages are required. The finite checks corroborate but do not prove the universal formula, whose proof appears in `RESULT.md`. The scope is a uniform *stub-pairing* regular configuration multigraph with at least three vertices. Historical priority outside the literature examined is not asserted. No independent external mathematical audit was performed.
