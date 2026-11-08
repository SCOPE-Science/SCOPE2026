---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Checked graph distances 2 among distinct points; 1/3 for incident/nonincident point-line; 2/4 for nonparallel/parallel lines. Incidence N obeys NN^T=qI+J and N^TN=qI+J-C. The centered quadratic form splits into q parallel-class scalar modes with eigenvalue (q-1)a²-qa, q²-1 paired blocks [-a,(1-b)sqrt(q);(1-b)sqrt(q),-a²], and one constant-population mode; dimensions exhaust N-1. At a=q/(q-1) the scalar is zero, paired determinant a³-q(b-1)² >=0 by b=3^p in [1+3(a-1)/2,2a-1], and remaining mode is strictly negative including q=2 checked separately. For p>p* a parallel-class difference has positive energy; for p<p* Schoenberg strictness follows via Gaussian positive definite kernels. Independently constructed affine planes q=2,3,5 and checked powered-distance centered inertia at/below/above the exact p*. No existence claim for unavailable orders.

## originality

PASS

Best-of-knowledge comparison of mathematical claims, implications, aliases and relevant primary texts; general tools are credited and historical priority is qualified. Maximal generalized roundness, supremal p-negative type and maximal real-Hilbert snowflake exponent are equivalent formulations under Schoenberg. Robertson 2020 provides a generic finite-metric determinant criterion but no evaluated affine-plane family formula.

## value

PASS

Affine-plane incidence metrics are canonical finite-geometric objects; the exact Hilbert snowflake threshold, its class-induced zero-sum nullity, and the special order-two embedding rank determine a natural all-order metric invariant including non-Desarguesian affine planes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
