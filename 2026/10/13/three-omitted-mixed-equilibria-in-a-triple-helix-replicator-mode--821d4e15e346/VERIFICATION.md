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
The printed vector field was reconstructed directly from Eq. (3.13) of the cited source. Exact rational enumeration at the published baseline yields eleven and only eleven equilibria in \([0,1]^3\): the eight corners, two face-mixed saddles, and one fully mixed saddle.

The exact symbolic checks confirm the fully mixed solution formula and
\[
\det J_*=-BE(A+D)x_*(1-x_*)y_*(1-y_*)z_*(1-z_*).
\]
Together with \(\operatorname{tr}J_*=0\), strict interiority, and \(B,E,A+D>0\), this proves one stable and two unstable spectral directions. For each face equilibrium, the \((x,y)\) tangent block has one positive and one negative eigenvalue and the transverse eigenvalue is strictly negative, proving one unstable direction.

The verification is finite and exact; it is not evidence for any global basin classification. `verify.py` is the reproducibility artifact used for the algebraic checks.
