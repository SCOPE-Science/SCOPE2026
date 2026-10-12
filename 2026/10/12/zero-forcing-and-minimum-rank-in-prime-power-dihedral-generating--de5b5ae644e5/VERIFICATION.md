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

The checker constructs the generating graph of \(D_{2p^k}\) from the exact two-generator criteria for rotation/reflection and reflection/reflection pairs.

For
\[
(p,k)=(3,1),(5,1),(3,2),
\]
every vertex subset is exhaustively tested for zero forcing and the resulting complete polynomial is compared with the closed formula.

For
\[
(p,k)=(3,3),(5,2),(7,2),
\]
the checker verifies the isolated-rotation count, all multipartite class sizes, every one-white profile, representative cross-part two-white profiles, and a three-white stalled profile. It also verifies that omitting an isolate can never succeed.

The rank witnesses are tested entry-by-entry against the graph zero pattern and their ranks are computed exactly over the rationals.

Exact replay output:

```text
p=3, k=1, order=6, polynomial={4: 6, 5: 5, 6: 1}, witness_rank=2
p=5, k=1, order=10, polynomial={8: 20, 9: 9, 10: 1}, witness_rank=2
p=3, k=2, order=18, polynomial={16: 81, 17: 15, 18: 1}, witness_rank=3
p=3, k=3, structural_profiles_ok, witness_rank=3
p=5, k=2, structural_profiles_ok, witness_rank=3
p=7, k=2, structural_profiles_ok, witness_rank=3
VERIFY_OK
```

The finite checks corroborate the arbitrary-\(p,k\) proof; the infinite theorem relies on the symbolic generation, forcing, and bilinear-form arguments in `RESULT.md`.
