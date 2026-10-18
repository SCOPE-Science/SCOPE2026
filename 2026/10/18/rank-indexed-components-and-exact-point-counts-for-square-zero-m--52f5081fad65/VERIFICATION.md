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

The exact proof uses the identity \((A+\varepsilon B)^2=A^2+\varepsilon(AB+BA)\), square-zero Jordan blocks, conjugation of \(A\) to \(-A\), a centralizer dimension calculation, orbit geometry, and a Gaussian-binomial flag count. Every stated component has geometric dimension \(n^2\); the argument applies in characteristic two as well as odd characteristic.

Run `python verify.py` with Python 3 (standard library only). The executable constructs all finite-field matrices in the selected small cases; it does not load an answer table as an oracle. Field arithmetic for \(\mathbb F_4\) uses the polynomial \(t^2+t+1\). The checker enumerates all square-zero reductions and calculates the linear map \(B\mapsto AB+BA\) by explicit matrices for \((q,n)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)\). It then directly tests every possible \((A,B)\) pair for \((q,n)=(2,2),(3,2),(4,2),(2,3)\). It compares all counts to the independently computed closed formula and ends with `VERIFY_OK` on success.

Verified totals in order are \(28,153,496,1184,44955,226816\). The direct-pair totals in the four listed cases are \(28,153,496,1184\). Only the finite sample checks are computational; the arbitrary-size proof is textual and requires human evaluation for independent certification. There has been no independent audit or validation of the mathematical discovery.
