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

Run `python3 verify_fano_nonincidence.py` with Python 3.9 or newer; it has no third-party dependencies. The verifier reconstructs all seven lines and seven cap tetrahedra from binary vector arithmetic, checks the complete seven-vertex face vector, exhausts 127 nonempty induced subcomplexes, computes exact rational boundary ranks, and enumerates all 168 collineations for signed Lefschetz characters.

The accompanying mathematical proof independently establishes simple connectivity of all induced subcomplexes with at least four vertices by coning every missing Fano-line triangle to a fourth vertex. Every tetrahedron has a triangular face appearing in no other tetrahedron; elementary collapses reduce each such complex to dimension two. Integral degree-two inclusion injectivity follows from this same unique-triangle property. These topological and chain-support arguments are not inferred solely from finite-field experiments or recorded rank logs.

The six-dimensional rational representation is identified using the standard character table of the 168-element group. The twenty-one minimal-carrier images span by group transitivity and rational irreducibility. No claim of saturated integral generation, a higher-order projective-plane generalization, or independent validation is made.
