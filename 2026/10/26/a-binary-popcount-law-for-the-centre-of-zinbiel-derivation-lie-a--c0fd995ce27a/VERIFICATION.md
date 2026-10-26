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

The arithmetic identities and centre assertions are proved in `RESULT.md`; `check_zinbiel_center.py` is an independent-form computational corroboration of finite cases, not a formal infinite proof. It uses only the standard Python library. Invoking `python check_zinbiel_center.py` printed `ZINBIEL_CENTRE_OK test_size_pairs= 360`.

The checker validates the integral Zinbiel and derivation coefficient identities, commutator coefficients by direct operator compositions, and central bases in characteristics two, three, five, seven and eleven across 360 dimension-characteristic cases. It also checks the binary popcount identity and the examples at dimensions thirteen and twenty-nine. Larger dimensions and other fields follow from the written integer identities and Lucas-parity argument, not from enumeration. No independent mathematical audit has been performed.
