---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The 4D nondegenerate alternating F3 form yields exactly 40 projective points and 40 totally isotropic lines, each with four incidences; the incidence graph has diameter four. For ordered point–line endpoints at distances 1 and 3, independently enumerated all length-five magnitude chains in degrees 2,3,4 and built the smooth-interior-deletion mod-two boundary matrices. At distance 1, chain dimensions (18,81,120) and ranks (18,63) give H3=0; at distance 3, dimensions (28,87,72) and ranks (28,50) give H3=9. Every degree-four column satisfies ∂3∂4=0 and ranks were computed by exact bit elimination. Explicit symplectic transvection generators act transitively on all 160 incident and 1440 nonincident ordered point-to-line pairs; reversal covers line-to-point. Bipartite length parity makes same-part chains vanish. Thus 2×1440×9=25920. The finite graph enumeration is exhaustive by exact group orbits, not an unjustified sample or an all-q extrapolation.

## originality

PASS

The closest published calculation determines the same bidegree for W(3,2), the 30-vertex Tutte–Coxeter graph, with local nonincident rank 4 and global rank 1440. The new order-three W(3,3) graph has 80 vertices, different chain matrices and local nonincident rank 9. The girth-controlled vanishing theorem has stronger girth hypotheses and does not imply the girth-eight boundary rank. A bounded exact-parameter search found no order-three table. This is best-of-knowledge acceptance with unindexed-table risk.

## value

PASS

The incidence graph W(3,3) is the canonical first thick symplectic generalized quadrangle beyond the published order-two Tutte–Coxeter example. The exact endpoint-local H3 rank nine and total 25920 determine a natural graph invariant at the first girth boundary where second-off-diagonal magnitude homology may persist; exhaustive group-orbit reduction makes this a reproducible reference for future q-general investigations. A complete natural finite invariant is valuable without proving a uniform q formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
