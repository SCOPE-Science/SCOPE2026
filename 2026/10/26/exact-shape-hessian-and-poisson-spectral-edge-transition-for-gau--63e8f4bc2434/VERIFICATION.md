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

# Verification of the Gaussian time–frequency shape theorem

The proof derives the actual infinite-dimensional localization matrix in the orthonormal Fock basis, computes the isolated vacuum eigenvalue's second derivative, and sums the full nonnegative resolvent correction. The exact denominator is \(\lambda_0-\lambda_n=e^{-s}\sum_{j=1}^n s^j/j!\). The first angular mode is a true null direction; the strict inequality for all higher modes follows from an exact finite falling-factorial comparison for each index. The large-area and edge limits follow analytically from a geometrically dominated coefficient ratio and the Poisson central/local limit theorems.

The accompanying standalone `checker.py` constructs finite Fock localization matrices directly from incomplete-gamma integrals and compares quadratic curvature for pure and mixed angular perturbations, including first harmonic. It independently computes exact mode-order checks at arbitrary precision and numerical Poisson asymptotic checks. The actual test command `python checker.py` produced `PASS 249 independent finite and high-precision checks`.

The numerical tests do not establish infinite-dimensional spectral convergence, the complete mode ordering, or asymptotic claims. The latter are proved mathematically in `RESULT.md`. The operator-norm expansion is local for fixed positive area and fixed real zero-mean \(C^2\) perturbation; no uniform remainder in area or angular frequency is claimed. Priority with respect to unindexed or implicitly equivalent prior formulations is not independently established.
