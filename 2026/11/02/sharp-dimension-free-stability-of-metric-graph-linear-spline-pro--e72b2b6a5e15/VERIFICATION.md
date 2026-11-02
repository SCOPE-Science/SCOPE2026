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

# Reproducibility and limitations

Run `python3 verify_graph_spline.py` using Python 3 and only its standard library. The checker uses exact `fractions.Fraction` operations for the nodal mass matrices, their inverses, signed-edge kernel integrals, hypercube Green recurrence and moment identities. In the completed test it passed 3,093 assertions. The recurrence checks cover \(1\leq d\leq16\); full hypercube assemblies cover \(1\leq d\leq4\); an additional 60 finite connected graphs have independently generated positive rational edge masses.

The finite checks do not establish the universal statement by extrapolation. The proof uses a convergent matrix Neumann series, a positive resolvent majorant and its conservation identity; the hypercube limit uses exact moment formulas and a backwards ratio inequality. The sign-of-kernel witness is bounded measurable and needs no vertexwise consistency as inputs are defined only almost everywhere. The unsupported cases include within-edge nonconstant densities, higher spline degrees and arbitrary graph sequences for the stated \(6/d\) asymptotic.
