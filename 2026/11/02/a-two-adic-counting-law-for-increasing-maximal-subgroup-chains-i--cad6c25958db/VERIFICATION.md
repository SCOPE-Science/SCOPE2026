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
# Verification

Run `python3 verify_increasing_dihedral.py` with Python 3 and no third-party packages. Its `VERIFY_OK` result is produced only when all independently enumerated subgroup-cover counts equal the closed formula on each listed small finite abelian kernel. Each group is constructed from its coordinate multiplication law; every subgroup and cover relation is generated directly, without using the subgroup-coset proof parametrization.

The tests include ordinary dihedral groups with cyclic kernels of orders \(2,3,4,5,6,8,10,12\) and noncyclic kernels \(C_2^2\), \(C_2\times C_4\), \(C_3^2\), \(C_2^3\), and \(C_2^2\times C_3\). The checker also counts unrestricted maximal subgroup chains and confirms that all sorted chains are among them. An observed successful run ended with `VERIFY_OK`.

The exhaustive list is finite; tests do not assert absence of a counterexample for arbitrary larger kernels. The infinite theorem relies on the explicit subgroup structure, maximal-cover correspondence, and two-primary insertion argument in RESULT.md. No external or independent audit has been performed.
