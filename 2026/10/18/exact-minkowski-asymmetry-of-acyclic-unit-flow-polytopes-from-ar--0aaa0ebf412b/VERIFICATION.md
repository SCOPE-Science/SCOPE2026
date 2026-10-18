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

# Reproducible verification and limitations

The finite checks are supplied as executable `verify.py` in this package. Run `python3 verify.py` with a standard Python 3 installation. No network, package manager, random external input, or solver is needed.

The program enumerates all nonempty forward-directed edge subsets on vertex sets of sizes 3, 4 and 5, plus 300 six-vertex examples chosen with a fixed pseudorandom seed. For each graph, it constructs the complete set of source-to-sink routes; computes the arc-precedence poset by independent reachability; enumerates all antichains; independently solves exact minimum route cover using set-cover dynamic programming; checks width equals cover size; and checks that each reflected route yields a nonnegative conservation-respecting integral flow with strength one less than width.

Observed output:

```
PASS exact enumeration: 1393 DAGs, 5538 source-sink routes, 5228 selected covering routes, 47468 antichains, 7570 total arc incidences
```

All comparisons use integers and explicit bitsets, not tolerance-based floating-point arithmetic. The proof in `RESULT.md`, not the verifier, establishes the theorem for all finite acyclic graphs. The program does not prove novelty, exhaust graphs on six or more vertices, or certify any claim independently of this package. The scientific scope excludes zero-dimensional flow polytopes and directed cycles.
