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

# Verification record

Run `python verify.py` with a Python 3 standard-library interpreter after extracting the files. The checker exhaustively enumerates every hash assignment for eleven left/right block allocations up to \((3,3)\), and every independent relative-sign assignment with actual exact integer determinants for five allocations. It checks the exact rational polynomial coefficients for those cases and verifies the covariance determinant-moment identity for all one hundred allocations \(1\le p,q\le10\). It separately checks the closed one-versus-many formula for fourteen values and four balanced rational examples.

The universal theorem follows from the signed-graph rank and determinant classification, bipartite rooted-tree exponential generating functions, and an exact formal bivariate coefficient transformation. Finite enumeration and determinant tests are consistency checks only. The sampling assumptions are independent uniform block hashes, independent fair signs, exact arithmetic and exactly \(p+q\) columns. No independent mathematical audit or exhaustive historical-priority determination has been performed.
