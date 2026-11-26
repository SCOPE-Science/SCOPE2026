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

Under the stated two-sided convention the transfer amplitudes from independent white-noise coordinates can be normalized to [(b+iω)+tρ, t sqrt(1-ρ²)] divided by (a+iω)(b+iω), with a common sqrt(2D_x). The squared norm gives the displayed PSD with c>0. For z=ω² the derivative has numerator a²b²-c(a²+b²)-2cz-z², strictly decreasing on z>=0. Its unique positive root when c<h gives the stated peaks (two strict local maxima attaining the same global value). Otherwise it is negative for z>0; at equality the leading drop in ω is -2D_x c ω^4/(a^4 b^4). The peak criterion is t²+2bρt+b^4/(a²+b²)<0: this requires negative ρ and its minimum over positive t is negative exactly at the claimed strict ρ gate. The limiting threshold uses t=b²/sqrt(a²+b²), not a peak at equality. For an independent covariance check, the stationary moment equations give Var(Y)=D_y/b, (a+b) Cov(X,Y)=kD_y/b+2ρsqrt(D_xD_y), and a Var(X)=D_x+k Cov(X,Y). For τ>=0, C_x'+a C_x=k Cov(X,Y) exp(-bτ). Solving gives the two-exponential expression when a differs from b and the affine-times-exponential expression at a=b. In a peaked case c<h<min(a²,b²), so the slower term is negative and the faster one positive, with positive sum at zero and strictly decreasing positive-to-negative-magnitude ratio; for a=b the affine bracket has strictly negative slope. This proves one sign change and also checks the equal-rate example. The frozen numerical verifier was inspected, not used as the universal proof.

## originality

PASS

Standard second-order rational spectra and linear-mode covariance formulas, and the broader observation of PSD peaks with real poles, are not new here. The distinct supported claim is the exact correlation-versus-gain feasibility boundary and one-crossing consequence in the stated two-input triangular model. The closest verified indexed real-pole resonance uses feedback and a different forcing structure; the examined stable-focus literature does not supply the anticorrelation gate. This is not an exhaustive priority determination.

## value

PASS

The useful exact result is a falsifiable boundary for when an apparent resonance can be produced by an overdamped feedforward system. It tells which anticorrelations cannot work at any positive gain, and identifies a time-domain signature consisting of one negative tail rather than repeated oscillations. This is a natural restricted null model and a sharp inferential countermechanism, not just a computed extremum at one parameter point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
