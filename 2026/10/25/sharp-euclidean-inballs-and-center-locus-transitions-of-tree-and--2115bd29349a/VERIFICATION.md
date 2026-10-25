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

# Checks and limitations

The independent-in-implementation standard-library checker `verify.py` reconstructs each finite graph from a Prüfer code or a cyclic edge list. It tests all graph cut ratios by rational cross-multiplication and compares the full predicted contact subspace against the span of minimizing indicator vectors. It additionally evaluates direct zonotope support-function values on integer-grid vectors and evaluates all connected-cut incenter constraints at the proposed even-cycle and star segment endpoints.

Replay with `python3 verify.py` from a folder containing the embedded script. The observed output is:

```text
EXACT_OK labeled_trees=1442 cycles=13 contact_cuts=4225 raw_support_vectors=7768
CENTER_OK all_cut_cycle_segment_checks=21756 star_bounds=117
```

Tree enumeration is complete only for orders up to six; cycle enumeration covers orders three to fifteen; interval feasibility checks cover finitely many even orders and employ floating-point square-root tolerance. The proof in `RESULT.md`, not these computations, establishes infinite families and exact interval endpoints. No external or independent scientific audit has been performed.
