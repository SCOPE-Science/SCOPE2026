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

# Reproducibility and limits

The theorem refers to consistent-mass piecewise-linear finite elements on six periodic intervals. Matrix entries are derived by assembling elemental contributions \(M_e=h\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}/6\) and \(K_e=\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}/h\), then multiplying the inverse of \(M+\tau K\) by \(M\). The rational factorizations in `RESULT.md` can be verified by direct adjugate expansion and cover arbitrary positive real parameters; their positive denominators make the necessity implications immediate. A supplied standard-library checker replays representative cases using exact rational arithmetic, verifies the factorized entries, and tests row sums, symmetry of the assembled matrices, and entrywise signs on a fixed rational grid. Finite sampling is not a proof of universal quantifiers.

The sufficiency proof uses strict diagonal dominance and the classical nonsingular \(M\)-matrix inverse-positivity theorem, not numerical eigenvalue inference. No longer cycles, nonconstant diffusivities, lumped mass scheme, or independent audit are certified.
