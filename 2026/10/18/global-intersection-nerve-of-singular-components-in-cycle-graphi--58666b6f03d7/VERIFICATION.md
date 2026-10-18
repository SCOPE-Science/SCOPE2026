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

Run `python3 verify.py` (Python standard library only). The output ends in `VERIFY_OK` if all assertions pass. It enumerates mixed-sign fan cones for \(n=4,5,6,7\), counts the minimal singular cones, verifies membership relations, checks the coface stars, computes pairwise intersection compatibility, tests maximal nerve simplices, and checks the five-cycle's 20 vertices and 30 inclusion edges.

The infinite theorem is proved by the signed-integral-lattice isomorphism, the normal semigroup generators and single primitive relation, the Jacobian calculation, and the star-fan/gluing argument in RESULT.md. Finite checks are not a proof for unbounded \(n\). No external independent audit was performed. The reduced-set assertions should not be interpreted as scheme-theoretic intersection multiplicity statements.
