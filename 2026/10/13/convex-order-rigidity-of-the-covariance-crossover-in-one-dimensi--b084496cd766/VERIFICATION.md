---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The intensity of component starts is λq for q=exp(-λμ), by insertion of a germ and the void event for grains covering its position. Almost surely starts are germs, with no random endpoint coincidences; positive vacancy and stationarity/ergodicity exclude an unbounded occupied component. The Poisson intensity of grains common to test sites at distance s is λh(|s|). Thus conditional vacancy at a test site is q exp(λh(|s|)) on the left and that quantity times the inserted grain's failure probability on the right. Subtracting unconditional occupancy and integrating over two sites in [0,T] gives the triangular kernel weight T-|s|. Its integrability follows from bounds by a constant times h plus the length tail; ∫h=E[L²]/2. Pairing the half-lines gives the claimed expression since ∫Pr(L>s) exp(λh(s)) ds=(exp(λμ)-1)/λ. The covariance of the boundary indicator with V_T is bounded by the integral of the vacancy covariance, q²∫(exp(λh)-1), so clipping does not change the density. To check the zero, expand H=exp(2λμ)κ: the coefficient at m≥2 is μ^m/m! minus 2∫h^(m-1)/(m-1)!. Since h≥(μ-s)_+ and its power integral is at least μ^m/m, all these coefficients are negative. The power series converges for every λ by boundedness and integrability of h; H/λ starts at μ, decreases strictly and is bounded above by (1+2λμ-exp(λμ))/λ. This gives the unique crossing and its orientation, the sharp deterministic upper bound (strict unless the continuous stop-loss transform is the deterministic one), and the second-moment bound from the quadratic coefficient. Strict ordered curves for distinct convex-ordered laws follow from strict increase of the exponential and continuous, distribution-determining stop-loss transforms; evaluating at a zero orders the roots strictly. The two-point positive laws in the proof have fixed mean and unbounded second moments, which yields infimum zero without attainment.

## originality

PASS

Hug–Last–Schulte cover existence and the mixed covariance in general form. Do not credit the density identity as a new general covariance formula. The supported distinct result is the all-grain single-zero theorem and its rigidity: the sign orientation, entire-curve and root ordering, and sharp deterministic equality boundary. The closest same-day result has a different model, parameter, and limiting constant. Priority beyond the comparisons is not determined.

## value

PASS

For two natural observables, component starts and covered length, this identifies the full qualitative intensity response even for unbounded grains with finite second moment. It gives an exact deterministic upper extreme and proves that mean alone supplies no positive lower bound; convex order ranks the whole response, not just low-intensity coefficients. This is useful structural information beyond the known general covariance formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
