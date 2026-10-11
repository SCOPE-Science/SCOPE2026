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

# Reproducibility and limitations

Run `python3 CHECK.py` with a standard Python 3 interpreter. Its exact-arithmetic test checks \(\sigma(L)=\{0,1,3\}\), \(a_*=11/5\), \(D_1=-64/25\), \(D_3=484/25\), and \(R_*=8/5\). Its deterministic floating-point tests compare interior mode rates to the two endpoint rates and check the gain-crossover expression for many parameter tuples. Successful finite tests are diagnostic only, not a proof of the all-parameter theorem.

The analytic proof is supplied in `RESULT.md`: (i) exact exponential-kernel state augmentation, (ii) affine shifted-Hurwitz interpolation between extreme eigenvalues, (iii) the one-mode derivative sign, (iv) the strict endpoint crossing and quadratic solution, and (v) the repeated-root distinction. Every bounded continuous history produces finite augmented initial states, and the history-construction formula proves that the spectral rate is actually observable. No computer algebra, floating-point solver, external dataset, or third-party paper is required to verify the displayed algebra.

Literature novelty cannot be mechanically certified. The accessible primary texts and the remaining potential coverage risk are identified in `REVIEW.md` and `AUDIT.json`. The result does not establish an attained exact endpoint exponential estimate in the equal-eigenvalue repeated-root case, and does not assert a rate theorem for other memory kernels.
