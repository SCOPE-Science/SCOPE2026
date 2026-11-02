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

# Verification record

The analytic argument reduces all weighted rooted trees to the two-level star via charge-positive edge rearrangements, then evaluates the best subset exactly. The source for the underlying finite free \(p\)-norm tree formula is Cúth–Raunig, arXiv:2311.02920v1, Theorem 2.2.

`python3 CHECK.py` independently enumerates \(7^5=16{,}807\) trees and five charge vectors at \(p=r=1/2\), then compares the minimal tree cost to the subset formula. The checked floating-point discrepancies are at most approximately \(2\times10^{-14}\); these numerical observations are not a proof for other exponents or larger cardinalities.

Limitation: all exactness statements are for nonnegative Dirac-coordinate coefficients. The full signed-coordinate inclusion distortion is not computed.
