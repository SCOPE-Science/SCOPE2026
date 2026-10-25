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

# Reproducible verification

Run `python verify_klein.py` using Python 3 with SymPy and NetworkX installed. The program computes the six facet-system representatives via exhaustive 2–2 flips, checks incidence-graph isomorphism and edge pseudomanifold conditions, constructs all 256 induced-subcomplex chain complexes for each type, and computes exact rational ranks of each deletion differential. It checks every differential composition, validates that no induced complex has rational second homology, and asserts all six expected rational HH rank profiles.

The verifier recomputes every rank using rational arithmetic; it does not infer infinite results from finite tests. The claim is a complete finite six-type calculation. The classification that exactly six vertex-minimal Klein-bottle types exist is an independently published mathematical premise, corroborated by the explicit enumerated flip closure. Integral torsion and any equivalent work outside the inspected literature have not been established or excluded.
