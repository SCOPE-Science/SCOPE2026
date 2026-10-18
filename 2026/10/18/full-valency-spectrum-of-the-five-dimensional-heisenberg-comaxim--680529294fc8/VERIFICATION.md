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

# Verification record
The accompanying standalone `verify.py` enumerates every reduced-row-echelon subspace of the five-dimensional vector space over the prime fields of orders \(2\) and \(3\). It tests Lie closure, derives the Lie-generated span using all brackets, computes every graph valency, and checks the full five-stratum spectrum against symbolic formulas.

Observed counts: \(156\) vertices over \(\mathbb F_2\) and \(691\) over \(\mathbb F_3\). All degree and multiplicity assertions in those two cases passed. Symbolic proof covers every prime power. The checks do not exhaust larger fields or independently validate general characteristic or all possible earlier literature.
