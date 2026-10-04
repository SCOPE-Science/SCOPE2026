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

The included checker constructs each double fan directly, computes all-pairs vertex distances by breadth-first search, and then constructs every mixed resolving neighborhood from the defining distances to vertices and edges.

It solves the original continuous program with all element-pair constraints for \(2\le n\le20\). It also minimizes and maximizes every coordinate over the optimum face to test the claimed uniqueness without substituting the reduced symbolic model.

Recorded output:

```text
VERIFY_OK
double_fan_parameters_checked = 19
n = 2..20
original_element_pair_constraints_checked = 23370
coordinate_optimization_LPs = 494
every two-vertex set occurred as an exact resolving neighborhood
all singleton resolving-neighborhood classifications matched
all original LP optima matched the closed formula
all optimum coordinate ranges collapsed to the predicted unique optimizer
```

The computation is finite corroboration only. The theorem for arbitrary \(n\) follows from the exact resolving-neighborhood reduction in the proof.
