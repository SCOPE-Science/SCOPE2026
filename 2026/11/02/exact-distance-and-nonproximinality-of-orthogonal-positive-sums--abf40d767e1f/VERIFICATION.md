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

# Verification record

The proof in `RESULT.md` is self-contained for every positive norm-one continuous input, every integer \(k\ge2\), and the piecewise-affine specialization. The finite checker is supplementary, not a substitute for the proof.

Execute `python3 checker.py` with Python 3's standard library. Observed output: `PASS: 940 rational finite consistency checks`.

The checker uses exact rational arithmetic for piecewise-affine examples. It compares the proposed finite-vertex formula with finer-grid alternating witnesses, checks monotonicity for successive summand counts, checks the linear identity-function distance, and verifies clipping-envelope interpolants and their required peaks and zeroes. It does not certify exhaustive continuous inputs, priority, independence, or the infinity-limit by computation. Those claims rely on the proved analytic arguments and literature comparisons in the report.
