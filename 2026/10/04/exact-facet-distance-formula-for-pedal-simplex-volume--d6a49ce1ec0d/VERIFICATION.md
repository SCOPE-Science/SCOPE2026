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

The exact proof is contained in RESULT.md. The bundled deterministic verifier constructs random simplices in dimensions \(2\) through \(6\), computes orthogonal feet directly, and compares direct determinant volumes with the closed facet-distance formula. It separately verifies the planar Euler specialization against circumcircle power.

Literature checking included targeted published-finding corpus searches and public inspection of Grace's Cambridge extract plus the accessible text of Yang--Cheng (2006). Grace's full article could not be read in this run after open-access attempts and an institutional retrieval attempt did not complete, so equivalence risk for a dimension-three explicit equation remains. This does not affect the mathematical proof, but it limits the historical originality claim as stated.

Deterministic replay output:

```text
VERIFY_OK
cases 1100
worst_formula_error 2.146e-15
worst_planar_euler_error 5.527e-15
```
