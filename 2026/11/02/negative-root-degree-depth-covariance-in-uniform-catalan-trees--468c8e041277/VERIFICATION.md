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

Run `python verify.py` in the same directory using Python 3. There are no external dependencies. The verifier checks:

- The area, root-excursion and mixed integer moment sums from an independently coded primitive-path recursion for every \(1\le n\le100\).
- The exact covariance and its sign for the same sizes, using rational arithmetic.
- Direct enumeration of all Dyck paths through ten upward steps, including the root-degree-conditioned area coefficient relation.
- The exact positive successive-ratio difference used for the strict sign.

Actual run: `PASS: 760 exact integer/rational assertions; direct enumeration through n=10 edges (16,796 Dyck paths); symbolic recurrence comparisons through n=100.`

This does not amount to exhaustive verification for unbounded sizes; the proof's differentiated generating functions and ratio inequality supply that conclusion. The literature comparison is based on inspected primary material and published records and does not certify exhaustive historical novelty.
