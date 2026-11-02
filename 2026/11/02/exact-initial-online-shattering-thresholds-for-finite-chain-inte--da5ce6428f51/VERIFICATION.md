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

`python verify.py` reproduces the full rank list through 55 and the exact least-chain-size thresholds for depths 1 through 10. The calculation memoizes every reached sorted multiset of surviving all-negative blocks; each transition is justified by the endpoint-factorization proof in `RESULT.md`. It independently checks n=1 through 12 using a direct bit-mask recursion over the actual interval concepts. It verifies the depth-ten witness tree at n=55, including all 1,024 unique leaf witnesses, and establishes that n=8 has 36 concepts but dimension only four.

This is a finite exact computation paired with an inductive mathematical recurrence, not a proof that an extrapolated threshold pattern holds for larger n. No independent scientific audit is claimed.
