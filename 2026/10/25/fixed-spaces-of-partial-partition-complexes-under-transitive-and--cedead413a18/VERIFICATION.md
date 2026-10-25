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

# Reproducibility and scope of checks

Run both `python3 check_fixed_points.py` and `python3 check_young_fixed.py` with Python 3 and no third-party packages. The first enumerates every partial partition for regular cyclic degrees two through nine and compares invariant full partitions with positive divisors. For the regular Klein four, symmetric-three, and dihedral-eight groups, it enumerates group subgroups independently and checks the commuting right-translation action. It finished with `PARTIAL_PARTITION_TRANSITIVE_FIXED_VERIFIED`.

The second enumerates every partial partition of label sets with Young factor sizes `(2,2)`, `(2,3)`, `(3,3)`, `(2,2,2)`, and `(2,2,2,2)`, tests invariance under generators, and separately constructs the proposed orbit complex. All invariant simplices match its faces. It computes exact binary boundary-matrix ranks for the orbit complexes with one through five Young factors, obtaining reduced Betti lists `[1]`, `[1,1]`, `[1,3,1]`, `[1,7,6,1]`, and `[1,15,25,10,1]` respectively, matching the independent combinatorial formula. It finished with `PARTIAL_PARTITION_YOUNG_FIXED_VERIFIED`.

The tests are exhaustive only for the specified finite parameters. The universal PL classifications and integral torsion-freeness rely on the written proof and the published nonequivariant homology theorem, not on these finite computations. No external independent validation was performed.
