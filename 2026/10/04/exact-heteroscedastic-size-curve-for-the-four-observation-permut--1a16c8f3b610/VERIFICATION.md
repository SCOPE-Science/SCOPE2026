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

The analytic verification proceeds in four steps: (1) enumerate the six allocations as three complementary pair partitions; (2) show that level-\(1/3\) rejection is equivalent to complete separation of the original samples; (3) orthogonalize the three Gaussian pair contrasts and compute the resulting trihedral solid angle; (4) use strict concavity of \(x\mapsto\operatorname{arsinh}(\sqrt{x})\) to obtain the sharp range and equality cases.

`verify.py` independently checks the closed form at equal variance, symmetry under reciprocal variance ratios, numerical approach to the sharp endpoint, and the deterministic combinatorial equivalence on representative quadruples. A separate seeded simulation stress test matched the analytic values within Monte Carlo error; the simulation is not part of the proof.

Limit: no claim is made for larger sample sizes, non-Gaussian laws, or studentized permutation statistics. The full text of Murphy (1967) was unavailable, leaving a literature-overlap risk but not a correctness risk.
