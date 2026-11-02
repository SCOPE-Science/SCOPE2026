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

# Computational verification and limits

Run `python verify.py` with the Python 3 standard library. The program numerically checks reflecting-path cosine eigenvectors and eigenvalues, the necessary strict mode-pair inequalities, probability normalization and nonnegativity, the spectral/physical squared-distance agreement, and finite odd-chain Hilbert--Schmidt and relative-entropy crossings. It reports 16,333 finite diagnostic assertions. Tested path sizes include odd \(N\) up to 201; the analytic argument in `RESULT.md` proves the statements for all odd \(N\ge5\) and the large-\(N\) claims. Diagnostic floating-point bisection and finite tests cannot certify an infinite-size theorem or its publication priority.

The derivations are reproducible from the normalized path generator, its discrete cosine spectral resolution, the explicit mode-pair inequality, and the discrete midpoint-cosine averages stated in `RESULT.md`. The analysis concerns the classical incoherent-limit semigroup; numerical checks do not establish its validity at finite quantum dephasing. No independent audit is represented or implied.
