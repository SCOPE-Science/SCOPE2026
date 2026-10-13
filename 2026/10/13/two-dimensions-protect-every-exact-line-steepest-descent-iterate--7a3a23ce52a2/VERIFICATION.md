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
The universal two-dimensional statement is proved analytically in `RESULT.md`. The critical steps are exact residual orthogonality, the trace identity for the two reciprocal line-search steps, the entrywise nonnegativity of \((\operatorname{tr}A)I-A\), and the Cayley--Hamilton reduction of the two-step residual polynomial to a scalar.

The standalone `verify.py` uses Python standard-library exact rational arithmetic. It checks the three-dimensional matrix's leading principal minors, exact inverse, strictly positive exact solution, first two line-search parameters, residual orthogonality, and the negative coordinate \((x_2)_3=-4/419\). It additionally replays representative rational two-dimensional systems only as a consistency check; finite examples are not used to establish the universal theorem.

`CHECK_OUTPUT.txt` records the successful replay as `VERIFY_OK`.
