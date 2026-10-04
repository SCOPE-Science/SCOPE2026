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
The proof was reconstructed from the printed equilibrium equations of the 2024 source.

Analytic checks:
- The substitution \(z=e^{m_1I^*}\) gives the scalar equation \(q=G_R(z)\).
- The derivative numerator has a unique minimum.
- Evaluating that minimum gives the exact transition \(R=4e^{3/2}\).
- The fold merger occurs at \(z=e^{3/2}\), giving \(q=2e^{-3/2}\).
- The Jacobian determinant is a strictly positive factor times \(G_R'(z)\).

Reproducibility checks:
- `verify.py` recomputes the threshold, fold levels, three-root witness, active-media inequalities, equilibrium residuals, and trace/determinant signs.
- The witness uses only positive parameters and has two locally asymptotically stable endemic equilibria separated by a saddle.

Limits:
- Numerical calculations certify the explicit witness only; the general root classification is analytic.
- No independent audit has been performed.
