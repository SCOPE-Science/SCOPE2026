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

The finite certificate is `verify_small_pawful_boundary.py`, which uses only the Python standard library.

It performs four checks from first principles:

1. It partitions every labeled simple graph on \(n\le 6\) vertices into full vertex-permutation orbits and verifies that those orbits cover all \(2^{\binom n2}\) edge masks.
2. It recomputes connectivity, diameter, and the pawful triple condition for every isomorphism representative.
3. It decides existence of Tajima--Yoshinaga Definition 5.1 maps by exhaustive backtracking over all allowable \(f_2\) choices, enforcing conditions (ii) and (iii), followed by the exact residual \(f_1\) choices.
4. It reconstructs Figure 3's graph \(G_1\) and replays the published ten \(f_1\) and thirty \(f_2\) values against the exact domains and all Definition 5.1 conditions.

Expected census rows, with columns `(n, all types, connected, diameter<=2, pawful, Definition-5.1, strict non-pawful)`, are:

`(1,1,1,1,1,1,0)`
`(2,2,1,1,1,1,0)`
`(3,4,2,2,2,2,0)`
`(4,11,6,5,5,5,0)`
`(5,34,21,15,13,13,0)`
`(6,156,112,60,47,48,1)`

A successful replay ends with `VERIFY_OK`. The computation proves only the stated six-vertex cutoff; it does not test larger graphs or classify all diagonal graphs.
