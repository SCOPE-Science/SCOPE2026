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

The file `verify.py` is a standalone Python 3 program using only standard-library modules. Execute `python3 verify.py` in the directory containing this file. A successful run prints `CHECK_OK checks=5337 asymptotic_constant=8.097627356867` followed by selected finite-order exponent estimates.

Actual checks: the script evaluates the two-layer Fourier spectrum for each odd order from \(5\) through \(101\), tests the exact Fourier identities at exponent \(1\), tests strict negativity of all nonconstant Fourier blocks there, and bisects finite-order critical exponents as numerical diagnostics. It compares the predicted block quadratic forms with direct quadratic forms from the full \(2n\)-vertex distance matrix for odd orders \(5,7,11\); the independent scalar quadrature verifies the cosine-integral constant. Numerical modes over the tested range select \(2\), but no general finite-order mode-selection theorem is claimed.

Proof-critical steps requiring no numerical extrapolation: the exact cyclic second-difference identity, the uniform Taylor estimate for the power perturbation, high-frequency decay from trigonometric-polynomial approximation, asymptotic odd- and even-frequency block analysis, and monotonicity of the cosine-integral ratio. Remainder bounds are qualitative and do not supply a numerical certified error bound for a specific finite order.

Independent mathematical verification has not been performed.
