---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The open-neighborhood definition excludes the common center. Every pair of rook cells admits a common distinct neighbor for m,n>=3; hence the one-skeleton is complete and the triangle-boundary matrix on the cycle basis gives integral H1. The package supplies three explicit integer minor witnesses of orders 26,54,105 with determinants -1,+1,+2, proving the upper invariant-factor bounds. Row/column integer cocycles give independent free-rank lower bounds at (3,3), and the row cocycle gives a nonzero infinite pairing at (3,4). The crossing-edge mod-2 cocycle pairs nontrivially with a corner three-cycle at (4,4). Connected-link vertex attachments, with links computed in the *full graph* induced subcomplex and old two-skeleton unchanged, propagate quotient bounds and cocycle lower bounds to every m,n>=4 and m=3,n>=4. Independently regenerated triangle matrices have GF2/GF3/GF101 ranks: (3,3)26/26/26 of 28, (3,4)54/54/54 of 55, (4,4)104/105/105 of 105 and (4,5)170/171/171 of 171; finite link graphs connected for (3,5),(4,5),(5,4),(5,5),(6,7). These finite checks do not establish integral Smith invariants or all-size link assertions on their own; proof uses exact certificate minors and general connected-link argument.

## originality

PASS

The all-rectangular first integral homology transition is not implied by the known exact 4x4 base calculation, by higher-degree rook calculations, nor by a general fundamental-group equivalence. The open neighborhood convention is essential.

## value

PASS

An exact natural H1 invariant of the Lovasz neighborhood complex for the entire rectangular rook family resolves a genuine 3-row/free versus >=4/torsion boundary, stronger than a single finite census. The nonvanishing persistent 2-torsion constrains wedge-of-spheres/homotopy modeling, and the induction mechanism via links can be reused for similar graph families. This is motivated topology, not isolated arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
