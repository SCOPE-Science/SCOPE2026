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

Proof checked: rotating-frame radial/tangent derivative of z|z|² is (3ρ,φ), giving J0=diag(-2,0) and Jh=[[3u,-v],[3v,u]]. Fourier eigenvalues of directed 3-cycle are λ,conj λ. Traceless C²=Δ²I and real tr(conj C C)=2h yield det=e^(-2Bτ), real tr=e^(-Bτ)[(1+r)cosh(2ξτ)+(1-r)cos(2ητ)]. Real 2×2 Schur test yields exact strict criterion. Large-v asymptotics make positive-phase peaks violate while interlaced troughs satisfy criterion for any prescribed finite N, with one chosen finite v; does not imply infinitely many windows at fixed v. Source verification code was read but not executed; exponential formulas independently inspected algebraically.

## originality

PASS

Pereti–Fanelli considers symmetric diffusive network swapping and critical rate, not the directed cubic three-oscillator model and N-window reentrance. Related 2026 general directed higher-order synchronization primary source could not be read in full; residual risk explicitly retained. Exact model-specific Floquet law is not asserted novel merely by parameter mismatch: general average criteria do not determine full Floquet trace or arbitrarily many alternations.

## value

PASS

Exact local Floquet boundary and unbounded number of rate-dependent stability reversals in a simple directed nonlinear coupling system reveal a mathematically motivated mechanism not resolved by fast-switching averaging; not a global stability assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
