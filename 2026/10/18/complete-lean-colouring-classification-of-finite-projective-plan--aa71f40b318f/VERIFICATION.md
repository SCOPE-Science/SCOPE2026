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

# Verification details

The complete proof is in `RESULT.md`, Steps 1–4. It relies only on the incidence axioms of a finite projective plane; the essential reductions are that two monochromatic lines would force a globally constant forbidden colouring, no monochromatic line forces a fully injective colouring, and a unique monochromatic line forces all outside colours to be pairwise distinct and different from its colour. The converse constructions are checked on every line. The named-palette count is a sum of two disjoint falling-factorial choices.

Run `python verify_projective_lean.py`. It reconstructs projective planes over prime fields of sizes \(2,3,5,7\), checks every incidence axiom (including unique line through every point pair and unique intersection of every line pair), and validates one optimal construction for each line. For the Fano plane, it checks all \(877\) set partitions of seven points, yielding exactly seven valid partitions with five colours and one with seven colours. These are exhaustive *for the Fano plane* up to colour renaming, not a census of all orders.

The bound comparison independently counts the incidence degree \(q+1\) versus the two-section graph's degree \(q^2+q\). The unrestricted theorem does not depend on the finite verification. No independent external audit or formal certification was performed.
