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

# Reproducibility and scope

Run `python verification/affine_rank5_probe.py` from the package root. This implements five-round type recursion by reducing ordered tuples to their affine-group orbit normal forms, and enumerates all possible one-point extensions. The program reports root type IDs for listed finite fields and dimensions; equal root IDs within the same execution mean identical five-round theories. It asserts nine sampled groups and their pairwise separation, including orders \(2,3,4,5,7,8,9,11,16\). The recorded output is `verification/orbit_output.txt`.

Run `python verification/affine_direct_small.py` from the package root. This program enumerates all ordered tuples of the small planes of orders \(2,3,4\) directly without the orbit reduction, computes bottom-up five-round types, and records its type counts in `verification/direct_output.txt`. These direct type IDs are local to each instance; they are not cross-instance class identifiers. No third-party packages are needed.

The infinite equivalences are proved by the line-intersection-pattern analysis and the affine-span response argument in RESULT.md; the finite calculations are corroborating checks only. Higher quantifier ranks and independent mathematical audit are not established by these programs.
