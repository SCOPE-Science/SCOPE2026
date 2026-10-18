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

For an orthonormal moving basis y1=(cosθ,sinθ), y2=(-sinθ,cosθ), F=1/(cosθ+a sinθ)^2+1/(cosθ-b sinθ)^2. Directly rederived F(0)=2 and F’(0)=2(b-a), forcing strict improvement whenever a≠b. For a=b=q, u=tan²θ reduces F to 2(1+u)(1+q²u)/(1-q²u)^2. Independent sympy differentiation agrees identically with the displayed rational derivative; monotonicity on either side of u=q^-2 gives min{2,2/q²}, with q=0 treated separately. Therefore equality sqrt2 iff a=b and |q|≤1, equivalently positive-semidefinite normalized 2×2 correlation matrix. Finite orientation sampling not used as proof. The equality is for the proof certificate, not the optimal geometric avoidance radius for every shift.

## originality

PASS

Best-of-knowledge only: the relevant new Akopyan–Polyanskii preprint was located but the full PDF could not be fetched; its abstract does not establish a classification of equality for the planar minimizing basis. A direct one-variable inequality proof and intended certificate boundary distinguish the scoped claim.

## value

PASS

A natural sharpness/equality classification of a newly introduced basis-minimization certificate in Ball’s plank argument. It identifies the PSD symmetric matrix locus and excludes nonsymmetric and indefinite matrices, clarifying exactly where the universal witness radius cannot be improved by this method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
