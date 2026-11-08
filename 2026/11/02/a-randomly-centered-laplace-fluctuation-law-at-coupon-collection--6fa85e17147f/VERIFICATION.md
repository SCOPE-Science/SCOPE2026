---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Poisson superposition gives independent Exp(1) first arrivals X_i and maximum M_n, with stopped arrival count distributed jointly as coupon completion time T_n and singleton count S_n. Given M_n=y, the last arriving process is singleton and the other n-1 are independent positive-truncated Poisson(y), so S_n=1+Bin(n-1,y exp(-y)/(1-exp(-y))). At y=log n+x, uniformly on compact x, its mean minus log(n)e^{-x} is O(1) and variance/log n tends to e^{-x}; conditional characteristic functions give the stable mixed normal (G,sqrt(e^{-G})Z). Zero-truncated Poisson moment bounds make T_n/n-M_n=O_P(sqrt(log n/n)); the random centers differ by o_P(sqrt(log n)), so Slutsky transfers to the discrete coupon process. Integrating exp(-t^2 E/2) with E~Exp(1) yields centered Laplace scale 1/sqrt2, and the Gamma joint characteristic function. Checked source finite DP and conditional formulas; independent small-n positive-truncated Poisson moment checks corroborated, not a proof of CLT.

## originality

PASS

Myers–Wilf (2003) already gives exact finite joint (T_n,S_n) distribution; exponential first-order singleton limit is also prior. The evaluated random-time-centered joint second-order mixed Gaussian/Gumbel and Laplace marginal are not stated in the primary materials read; extracting an asymptotic from known finite formulas requires nontrivial analysis but could have been done earlier.

## value

PASS

The self-centering by realized completion time reveals a distinct second-order fluctuation that is not Gaussian despite a conditional Gaussian law. The exact joint Gumbel–Gaussian mixture with exponential mixing and Laplace marginal supplies a precise natural asymptotic statistic at the classical coupon-collection stopping time, extending known first-order singleton laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
