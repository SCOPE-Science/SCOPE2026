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

The proof in `RESULT.md` is self-contained once the standard compact-Hilbert singular-value variational principle and compact one-dimensional Sobolev embedding are admitted. Verify first that the target's point coordinate uses the **left** state value at the atom. The correct two interface identities are
\[
 u_-'(1/2)-u_+'(1/2)=a\kappa^2u_-(1/2),\quad
 u_+'(1/2)=\bigl(u_+(1/2)-u_-(1/2)\bigr)/a.
\]
Both are needed before the characteristic determinant can be factored. The resulting two monotone cotangent root branches give all eigenvalues, without finite-rank extrapolation.

The executable `verify_atom.py` uses `numpy` (dependency declared in `requirements.txt`) to check: four distinct positive atomic masses; root ordering and interface branch identities; a separate unfactored determinant identity; fourth-power singular-gap values at ranks corresponding to \(m=100\) and \(m=300\); and a weighted Nyström matrix with a separately represented atomic coordinate and a direct Hilbert–Schmidt sum. Run from the directory containing the files with `python verify_atom.py`. Successful output ends with the literal marker `ATOMIC_STIELTJES_SPECTRUM_CHECKS_OK`.

Numerical singular values of finite quadrature matrices are approximate and do not prove an infinite spectrum. Large-index cancellation restricts direct double-precision accuracy of the quartic coefficient, so tests use moderate indices and loose diagnostic thresholds. No computer algebra or external infinite-dimensional certificate is claimed. Independent audit has not been performed.
