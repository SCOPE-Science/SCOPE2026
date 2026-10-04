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

The standalone `verify.py` artifact was executed from the packaged path.

For eleven non-power-of-two parameters between \(3\) and \(15\), it constructs the dicyclic multiplication table directly, computes generated subgroups, recovers the cyclicizer exactly, and checks every adjacency/nonadjacency against the claimed complete multipartite decomposition. It also checks the arithmetic obstruction that eliminates cyclicizer size \(1\).

Exact output:

```text
n=3 order=12 cyclicizer=2 parts=[4, 2, 2, 2] reconstruction_c=2
n=5 order=20 cyclicizer=2 parts=[8, 2, 2, 2, 2, 2] reconstruction_c=2
n=6 order=24 cyclicizer=2 parts=[10, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=7 order=28 cyclicizer=2 parts=[12, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=9 order=36 cyclicizer=2 parts=[16, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=10 order=40 cyclicizer=2 parts=[18, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=11 order=44 cyclicizer=2 parts=[20, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=12 order=48 cyclicizer=2 parts=[22, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=13 order=52 cyclicizer=2 parts=[24, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=14 order=56 cyclicizer=2 parts=[26, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
n=15 order=60 cyclicizer=2 parts=[28, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] reconstruction_c=2
VERIFY_OK
```

The finite replay does not certify the infinite family. The arbitrary-\(n\) conclusion is supplied by the symbolic reconstruction proof in `RESULT.md`.
