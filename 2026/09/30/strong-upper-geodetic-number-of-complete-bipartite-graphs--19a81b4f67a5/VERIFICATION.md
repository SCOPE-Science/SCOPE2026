---
{"schema_version":1,"independent_audit":{"status":"not_performed","evidence":null},"lean_verification":{"status":"not_performed","evidence":null},"expert_attestation":{"status":"not_performed","evidence":null}}
---

# Verification

`verify.py` constructs every labeled complete bipartite graph \(K_{a,b}\) with \(1\le a\le7\) and \(a\le b\le8\), enumerates every vertex subset, and checks strong-geodetic coverage through an explicit matching between omitted vertices and available selected same-part geodesic slots. It then tests minimality by every one-vertex deletion and compares the optimum, all maximum-set part-count patterns, and all maximum-set counts with the theorem.

The archived output is `VERIFY_OK types 35 subsets 108204 minimal_sets 14183 max_sets 1625`. This is same-source computational corroboration, not an independent audit, Lean verification, expert attestation, or a substitute for the proof for arbitrary parameters.
