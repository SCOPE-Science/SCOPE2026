---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the finite-generator calculation in RESULT.md lines 55–114. With ε=1/r, eliminating fast states gives M(ε)=S_CC+S_CF(D−εS_FF)⁻¹(R_FC+εS_FC), analytic at zero. At ε=0 every state in the reduced chain has a positive-rate path to A, the only closed class. The stationary equations plus normalization, including fast-state mass, therefore have an analytic solution near zero. The fast mass at first order is δ_B. In the derivative of the row at A, injection from B gives α into S₂; at L≥3 the slow one-particle hop from B still resets to A, while at L=2 extraction adds β into the empty state. The leading reduced chain cannot increase extra-particle count, so no sector with at least two extra particles has a first-order source. In the one-extra-particle sector the two possible fast resets after a site-1 hop give S_j→S₂ at rate 1/2 for j≥3. Back substitution gives βc_L=α, c_{L−1}=(β+1/2)c_L and c_{j−1}=(3/2)c_j for 3≤j<L, with the site-2 balance supplied by conservation. As a separate L=2 check, direct stationarity gives π_A=(r+α+β)π_B, π_00=(β/α)π_B and π_S₂=(α/β)π_B. The current follows from last-site occupation, and Cov(η₁,η₂)=−Pr(η₁=0,η₂=1)+Pr(η₁=0)Pr(η₂=1), with joint probability ε+O(ε²) and the product O(ε²). The conditional limits follow from the corresponding vacancy coefficients. The specified checker was inspected, not executed: its exact rational solves and reduced recurrence checks are finite, and its asymptotic comparisons use tolerance 5,000,000/r. The package's report of a run is not independent execution evidence.

## originality

PASS

The process is known. The supported distinct contribution is the full fixed-length first-order stationary law, in particular the bulk and terminal ratios and the joint boundary effect. There is exact indexed overlap for current and small-size covariances; those are not credited as uniquely established by this record. No inspected matching statement covers the full law.

## value

PASS

The full law quantifies a concrete breakdown of boundary independence: conditioned on a vacancy at site 1, site 2 is occupied with probability tending to one for L≥3 even as its marginal tends to zero. The geometric accumulation gives a length-dependence obstruction invisible in the overlapping leading current result. These conclusions make the fixed-length theorem useful as a benchmark for approximations to the known model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
