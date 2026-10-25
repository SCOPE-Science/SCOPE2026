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

The standalone `check_fence.py` computes the leading Nyström eigenvalue of the weighted positive kernel and compares it with the analytic root equations at ten real tilt values. It checks one-peak volume \(1/3\), mean \(3/8\), variance \(11/320\), and asymptotic first two cumulants, plus six finite-length transfer calculations. With Python, NumPy and SciPy installed, run `python check_fence.py`. The observed completion message was `VERIFY_OK eigenvalue_cases=10 moments=3 cumulants=3 finite_transfer_cases=6 total=22`.

The numerical discretization has explicit finite tolerances; it is not an exhaustive finite certificate, a computer-assisted proof of arbitrary dimension, or an independent audit. The proof of the exact operator identity, all-real spectral branch, analytic central limit and large deviations is mathematical and is written in RESULT.md. The sampling-based first-order mean was established in previously published literature. No independent mathematical validation has been performed.
