---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

With Y=X² the correctly normalized CIR generator is 2(alpha+D-beta y)partial_y+4Dy partial_yy; independent rate-r reset adds r(E f(Z)-f(y)). Stationary renewal mixture and common-reset coupling guarantee existence, uniqueness and moments. Testing y,y² yields (2beta+r)m1=2(alpha+D)+rz and (4beta+r)m2=4(alpha+3D)m1+r(z²+w). Completing the square produces K=4beta²r/((2beta+r)²(4beta+r))>0 and a dispersion penalty r w/(4beta+r); strict z>0 and w>=0 prove the interior/boundary cases and uniqueness without assuming deterministic resets. Independently verified symbolic equality and the alpha=3,beta=2,D=r=1 example gives Var(Y)=5/3, randomized w=1/4 cost 1/36.

## originality

PASS

Gültekin determines stationary density for a fixed reset point and morphology thresholds. Olsen gives the general reset-to-distribution moment strategy with additive OU/run-and-tumble examples. Neither inspected statement establishes a global optimizing reset distribution for the squared-CIR observable and exact transition region; standard generator calculations and reset renewal methods are acknowledged prior.

## value

PASS

The reset point is a natural externally controllable choice in a logarithmic-harmonic diffusion; stationary harmonic-energy variability is a physical observable. The exact phase boundary, optimal deterministic law among all randomized laws, and strictly quantitative dispersion penalty provide a complete parameter-dependent control law rather than a generic moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
