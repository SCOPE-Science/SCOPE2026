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

The proof is analytic, based on conditional independence and counting anchored directed cycles. Independently enumerating every labeled orientation of a complete graph verifies the exact result for \(n=3,4,5,6\), encompassing 8, 64, 1,024, and 32,768 tournaments. The code checks all 90 cycle-length/degree and cycle-length/outdegree-threshold exact covariances using `fractions.Fraction`, plus 89,996 finite sign comparisons for sizes through 300 vertices.

Run `python verification/check_cycles.py` using Python 3 and only the standard library. Expected concluding output is `verified exact enumeration cases: 90 finite sign comparisons: 89996`. This does not constitute a computer-assisted proof for unbounded \(n\); the conditional-expectation derivation in `RESULT.md` supplies that proof.

The necessary edge-independence assumption holds only for the independent fair tournament model. No independent audit or validation has been performed.
