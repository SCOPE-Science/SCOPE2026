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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

It builds projective points and lines over \(\mathbf F_2\) and \(\mathbf F_3\), constructs the subgroup-intersection adjacency relation, enumerates every projective-linear transformation, checks the predicted group orders and verifies that each transformation preserves the graph.

For \(p=2\), every two-vertex candidate is rejected and all \(56\) minimum three-vertex bases are recovered, with \(28\) point triples and \(28\) line triples.

For \(p=3\), every three-vertex candidate is rejected and all \(2340\) minimum four-vertex bases are recovered. The exact type counts are \(234,936,936,234\) for four points, three points plus one line, one point plus three lines, and four lines respectively; no two-plus-two base occurs.

The closed counting identities are additionally replayed for \(p=5,7,11\).

Exact replay output:

```text
p=2: |PGL|=168, minimum determining sets=56, type counts={3: 28, 0: 28}
p=3: |PGL|=5616, minimum determining sets=2340, type counts={4: 234, 3: 936, 1: 936, 0: 234}
odd-prime counting identities checked for p=3,5,7,11
VERIFY_OK
```

The finite checks corroborate the symbolic projective proof and do not substitute for it.
