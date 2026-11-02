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
# Verification and boundaries

The main proof uses an exact decomposition of the sketched Ritz matrix, a sharp almost-isometry cross-block bound, a normal-matrix spectral-disk argument, and an explicit four-dimensional positive-definite witness. The completed mathematical check established: the claimed cross-Gram extremizer makes the constant in the operator inequality an equality; the constructed Gram matrix has eigenvalues exactly \(1\pm\varepsilon\); the sketched Ritz characteristic polynomial has exactly the stated discriminant and becomes defective at the critical parameter.

Reproduce the standalone checks with `python verify.py` (Python 3 and NumPy). Its exact rational case verifies the rational example with \(\varepsilon=3/5\) and two nonreal eigenvalues \(3\pm i\sqrt5/4\). It also checks algebraic threshold equivalences and 800 seeded finite matrix trials of the perturbation inequality and its spectral consequence; total 1742 assertions passed in the supplied run. These are finite diagnostics and are **not** a certificate of any infinite quantified statement by enumeration.

The norm bound and spectral reality test hold in exact arithmetic, conditionally on embedding \(\operatorname{span}\{V,AV\}\). The example permits arbitrary ambient dimension but sketch dimension four. Claims about random embedding probability, floating point, or global iterative convergence are excluded. Independent mathematical validation is not yet available.
