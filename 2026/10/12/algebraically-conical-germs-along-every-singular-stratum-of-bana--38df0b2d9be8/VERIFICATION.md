---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

On the chart where n-k nonzero coordinates are inverted, the actual equation is U^{-1}Psi=e_{k-1}(x)+c e_k(x). Writing P=product_{i<k}x_i and S=e_{k-2}(x_1,...,x_{k-1}), substitution x_k=y/(1-cy) gives exactly (1-cy)(P+x_k(S+cP))=P+yS. This is invertible near the point and proves the all-order model, including singular points k=3..n-1. The gradient vanishes precisely for at least 3 zero coordinates; irreducibility plus codimension-2 singular support yields normality via Serre. Independent tests confirmed 105 rational exact local identities, and the Hilbert-series follows from homogeneous hypersurface equation rather than the finite checks.

## originality

PASS

Aluffi–Marcolli and Patterson already supply the banana polynomial, coordinate-incidence and tangent cone/multiplicity descriptions. The exact all-order regular coordinate change is stronger than an initial form and is not established by those inspected prior theorems. Equivalent toric local trivialization in other terminology remains a risk.

## value

PASS

A uniform algebraic local product normal form, valid at every singular stratum including high-multiplicity intersections, is an intrinsically useful singularity-classification statement; it fixes the complete analytic/contact type rather than a small numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
