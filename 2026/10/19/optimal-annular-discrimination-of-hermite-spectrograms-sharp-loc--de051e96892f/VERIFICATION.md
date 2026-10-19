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

# Verification notes

The proof is analytic and applies for all integers \(0\le n<m\), every finite positive area and both stated asymptotic regimes. Critical steps: (i) the Bargmann normalization makes the radial contrast a difference of two Gamma densities and makes \(t=\pi|z|^2\) the area coordinate; (ii) its explicit logarithmic second derivative is strictly negative on its positive branch; (iii) strict equal-height superlevel geometry and the bathtub identity establish uniqueness among all measurable competitors; (iv) the inside/outside boundary quantile expansion has slope \(1/g'(a)+1/(-g'(b))\), with *two* equal exchanged masses of half the symmetric difference; (v) uniform Gamma local limits and monotone-root bracketing yield both Gaussian scaling formulas.

`VERIFY.py` is a standalone supplemental test. Execute `python VERIFY.py` with Python 3, NumPy and SciPy. It verifies exact Gamma tail vs quadrature, optimality against shifted radial intervals, numerical collar sharpness and both limiting regimes; it is neither exhaustive over measurable sets nor a substitute for the strict-concavity and quantile proofs. Numerical tests have rounding error and support, but do not establish, universal quantifiers.

The primary July 2026 paper and the older localization formulas were compared by claim rather than matching terminology. A general earlier theorem deducing the complete result by immediate specialization would defeat originality; such a theorem was not identified in accessible material. No independent audit has been carried out.
