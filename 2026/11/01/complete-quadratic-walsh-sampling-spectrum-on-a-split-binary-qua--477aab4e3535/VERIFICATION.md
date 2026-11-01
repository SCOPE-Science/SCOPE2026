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

# Verification of the quadratic Walsh sampling spectrum

Execute `python3 artifacts/verify.py` with NumPy and SymPy installed. The checker independently enumerates all split-quadric sample points for parameters \(m=2,3,4,5\) and recomputes the Walsh evaluation matrix and every Gram entry exactly after clearing integer denominators. It separately computes the predicted spectral multisets and compares them with direct matrix eigenvalues, checks exact ranks, and verifies the cubic-characteristic-polynomial, Sylvester-determinant, and polynomial-division identities symbolically.

The recorded successful run reported 5,110 exact Gram entries, 126 spectral values, four polynomial identities across finite parameter values, and four rank checks. The symbolic and analytic proof in `RESULT.md` establishes the universal theorem; this program corroborates specific dimensions only. No outside audit or independently performed certification is claimed.
