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

The proof uses an exact six-type abstraction of deleted matching pairs, with each multiplicity recorded as zero, one, or at least two. This abstraction is transition-complete because successor-neighbor detection depends only on whether the global successor-color population is zero, one or at least two and whether the unique successor-colored vertex is the matching partner.

Run `python verification/certificate.py` (tested with Python 3.13.5 and SymPy 1.14.0). This checks every one of the 707 admissible capped vectors, including per-pair rather than aggregate state identities, plus the exponential-generating-function equalities. The recorded successful output is `verification/certificate_output.txt`.

For an independent explicit graph implementation, compile `g++ -std=c++17 -O2 verification/independent.cpp -o independent` and run `./independent`. The implementation tests every labelled initial configuration at graph sizes with three through seven deleted pairs. The recorded successful output is `verification/independent_output.txt`.

The exhaustive finite reduction applies to every graph order at least six because types of multiplicity at least two are handled symbolically. The independent direct enumeration is finite corroboration only. The original source literature addresses the broader model and eventual synchronization; the current proof supplies a graph-family-specific exact temporal classification. No independent external audit or formal-proof certificate is claimed.
