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

The mathematical classification is proved in RESULT.md, in particular the all-to-all Hamiltonian decomposition and uniqueness of the scalar minimization root. Reproduce independent finite checks with `python checker.py`; dependencies: Python, NumPy and SciPy.

The direct Hamiltonian loop evaluates original pairwise couplings without using the reduced energy. The checker constructs candidate minimizers and tests 33 inhomogeneous and homogeneous parameter samples with independent bounded differential-evolution optimizers, plus critical-coupling continua and one-sided threshold approaches. Its recorded execution passed 198 checks with an absolute optimizer discrepancy below \(1.6\times10^{-8}\).

These checks are finite examples and do not establish completeness for all \(m\) or all couplings. That completeness rests on the fully stated symbolic argument. All test files are standalone; no inaccessible code, prior test log or private artifact is needed. Historical priority and external independent audit remain unverified.
