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
# Reproducible exact verification

Run `python verify.py` with Python 3 and SymPy available. The code requires no downloaded data and constructs the actual \(3\)-dimensional Fourier matrix, \(9\)-dimensional bipartite density matrices and local observables from their definitions. It checks all claimed exact fractions, the mutually unbiased property, normalization and orthogonality, and the full-rank mixture's strict inequality.

Actual run produced:

`VERIFY_OK MUB=passed separable_decomposition=passed Pearson_A=17/33 Pearson_C=841/1394 excess=5449/46002 full_rank=passed`

The qubit statement is verified analytically in `RESULT.md`: the Bloch-vector variance inequality bounds both weighted covariance norms by \(1\). The checker performs **finite symbolic algebra**, not infinite-dimensional certification. The full-rank state's positivity follows from \(\rho_\varepsilon\ge\varepsilon I_9/9\), and its classical-classical nature follows from simultaneous diagonality in the indicated product basis. The document does not assert independent verification.
