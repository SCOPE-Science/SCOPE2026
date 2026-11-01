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
# Verification of the stated quotient

Run `python3 verify_franklin.py franklin_collapse_certificate.json` with Python 3 (standard library only). The complete certificate is encoded in the standalone JSON file, and the verification program does not trust precomputed group elements, source face lists or orbit lists.

The executed output was:

```
AUTOMORPHISMS=48; ORIGINAL_NONEMPTY_FACES=195; QUOTIENT_CELLS=630; VALID_COLLAPSES=299; RESIDUAL=(7,15,10); ALL_VERTEX_LINKS_CIRCULAR; EULER=2; CONNECTED=YES
FRANKLIN_QUOTIENT_SPHERE_VERIFY_OK
```

The program independently enumerates adjacency-preserving permutations and all strictly nested independent-set chains, checks the 630 distinct orbit representatives, confirms every pair removes a genuinely free geometric face, and tests every edge incidence and vertex link after all collapses. A separate signed simplicial trace calculation verifies the orbit Euler characteristic.

The finite computation exhausts the exact specified graph and group; it is not a proof for larger graph families. No separate external audit or source-priority certification has been performed.
