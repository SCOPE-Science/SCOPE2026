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

# Reproducible finite verification

The ambient coefficient space has 15 binary dimensions. `flex_quartics.py` produces 279 exact projective orbits of nonzero forms, performs exact Jacobian-ideal smoothness tests on all representatives, and writes the complete orbit classification. It was executed from the packaged file content, giving 78 geometrically smooth orbits, 10,920 equations, and 34 joint rational contact profiles.

`verify_contacts.py` independently implements only the local-contact *calculation*, substituting explicit parametric tangent lines into each smooth representative; it reproduces every representative's three contact counts, all 34 weighted profile frequencies and their sum. This is a computational cross-check, **not** an independent mathematical audit.

The two TSV tables are machine-readable, with the 15 basis monomials ordered by increasing first and second exponents. The exact 78 representative coefficient masks and orbit sizes permit regeneration. The proof of geometric smoothness uses unit ideals in three affine charts, not absence of singularities in bounded extensions. There is no higher-field assertion or independently certified computational proof.
