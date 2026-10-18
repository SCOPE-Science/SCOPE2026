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

`verify.py` is a standalone Python 3 script using only the standard library. It constructs each direct product graph explicitly using the test that both coordinates differ, enumerates every pair or triple of defender vertices, determines the zeros forbidden by those defenders from the actual adjacency lists, and counts all legal minimum-weight placements of label-one vertices. The proof rules out zero and one defenders, as well as any weight below six. All eight checked boards exactly match the closed formula; the actual output is `verification_output.txt`.

The verification is finite and does not establish the infinite theorem without the proof in `RESULT.md`. The graph is a **direct product**; checking Cartesian rook-graph adjacency would not verify this claim.
