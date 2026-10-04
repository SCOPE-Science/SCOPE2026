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

The checker constructs every tested double star from its adjacency list. It enumerates all nonempty vertex subsets and tests the fort condition directly: each outside vertex must have a number of neighbors in the candidate set different from one. Inclusion-minimal forts are then extracted without using the theorem.

For the same graphs it solves the fractional fort-cover LP, optimizes every vertex coordinate over the optimum face, and independently simulates the ordinary zero forcing color-change process over all initial subsets.

Recorded output:

```text
VERIFY_OK
double_star_parameter_pairs_checked = 25
vertex_subsets_checked_for_zero_forcing = 61504
minimal_forts_checked = 350
coordinate_optimization_LPs = 500
parameters a,b = 2..6
all minimal forts are same-side leaf pairs
all fractional optima equal (a+b)/2
all optimal-coordinate ranges match the stated optimizer classification
all zero-forcing numbers equal a+b-2
```

The finite checks are corroborative only. The theorem for every \(a,b\ge2\) follows from the structural proof.
