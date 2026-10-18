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

The stand-alone `verify.py` uses only the Python standard library. Execute `python3 verify.py` from the directory containing this file. It independently counts cube residues by convolution for all residues modulo \(7^n\), \(n=1,2,3,4\), verifies the closed recurrence, checks exact masses and the rational finite moments, and checks four tiers of explicit valuation-shell values.

The infinite conclusions are not inferred from these finite tests. The supplied proof derives the lifting and singular-branch recurrences, the martingale and second-moment fixed-point identity, and a complete shell analysis establishing the exact \(L^s\) threshold. No independent audit has been performed.
