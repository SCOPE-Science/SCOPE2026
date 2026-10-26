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
# Computational verification and limits

Run `python3 verify_general.py` from the directory containing the file. The program uses Python standard library only; it explicitly constructs the finite generalized dihedral multiplication, enumerates every subset containing the identity, checks the centrality reduction directly against every two-point subset, and independently evaluates the coset and subgroup-count descriptions.

Actual checks performed:

```
H= (3,) |H|= 3 subgroup sizes= {1, 3} center= 9 formula= 9
H= (5,) |H|= 5 subgroup sizes= {1, 5} center= 25 formula= 25
H= (7,) |H|= 7 subgroup sizes= {1, 7} center= 79 formula= 79
H= (9,) |H|= 9 subgroup sizes= {9, 3, 1} center= 287 formula= 287
H= (3, 3) |H|= 9 subgroup sizes= {9, 3, 1} center= 305 formula= 305
VERIFY_OK
```

These checks are exhaustive in the enumerated cases, but they are not an exhaustive computation over all finite abelian groups. The universal claim follows from the symbolic proof in `RESULT.md`. Self-review: passed. Independent audit: not performed.
