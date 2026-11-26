---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently solving the sticky-state equations in midpoint coordinates gives an allocation-dependent part of M/T equal to 2(1+eta)((lambda+1)h^2+wh)/(4eta+F(1-h^2)), up to an h-independent constant. In detail, take l=beta(1+h)/2, r=beta(1-h)/2, delta=(m_+(L/2)-m_-(L/2))/T, and Q the mean of the two dimensionless wall orientation averages minus 1/2. The boundary equations are lQ-[eta+(lambda+1)l/2]delta=1+eta and rQ+[eta+(lambda+1)r/2]delta=1+eta. Their determinant is eta beta+(lambda+1)lr>0 even at zero allocation to one wall. Differentiating the resulting mean gives the asserted prefactor and P(h)=2(lambda+1)Hh+w(H+Fh^2). Its derivative is at least 8eta(lambda+1), and its two endpoint signs are strictly negative/positive even at |w|=lambda+1. The displayed stable root, strict interiority, oddness and monotonicity follow. Finite mean at zero allocation on one side follows from a uniform positive chance in bounded time to reach and be killed at the active wall: use runs without tumbles and, if needed, a bounded wait for release from the opposite sticky state. The frozen proof and checker support the model; the script was inspected, not run, and the recorded simulation is not used.

## originality

PASS

The published primary sources inspected give the stochastic model, asymmetric boundary first-passage formulas, or optimization of a different control. The closest catalogued fixed-budget result has unbiased headings and is later-dated. The full fixed-budget sign and interiority theorem for all initial orientations with the effective bias and closed optimizer remains distinct on the inspected evidence.

## value

PASS

A fixed amount of wall reactivity is a natural design constraint and makes all-at-one-wall choices plausible for strongly polarized or off-center starts. The theorem excludes both extreme allocations uniformly, gives an explicit optimum, and identifies how location and heading compensate. This is a complete design answer rather than an enumeration or a relabeled exit-time formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
