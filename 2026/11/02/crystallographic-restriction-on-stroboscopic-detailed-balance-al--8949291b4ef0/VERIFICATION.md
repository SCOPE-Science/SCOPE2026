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

Execute `python CHECK.py` (requires Python 3 with NumPy and SciPy). It constructs independent finite Markov generators and evaluates their matrix exponentials for ring sizes \(3,4,5,6,7,8,9,10,11,12,13,14,15\) with two rate pairs. The 182 assertions test exact predicted resonance times up to floating-point tolerance, symmetry and stationarity, the odd-index negative spectral mode, the even-index symmetric-generator identity, sampled nonexceptional asymmetry and Fourier spectra.

The proof for all ring sizes depends critically on the exact identity \(\sin(4\pi/n)/\sin(2\pi/n)=2\cos(2\pi/n)\), rationality of integer phase ratios, and the algebraic integer property of \(\zeta_n+\zeta_n^{-1}\). These are established in the full mathematical proof and require no finite exhaustive enumeration or numerical spectral certificate. The claimed temporal classification does not extend by default to heterogeneous rates or noisy sample estimates. Odd resonance spectra may become numerically ill-conditioned for very long sample intervals; the checker treats near-zero roundoff conservatively.
