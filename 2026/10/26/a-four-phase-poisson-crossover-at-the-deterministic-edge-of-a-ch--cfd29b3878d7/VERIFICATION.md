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

# Verification of analytic result

The proof uses the exact physical coin and clockwise permutation in the cited model. The center offsets satisfy \(B_{Pd}+v_{Pd}=B_d\) for all four directions. Conjugating the finite-dimensional Fourier operator by these offsets gives a four-cycle plus a small mixing perturbation; expansion of four factors gives a uniform \(O((1-p_n)^2)\) remainder for each fixed Fourier variable. With \(n(1-p_n)\to\lambda\), the limiting exponential follows by finite-dimensional matrix calculus. The twirl of the uniform-reset operator has cyclic coefficients \(1/4\), \((\cos\theta_1+\cos\theta_2)/8\), and \(\cos\theta_1\cos\theta_2/4\), yielding the three eigenvalues in the manuscript. Fourier inversion is justified by continuity at the origin.

`verify.py` requires Python 3 and uses only the standard library. Run `python verify.py` in the directory containing this file. Its 124 assertions independently enumerate short-time distributions, test the exact mean-square identity, and compare the high-power physical Fourier operator with the claimed characteristic function across four residue classes and several critical parameters. These tests were executed successfully. Numerical tests are finite and do not replace the proof of the limit. No independent external audit has been performed.
