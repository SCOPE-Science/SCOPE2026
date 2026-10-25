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
# Mathematical verification

The proof in RESULT.md establishes the signed convolution recurrence from \(T(z)=(1-z)T(z^2)\); the resulting three-fifths bound is proved for all even arguments and propagated through trailing binary ones. Multiplying the two digit-parity indicators recovers the exact mixed-sum count.

The accompanying pure-Python script `verify.py` ran successfully. It tests 524288 coefficients and representation bound cases, and independently sums all binary-parity pairs at each of the first 2049 indices, including the exceptional and extremizing families encountered there. These experiments provide corroboration and a reproducible guard against indexing or normalization errors, not an infinite proof or a substitute for it.

The arithmetic results have undergone only self-review. Independent audit has not been performed. Earlier unindexed equivalent inequalities are a residual priority risk.
