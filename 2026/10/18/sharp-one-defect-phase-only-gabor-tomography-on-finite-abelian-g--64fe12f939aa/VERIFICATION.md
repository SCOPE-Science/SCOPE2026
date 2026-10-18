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
The proof computes each ambiguity coefficient directly from two exceptional terms, identifies the Weyl projector-span spectrum, and optimizes root distances on the full unit circle. Edge cases \(N=6\) and \(N=7\) are treated separately; for \(N\ge8\), the scalar branch cannot be minimal. The finite Python checker directly sums ambiguity functions and checks 12 finite abelian groups, including different exponents at the same order, then compares with a discretized phase scan. These finite tests are not a substitute for the universal optimization proof. Independent verification has not been performed.
