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

The explicit certificate is self-contained. The checker verifies:

- \(2,3,11,23,31\) are prime and multiply to \(47058\);
- \(1+\sum_{p\mid47058}47058/p=47058\);
- every listed member of \(S\) is a divisor of \(47058\);
- \(S\) has 16 distinct elements and is closed under \(d\mapsto47058/d\);
- \(\sum_{d\in S}d=94116=2\cdot47058\).

No randomization, search cutoff, floating-point arithmetic, or external certificate is used. The computation only replays the finite witness; the mathematical conclusion follows directly from the definitions.
