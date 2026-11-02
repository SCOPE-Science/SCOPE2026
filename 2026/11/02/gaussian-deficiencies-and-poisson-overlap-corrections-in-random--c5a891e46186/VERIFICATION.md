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

# Verification methods and limits

Run `python3 verify.py` with Python's standard library. The script separately enumerates all partial bijections, composes actual maps, and generates an exact rank/overlap histogram from the independent binomial-coefficient transition. It checks equality of the complete histograms for the eight parameter pairs \((n,m)=(1,2),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\). The case \((3,4)\) contains exactly \(1{,}336{,}336\) ordered tuples. It additionally checks the complete state-count normalization and a cross-multiplied integer form of the exact expected rank identity, and prints large-\(n\) deficiency means for sanity checking the constant term.

The successful execution reports `VERIFY_OK 8 exhaustive direct-composition cases`. The finite enumeration is exhaustive only at the listed sizes, not for all \(n\) or arbitrary product length. The infinite claim is justified in the accompanying proof by the Laguerre asymptotic and uniform conditional hypergeometric factorial-moment analysis. No independent audit or outside formal verification was performed.
