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

The bundled symbolic checker reconstructs
\[
F_\lambda=(xz-y^2)y(x-y)\bigl(x-(1+\lambda)y+\lambda z\bigr)(y-\lambda z)
\]
over the polynomial ring \(\mathbb Q[\lambda,x,y,z]\). It verifies the displayed quadratic Jacobian syzygy exactly and computes a \(9\times9\) coefficient minor for a general linear Jacobian relation, obtaining \(108\lambda^2\). Thus the computational part proves \(\operatorname{mdr}(F_\lambda)=2\) uniformly for \(\lambda\ne0\).

The checker also verifies the four named conic-line-line triple points, the two opposite-line nodes, the chord restrictions to the Veronese parameterization of the conic, and the degree-six numerical near-freeness identity with \(\tau=18\). It additionally checks the standard parameterization of the symmetric circle used to relate the lead source's example to a harmonic four-point configuration.

Run:

`python artifacts/verify.py`

Expected final line: `VERIFY_OK`.

The global reduction from arbitrary realizations to the four-cycle chord normal form is proved separately by line-pair counting and Bézout. The finite symbolic checker is not used as a substitute for that universal geometric argument, and no exhaustive literature claim is inferred from search failure.
