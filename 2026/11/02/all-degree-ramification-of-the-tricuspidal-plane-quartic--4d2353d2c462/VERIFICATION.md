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
# Verification of the complete ramification divisor

The standalone `verify.py` computes exact polynomial and linear-algebra checks in SymPy, without floating point. The actual package was assembled from the files and the script executed successfully, returning `VERIFY_OK: plane equation, coefficient-jet constraints, cusp dimensions m=2..10, full Wronskians m=2,3`.

The verifier checks: (a) the quartic vanishes identically on its normalization; (b) all pulled-back plane monomials of degrees two through five satisfy the three stated cusp-jet conditions; (c) the coefficient-condition matrix has rank three and the predicted spaces of sections vanishing to each allowed order have the stated dimensions for each of the integer degrees two through ten; and (d) Wronskian determinants of the complete conic and cubic series have exactly the predicted nonzero scalar times affine factorization.

The full mathematical proof is in `RESULT.md`, Steps 1–4: independent jet conditions, local rank formula for arbitrary degree, Plücker weight total, and symmetry-orbit exhaustion. Finite arithmetic is corroboration only. The script is not a certificate of historical originality. The calculation is over \(\mathbb Q\) for the displayed model and the theorem over \(\mathbb C\) by algebraic arguments. No independent audit was performed.
