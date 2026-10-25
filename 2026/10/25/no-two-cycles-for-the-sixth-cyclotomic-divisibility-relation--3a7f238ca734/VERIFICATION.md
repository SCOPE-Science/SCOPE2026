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

# Verification and limitations

The supplied `verify.py` uses integer arithmetic only: it enumerates reciprocal-divisibility candidates with smaller and larger entries both at most 1000; checks exact prime factors, the relation \(7\to157\to13\to43\to7\), multiplicativity, and a direct gcd summation for \(n=614341\). The algebraic proof in RESULT.md is universal; these finite calculations merely corroborate it. The result makes no assertion about 3-cycles, higher prime powers, or independently established originality.
