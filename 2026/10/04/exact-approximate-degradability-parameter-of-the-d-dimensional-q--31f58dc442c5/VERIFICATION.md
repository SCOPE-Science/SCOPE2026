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

The proof was reconstructed at the level of the channel action, covariance reduction, maximally-entangled lower bound, explicit degrading map, and Choi semidefinite-program certificate for \(\|\operatorname{id}-\mathcal R\|_\diamond\).

`verify_erasure_degradability.py` supplies supplementary exact-rational checks. It verifies the scalar lower-bound inequality on a dense rational grid for \(2\le d\le12\), checks the Choi positive-part partial trace exactly, verifies validity of the proposed optimizer on many rational \(p>1/2\), and verifies the exact degrading probability below the threshold. The replay returns `VERIFY_OK`.

The grid is not used as an infinite proof: the continuum minimization is the explicit three-interval absolute-value calculation in `RESULT.md`. This is a same-model verification only, not an independent audit.
