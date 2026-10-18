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

# Mathematical verification record

The exact simplex Jacobian and Dirichlet law are derived in RESULT.md. The decisive nonstandard inputs are the uniform \(\log g(t)=t/2-t^2/12+O_\beta(t^4)\) expansion on the fixed level interval and exact first, second, and fourth Dirichlet moments. Those inputs imply \(\mathbb E Q^2=O(n^{-2})\) and \(\mathbb E\sum Z_i^4=O(n^{-3})\), making the infinite-dimensional remainder rigorous.

Executed standalone verification: `python check_volume.py`. It passed exact rational moments in 44 dimensions, 999 Jacobian checks, three independent direct planar integrals, and seeded numerical Dirichlet checks at dimensions 20, 100 and 400. The independent exact planar ratios at level one and at dimension two agreed with the separately integrated area. None of the finite computations is interpreted as an exhaustive proof for all dimensions.

The validity domain is every fixed positive level and integer dimension tending to infinity. Originality remains a best-knowledge comparison with published full texts and accessible documented mathematical results, not an absolute priority certificate. Independent audit and independent validation have not been performed.
