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

For W whose columns indicate all length-(k+1) intervals of the ell-leg, W has rank ell-k, D=WW^T has exact within-leg distance<=k support and nullity k. Across-leg matrix C_ab=1 iff a+b<=k and center d_a=1 iff a<=k give an exact graph-pattern symmetric block matrix X. For every k-dimensional x_i in ker D with sum_i x_i=0, X(0,x_1,...,x_m)=0, a subspace of dimension k(m-1). General M<=Z and published Z<=k(m-1) yield equality for all m>=2,k>=1,ell>=k+1. Independent exact Fraction rank/support tests passed 48 parameter triples; underlying verifier script and source tree also inspected.

## originality

PASS

PASS best knowledge: The original 2026 graph-powers preprint poses equality as Conjecture 10, while its Proposition 9 provides only an upper bound. No inspected prior result gives the all-parameter maximum-nullity lower bound with exact off-diagonal support. The first assigned record is a strictly weaker contemporary special case, not covering this theorem.

## value

PASS

Solves a naturally stated equality conjecture for all equal-leg-spider graph powers and, more strongly, computes exact maximum nullity and minimum rank through a graph-pattern matrix construction in all parameters. The complete bound is useful beyond finite instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
