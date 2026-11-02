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

# Reproducibility and limits

Run `python3 multipartite_config_checker.py` with Python 3.9 or later, using only the standard library. The checker builds the unordered cubical two-particle model for three complete multipartite graphs; computes all cubical boundary columns with signs; checks boundary composition; reduces the matrices modulo three; and compares exact signed fixed-cell counts with the closed formulas on selected nontrivial automorphisms. The expected final success marker is `MULTIPARTITE_TWO_PARTICLE_EXACT_CELL_CHECKS_OK`.

The exact finite computations use characteristic three and are not, by themselves, certificates of rational rank or of the infinite-family theorem. Rational first homology follows from the published graph-braid theorem and the explicit equivariant cycle map. The second-homology character and quotient invariant dimensions follow from exact cellular trace and orbit calculations in the proof. Integral quotient torsion and independent audit have not been evaluated.
