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
The infinite reduction is proved symbolically in `RESULT.md` from the defining divisibility condition.

The accompanying `verify.py` checks the explicit witnesses
\[
145\in S_{256},\qquad 627\in S_{65536},
\]
and regression-tests the constructive formulas on positive parameters through \(50000\). It also checks the expected prime-exponent pattern for Fermat-type values over a finite test range.

The finite checks are supporting replay only; the universal claim rests on the displayed proof.
