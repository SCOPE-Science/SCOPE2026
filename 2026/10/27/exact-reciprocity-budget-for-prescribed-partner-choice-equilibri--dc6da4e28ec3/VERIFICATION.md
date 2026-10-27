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

Execute `python check.py` with standard Python. The exact-rational witness construction was directly replayed for all 50,069 labeled maps of orders one through six with heterogeneous row gaps equal to the positive integer type index. Every matrix remained positive, every prescribed gap was satisfied, and its largest asymmetric entry gap equaled the maximum length-at-least-three cycle-mean gap. The map counts by order were 1, 4, 25, 218, 2451, and 33832, matching already published OEIS A209319.

Where NumPy and SciPy are installed, the same command additionally solves 283 independent linear programs for all maps of orders three and four; numerical minimax optima agreed with the cycle-mean values within 1e-7. The LP uses nonnegative matrix variables while the constructive witnesses are strictly positive, so it gives a valid independent lower-bound comparison. The analytical proof in RESULT.md, not this bounded replay, covers arbitrary finite type counts and real positive margins. External independent scientific audit has not been performed.
