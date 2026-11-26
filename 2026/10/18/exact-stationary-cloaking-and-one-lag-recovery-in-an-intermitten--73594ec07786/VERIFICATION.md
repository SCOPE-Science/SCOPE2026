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

Full-state Poisson regeneration gives the unique stationary joint law by exponential-age sampling, with finite moments. A backward exponential-age resolvent independently yields the spatial transform. Its difference from the Brownian transform has factors q²(DB−v²)[α+(1−p)(r+Dq²)] over a strictly positive denominator, so at any nonzero frequency it can vanish only at balance, including both endpoint mixtures. Substitution then gives the Laplace law. Off balance the stationary variance has nonzero slope 2(DB−v²)/(BΛ). For the two-time check, trajectories with an intervening reset give zero covariance with the initial position; conditional on no reset, the expected net drift from initial mode S is vS(1−exp(−βt))/β, with Brownian increments of mean zero. The stationary occupation of the ballistic modes is [α+(1−p)r]/Λ, and averaging the sign-memory kernel on a regenerative age, or stationarity of XS, gives E[XS]=vπ_ball/B. Substitution at balance yields the claimed Cₚ(t), its strict ordering and the inverse for every t>0. The independent symbolic replay of the backward resolvent confirms the factorization, balance substitution, and variance slope.

## originality

PASS

Credit the 2024 intermittent-walk paper with the underlying renewal resolvent, both fixed reset protocols and the half mixture; the static family follows by mixture linearity and algebra from that machinery. The supported distinction is the sharp stationary two-time separation of all the indistinguishable mixtures in this particular model, and hence exact one-lag recovery, not a new stationary resolvent. The strongest exact catalogue overlaps are later than the frozen item and are identified explicitly below.

## value

PASS

The covariance formula resolves an actual identifiability obstruction: every one-time position statistic loses dependence on p exactly at balance, while every strictly positive stationary lag separates all mixtures and Brownian resetting. The proof exposes the remaining signed ballistic memory and gives an exact observable for the masked parameter. The value is the stationary temporal invariant and its scope, not just a static factorization or algebraic inverse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
