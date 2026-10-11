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
The theorem is proved symbolically from the published cellular action. The replay program `verify.py` is a finite consistency check.

For each \(2\le n\le8\), it constructs the degree-three basis, implements the Artin generators, verifies the braid relations, builds every standard \(A_{ij}\), and checks that every \(N_{ij}N_{kl}\) is zero, that \(\sum_{i<j}N_{ij}=0\), and that the operator lattice has rank \(\binom n2-1\).

The replay output is:
```
n=2 H3_basis=3 pure_generators=1 nilpotent_offset_rank=0
n=3 H3_basis=7 pure_generators=3 nilpotent_offset_rank=2
n=4 H3_basis=14 pure_generators=6 nilpotent_offset_rank=5
n=5 H3_basis=25 pure_generators=10 nilpotent_offset_rank=9
n=6 H3_basis=41 pure_generators=15 nilpotent_offset_rank=14
n=7 H3_basis=63 pure_generators=21 nilpotent_offset_rank=20
n=8 H3_basis=92 pure_generators=28 nilpotent_offset_rank=27
VERIFY_OK all_cases=2..8 formula=binom(n,2)-1
```
The arbitrary-\(n\) conclusion is supplied by the proof in `RESULT.md`, not by finite enumeration.
