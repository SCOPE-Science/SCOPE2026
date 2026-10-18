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
# Reproducible checks

The `VERIFY.py` script, requiring Python 3 and NumPy, constructs the finite non-Hermitian tight-binding matrix directly in the site basis. It checks an independently derived Chebyshev secular formula with 33 numerical determinant evaluations over \(3\le N\le13\), and tests the analytic quadratic linewidth against 195 independently diagonalized eigenvalues over \(3\le N\le12\). Both special fluxes, multiple hopping strengths, and multiple loss strengths occur. The script prints detailed maxima and a PASS result only after its assertions succeed. The observed largest determinant relative error is \(1.33\times10^{-15}\); largest relative linewidth discrepancy at \(\delta=0.006\) is \(5.33\times10^{-5}\). The largest scaled quadratic real-shift ratio is \(1.20\times10^{-5}\).

This program performs **finite** numerical checks. It does not certify the theorem for all system sizes; that follows from the exact characteristic polynomial, simple-root calculation, and analytic implicit-function theorem in `RESULT.md`. The asymptotic is fixed-parameter, local in detuning. No independent audit or external certification is claimed.
