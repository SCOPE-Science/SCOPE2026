---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The Reuleaux triangle curvature radius has a threefold periodic square wave, with nonzero odd 3ell Fourier modes. Inverting h+h″=rho gives support coefficients proportional [ell(1-9ell^2)]^-1, which are absolutely summable; rotating/averaging multiplies nth harmonic by cos(n delta/2). Parseval/Green area formula yields D(x)=1/pi sum_{ell odd}(1+cos(ell x))/(ell^2(9ell^2-1)), x=3delta. The exact cosine expansion sum_{odd} cos(ell x)/(9ell^2-1)=pi/36*(sqrt3*cos(x/3)-3*sin(x/3)) holds by direct cosine-coefficient integration; differentiating twice with D′(0)=0, D(pi)=0 yields claimed trigonometric area. Its derivative is (2sqrt3 cos(delta-pi/6)-3)w^2/4>0 for 0<delta<pi/3, and trigonometric reflection proves the sum conservation. The verifier additionally checks symbolic identities and finite independently sampled circle-arc support areas; not relied upon for continuum proof.

## originality

PASS

Best-of-knowledge PASS for the exact full relative-angle area correlation, not for the standard support-function Fourier identities or two classical endpoints. Resnikoff develops general constant-width Fourier/area tools, while Bogosel studies opposite-body mixed area at delta=pi/3. Accessible public descriptions do not establish interior-angle formula, but full primary texts could not be read during this run; historical constant-width literature is real residual risk.

## value

PASS

Minkowski averaging with a rotated copy is canonical and has the Reuleaux triangle and disk as known extreme fixed-width shapes. The theorem gives a complete intrinsic angle-parametrized continuous area path, strict growth speed, and a complementary-angle invariant, not just re-evaluation of classical endpoint areas; this is a meaningful exact geometric invariant of a canonical body.

The dated certificate retains the supplied scientific assessment, sources and limitations.
