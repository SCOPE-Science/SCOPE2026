---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Conditional on assignment history, a newly protected position is globally top-choice with probability r_j/n, whereas an unprotected position avoids envying the t_j previously protected allocations with probability r_j/(r_j+t_j). Adjacent interchange of one protected status and one unprotected status leaves the product unchanged; hence the k-wise event equals the final-k-positions probability k!/n^k for every specified set. Summing joint events gives falling-factorial moments (n)_k/n^k, binomial inversion the exact distribution and pgf convergence 1/(2-z). Independently implemented profile enumeration over all 24^4=331776 n=4 strict preference profiles and exact subset probabilities for n<=9 corroborated the identity. No independence of the indicators is claimed.

## originality

PASS

Ortega et al. 2026 establish separate first-choice and unenvied marginal expectations and use coupon-collector arguments for related DA observables; Myers–Wilf count coupon singletons. Neither marginal determines the joint intersection law of doubly qualified students, and the inspected primary propositions do not state the k-wise exchangeability/geometric limit. Related Resultary RSD studies concern small-market lottery or inefficiency shapes, not this count.

## value

PASS

Exact k-wise intersection probabilities give an unusual position-exchangeable statistic despite position-sensitive marginals, and the non-Poisson geometric limit yields a natural complete probabilistic law for simultaneous absence of both directions of envy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
