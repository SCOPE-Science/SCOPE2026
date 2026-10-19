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

The mathematical proof establishes a general constant-prefix morphism lifting lemma, five valid optimal pairs for every order \(n\ge3\), and a lower bound of two using both one-letter factors.

The program `verify_period_doubling_circular.py` constructs exact cyclic factor labels, checks necessary hitting constraints exhaustively for every possible pair at every selected critical length through order \(13\), and independently verifies complete factor coverage for the five pairs at order \(11\). The base word of order \(3\) is checked over all factor lengths. The saved output is `period_doubling_circular_checks.txt`. A finite check is used only to settle the explicit finite classification, not the all-order theorem.

No independent audit or formal proof assistant verification was performed. Completeness of the five-pair classification for orders \(n\ge14\) is neither proved nor claimed.
