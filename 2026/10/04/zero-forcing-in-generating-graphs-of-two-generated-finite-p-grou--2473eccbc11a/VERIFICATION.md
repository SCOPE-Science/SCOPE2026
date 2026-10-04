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

The standalone `verify.py` artifact was read from its packaged path before replay.

For representative pairs \((p,f)\), it constructs the graph as \(f-1\) isolated Frattini vertices plus \(p+1\) multipartite classes of size
\[
s=(p-1)f.
\]

For graphs of order at most eight, it exhaustively enumerates every vertex subset and reproduces the complete zero forcing polynomial. For the larger tested graphs, it checks every possible two-vertex complement and verifies that it is zero forcing exactly when the omitted vertices belong to distinct nonisolated multipartite classes.

The verifier independently constructs the real symmetric rank witnesses:

- an all-ones rank-one witness when \(s=1\);
- a hyperbolic rank-two witness when \(s=2\);
- a Lorentz rank-three witness using rational isotropic vectors when \(s\ge3\).

Every off-diagonal zero/nonzero entry is checked against the graph, and all ranks are computed exactly over the rationals.

Exact replay output:

```text
p=2, f=1: n=3, exhaustive polynomial={2: 3, 3: 1}, mr=1
p=2, f=2: n=7, exhaustive polynomial={5: 12, 6: 6, 7: 1}, mr=2
p=2, f=4: n=15, structural Z=13, min_sets=48, mr=3
p=3, f=1: n=8, exhaustive polynomial={6: 24, 7: 8, 8: 1}, mr=2
p=3, f=2: n=17, structural Z=15, min_sets=96, mr=3
p=5, f=1: n=24, structural Z=22, min_sets=240, mr=3
VERIFY_OK
```

The finite checks do not establish the arbitrary-group statement. The general result follows from Burnside's basis theorem, the complete two-white forcing classification, and the bilinear-form rank arguments in `RESULT.md`.
