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

# Reproducible exact computation

Run `python3 burkhardt_incidence_verify.py` in the same directory. It uses only Python's standard library and does not contact any network service. Exact checks:

- Enumerate all 45 singular coordinate patterns in \(\mathbb F_4\), confirm \(\sigma_1=\sigma_4=0\), and verify at most three nodes lie on a line.
- Enumerate all noncollinear node triples, recover 40 distinct nine-node planes, and expand \(\sigma_4\) coefficientwise on each plane to verify scheme-theoretic containment.
- Form the full integral incidence matrix and verify row/column degrees, the strongly regular adjacency parameters \((45,32,22,24)\), and binary rank \(15\).
- Exhibit the precise maximal minor with determinant \(-1024\). This, together with rational rank \(25\), proves the Smith factors without relying on a black-box Smith-normal-form routine.

Expected last line: `VERIFY_OK`. Finite computations establish the displayed exact integral invariant because the mathematical proof identifies the complete finite geometric node/plane sets. They do not determine the divisor class group or establish historical novelty. No independent scientific validation has been performed.
