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

It reconstructs all thirteen normalized projective points and thirteen line normals over \\(\\mathbb F_3\\), verifies the \\(13\\times13\\) incidence matrix and the exact identity \\(BB^{\\mathsf T}=3I+J\\), constructs the symmetric rank witness, and row-reduces it over exact rational arithmetic to rank \\(13\\). Every off-diagonal zero/nonzero entry is checked against the independently constructed graph.

The same verifier replays the explicit thirteen-vertex forcing seed and its thirteen chronological forces. It also derives the natural point/line permutations from four projective matrix generators and verifies that they generate a group of order \\(5616\\).

Exact replay output:

```text
PG(2,3) incidence: 13 points, 13 lines, row/column sum 4, BB^T=3I+J
Gram-pattern witness: exact real rank 13 and correct off-diagonal graph pattern
explicit forcing witness mask: 1499455
forcing sequence: [(0, 23), (1, 19), (4, 16), (8, 21), (3, 25), (5, 22), (2, 24), (14, 6), (16, 12), (18, 9), (15, 11), (20, 10), (13, 7)]
PGL generator action: order 5616
VERIFY_OK
```

The standalone `enumerate.cpp` exhaustively checks all \\(2^{26}\\) vertex subsets by the standard zero forcing rule. It then enumerates all minimum sets and their orbits under the four projective generators. Stored exact output:

```text
polynomial 13:1246986 14:3599154 15:4874220 16:4326426 17:2872233 18:1515501 19:651950 20:229801 21:65767 22:14950 23:2600 24:325 25:26 26:1
minimum_sets=1246986 orbits=254 orbit_hist 234:1 936:9 1404:2 2808:44 5616:198
minimum_point_profile 6:556686 7:690300
ENUMERATE_OK
```

The finite exhaustive enumeration proves the complete polynomial and orbit census for this 26-vertex graph. The equality \\(Z=M=13\\) additionally has an independent symbolic rank lower bound and explicit forcing upper bound.
