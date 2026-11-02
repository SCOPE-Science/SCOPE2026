---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The objective p^T Bq on the compact 10-variable polytope Az=(1,1,0,0), z>=0 equals the common-edge probability. At any minimum-support maximizer the tangent Hessian must be negative definite: a nonzero null direction of a negative semidefinite quadratic at a stationary point would give a constant feasible segment to smaller support. The inspected exact Q(sqrt(5)) checker represents all 1023 support masks by 77 dihedral/exchange orbits; only eleven positive strict stationary candidates remain, uniquely maximal at mask 0x175. Strictly negative reduced gradients on each of the four absent coordinates rule out flat larger-support maximizers. I independently checked the displayed exact distributions (normalization, collective centering, objective), their reduced gradients, and a separate numerical constrained Hessian enumeration of all 1023 supports (ten symmetry-related top candidates). Numerical screening supports but does not replace exact-field algebra.

## originality

PASS

The 2026 Martínez-Sandoval–Olvera-Sampieri paper defines rainbow pushability and affine invariance and proves general bounds and cube evaluations, not the centered affine-regular pentagon two-color exact value or ten maximizers. Two semantically close Resultary pentagon records concern affine diameters and total Parseval-frame determinants, not a common-edge probability subject to collective centering.

## value

PASS

The first nontrivial odd affine-regular polygon beyond a triangle has a natural new two-color combinatorial probability invariant with quadratic-irrational sharp value and rigid optimizer orbit; the exact face-escape extremum is an independent, motivated answer to the source paper’s request for new exact polytope values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
