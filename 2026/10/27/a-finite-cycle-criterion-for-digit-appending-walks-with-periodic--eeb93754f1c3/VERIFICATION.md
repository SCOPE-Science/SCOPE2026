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

# Reproduction and limits

Execute `python3 verify.py` using only Python's standard library. The checker prints all seven test-case graph thresholds, verifies 385 exact positive-integer index-jump and digit-length comparisons using rational arithmetic, and terminates with `CERTIFICATE_OK`. The period-four bottleneck, positive-correction obstruction, rational repunit and polynomial-residue pruning are included.

The mathematical proof, not the finite checker, establishes the theorem for all parameters and unbounded walks. A bounded certificate cannot establish an unrestricted statement. No independent mathematical audit has been performed.
