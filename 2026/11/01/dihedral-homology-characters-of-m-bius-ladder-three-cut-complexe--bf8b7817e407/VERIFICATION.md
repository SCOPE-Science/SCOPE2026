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

The standalone `verify.py` uses only Python 3 standard libraries. Execute `python3 verify.py`. On the tested run it printed:

```
VERIFY_OK n=5..16; element cases= 504
DIRECT_CUT_LEFSCHETZ_OK n=5..7; full face enumeration
DUAL_BOUNDARY_RANK_OK mod2; proof supplies primitive integer minor
```

The program builds each graph directly from modular edges, builds the Alexander dual through connected induced triples, counts all four-faces, computes signed oriented simplex characters for each rotation and reflection, and checks mod-two boundary ranks. For \(n\le7\), it separately constructs the ordinary cut complex on all vertex subsets and calculates the signed reduced Lefschetz number directly. The finite tests do not prove the infinite theorem or integral torsion exclusion; those rely on the explicit integer-unit boundary minor and Alexander duality in `RESULT.md`.

Independent audit: not performed. No external validation or formal certification is claimed.
