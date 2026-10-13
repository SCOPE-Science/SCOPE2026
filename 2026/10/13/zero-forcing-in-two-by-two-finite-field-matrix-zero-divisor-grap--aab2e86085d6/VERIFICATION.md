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

The verifier checks the explicit chronological forcing sequence for every integer \\(2\le q\le9\\) in the abstract image-kernel type graph. It exhaustively enumerates every type profile for \\(q=2\\) and \\(q=3\\), confirming that the largest reducible white profiles have sizes \\(4\\) and \\(6\\) and that every reducible profile is acyclic.

It then constructs the full nonzero singular-matrix graph directly over \\(\mathbb F_2\\), \\(\mathbb F_3\\), and \\(\mathbb F_5\\), computes every pairwise zero-product adjacency, and checks agreement with the image-kernel criterion. The observed vertex counts are \\(9\\), \\(32\\), and \\(144\\), exactly matching \\((q-1)(q+1)^2\\).

For \\(q\ge3\\), it also checks an auxiliary \\(K_{2q+1}\\)-minor construction. That computation is additional corroboration and is not used to prove the zero forcing lower bound.

Exact replay output:

```text
q=2: N=9, explicit forcing set size=5, omitted=4
q=3: N=32, explicit forcing set size=26, omitted=6
q=4: N=75, explicit forcing set size=67, omitted=8
q=5: N=144, explicit forcing set size=134, omitted=10
q=6: N=245, explicit forcing set size=233, omitted=12
q=7: N=384, explicit forcing set size=370, omitted=14
q=8: N=567, explicit forcing set size=551, omitted=16
q=9: N=800, explicit forcing set size=782, omitted=18
q=2: exhaustive type profiles max omitted=4, profile_count=108
q=3: exhaustive type profiles max omitted=6, profile_count=4752
F_2: direct M2 multiplication matches image-kernel graph on 9 vertices
F_3: direct M2 multiplication matches image-kernel graph on 32 vertices
F_5: direct M2 multiplication matches image-kernel graph on 144 vertices
q=3: explicit K_7 minor certificate OK
q=4: explicit K_9 minor certificate OK
q=5: explicit K_11 minor certificate OK
q=7: explicit K_15 minor certificate OK
q=9: explicit K_19 minor certificate OK
VERIFY_OK
```

The exhaustive computations are finite checks. The arbitrary-prime-power result rests on the symbolic rank-one decomposition, the bipartite forest obstruction, and the explicit force sequence.
