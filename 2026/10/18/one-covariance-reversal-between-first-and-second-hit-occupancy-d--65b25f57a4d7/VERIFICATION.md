---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

In the fixed-s balls, b equally likely boxes model, U counts boxes with N_i>=1 and V those with N_i>=2. Summing diagonal and off-diagonal indicator covariances yields Cov(U,V)=bH_b(s), q=(b-1)/b,r=(b-2)/b. Independently enumerated all labelled allocations and compared exactly for b=3..6,s=2..6 (20 exact cases). H_b(x) combines three distinct real exponential bases r<q²<q with polynomial coefficients of degrees 1,1,0, so generalized Rolle bounds all real zeros counting multiplicity by 4; H(0)=H(1)=0, H′(1)<0, H(2)<0, H(x)>0 eventually; multiplicity/sign parity forces a unique root ξ_b>2. For b=2 direct allocation gives negative at s=2, zero at s=3, positive for s≥4. Uniform asymptotic expansion x=lambda b gives e^-lambda-(1+lambda+lambda²)e^-2lambda and yields ξ_b/b→unique positive λ solving exp(lambda)=1+lambda+lambda². Numerical ξ_3≈5.0464, ξ_10≈17.7317, ξ_100≈179.1617 corroborate but not prove infinite assertions.

## originality

PASS

A 2026 published paper gives Cov(K,K_r) and one sign switch in **frequency r**; summing over r>=2 recovers the raw finite covariance, which is not claimed novel. It does NOT itself establish a unique change across ball number s for fixed b, nor the universal limiting λ*. The latter analytic zero-count parameter-direction phase diagram is the distinct increment.

## value

PASS

The negative-to-positive covariance crossover links first-hit richness and repeated-hit diversity for a canonical occupancy model; its **unique load transition** and universal λ* are structural probabilistic information beyond a raw covariance identity or frequency-index sign theorem, useful for occupancy dependence and de-Poissonization intuition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
