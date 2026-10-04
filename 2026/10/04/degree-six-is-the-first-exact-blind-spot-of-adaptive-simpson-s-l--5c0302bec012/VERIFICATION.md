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
`verify.py` uses only exact rational arithmetic. It evaluates the exact integral, the one-panel Simpson functional, and the two-half-panel Simpson functional on monomials through degree six. It checks the two nontrivial difference coefficients, reconstructs the false-zero relation, verifies that no degree-at-most-five polynomial can have zero difference and nonzero true error, and checks the degree-six witness exactly.

For the witness it verifies \(S_1=S_2=4/21\), exact integral \(5/21\), and the algebraic positivity lower bound \(p(t)\ge1/84\) on \([-1,1]\). It also checks the affine scaling formula on rational test intervals.

The replay verifies finite algebraic identities, not floating-point behavior of production quadrature software. The theorem concerns the exact mathematical stopping signal.
