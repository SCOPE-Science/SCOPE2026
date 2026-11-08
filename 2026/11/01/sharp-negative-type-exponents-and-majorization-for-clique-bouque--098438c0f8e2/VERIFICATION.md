---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For r>=2, m_i>=1, t=2^p and zero-sum vertex coefficients, eliminating the hub yields the exact distance-power quadratic Q=-sum_{i,a} x_{i,a}^2+(1-t)sum_i s_i^2+(t-2)(sum_i s_i)^2, with s_i the blade totals. The sharp inequality sum_a x_{i,a}^2>=s_i^2/m_i reduces conditional negativity to a diagonal form a_i=t-1+1/m_i and a rank-one correction. Weighted Cauchy-Schwarz gives the necessary and sufficient F(t)=(t-2)sum_i a_i^-1<=1 (for t>2), with equality vector and strict sign witness. F strictly increases from 0 at t=2 to r>1; hence a unique t_*>2. Strictness below and one-dimensional endpoint radical follow from equality conditions; basepoint Euclidean Gram rank is M below and M-1 at the endpoint. Concavity of g_t(m)=m/((t-1)m+1) and integral unit transfers classify unique balanced and extreme partitions for fixed r,M. Independently constructed small bouquet zero-sum matrices and found their maximal eigenvalue zero at the computed t_*; finite checks do not replace these all-size arguments.

## originality

PASS

Doust-Weston arXiv:0705.0411 Theorem 5.6 determines the star case, recovered by m_i=1, so stars are explicitly prior. Li-Weston arXiv:0901.0695 yields general p-negative-type strictness principles but no bouquet-specific root. Abiad et al arXiv:2206.07561 directly study unequal-clique windmill/block-graph *ordinary distance characteristic polynomials*, not continuum distance-power kernels, endpoint negative-type nullity, or fixed-size majorization; a spectral paper on the same object alone is not the same invariant. No found source dominates the unequal-blade classification, with residual risk of older generalized-roundness literature.

## value

PASS

Supremal negative type is a natural precise Hilbert snowflake-embedding frontier for finite metric spaces. The theorem supplies a full unequal-size clique-bouquet root formula, endpoint radical/embedding dimension, and exact balanced-versus-extreme partition ordering; not a one-case numerical computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
