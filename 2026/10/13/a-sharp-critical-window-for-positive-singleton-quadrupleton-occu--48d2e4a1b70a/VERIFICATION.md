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

Reconstructed joint probability P(N_1=1,N_2=4)=n!b^{n−5}/(4!(n−5)!m^5) and marginal binomial means, giving exact Q. Consecutive quotient Q(n+1)/Q(n)=m(m−2)n(n−3)/[(m−1)^2(n+1)(n−4)], increases up to integer 2m, decreases thereafter, with peak Q(2m)>1 using strict log inequalities. Direct Taylor expansion near n=2m+z√m gives log Q=(1−z²/2)/m²+O(m^{−5/2}) and E1E4/m²→(4/3)e^{−4}; fixed-load covariance/m→−c^4(c−2)^2e^{−2c}/24. Endpoint scaling follows monotonicity. n=4 Y1Y4=0 so negative covariance. Independent exact small m,n rational calculations matched positive intervals; finite checks do not replace proof.

## originality

PASS

Multinomial moments are classical and not independently new. Poissonized cross-frequency negative covariance or first-order joint Gaussian theory does not imply the exact positive O(1) covariance cancellation window for fixed n. A directly plausible 1964 occupancy CLT paper remained full-text inaccessible (institutional VPN disconnected); risk is documented and not treated as automatic failure.

## value

PASS

Frequency-one and frequency-four cells are natural occupancy statistics. Their first-order density covariance vanishes at load 2, hiding a genuine sign reversal of order one in a mathematically sharp √m neighborhood. The all-m sign interval and limiting quadratic profile resolve a specific structurally induced degeneracy of standard first-order approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
