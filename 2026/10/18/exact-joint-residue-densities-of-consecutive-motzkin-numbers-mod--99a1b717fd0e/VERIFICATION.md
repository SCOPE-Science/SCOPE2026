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

# Reproducibility and limits

Run `python3 verification.py` from the directory containing the result. The program uses only the Python standard library and exact integer/rational arithmetic. It prints `VERIFY_OK` if and only if its assertions pass.

The checks comprise: exhaustive 16-state graph reachability and its uniform incoming transition counts; all 64 entries of the rational matrix; all marginal sums and the 44 positive entries; congruence invariance on the four-step exceptional-prefix increment for representative and additional exponents; and congruence agreement against 4096 exact recurrence terms.

The infinite density conclusion is mathematical, not a claim of exhaustive enumeration: it also needs the primitive finite-chain convergence, the complete binary-prefix partition, the geometric-series identity and the argument upgrading dyadic blocks to ordinary natural density. No independent audit has been performed.
