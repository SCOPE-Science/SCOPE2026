---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all a,D,x0,r>0 and s=r/a,y0=x0 sqrt(a/D), the Gaussian-age renewal integral gives a normalized positive stationary density solving rho''+(y rho)'-s rho=0 away from y0 and derivative jump -s. On the left the decaying solution is e^{-y²/2}U_s(y), U_s(y)=integral t^{s-1}exp(yt-t²/2) dt; on right e^{-y²/2}U_s(-y). The logarithmic derivative is q_s(y)=m_s(y)-y left and -y-m_s(-y)<0 right. Integration by parts gives q_s'=s-1-m_s q_s. For 0<s<1 q_s(0)>0, q_s(y)=(s-1)/y+O(y^{-3}) as y→∞, and every root has negative derivative s-1, hence exactly one. For s=1 q_1=1/U_1>0; positive Cov(t,log t)=∂_s m_s implies q_s>0 for all s≥1. Strictly positive covariance and implicit differentiation give unique increasing root zeta(s), endpoint limits 0 and +infinity, small-s zeta~sqrt(pi/2)s. The right derivative is negative and the left sign pattern gives unique global mode min(y0,zeta(s)). The strictly increasing inverse yields unique pinning threshold s_c(y0)∈(0,1), with small-y0 inverse asymptotic sqrt(2/pi)y0. Independently evaluated root integrals and recovered zeta(.2)=.2680583634, zeta(.5)=.76495086739, zeta(.8)=1.53077076608. Numeric instances corroborate but do not prove all-parameter sign/crossing assertions.

## originality

PASS

Best-of-knowledge original scientific contribution confined to the exact theorem beyond explicitly acknowledged prior partial coverage. Meaningful searched aliases, broader-result implications, primary source materials, and access limits are documented below.

## value

PASS

The most likely position of a reset-driven harmonically confined tracer is a natural observable beyond its stationary density. A sharp all-rate and all-distance classification including a universal saturated mode, unique rate-dependent onset threshold, and endpoint scaling is a mathematically substantive special-function crossing theorem, not a redefinition or trivial numeric fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
