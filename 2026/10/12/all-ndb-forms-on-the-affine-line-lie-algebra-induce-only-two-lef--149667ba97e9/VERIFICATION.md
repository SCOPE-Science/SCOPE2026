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

The symbolic checker `verify.py` reconstructs the NDB criterion on all basis triples for a general matrix \(\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\). Its only nonzero residuals are \(\pm(b+c)\) and \(\pm2d\), so in characteristic different from \(2\) the form is forced to \(\begin{psmallmatrix}a&b\\-b&0\end{psmallmatrix}\), with determinant \(b^2\).

The checker then solves the defining pairing equations for the induced product, verifies the left-symmetric representation identity, computes the full automorphism pullback formula \(\Phi_{a,b}\mapsto\Phi_{a,b\lambda}\), derives the product-isomorphism defect \(s-r\lambda\), and checks the idempotent equations. The recorded run in `verify.log` terminates with `CHECK_OK`.

The computation is a symbolic replay of the proof and does not replace the universal argument. The characteristic restriction is essential: in characteristic \(2\), the residual \(2d\) does not force \(d=0\).
