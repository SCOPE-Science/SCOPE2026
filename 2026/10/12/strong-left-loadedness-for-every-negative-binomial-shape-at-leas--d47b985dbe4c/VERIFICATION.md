---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For NB integer r>=3 and success p=t/(t+1), m=rt integer, the exact ratio beta_i=w_{m+i}/w_{m-i} satisfies beta_(i+1)/beta_i=(t/(t+1))^2 (m+i+r)(m-i+r-1)/((m+i+1)(m-i)); its cross difference is (2t+1)[i(i+1)-rt(t+1)] (independently expanded symbolically to zero). Thus the centered alpha_i differences w_{m+i}-w_{m-i} have one-turn U-shape. The universal integer-mean identity sum_{i=1}^m alpha_i=E[(X-2m)_+]>0 implies alpha1>0 when endpoint alpha_m<0. Endpoint is P(X>=2rt)>P(X=0): exact Vandermonde amplification covers t<=5 from quoted rational seeds (including direct tail bases), and for t>=6 a geometric-sum event gives comparison (t/(t+1))^(2rt)>(t+1)^-r from monotonic h(t). This supplies strict endpoints and one ordered positive-to-negative crossing for all stated integers, not only a finite sample.

## originality

PASS

Best-of-knowledge implication comparison of assigned exact claim against primary literature and semantic Resultary search. The same distribution/parameter aliases were checked, but a one-index center-tail inequality or modal right-skewness does not decide the entire (alpha_i) sign vector. Full Perrin text unavailable: no whole-paper claim of noncoverage. Neither inspected full Fokkink article nor the accessible Perrin abstract logically imply full L1 for every integral shape r>=3 and t>=1. Inaccessible Perrin full text remains a named priority risk.

## value

PASS

Fokkink et al introduce strong left-loadedness L1 to transfer centered tail inequalities, and explicitly leave non-Poisson families difficult. The theorem supplies the full L1 sign pattern in a substantial naturally parametrized negative-binomial family, not merely one center-tail inequality, allowing this distribution as a right-skewed convolution increment. The Vandermonde all-parameter endpoint mechanism addresses the hard obstruction, so its value is independent of any universal theorem outside this range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
