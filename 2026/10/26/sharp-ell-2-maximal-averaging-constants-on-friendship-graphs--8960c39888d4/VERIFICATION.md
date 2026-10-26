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
# Verification

Run `python3 check_friendship.py` with Python 3 and no third-party dependencies. The checker constructs exact integer-scaled row-selection matrices for all \(m=1,2,3\) (the first case is a classical benchmark). It examines \(438\) matrices modulo permutations of triangles. The Faddeev--LeVerrier characteristic-polynomial and quadratic-field sign tests use unbounded Python integers and test **all** polynomial coefficients, so the finite checks are exhaustive and non-numerical. The equivalence between coefficient nonnegativity and positive semidefiniteness follows from real-rootedness of characteristic polynomials of symmetric matrices.

The general step \(m\ge4\), the eigenvalue formula, positivity of the Perron test vector and the extremizing input are analytical parts of RESULT.md; the code does not claim to certify infinitely many parameters. Literature priority has not been independently audited.
