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

Run `python verify.py` using Python 3, NumPy and SciPy. In the recorded execution (NumPy 2.3.5; SciPy 1.17.0), the script emitted:

`PASS {'analytic_spectrum_checks': 78, 'asymmetric_feasible_checks': 1950, 'constrained_optimizer_upper_checks': 36, 'independent_scalar_checks': 108}`

The spectral checks build each full \(2m\)-by-\(2m\) weighted graph Laplacian and compare \(\lambda_2\) with the formula for \(2\le m\le14\), six price pairs and unit budget. Random asymmetric configurations are normalized to the exact price budget and compared with the candidate bound. The unconstrained-edge SLSQP runs are *upper-bound checks only*: nonsmooth repeated eigenvalues can cause early solver termination, and a successful stop is **not** treated as evidence of global attainment. The scalar bounded optimizations independently find the orbit optimum for \(2\le m\le19\).

An additional exact symbolic computation for \(m=3\), \(p=1\), \(q=4\) and \(B=1\) yields \(a_*=2/21\), \(b_*=5/84\), \(\lambda_2=1/14\), and Laplacian spectrum \(\{0,1/14,1/14,5/21,5/21,13/42\}\). The infinite statement, uniqueness and asymptotics are proved symbolically in RESULT.md, not certified by finite testing. Independently performed audit: not yet performed.
