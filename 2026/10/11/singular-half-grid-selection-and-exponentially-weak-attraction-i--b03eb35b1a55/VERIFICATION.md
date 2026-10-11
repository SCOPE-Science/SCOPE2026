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

The mathematical proof is contained in `RESULT.md`. In particular, the only terms of order \(e^{-a/(2n)}\) in the return displacement arise from the two lattice sites nearest zero. Their opposite signs select the midpoint, and their derivatives give the exact leading full-return spectral gap. The argument is analytic for every fixed coprime pair \(1\le k<n\).

`check_eos.py` was run from the package directory using Python 3 and the standard-library `decimal` module with 85-digit working precision. Five cases passed: \((n,k)=(2,1),(3,1),(5,2),(7,3),(11,4)\), all evaluated at \(a=24n\). Each case checked primitive itinerary length, an \(n\)-step periodic residual below \(10^{-65}\), the exact combinatorial first-order sign pattern, and the normalized multiplier gap. Maximum observed relative profile discrepancy was below \(0.000403\); the largest normalized multiplier-gap discrepancy was below \(0.0000127\). These finite tests do not certify the uniformity of an infinite limit or imply any untested case.

Limits: the estimates are asymptotic for fixed \(n,k\). No independent audit has been performed. Reproduction command: `python3 check_eos.py`.
