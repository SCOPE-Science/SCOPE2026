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

Reconstructed normalized first-arrival exponentials and weighted empirical CDF inversion: centered increments over O(a_N) windows have variance ≤O(a_N³), giving Bahadur-type crossing expansion despite jump sizes possibly ~a_N. For s≤1/2 max_i i^-s/sqrt(H_N^(2s))→0, yielding Lindeberg joint bridge; for s>1/2 coefficients converge in l² to the persistent Bernoulli series. Exact H_N power sums produce sqrt(N), sqrt(N/logN), N^(1-s) scaling and stated constants; third cumulant is nonzero except theta=1/2, where fourth cumulant is -1/8 times coefficient fourth-power sum, excluding a Gaussian law. Independently evaluated Bernoulli cumulants at theta=1/4,1/2,3/4, with central fourth cumulant -1/8. Only fixed finite level sets and homogeneous clocks are proved.

## originality

PASS

Best-of-knowledge sharp s=1/2 second-order phase transition for homogeneous Poisson rates and normalized Zipf *quorum weights* is not covered by Müller–Šebek’s first-order homogeneous-weight law or their separate aligned-rates-and-weights Zipf model. General Lindeberg and weighted quantile results are used but not presented as new; specific constants and persistent-weight Bernoulli-series law are the additional mathematical claim.

## value

PASS

Quorum fluctuations are natural second-order invariants beyond universal first-order concentration. The sharp square-summability threshold s=1/2 separates Gaussian and non-Gaussian laws for homogeneous-clock Zipf-weighted discovery. The exact joint constants and infinite Bernoulli-series limit are motivated, not arbitrary parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
