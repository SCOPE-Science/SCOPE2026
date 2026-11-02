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

The mathematical proof of the unrestricted binary order-\(n\) bit-reversal identity is in `RESULT.md`; finite checking is not used in place of that proof.

The self-contained Python 3 program `verify_reversal.py` was executed on the complete 65536-mask space at order five and prints `VERIFY_OK`. It also checks both complete cyclic BWTs directly against the symbolic formula for all de Bruijn necklaces at orders 2, 3, 4 and 5. A distinct Euler-tour enumeration of the order-four directed de Bruijn graph independently generates exactly the same 2048 cycles and the same complete joint run-count table.

The proof of exhaustive coverage is the bijection between a single-cycle successor permutation and one binary de Bruijn necklace, with a unique root at its all-zero state. The audit of the 2048-cycle table therefore does not extrapolate from a sample.

Scope: sentinel-free cyclic-rotation BWT; *linear* run count of the BWT result; arbitrary binary de Bruijn order \(n\ge2\) for the exact transport identity; order five only for the joint distribution and the sharp gap. No independent validation has been performed. Historical-priority checking covers the named accessible literature and searchable records, not all possible historical sources.
