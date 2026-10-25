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

Directly computed P(K=1,2,3)=(v,3(u-v),1−3u+2v), u=Σp_i², v=Σp_i³. Bernoulli-sum factorization of a nonnegative quadratic with F(1)=1 is equivalent to Δ=(3u−v)²−4v≥0. Δ decreases strictly in v at fixed u; sharp centered five-coordinate cubic inequality Σ(p_i−1/5)³≤(3/sqrt(20))(u−1/5)^{3/2} follows two-level Lagrange multiplier optimization, even with some zero masses. One-heavy/four-equal vector q(t)=(1−4t,t,t,t,t) maximizes v for each u in [1/5,1], t∈[0,1/5]; its Δ=48t³(75t³+30t²−27t+4)≥0, with H(1/5)=2/5 and H decreasing. Independently recomputed polynomial factor and six-category Δ=−1439/810000; equality/degenerate Bernoullis and ≥6 full-support perturbations covered. Finite vector checks supplement global analytic optimization.

## originality

PASS

Tang–Tang already identify the general equivalence of Poisson-binomial laws and real-rooted probability-generating polynomials; O'Neill studies uniform occupancy with fall-through rather than arbitrary unequal masses. Neither materially inspected result implies this sharp 5/6 support threshold; it arises from a specific sharp five-coordinate centered cubic bound. Hidden classical occupancy real-rootedness or coefficient inequality remains a priority risk.

## value

PASS

Natural complete sharp finite support classification for three-draw species richness, across a continuous simplex of arbitrary sampling probabilities; six-category explicit rational obstruction. Useful precise boundary between Bernoulli-sum occupancy representations and failure, beyond a numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
