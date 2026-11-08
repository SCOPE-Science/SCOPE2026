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

For r>=3, u=a+b>=4 and graph metric K_{a,b,1,...,1}, reconstructed the exact zero-sum quadratic form (2^p-1) sum_i s_i^2 - 2^p sum_x alpha_x^2 and the partwise Cauchy-Schwarz reduction to Rayleigh quotient min_{sum s=0} (sum s_i^2/n_i)/(sum s_i^2). Averaging singleton coordinates reduces the minimum to a two-dimensional generalized eigenvalue. Its determinant is rv*mu^2-((r-1)u+2v)*mu+(u+r-2)=0, v=ab; the smaller root is in (0,1). The exact negative-type boundary is -log2(1-mu), included at equality and violated above it by a partwise-constant witness. Since F(2/r,v)=(r-2)(1-u/r) and dmu/dv=mu(r*mu-2)/sqrt(discriminant), balancing decreases the exponent for u>r, increases it for u<r, and is flat for u=r. Recomputed exact rational exemplar roots and discriminant signs; numerical diagonalization is corroborative, not an infinite proof.

## originality

PASS

No inspected current-priority source states or unambiguously implies the precise new theorem; methods and covered neighbors are credited explicitly, and residual inaccessibility/overlap risks remain. Best-of-knowledge originality, not world-priority certification.

## value

PASS

A sharp global allocation-reversal/equality-line theorem for natural finite two-distance graph metrics, with exact exponent and extremal splits. It resolves the nontrivial question of how balancing fixed-budget non-singleton parts changes generalized roundness as the number of singleton parts varies; not merely a relabeling of a spectral formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
