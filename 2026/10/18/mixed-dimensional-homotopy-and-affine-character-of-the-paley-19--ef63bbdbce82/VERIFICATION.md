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

# Verification instructions

Run `python3 make_certificate.py` in this directory to regenerate the complete integer certificate, then `python3 verify_certificate.py` and `python3 independent_mod2.py` to check it. They require Python 3.10+ only. `CHECKS.txt` records the exact expected console output. All paths refer to files in this package.

`make_certificate.py` enumerates every face of nineteen nine-point quadratic-residue blocks, records exactly 3508 elementary simplicial face/coface collapses, reconstructs the final signed integer boundary from tetrahedra to triangles, and records 404 unit pivots. `verify_certificate.py` uses a different face enumeration and replays every recorded collapse against the *current* face/coface structure and every integer pivot against the *current* sparse matrix. It also checks all 171 affine automorphisms and orientation-sensitive Lefschetz traces.

`independent_mod2.py` never uses the collapsed complex or certificate: it independently computes the original unreduced simplicial boundary ranks over the two-element field, confirming the predicted Betti dimensions. This finite-field calculation is not used to infer integral torsion-freeness. Instead, the integer unit-pivot certificate establishes that all nonzero Smith factors of the signed boundary are units. Simple connectivity is established separately from the complete initial two-skeleton; the wedge homotopy conclusion uses Hurewicz and the homotopy classification of three-cell attachments to a simply connected two-complex.

Scope: a single finite 19-vertex tournament, its out-neighborhood complex, and the specified odd-order affine group. No statement about all primes, unknown higher-dimensional families, or integral orbit-space torsion has been verified. Independent mathematical audit has not been performed.
