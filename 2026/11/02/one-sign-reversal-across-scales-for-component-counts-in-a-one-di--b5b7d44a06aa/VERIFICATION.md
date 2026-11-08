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

Uniform order-statistic gaps, including endpoints, form Dirichlet(1,...,1); K_n(t)=1+sum of n−1 internal gap exceedance indicators. One-gap P(D>r)=(1−r)^n and two-distinct-gap joint P(D>r,D>s)=(1−r−s)_+^n give the identity after separate same/distinct covariance. Divide by positive (n−1)(1−s)^n: sign is B=1−(n−1)(1−r)^n+(n−2)[(1−r−s)_+/(1−s)]^n, strictly decreasing on s<1−r and constant afterwards. Variance at s=r positive by configurations with distinct component counts, so exact threshold implies unique root and signs. Sparse limit expands the two-coordinate covariance with cancellation at leading order, yielding −cd e^(−c+d neg) term and stated d_*. Rechecked n=3,r=2/25,s=7/10 gives −17192/1953125, with exact rational grid for n=3..8 and variance positivity. Source typo potential: e^c>1+c² is valid for c>0, so d_*>c.

## originality

PASS

Decreusefond–Ferraz 2011 treats a Poisson point process at a fixed radius and evaluates its cluster-count distribution, not the fixed-size two-threshold covariance sign law. Classical uniform-spacing empirical processes likely yield sparse-limit covariances but inspected material does not establish the exact all-n sign boundary or rational root. Resultary nearest published component/triangle covariance on independent bond percolation, a different model.

## value

PASS

Shows a counterintuitive negative covariance between nested, pointwise decreasing component counts; gives the unique finite threshold and sparse asymptotic boundary. This is a precise reliability/scale-comparison invariant for a natural fixed-sample random geometric graph, not a routine single-radius moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
