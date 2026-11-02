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
# Verification and reproducibility

The proof is given in `RESULT.md`, Steps 1–4. The accompanying `verify.py` was executed with NumPy and SciPy and passed **793** algebraic, matrix-spectrum, probability and asymptotic checks. For the seven positive parameter pairs chosen in the program it reconstructs the rank-one Nyström eigenvalue directly from \(A\omega\), constructs \(P^{1/2}HP^{1/2}\), and compares the sign of its spectral condition-number change against the cubic crossing at 110 positive angular values each. Seeded Gaussian samples compare both exact Cauchy probabilities with empirical frequencies, and direct coefficient/limit checks compare the high-contrast constants.

Reproduce with `python verify.py`. Output ends with `PASS 793 independent algebra/matrix/probability/asymptotic checks`. Finite sampling gives empirical corroboration only and cannot prove the exact probability identities, uniqueness or asymptotic equivalences. Those conclusions are proven analytically in the result file. Source priority has not been independently audited; this is not a certification of historical novelty.
