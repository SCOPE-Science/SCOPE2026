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

The analytic proof is in `RESULT.md`; the independent finite checker `verify.py` requires Python 3 and NumPy. Run `python verify.py` from the directory containing it. A successful run prints `VERIFY_OK`.

The checker visits **all 1,002** nontrivial sign patterns for integer vertex counts \(3\le m\le9\). It constructs intersections of each crossed edge and the central cutting plane using exact rational barycentric coordinates and confirms that distinct crossings yield distinct points, belong to the section, and have the claimed count. This is exhaustive for those small sign patterns but not for all dimensions.

It also checks the exact expectation \(\mathbb E N_3=2\) and \(\mathbb E N_4=3.649040687816356\ldots\). Seeded Gaussian draws at \(m=3,4,5,10,50,250,1000\) compare their sample mean to the analytic expectation and compare normalized sign-count fluctuations to \(\sigma^2=1/4-1/(2\pi)\). For the two largest dimensions it also compares three continuity-point CDF values to the limiting \(\chi_1^2\) law; smaller thresholds can show lattice corrections at finite size. In the recorded execution the code printed `exact_sign_patterns=1002` and `VERIFY_OK`.

The finite enumeration does not prove the moving-threshold empirical-CDF estimate or any high-dimensional probability limit. Those assertions use the uniform grid, Chebyshev bound, Gaussian Taylor expansion and central limit theorem supplied in `RESULT.md`. The main source of originality uncertainty is possible preexisting unindexed geometric or Gaussian-orthant work; the motivating September 2026 manuscript was available only at public-abstract level. No independent scientific audit has been conducted.
