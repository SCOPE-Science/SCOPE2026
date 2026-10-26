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

# Verification and reproducibility

Run `python3 check.py` using an ordinary Python 3 interpreter. The checker computes the coefficient of each positive integer in the finite truncations of the odd-multiplicity binary partition generating function by dynamic programming, once with weight one per occupied part size and once with weight two per occupied part size. It separately calculates the semi-Fibonacci and semi-Pell recurrences. It compares all \(2048\) positive indices and raises an exception upon any mismatch.

The finite comparison is independent of the symbolic proof of the asymptotic claims. That proof requires no computer-assisted infinite certificate: support upper bounds, an injective completion construction at prescribed support size, and a weighted-average sandwich imply the stated rate and ratio. The checker does **not** numerically establish the infinite logarithmic limits, the error terms, literature priority, or independent validation.
