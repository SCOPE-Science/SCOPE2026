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

Run `python verify_commutator.py` with Python 3 using only its standard library. The checker exhausts \(\Pi\in S_n\) for each \(\eta\in S_n\) when \(n=3,4,5\), then exhausts \(\Pi\in S_6\) for five deterministic \(\eta\). It independently counts all event joint occurrences and computes exact rational covariances before comparing them with the closed formulas and aggregate identity. It passed 3,773 checks.

The exact theorem for all \(n\ge3\) is verified by the counting proof in `RESULT.md`; exhaustive finite checks cannot certify an infinite statement. No external or independent audit has been performed.
