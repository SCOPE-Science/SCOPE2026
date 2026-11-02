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

## Actual checks
The accompanying `verify.py` uses exact characteristic-seven polynomial arithmetic and verifies the quartic parametrization identity, the degree-two projection discriminant, the local valuations two and seven, the numerical semigroup gaps \(1,3,5\), and a finite-field point-count sanity check (eight points over \(\mathbb F_7\)). Its source can be executed with Python and SymPy.

## Proof limits
The singularity and conductor assertions use the complete proof in `RESULT.md` alongside exact computations. The infinite family of point counts follows from the geometric normalization; only the \(\mathbb F_7\) count is enumerated in code. There has been no independent mathematical audit. The conclusions concern the *naive singular plane model*, not potentially good reduction.
