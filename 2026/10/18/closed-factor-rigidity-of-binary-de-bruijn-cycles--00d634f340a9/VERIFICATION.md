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

The bundled `verify.py` implements two exhaustive generation methods for all binary de Bruijn cycles of order five: all \(2^{16}\) local edge-pairings and an independent Eulerian-circuit depth-first search. It checks that both give the same 2048 canonical cycle words, and then checks the full closed-factor distribution using two border predicates and first-return enumeration. Each counted circular factor has length at most 32; overlapping border occurrences are permitted. The terminal `VERIFY_OK` line documents an actual execution of this bundled program.

The all-order bound is a mathematical argument, not a finite extrapolation. The checker verifies only order five. The supplied code is finite, fully self-contained Python 3, and performs no external scientific certification.
