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

## Reproducibility

Run `python3 verify_fixed_space.py` using Python 3 without external dependencies. It independently constructs the actual labeled Möbius ladder, enumerates perfect matchings and every down-closed extendible face, computes the antipodal graph-edge orbits, compares the entire geometric orbit-face model with original extendible faces for each n from 2 to 8, and computes exact mod-two boundary ranks. The process prints `VERIFY_OK` on success. In total it checks 1,966 fixed orbit faces across seven sizes. This is a finite check, not a proof of infinite correctness.

## Proof checkpoints

The orbit PL triangulation is valid because invariant barycentric coordinates are constant on vertex orbits. Every intersection of spoke stars is a cone on an admissible simplex; the nerve is full. Outside that core there are exactly zero (odd width) or two (even width) complete rim dimer tilings. The even simplices have full boundaries inside the core. Case n=2 is an edge and two isolated vertices. Only these structural arguments give the universal claim.

## Limits

The independent-audit channel is not performed. No formal proof assistant or external mathematical certifier is asserted. The integral homotopy type follows from ordinary topology, not from finite mod-two ranks. Originality remains qualified by the possibility of unindexed equivalent work.
