---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For even d>=4, nondegenerate β and Q(0)=0, pure qubit graph-state bipartition across affine flat A=a+U, graph-state Schmidt entropy is binary cross-adjacency rank r. On k<=d-2 flats the complement affinely spans F2^d; row differences D_u(z)=β(u,z)+Q(u)+β(u,a) produce k dimensions and, precisely for nonisotropic U, the constant direction. The first row Q(a+z) cannot be affine-linear on the complement because any nondegenerate quadratic plus affine linear term has support at least 2^{d-1}-2^{d/2-1}>2^{d-2}. Thus r=k+1 or k+2. On hyperplanes, β restricted to U has 1-dimensional radical, difference-row span has dimension d-1 including constants, and the nonlinear row yields r=d. Finite independent row-reduction examples in dimension 4 agree with formula; argument handles every k, affine offset and quadratic refinement. Flat Schmidt spectrum follows from reduced-state cosets of kernel of cross matrix.

## originality

PASS

Bounded best-of-knowledge originality: exact specialized formula and classification not shown to follow from inspected prior theorems; known general mechanisms and finite examples are credited, with residual priority risk.

## value

PASS

Evaluating the exact entire affine-cut entanglement profile of a structured exponential-size graph-state family yields a concise symplectic isotropy dichotomy, one-ebit gap, and Arf-invariant independence. The explicit rank evaluation is not merely restating the general cut-rank principle; it is a natural quantum-information invariant useful for bipartition design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
