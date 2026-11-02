---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: From the generator L_theta=q d²/dtheta²+r[f(theta*)-f(theta)], stationarity yields E exp(ik(Theta-theta*))=r/(r+q k²). Thus E cos(2(Theta-phi))=A cos(2psi), Var cos(2(Theta-phi))=V_phi=[1-A²+(B-A²) cos(4psi)]/2 with A=r/(r+4q), B=r/(r+16q). The centered degree-two angular harmonic is an eigenfunction of the resetting generator of eigenvalue -(r+4q); its stationary covariance decays exactly as V_phi exp(-(r+4q)|t-s|). Conditional on the full independent angle trajectory, the projected spatial displacement is centered Gaussian with random variance 2D0t+2delta integral cos(2(Theta-phi))ds. Consequently its fourth CUMULANT, not its raw fourth moment, equals three times the random conditional-variance variance: 24 delta² V_phi [t/(r+4q)-(1-exp(-(r+4q)t))/(r+4q)²]. SymPy independently verified B-A²=8rq(2q-r)/((r+16q)(r+4q)²), yielding the sole positive crossover r=2q. At crossover, variance remains anisotropic by 4 delta t/3; strict fourth-cumulant positivity requires delta!=0 and t>0. For deterministic initial angle, stationary formula is asserted only to leading long-time order and follows from exponentially relaxing two/fourth Fourier harmonics. This is an analytical proof; symbolic checks alone do not establish stationarity or infinite-time claims.

## originality

PASS

PASS, best-of-knowledge: the sampled passive Brownian model and its covariance/effective diffusivity under orientation-only resets are explicitly prior work of Chaki, Olsen and Löwen 2024. The new asserted content is the exact all-positive-time fourth cumulant and its unique r=2q angular cancellation while covariance remains anisotropic. Closest inspected papers contain second-moment analyses, or treat active self-propulsion or no reset; no identified theorem implies the higher cumulant and cancellation. Generic conditional Gaussian-mixture and harmonic-semigroup identities are standard methods, not original primitives. Searches cannot exclude an equivalent switching-diffusivity fourth-cumulant calculation outside this terminology.

## value

PASS

PASS: The finite-time fourth-cumulant tensor is a natural first non-Gaussian observable beyond previously derived anisotropic effective diffusion. Its sharp rate r=2q is a mathematically explanatory boundary at which a genuine fourth-cumulant isotropy occurs without covariance isotropy. The distinction between cumulants, raw fourth moments and excess kurtosis is substantive and rigorously delimited. This is a motivated exact observable of an established stochastic model, not merely a reparameterized variance formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
