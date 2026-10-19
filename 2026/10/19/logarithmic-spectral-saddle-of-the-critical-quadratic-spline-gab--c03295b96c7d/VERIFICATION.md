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

# Reproducibility and limits

The included `verify_b3.py` is standalone Python code using NumPy and SciPy. Run it directly from the extracted files with `python3 verify_b3.py`; actual results are preserved in `verification_output.txt`. It checks 600,000 deterministic points against the direct finite Zak sum, independently integrates the exact spectral density, compares selected densities to direct Monte Carlo estimates away from very rare events, and checks finite-difference singularity slopes and upper-edge constants. For example, the finite-difference logarithmic coefficient is approximately \(0.318284638\), against the proved \(1/\pi\approx0.318309886\).

The complete all-parameter spectral classification and asymptotic claims are proved analytically in `RESULT.md`; finite verification cannot certify an infinite statement, nor does this procedure constitute independent auditing. The numerical integration uses SciPy's quadrature and is not an interval-arithmetic certificate; the analytic Morse and edge computations are the decisive evidence.
