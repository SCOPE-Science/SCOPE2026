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

The direct-stencil executable `artifacts/verify.py` was run from the complete scientific package. It returned `VERIFY_OK cases=19 direct_stencil=passed last_nonzero=passed`.

The cases cover prime \(p\in\{2,3,5,7,11\}\), both square and nonsquare prime-power tori, and small degenerate-looking cyclic sides where neighbors have multiplicity. For every case, the program independently computes each intermediate iterate of a delta seed through the predicted extinction time, checking nonzero before the final step and exact zero at that step. For odd primes, it checks the complete constant terminal impulse pattern and several non-delta initial states against the predicted total-mass coefficient.

The universal theorem is established by the truncated-polynomial proof in `RESULT.md`, not by the finite checks. The script tests neither arbitrary field masks nor infinite lattices, and no independent mathematical audit has been performed.
