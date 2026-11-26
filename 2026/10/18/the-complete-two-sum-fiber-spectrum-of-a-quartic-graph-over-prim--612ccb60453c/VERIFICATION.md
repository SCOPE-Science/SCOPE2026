---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The package's `artifacts/verify.py` and `artifacts/verify_output.txt` concern the aggregate two-sum multiplicity histogram, including zeros, and energy for the six listed small primes. They do not test the location of each exceptional fiber or any Fourier identity. The separate finite checks in the result compare the multiset at each fixed sum and give the two energy counts relevant to the order-five character example. The proof for all primes gives the individual exceptional lifts and treats primitive and imprimitive characters separately by their different orthogonality relations.
