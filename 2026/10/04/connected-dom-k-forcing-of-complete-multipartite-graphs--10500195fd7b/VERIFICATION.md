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

The analytic proof establishes the universal formula. Its critical steps are: (1) isolate the unique possible one-vertex case; (2) at the first nonempty force from part \(V_i\), bound the white vertices outside \(V_i\) by \(k\); (3) after that force, bound the remaining whites inside \(V_i\) by \(k\); (4) use connectedness to reserve an initially black vertex on each side; and (5) realize all four bounds simultaneously by an explicit two-round construction.

The bundled `verify.py` independently constructs every complete multipartite graph type through order nine. For each graph and each admissible \(k\), it enumerates every vertex subset, checks connectedness and domination directly, simulates the forcing rule to closure, and compares the minimum with the formula. Running `python verify.py` produces:

`ALL CHECKS PASSED; multipartite_types=87; parameter_cases=524; max_order=9`

The finite enumeration is not used to infer the theorem for larger graphs. It is a boundary and implementation stress test only. No external validation has been performed.
