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

For 0<alpha<1, DLMF 18.15.10 supplies a uniform interior asymptotic C_k^(alpha)(cos theta) with amplitude (2alpha)_k/(alpha+1)_k∼k^(alpha-1), decreasing to zero and oscillatory phase; the remainder O(k^(alpha-2)) is summable. Uniform Dirichlet summation proves S_n^(alpha)(x)=(2-2x)^(-alpha)+O_K(n^(alpha-1))>0 on compact K⊂(-1,1). The exact derivative identity S_n'=2alpha S_(n-1)^(alpha+1), together with Tran–White’s all-real derivative zeros and arcsine limiting density for alpha+1>1, bounds the number of real S_n zeros by derivative zeros in shrinking endpoint neighborhoods plus at most three (two components and one negative exterior root). x>=1 positivity follows from generating-function coefficient positivity; x<=-1 admits at most one zero since the derivative has no exterior zeros. The endpoint arcsine mass tends to zero, yielding R_n/n→0. Tran–White Theorem 1 covers alpha>=1; α=1 classical Chebyshev. Exact rational Legendre recurrence checked n=3,5,8,10,12 as a diagnostic only.

## originality

PASS

The complete Tran–White full text proves eventual all-real zeros and arcsine distribution only for alpha>=1, with the Legendre case illustrated as nonreal but without an all-alpha<1 real-zero-density bound. DLMF provides the classical ultraspherical asymptotic, not the new zero-count inference via derivative interlacing and endpoint concentration. Ruscheweyh’s 1978 Gegenbauer partial-sum zero-free theorem is about a DIFFERENT polynomial in an auxiliary generating variable with normalized coefficients; it does not imply a count of zeros in x for unweighted sums. No equivalent all-subcritical asymptotic found.

## value

PASS

The previously one-sided real-rootedness threshold is shown to be a genuine discontinuity of asymptotic zero geometry: real fraction jumps from zero below alpha=1 to one above. This is a complete natural qualitative phase classification requiring nontrivial uniform asymptotic and derivative zero-density control, although it neither determines finite-n counts nor the complex limiting measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
