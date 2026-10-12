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

The proof certificate is `ladder_upper_certificate.py`, with the execution output recorded in `certificate_output.txt`. Run it using Python 3 with no dependencies. The local predicate explicitly checks domination and private closed neighbors in every five-column window; a 625-state integer potential proves that every minimal dominating set has size at most the number of ladder columns. A synchronous product automaton checks the complete infinite-language equivalence with the six periodic patterns, not just finitely many terms. A separate direct closed-neighborhood brute-force enumeration checks orders through ten columns. No external audit or independent certification is asserted.
