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

# Verification procedure and limits

Run `python3 verify.py` using Python 3's standard library only. The saved checker independently enumerates the source-model transition graph and its four-step transition kernel using `fractions.Fraction` and checks 4,488 exact finite statements, including 2,001 starting positions, 40 successive outward levels and the tail-shell normalization identities. The observed output was:

`PASS 4488 exact finite checks; analytical infinite-state proofs are separate.`

The checker's finite enumeration does not prove existence, uniqueness, support completeness, moment boundaries, limits or the all-integer mixing rate. Those claims follow from the infinite-series/graph/Doeblin arguments in RESULT.md. The analytic proof uses no third-party input files, no unverifiable numerical certificates, and no assumed continuum approximation. The originating preprint and broader discrete-scale-invariance prior work are expressly credited. Independent scientific audit and outside reproducibility assessment have not been performed.
