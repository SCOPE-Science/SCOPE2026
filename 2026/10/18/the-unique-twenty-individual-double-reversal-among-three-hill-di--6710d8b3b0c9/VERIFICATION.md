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

# Reproducible verification

Run `python3 verify_hill20.py` (Python 3 standard library only). The program verifies its nonincreasing integer-partition generator against independent unbounded-coin partition counts for every census from one to twenty; tests 49,958 unordered profile pairs at identical census and richness with both orientations; and establishes exactly one oriented strict reversal at census twenty. Exact integer products, squared sums and maxima certify the three Hill-order inequalities.

A separate preliminary enumeration of partitions in ascending rather than descending order reached the same smallest census and boundary pair. All computations are finite exact integer operations; the code is not evidence for any larger census or other order triple. Source comparisons are documented in the scientific review and originality checks. External independent audit has not been performed.
