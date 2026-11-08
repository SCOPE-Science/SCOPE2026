---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The count Z_{r,s}=sum_{k=1}^{min(r,q-1)}(q)_k S(r,k)(q-k)^s follows by surjections on the left. Identifying two same-shore vertices yields equality probabilities Z_{r-1,s}/Z_{r,s} or Z_{r,s-1}/Z_{r,s}. Color-permutation symmetry gives E[conj(phi_v,t)phi_w,u]=1_{t=u}(qp-1)/(q-1), hence one constant eigenvalue and q-1 identical block matrices with within-shore correlations rhoA,rhoB and across-shore -1/(q-1). Side contrast and normalized shore constants exactly diagonalize all blocks. A coordinate variation argument with q>=3 proves positivity. As s->infinity with q,r fixed, the k=1 and k=2 Stirling terms show 1-rhoA~q*2^{r-2}((q-2)/(q-1))^s when r>=2, while the largest eigenvalue ~s/(q-1)^2; for r=1 the small mu_-~q(q-2)/s instead. Independent proper-colouring enumerations and direct Fourier Gram eigenvalue computations matched q=3,4 and several (r,s), including r=1 boundaries. Finite checks do not imply the asymptotic theorem.

## originality

PASS

Bounded best-of-knowledge originality after comparing equivalent mathematical statements, stronger-coverage implications and relevant primary material. No inspected source is shown to imply the target exact statement; incomplete historical coverage is retained as a risk.

## value

PASS

The first Fourier band is a natural basis for extracting site-wise color information from proper-colouring samples. The complete exact Riesz spectrum classifies all finite parameters, and the abrupt quadratic-to-exponential change in stability when the thinner shore grows from one to two vertices is a substantive constrained-sampling phenomenon, not just a chromatic count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
