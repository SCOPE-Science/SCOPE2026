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

# Reproducible computations and mathematical limits

The accompanying `verify_dephased_battery.py` uses Python 3, NumPy and SciPy, constructs the entire Liouvillian on vectorized \(4\times4\) matrices (column-major order), and checks \(80\) seeded independent parameter/state choices. Run from a directory containing the script:

```bash
python verify_dephased_battery.py
```

Recorded output from a run against the included script:

```text
80 random positive-parameter, random full-rank-state tests passed
max commutation/Q² error 7.195e-16
max stationary residual 1.888e-16
max stationary scalar error 1.110e-16
max asymptotic numerical density-matrix error 7.228e-09
max battery ergotropy/Bloch error 5.551e-17
ground-state source ergotropy 0.25 exactly reproduced
```

Every sampled numerical Liouvillian had exactly two zero eigenvalues within tolerance \(10^{-9}\), and remaining eigenvalues had negative real parts below \(-10^{-10}\) (for that sample). Numerical claims concern only those sampled inputs. The analytical proof in `RESULT.md` establishes the infinite-time and all-initial-state assertions; **finite sampling does not certify the universal theorem**. The actual program itself is embedded separately in this package rather than incorporated by reference to an earlier run.

The publication-date evidence for the motivating model is the dated 2024-02-26 v1 record of arXiv:2402.16999, not the 2025 journal issue. Full-text comparisons and one inaccessible supplementary contribution are described in `REVIEW.md` and `AUDIT.json`. No external audit or independent scientific validation is represented as having taken place.
