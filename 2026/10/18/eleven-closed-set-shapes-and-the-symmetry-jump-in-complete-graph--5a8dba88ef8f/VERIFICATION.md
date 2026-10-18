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
The source file `verify_overlap_context.py` uses only the Python standard library. Run `python verify_overlap_context.py` to independently compute the finite Galois closures and the explicit candidate classes. It enumerates all starting attribute subsets for \(n=3,4,5,6\), then constructs neighborhood intersections and compares the eleven shape classes for \(3\le n\le9\). It tests the cardinality formula and the third-edge closedness invariant used to recover the underlying line graph.

Observed terminal output:

```
CASE n=3 concepts=1 exhaustive_initials=8 PASS
CASE n=4 concepts=64 exhaustive_initials=64 PASS
CASE n=5 concepts=187 exhaustive_initials=1024 PASS
CASE n=6 concepts=448 exhaustive_initials=32768 PASS
CASE n=7 concepts=926 exhaustive_initials=0 PASS
CASE n=8 concepts=1718 exhaustive_initials=0 PASS
CASE n=9 concepts=2939 exhaustive_initials=0 PASS
VERIFY_OK generated_concepts=6283 exhaustive_initial_sets=33864 line_graph_pair_witnesses=1368 n=3..9 direct_classification=PASS automorphism_invariants=PASS
```

**Limits:** Exhaustive computations cover the indicated finite parameter ranges only. The proof's structural dichotomy, enumeration and graph-reconstruction steps establish the infinite theorem; the script does not certify all \(n\). No external independent audit is claimed.
