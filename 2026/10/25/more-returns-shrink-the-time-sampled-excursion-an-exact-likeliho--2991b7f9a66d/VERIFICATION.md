---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every n>=2 and 1<=k<n, the exact law q_{n,k}(l)=k*l*C_{l-1}*Z(n-l,k-1)/(n*Z(n,k)) follows by Catalan primitive-excursion enumeration and size-biasing by the chosen two-step cell. Z(m,j)=j/(2m-j)*binom(2m-j,m-j). The consecutive-k likelihood ratio is proportional to k/(k-1)*(m-k+1)/(2m-k), m=n-l, increasing in m for k>=3 and constant when k=2; finite support loss makes adjacent laws distinct, and k=1 is a top-atom boundary. The conditional fair excursion signs give Var(A|K=k)=n/4 E[L*|K=k], strictly decreasing from n^2/4 to n/4. For k/n->rho in (0,1), recurrence q(1) plus uniform subcritical geometric bounds on ratios gives the claimed q_rho and first-moment convergence. Checks: independently enumerated every balanced 2n-step bridge n<=7, giving 140 exact cell-size probabilities and strict mean monotonicity. Source RESULT.md Git blob 176378ba2f6495917e1e44ef7352f5c69782f4ec; verify.py blob 3cc4aee4a334a0494cbb1c7d39a93846893637fe. Finite checks are corroborative, not proof of all n.

## originality

PASS

The exact Catalan-product factorization and laws of excursions tied to the zero count are known; distinct comparative likelihood-ratio ordering across consecutive return counts, the positive-excursion semiduration variance hierarchy and the k/n->rho moment limit are not established by the inspected theorems. Primary comparisons distinguish longest/ranked excursions and the few-zero invariance regime from size-biased finite all-k order. Best of knowledge; possible coverage by general renewal/conditioning monotonicity results remains a residual risk.

## value

PASS

A natural size-biased excursion invariant captures the duration encountered by an independently uniform time cell. Strict likelihood-ratio order gives monotonicity for all increasing observables, and in particular an exact fluctuation reduction of excursion-level positivity under more zero returns, plus a nontrivial density-scale limit. This is more than Catalan enumeration alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
