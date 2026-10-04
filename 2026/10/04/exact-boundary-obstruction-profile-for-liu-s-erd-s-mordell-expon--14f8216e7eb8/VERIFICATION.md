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
The analytic proof derives all distance formulas from coordinates and reduces the isosceles boundary minimization to one variable. The derivative factor \((1-t)^{-k/2-1}-(2+2^k)\) is strictly increasing on \((0,1)\), so the displayed critical point is the unique global minimum.

`verify_boundary.py` supplies an exact certificate for the representative extension exponent \(k=7/4\). It expands the equivalent inequality, reduces powers using \(x^{60}=2\) for \(x=2^{1/60}\), proves \(1011/1000<x<253/250\), and evaluates the reduced integer polynomial by rational interval Horner arithmetic. The resulting interval is strictly positive, which proves \(m(7/4)<0\).

The script also prints floating-point diagnostics for the boundary profile near \(k=1.73\). These numbers are not used as proof. In particular, no claim is made that the numerical zero is unique or globally sharp over all triangles. The proof does not certify Liu's conjecture at \(k=1.73\).
