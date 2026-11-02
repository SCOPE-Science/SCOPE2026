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

# Reproduction and boundaries

Run `python CHECK.py` with Python 3.9 or later. No nonstandard packages or network access are required. The checker uses exact fractions and complete Prüfer-code enumeration of the finite trees indicated in the proof, and verifies the distribution inequality, short-range polynomial identities, cut-contribution formula, and endpoint-geodesic representation. It also checks the sharp nonstar witnesses.

Finite enumeration does not certify the infinite integer family. The universal result rests on the leaf-deletion induction, edge-pair distribution identity, and cut double counting in `RESULT.md`. The checker must execute successfully against the file actually included in the delivered package; running a copy from an unrelated source is insufficient. Independent review has not been performed.
