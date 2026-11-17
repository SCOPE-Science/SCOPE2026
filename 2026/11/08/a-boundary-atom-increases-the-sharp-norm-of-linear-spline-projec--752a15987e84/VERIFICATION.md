---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

On an m≥2 unit-edge real metric star with arclength plus w>0 Dirac at exactly one OUTER leaf, nodal Gram G_w=G_0+w e1e1^T is positive definite and Sherman–Morrison gives the stated inverse. At ordinary leaf, the affine kernel has negative common center and positive outer endpoint values, plus positive atom q; exact absolute-linear integral J(a,b)=(a²+b²)/(2(a+b)) yields the rational Λ_m(w). Explicit positive-polynomial differences prove R_ordinary>R_hub and R_atom for all m,w; affine kernel convexity, with strict sign disagreement, excludes all interior normers. Differentiating gives a coefficientwise positive derivative; rank-one limits and the m=2 cubic give the unique crossover. Since P1=1, negative-part mass gives exact positivity defect and witnesses. Independently formed exact rational Gram inverses and absolute kernel integrals in SymPy for m=2,3,4,6 and w=1/10,1,4: all twelve cases match Λ and the proposed norming leaves. Actual verify_leaf_atom.py read and symbolic identities/finitude checked; symbolic algebra plus positivity reasoning establishes universal claims.

## originality

PASS

Earlier exact weighted-metric-star spline formula assumes purely diffuse edge measures; a different same-day mixed-measure theorem places a positive atom at the hub and obtains a different norm/threshold and norming leaves. Neither permits relocating the atom to a single OUTER leaf via an isometric symmetry of the star (center has degree m). Oswald concerns Euclidean triangulations and a uniform-bound counterexample, not this atomic graph. The new rank-one perturbation at a leaf, strict increase and movement of worst evaluation to other leaves survive best-of-knowledge with residual specialist literature risk.

## value

PASS

Computes a sharp stability constant and all extremizers for a natural mixed-measure finite-element projector. The boundary mass causes counterintuitive amplification at other leaves and crosses the numerical threshold 2 in a two-arm family; positivity loss and sensitivity are mathematically motivated, not just an arbitrary rational number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
