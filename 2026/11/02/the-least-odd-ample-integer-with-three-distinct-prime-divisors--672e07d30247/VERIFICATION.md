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

# Exact verification protocol

Run `python3 verify.py` in an environment with Python 3 and its standard library. No dependencies, network access, external data, stochastic search, or specially configured interpreter are necessary.

The program checks the complete logically bounded space of all exponent triples \((a,b,c)\) with \(a,b,c\ge1\) and \(3^a5^b7^c\le801204488268064453125\). It uses two algebraically independent integer recurrences for every cell of the larger enclosing box, cross-checks 343 initial cells by direct proper-divisor loops, and performs seven comparisons against Fink's binomial identity. It counts 4,650 triples in the closed range; 4,649 strictly smaller candidates all satisfy \(\kappa(n)\le n\), and precisely the boundary triple \((20,9,6)\) is ample. The exact candidate valuation is \(841632661765951062016\).

A successful run prints `VERIFY_OK`, the counts and a SHA-256 checksum of the canonical ordered census. Since this is a finite exhaustive certificate, its reliability depends on the proved exponent reduction and on executing the complete checker. It does not certify bibliographic priority or replace independent scientific review.
