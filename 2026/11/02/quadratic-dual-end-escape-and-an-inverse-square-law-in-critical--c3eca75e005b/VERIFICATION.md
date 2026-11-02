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

Run `python CHECK.py` with a Python 3 environment containing NumPy. The program verifies the exact inverse-branch formulas, the rational specialization \(A=96\) and \(B=9872/33075\), and numerical leading eigenvalues of the two killed transfer operators. The computed ratios decrease toward the predicted limiting inverse-square factor when the endpoint hole shrinks. The finite-grid computation is nonrigorous and is provided only as an independent numerical sanity check.

The analytical certificate is the proof in `RESULT.md`: the stationary density's endpoint traces come from the exact Perron–Frobenius identity; the two local measures follow from integrating the traces; the return probabilities follow from the local expansion at the fixed endpoint and the nonperiodicity of the opposite endpoint; and the eigenvalue limits follow from the standard spectral small-hole theorem with its BV smallness condition checked here. No interval-arithmetic certificate, formal proof, or independent validation has been performed.
