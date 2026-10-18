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
# Verification of the complete Jordan census

The standalone `verify_jordan_census.py` reconstructs multiplication operators from the nine monomial basis elements, evaluates the square matrix by matrix multiplication, and obtains ranks using finite-field Gaussian elimination. The algebraic theorem holds for every \(q=3^f\), \(f\ge1\); the program verifies only the finite cases stated here.

The program exhaustively enumerates \(3^8=6561\) augmentation coefficients in \(\mathbb F_3\), obtaining the exact pairs and counts: \((0,0):1\), \((1,0):2\), \((2,0):24\), \((3,0):216\), \((4,1):486\), \((6,3):5832\). Over \(\mathbb F_9\), it checks all \(9^3=729\) quadratic-leading triples with chosen higher terms, all \(9^2=81\) cubic-leading pairs, all nine quartic-only elements, and one thousand linear-leading elements; arithmetic is performed in \(\mathbb F_3[u]/(u^2+1)\). The coefficient-sum identity is also checked for \(q=3,9,27,81\).

Executed as `python verify_jordan_census.py` with the file extracted from this finding. The verification terminates with `VERIFY_OK_C3_SQUARE_JORDAN_CENSUS`. The computation is a finite cross-check, not a proof of the general field-uniform formula and not an external independent audit.
