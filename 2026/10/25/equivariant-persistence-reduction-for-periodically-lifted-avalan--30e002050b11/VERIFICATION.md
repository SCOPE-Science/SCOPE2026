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

The general proof is the equality of the parallel-firing recurrences on quotient fibers and the explicit convex homotopy \(H_s=(1-s)\mathrm{id}+sJ\Pi\) within each inflated firing simplex. Both facts hold for every nonnegative base vector and arbitrary repetition factor, independently of numerical testing.

Execution: `python3 verify.py`. The included standard-library program independently advances sandpile configurations on both cycle lengths; enumerates every firing set in the finite tested recurrence orbits; compares the lifted full simplicial face sets at prefixes; computes sample simplicial mod-two Betti numbers using a separate boundary reduction; and checks the two special periodic sphere/disconnected configurations from the facet combinatorics.

Recorded terminal output:
```
VERIFY_OK
complete_configuration_checks 450
independent_firing_step_comparisons 2270
enumerated_lift_faces_with_fiber_projection 192584
independent_mod2_Betti_comparisons 19
periodic_class_partition_benchmarks 14
```

The finite tests range over \(2\le k\le6\), selected \(m\in\{2,3,4\}\) with \(mk\le12\), and base entries from \(\{0,1,2\}\) of total grain count at most four; full-face comparisons are restricted to \(mk\le10\). The residue-class benchmarks use \(2\le k\le8\) and \(m=3\). These bounds are limitations of the computer check, not limitations of the theorem. The code's homology calculations are over \(\mathbb F_2\); integrality follows from the explicit homotopy proof, not those computations. No independent mathematical audit has been performed.
