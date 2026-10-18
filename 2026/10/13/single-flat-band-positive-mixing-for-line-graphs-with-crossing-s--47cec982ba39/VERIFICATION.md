---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For unsigned incidence B, BᵀB=2I+A(L(H)), so -2 flat band is ker B. For each root edge e, alternating ±1 vectors on two 4-cycles meeting only at e both lie in ker B, norm 2, and their entrywise product is ±unit_e. With symmetric orthogonal P, zᵀ(P∘P)z=tr((P diag(z)P)^2)=||P diag(z)P||_F². Pairing that compression against the two cycle vectors gives |z_e|≤4||P diag(z)P||_F, yielding the universal 1/(16m) Loewner bound. Time-average spectral identity is Σ_θ E_θ∘E_θ, so additional bands only add PSD matrices. For three-factor Cartesian products, use distinct other coordinate directions to create the required squares; no isolated factor vertices. Independent exact rational Q3 projector/Schur check gave strictly positive gap; Q2 spectral decomposition yields rank 2. Finite checks are corroboration; the compression argument establishes all eligible graphs.

## originality

PASS

Spectral-projector formula for quantum average mixing and incidence -2 flat band are established. The localized crossing-square-cycle product certificate, universal quantitative positivity gap and hypercube d=3 cutoff are not statements of the inspected foundational average-mixing paper; queried published Resultary material did not show a covering criterion. O PASS best of knowledge, with possibility of equivalent diagonal-compression test in other literature.

## value

PASS

A graph-local sufficient condition for a global positive-definite quantum mixing invariant, with a dimension-uniform explicit quantitative eigenvalue bound and a natural binary hypercube cutoff. Identifies a structural fact beyond known formulas and does not conflate failure of sufficient criterion with singularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
