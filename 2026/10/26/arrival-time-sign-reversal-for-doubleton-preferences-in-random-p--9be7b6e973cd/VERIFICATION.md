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

# Reproducibility

Run `python3 verify.py` with Python 3.9 or newer, using only the standard library. The script enumerates every classical parking function for \(2\le n\le7\), computes exact rational covariances independently of the formula, checks the formula across all arrivals and frequency classes, and checks the symbolic sign classifications and the distinct-preference identity through \(n=200\). The general theorem is proved analytically in `RESULT.md`. The finite test does not certify an infinite family or historical priority.
