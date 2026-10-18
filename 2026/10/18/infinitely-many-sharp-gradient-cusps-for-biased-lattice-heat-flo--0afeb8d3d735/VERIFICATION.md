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

The standalone `checker.py` uses Python 3 and SciPy. Run `python checker.py` in a directory containing that file. At packaging it completed 240 finite checks with no failed assertion; it evaluates the modified-Bessel mass formula using exponentially scaled Bessel functions, checks total variation against twice the modal mass, verifies that adjacent masses meet at strictly ordered crossing times, and compares high-index times with the analytical two-term expansion. The checks are over several unequal rate pairs, symmetric rates and a range of indices and times. They are finite diagnostic calculations, not an infinite proof or an independent mathematical audit.

For mathematical verification, the essential independent steps are: derive the Poisson-difference heat kernel; use strict Bessel Turán inequalities to establish two-sided log-concavity; telescope total variation of adjacent translated masses; prove the ratio Riccati monotonicity and its strict order dependence; differentiate the two competing modal branches to recover the positive cusp formula; and perform the stated Fourier saddle expansion uniformly when \(|k-(a-b)t|\) is bounded. The latter establishes the \(O(k^{-1})\) correction and is the essential infinite-parameter step not covered by finite tests.

The analysis does not claim independent audit, external certification, a general-graph extension or uniformity at vanishing drift. For rates \(a<b\) use index reflection. Historical priority beyond inspected accessible sources remains a residual uncertainty.
