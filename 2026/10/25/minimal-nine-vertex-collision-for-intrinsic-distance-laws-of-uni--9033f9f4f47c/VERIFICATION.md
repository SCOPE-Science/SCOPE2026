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

# Reproduction of the finite certificate

Execute `python verify_tree_distance.py` with the Python 3 standard library. The output from the actual program was:

```
A degree sequence (1, 1, 1, 1, 1, 2, 3, 3, 3)
B degree sequence (1, 1, 1, 1, 2, 2, 2, 2, 4)
common edge-pair separation counts ((0, 10), (1, 10), (2, 6), (3, 2))
exact density intervals independently checked
Exhaustive labeled Prufer trees:
n=2 labeled=1 nonisomorphic=1 signatures=1 collision=none
n=3 labeled=3 nonisomorphic=1 signatures=1 collision=none
n=4 labeled=16 nonisomorphic=2 signatures=2 collision=none
n=5 labeled=125 nonisomorphic=3 signatures=3 collision=none
n=6 labeled=1296 nonisomorphic=6 signatures=6 collision=none
n=7 labeled=16807 nonisomorphic=11 signatures=11 collision=none
n=8 labeled=262144 nonisomorphic=23 signatures=23 collision=none
CERTIFICATE_OK
```

The program builds Prüfer trees and checks their edge histograms by a combinatorial breadth-first-distance algorithm, plus rooted-center canonical isomorphism codes. Equality of piecewise density expressions is checked exactly at multiple rational points per affine piece, and follows universally from the proof's convolution identity. No sampling or random seeds are involved.

**Limits:** Enumerating finite trees through eight vertices cannot prove claims for arbitrary weighted trees, non-tree metric graphs, or higher-order random-point statistics. The nine-vertex witness is checked directly. Historical-priority verification and independent mathematical auditing have not been performed.
