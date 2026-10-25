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
# Verification

The analytic proof derives the spectrum and Fredholm essential spectrum on both BMOA and Bloch using duality, infinitely independent predual eigenfunctions, closedness of the Fredholm-essential spectrum, and spectral mapping in the Calkin algebra. A local variable change classifies and excludes all possible operator eigenvectors.

The included Python 3 script `verification/checker.py` was executed at its packaged path and reported `PASS: 21360 exact rational coefficient assertions`. It checks Hausdorff-matrix semigroup multiplication, coefficient-level eigenfunctions and an exact two-atom instance. Finite checks neither prove the infinite-dimensional spectral assertions nor certify priority.

The focal 2026 source was read in full and its sectorial Mellin condition distinguished from periodic Mellin transforms. The original 2006 boundedness paper was consulted; the full 2024 generalized spectral paper was unavailable. Independent auditing and publication-priority verification have not been performed.
