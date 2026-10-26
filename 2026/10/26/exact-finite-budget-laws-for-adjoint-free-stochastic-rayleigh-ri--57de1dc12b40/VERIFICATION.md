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

## Analytical checks

The proof identifies the maximizing vector as the normalized projection of the spike eigenvector onto the sampled augmented subspace. Orthogonal decomposition then gives the exact gap ratio \(1-\|P_Ww\|^2\), with \(w\) the normalized tangent component of the spike vector. Haar invariance supplies the beta law, and the state-independent conditional distribution supplies independence over repeated adaptive steps. The gamma identity, strong law, block-merging inequality and large-dimensional beta limits prove the claimed quantitative consequences.

## Executable checks

Run `python verify.py` with Python 3, NumPy and SciPy. The saved standalone verifier passed 837 deterministic assertions involving direct reduced Rayleigh–Ritz eigensolves for random instances, exact beta-moment formulas, strict batching inequalities and seeded samples. These finite tests do not establish the universal claims or originality by themselves.

## Boundaries

Only exact one-spike two-level spectra, exact Haar tangent sampling, exact reduced optimizers and perfect forward operator evaluations are covered. A block and the corresponding number of single-direction steps have the same number of *new forward products* when intermediate forward images are reused, but not the same memory, arithmetic or wall-clock cost. Publication-priority verification remains independent and unperformed.
