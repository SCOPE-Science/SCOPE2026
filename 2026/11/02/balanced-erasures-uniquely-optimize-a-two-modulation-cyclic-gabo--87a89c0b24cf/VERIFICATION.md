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

Run `python CHECK.py` using Python 3 and NumPy. The completed local replay reported: `PASS: 4126 numerical spectral comparisons across 190 parameter families; monotonicity and hyperbolic root tests.` It enumerates every cyclic translation-erasure subset for dimensions \(3\) through \(11\), every non-antipodal nonzero modulation index and admissible erasure count. For each surviving pattern, it independently constructs the full complex frame operator and each real path-block matrix, compares the extremal eigenvalues, compares the sharp predicted minimal condition number, and verifies the complete optimizer count. The checker additionally compares hyperbolic-root evaluations with the smallest path eigenvalues for multiple positive coefficients and lengths up to \(99\).

Numerical eigenvalue tolerances are used. These checks supplement rather than prove the result for unbounded dimensions. The all-dimensional certificate is the explicit rank-two edge sum, exact unitary path reduction, Perron and hyperbolic monotonicity arguments, and integer gap-counting proof in `RESULT.md`. No unsupplied external result, external certificate or pre-existing local log is needed to follow the analytical proof.
