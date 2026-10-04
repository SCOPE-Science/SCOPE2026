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

The all-order proof is structural. The bundled script independently checks the finite odd orders \(3\le n\le17\) by reconstructing each tournament from its edge rule, enumerating all transitive vertex subsets, comparing the two complexes exactly, and computing mod-2 boundary ranks.

For every tested odd \(n\), it verifies all of the following:

- the original directed flag complex consists exactly of subsets of the cyclic blocks \(\{a,a+1,\ldots,a+m\}\);
- no original simplex is removed by reversing \(0\to1\);
- the unique newly added simplex is \(\{0,1,m+1\}\);
- the reversed complex has mod-2 Betti vector \((1,0,\ldots,0)\).

The finite homology calculation does not prove contractibility or the infinite range. Those follow from the explicit simplex comparison plus the good-subcover nerve argument in `RESULT.md`.

Replay with `python3 verify_edge_reversal.py`; success ends with `VERIFY_OK`.
