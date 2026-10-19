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

Run `python3 verify.py profiles.csv` with Python 3 and the included `profiles.csv`; no external dependencies are needed. The checker implements exhaustive Eulerian-circuit enumeration and, independently, a complete enumeration of local in/out edge matchings. It checks equal cycle sets, all five-factor universality properties, and agreement of direct-rotation and proper-suffix Lyndon tests for every circular factor of lengths \(1\) to \(19\).

The complete finite checks establish \(2048\) distinct cyclic words; \(2047\) distinct signatures through length \(18\), with one doubleton; and \(2048\) distinct signatures through length \(19\). The checker regenerates the full table of \(2048\) rows, not just its frequency summaries. The code and table are part of this research package and were actually run together.

Verified output:

```
VERIFY_OK distinct_de_bruijn_cycles=2048 pairing_assignments=65536 independent_eulerian_enumeration=yes independent_lyndon_criteria=yes distinct_profiles_cutoff18=2047 unique_profiles_cutoff19=2048 sole_cutoff18_collision=2 cycles
```

No statement for unbounded order or independent external certification follows from the finite verification.
