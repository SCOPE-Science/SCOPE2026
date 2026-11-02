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

Two standalone Python 3 checkers were executed against the embedded `certificate.json`:

```sh
python cycle_exact.py certificate.json
python cycle_combinatorial.py certificate.json
```

The mask-based checker exhaustively enumerated independent dominating sets of each cycle on \(3\) through \(13\) vertices, all query supports for their VC dimensions, and all feasible adaptive first-query branches for exact Littlestone dimensions. It verified a complete depth-five tree on the thirteen-cycle with \(31\) internal nodes, \(32\) distinct valid terminal concepts, and all root-to-leaf answers consistent. It independently computed the entire five-query trace histogram over \(1287\) supports; the maximum number of traces is \(29\), attained at \(13\) supports. It also checked the complete four-query histogram.

The second checker did not use the mask-based enumerator: it reconstructed concepts from all cyclic compositions into distances of two or three, used a separate depth-feasibility recursion, and repeated the exhaustive five-query support check. Both programs completed with all assertions satisfied. The fixed certificate contains all witnesses; it does not rely on filenames or outputs from other packages.

These finite checks establish the first cycle threshold through thirteen vertices. The all-width VC formula, disjoint-union additivity, and unbounded regular vertex-transitive separation are proven in `RESULT.md`. Computations at finite sizes are not invoked as proofs of infinite claims. No external proof assistant or independent scientific review was used.
