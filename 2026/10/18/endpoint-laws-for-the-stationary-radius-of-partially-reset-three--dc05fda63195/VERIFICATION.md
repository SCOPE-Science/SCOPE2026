---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Lift BES(3) reset at rate c and factor c to the norm of three-dimensional Brownian motion with vector contraction. Stationarity has Y=sum_{j>=0}c^j B_j(E_j) and positive radial Fourier product, integrable over R^3 using the first two factors. Therefore the invariant density at zero is finite and positive, giving pi_c(0,r)~K(c)r^3 with the stated Fourier integral and prefactor. Rescale t to s=ct and dominate by (1+s^2)^-1 to prove c I(c)->pi/2 and K(c)/sqrt(c)->2sqrt2/3. For c->1 coordinate variance sigma^2=1/[c(1-c^2)], the normalized characteristic product converges to Gaussian; first ceil(4/(1-c^2)) factors bound it by integrable (1+e^-6|xi|^2/2)^-4 so L1 convergence yields 4/(3sqrt(pi))*(1-c)^(3/2). Stationary generator gives E[R^2]=3/[c(1-c^2)], separately cross-checked algebraically for c=1/5,1/2,4/5 against the erroneous positive-radial-sum moment. Parameter limits are after r->0, not joint.

## originality

PASS

Kolb and Wuebker (2026) Proposition 10 identifies the rate-c conditioned BES reset but Corollary 11 sums independent nonnegative Erlang radii in error; vector sums must precede norm, invalidating its Lemma 12 flat-origin law. Grzywny et al 2024/2026 Theorem A, Proposition 2.22 give stationary density existence/smoothness for general partial resetting, overlapping fixed-c facts, but not the two tuned c->0 and c->1 constants. The sharp endpoint asymptotics are the surviving claim.

## value

PASS

The error in a directly motivating published distributional representation leads to a wrong qualitative small-ball conclusion. Identifying the true positive cubic coefficient, its two sharp singular perturbation regimes and forced interior maximum supplies a useful quantitative correction in a natural conditioned stochastic process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
