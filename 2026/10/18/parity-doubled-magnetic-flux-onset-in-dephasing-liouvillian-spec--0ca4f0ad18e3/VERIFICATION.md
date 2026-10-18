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

`CHECK.py` constructs the full matrix representation and directly checks the first flux-sensitive superoperator moment and the vanishing of all preceding flux contrasts. It tests integer cycle lengths 3 through 8, three rate/hopping configurations including heterogeneous sitewise rates, and three nonexceptional fluxes: 432 separate comparisons. All passed, with worst normalized matrix discrepancy approximately 2.1043084006943005e-15.

The infinite-size quantifiers rely on the closed-walk and spectral-trace identities in `RESULT.md`; the finite script does not constitute an exhaustive proof. No independent mathematical audit has been performed.
