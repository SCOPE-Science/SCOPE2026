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

# Reproducibility

Run `python verify.py` from the directory containing `verify.py` and `witnesses.json`. Python 3 and its standard library suffice; there are no external dependencies. Compare stdout with `verification_output.txt`.

The checker independently generates interleavings as nondecreasing gap vectors, verifies four complete binary adaptive trees and all their leaf words, calculates the recursive adaptive dimensions for twelve unordered two-chain profiles with at most seven total elements, supplementarily checks the previously studied two-row chain family through \(b=7\), and verifies the exact first-query binomial counts for \((3,4)\). It also checks VC dimensions for the twelve small profiles. The four certificates were constructed by a separate word-based search and stored as explicit data, not regenerated on replay.

Computational agreement is supporting evidence; the binomial branch argument proves the upper obstruction and explicit tree leaves prove the lower bounds. No experiment asserts a statement for arbitrary untested parameters, and no independent external audit has been performed.
