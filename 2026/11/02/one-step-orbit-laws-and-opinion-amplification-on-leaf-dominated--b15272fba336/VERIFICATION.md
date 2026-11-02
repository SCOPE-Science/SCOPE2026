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

The proof is self-contained in `RESULT.md`. For supplemental independent exact-arithmetic tests, run `python3 verification/check.py` using Python 3's standard library. The verifier enumerates all \(2^N\) initial states for graphs of up to \(N=12\) vertices, including a tie-prone instance, checks exact one-round distributions and the subsequent deterministic involution, verifies class counts and the full orbit distribution at \(p=1/3,2/3\), and compares expected long-run blue occupancy against the closed binomial formula. It also checks the binomial majority recurrences at rational \(p\). A complete successful replay has 16,412 exact comparisons.

The finite tests cannot establish the theorem for all finite graphs or all real \(p\); those quantifiers are proved in `RESULT.md`. No independent external audit has been performed.
