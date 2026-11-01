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
The companion `verify.py` constructs the full two-point unordered cubical cell set for the once-subdivided trees using only Python's standard library. It checks all graph automorphisms in six tree examples, computes the signed fixed-cell traces without relying on the local-character formula, independently computes the fixed-direction/two-cycle trace, constructs simplicial cubical boundary maps over the field with two elements, verifies the chain identity, rank and connectivity, and compares every computed character. Exact execution output is embedded as `verification_output.txt`. The program was run directly from the source included with this package and exited with `VERIFY_OK`.

The general proof is in RESULT.md and does not rely on finite testing as a universal certificate. This is a self-review only. An independent audit has not been performed.
