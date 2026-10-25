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

## Actual checks and boundaries

The attached `verify.py` enumerates every valid regular Hom cell for odd target orders 5, 7, 9 and 11, forms binary cellular boundary columns, computes their exact ranks, and compares the resulting Betti vectors with those predicted by the proof. It enumerates all subsets of the target vertices to check the nerve condition independently. The proof itself is symbolic and valid for every odd target order at least five; exhaustive finite checks are only supporting evidence. The face-poset order maps and their naturality under cyclic target rotation are described in the proof. No independent external audit is claimed.
