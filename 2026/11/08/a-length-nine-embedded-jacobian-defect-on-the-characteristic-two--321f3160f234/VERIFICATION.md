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
# Verification and reproducibility

For an algebraically closed field of characteristic \(2\), all critical arguments are symbolic ring computations. Use `python verify.py` with SymPy installed; the recorded output is in `verification_output.txt`.

The program checks the derivatives of \(F=(XY+XZ+YZ)^2+WXYZ\) modulo \(2\), the full projective Jacobian Gröbner basis, the chart \(X\ne0\) quotient relations \(ab=ac=bc=0\), \(b^2=c^2\), and the nilpotence identities \(b^3=c^3=0\). It checks nonzero normal forms for \(b,c,b^2\) and computes exact Hilbert-function values for degrees \(0\) to \(12\); for the tested degrees \(5\le d\le12\) these match \(3d+10\).

The program alone is **not** a proof of the infinite Hilbert-polynomial statement: the exact local normal forms, the symmetric three-chart coverage and the sheaf-length sequence in `RESULT.md` provide that proof. Only self-review has been performed; independent validation remains unperformed.
