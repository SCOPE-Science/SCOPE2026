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

# Verification of mathematical claim

The proof is in `RESULT.md`; its two governing formulas are the exact lower and upper variance of an atomic distribution with fixed mean, followed by extremal one-per-stratum interval geometry. The strict inequality is essential: at a sharp witness, a bounding moment lies on a supporting face and cannot give all nodes positive weights.

Run `python3 verify.py` with the standard library. The checker uses rational arithmetic for the exact extremizers in each of 148 stratum counts, all 2,040 closed-endpoint choices for counts three through ten, 21,000 rational pseudorandom interior node sets, and 120 explicit strictly positive rational moment-matching solutions. Those finite checks support but do not certify the universal real-parameter theorem. The result is deliberately restricted to quadratic exactness and centered target laws. Independent audit is not performed.
