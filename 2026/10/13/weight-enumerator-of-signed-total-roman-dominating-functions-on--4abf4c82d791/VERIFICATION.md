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

The analytic proof is primary.

`artifacts/verify.py` enumerates every connected complete multipartite part-size profile of total order \(2\) through \(8\). For every profile it tests all \(3^N\) labelings directly from graph adjacency.

The direct test checks each open-neighborhood sum and every \(-1\)-vertex's adjacency to a \(2\). An independent structural test uses only the part sums and outside-\(2\) counts. A third computation expands the multinomial weight enumerator from part-count triples.

Replay output:

`ALL CHECKS PASSED; profiles=58; labelings_checked=177534; orders=2..8`

The exhaustive range is finite corroboration only. The arbitrary-order result follows from the exact complete-multipartite neighborhood identities.
