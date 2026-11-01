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

The algebraic proof uses an exact signed SVD reduction and the contractive scalar map \(r\mapsto|sr-\tau|\), with a separate convention for zero singular values. The unique positive fixed radius, the complete countable zero-preimage set, and the matrix sign transition are derived explicitly in RESULT.md.

To reproduce checks, run `python verify.py` in an environment with Python 3 and NumPy. One observed execution printed `CHECKS_OK 156222`; the checks cover rational exact-resonance and contraction identities, dense rectangular SVD iterations for both stepsize regimes, and finite termination of the proximal comparator. The finite tests do not replace the infinite-dimensional quantifiers over matrix dimensions and iterate indices proved analytically. Approximate polar factors and floating-point near-resonance behavior are not covered. No independent audit has been performed.
