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

# Verification

Run `python3 verify_heawood_equiv.py` in an environment with Python 3 standard library. The program must finish with `VERIFY_OK`. No external packages, source downloads or hidden artifacts are required.

It enumerates the graph incidence relation from the nonzero three-bit vectors and covectors, verifies point-line incidence constraints, exhausts \(3{,}462\) augmented faces, and computes six exact mod-two simplicial boundary ranks. It enumerates all invertible three-by-three binary matrices, computes both a direct signed fixed-simplex sum and an independent signed orbit polynomial, and asserts equality for every group element. It also constructs and classifies the eight Sylow-seven subgroups, computes their conjugation permutation character, and verifies all character inner products exactly.

Expected numerical certificate: face vector \((21,168,644,1218,1050,336,24)\); mod-two boundary ranks \((20,148,496,722,312,24)\); group element counts by orders \((1,2,3,4,7)\) equal \((1,21,56,42,48)\); homology character \((16,0,1,0,2)\); Sylow-seven permutation character \((8,0,2,0,1)\).

The certificate is exhaustive for this finite complex and this group. It does not test arbitrary graph families, integral representation lattices, or the additional graph duality automorphisms. Self-review does not constitute independent external validation.
