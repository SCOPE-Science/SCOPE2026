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

# Analytical and computational verification

The finite standard-library program `checker.py`, executable by `python3 checker.py`, reports **4,395** exact rational and finite numerical assertions. Exact-integral checks expand the radial polynomial against several integer weights, degrees and rational inner radii, and compare the beta representation and strict order. Additional finite tests sample the asymptotic coefficients and counting estimates at increasing degrees and logarithmic thresholds. The analytic proof, not these finite tests, establishes all infinite-degree limits.

The radial PDE substitution and the normalization of the n=4 harmonic degree multiplicity are explicitly derived in `RESULT.md`. The measure is normalized to unit mass but its constant cancels in every eigenvalue. Important boundaries are \(s>-1\), \(R\in(0,1)\), \(m\in\mathbb Z_{\ge0}\), and \(\varepsilon\downarrow0\); the endpoint radii and moving-parameter uniform limits are outside the claim. The earliest public source date is April 10, 2024. Independent verification has not been performed.
