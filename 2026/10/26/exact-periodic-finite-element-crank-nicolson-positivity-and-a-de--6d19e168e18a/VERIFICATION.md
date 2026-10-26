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
# Reproducible checks and limits

Run `python verify_periodic_cn.py` with Python 3; it requires only the standard library. In the completed check, all 121 direct matrices for \(3\le n\le13\) and eleven rational ratios were inverted by exact Fractions. Their entrywise signs agreed with the predicted intervals; the negative distance-two witness was verified whenever \(0<r<1/3\) for \(n\ge4\); every tested matrix had row sum one and circulant symmetry. Each exact diagonal was also compared independently against the Fourier sum with numerical residual below \(2\times10^{-12}\).

The script computes the finite-size upper roots for \(3\le n\le13\) by Fourier bisection and verifies strict decrease for these finite test sizes. The limiting radical is checked to fourteen significant digits. Crucially, no finite test is claimed to prove the all-\(n\) statements: these follow from the explicit cyclic inverse, exact Green-periodization correction and spectral monotonicity in RESULT.md.

No machine-verified theorem prover, independent auditor, or external certification is claimed. Numerical equality close to a sign threshold may be sensitive to floating-point rounding; the theorem is an exact-arithmetic statement.
