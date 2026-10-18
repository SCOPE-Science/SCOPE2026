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

# Reproducibility and proof boundary

Run `python3 verify_phase.py` using Python 3.10 or newer and its standard library. It exhaustively constructs the union-generated families from at most four labelled valuations, checks singleton profiles against the exact formula, and compares finite normalized distributions for six specified sample sizes with the leading and corrected phase approximations. A successful run prints `VERIFY_OK`.

The proof of the infinite, phase-indexed local limit and the uniform squared-logarithmic remainder is in `RESULT.md`; finite enumeration or floating-point agreement does not establish that proof. No external audit, separate certification, or machine-checked infinite proof is asserted.
