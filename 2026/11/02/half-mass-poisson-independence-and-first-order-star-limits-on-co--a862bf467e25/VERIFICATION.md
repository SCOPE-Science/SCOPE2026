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

# Checks and reproducibility

Run `python3 checker.py` with a standard Python 3 installation. The checker uses exact rational arithmetic and validates single-event probabilities, joint same-center constraints, factorization for disjoint input neighborhoods, and the uniform short-distance joint bound for representative dimensions and palettes. It enumerates every coloring for selected small instances and checks the critical-event expected count exactly.

Actual execution on the supplied checker printed `ALL_CHECKS_OK exact_pair_checks=82096 joint_histogram_states=203`. Checked cases include the fair two-color hypercube through dimension four, a nonuniform three-color palette with masses \(1/2,1/3,1/6\), and the uniform four-color palette. These finite tests do not verify the Poisson limit for every dimension.

The general proof reduces all critical events to Bernoulli indicators on closed radius-one color neighborhoods, applies Theorem 2 of Arratia, Goldstein and Gordon (1989), and bounds the dependency terms using exact cube-distance geometry. The theorem's asymptotic quantifier and the independent-audit channel are not computationally certified.
