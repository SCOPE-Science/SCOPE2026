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

Run `python3 verify.py` with Python 3 and its standard library from the extracted package directory. The program performs exact-rational checks of the homogeneous decomposition, numerical tests of strict potential monotonicity on simplex orbits, convergence to water-filling profiles, and the exact critical-radius cocycle using long finite truncations. The truncation comparisons are bounded by the analytical \(2^{-N}B\) estimate, not taken as proof of the infinite series identity.

The proof in RESULT.md establishes all dimensions, all positive coefficient arrays and all nonnegative initial points; empirical tests cannot certify those quantifiers. Scientific priority remains open to independent literature review.
