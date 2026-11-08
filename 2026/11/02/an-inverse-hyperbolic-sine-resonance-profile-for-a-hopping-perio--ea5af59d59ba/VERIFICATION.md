---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For F(x)=x+b-(1+exp(-ax))^(-1), q=exp(-a/6), b=1/3+sigma q, x=-1/2+z/a, the exactly defined scaled 3-step displacement H=q^(-1)(F^3(x)-x) admits uniform C^1 expansion H=3sigma-2sinh(z)+O_S(aq), H_z=-2cosh(z)+O_S(aq), H_sigma=3+O_S(aq) for bounded sigma,z. Its negative derivative, end signs, and implicit differentiation prove the unique local primitive attracting 3-cycle at z=arsinh(3sigma/2)+O_S(aq); multiplier 1-2aq sqrt(1+9sigma^2/4)+O_S(a^2q^2); slope 3/[2aq sqrt(1+9sigma^2/4)](1+O_S(aq)). Verified the derivative identity (mu-1)/(aq)=H_z directly and independently solved exact logistic iterations in high precision for several sigma and a. Tests diagnose, not prove, the all-large-a compact-uniform theorem.

## originality

PASS

Bielawski et al. analyze a hopping period-three attracting orbit at b about 1/3 (same logistic map), and earlier fixed-rational half-grid asymptotics include the central multiplier but hold b fixed. The new genuinely joint detuning scale b-1/3=O(exp(-a/6)), nonlinear arsinh response and inverse spectral-gap slope relation are not mathematical consequences of the inspected fixed-b assertions. O PASS best of knowledge, not historical certification.

## value

PASS

The exact nonlinear crossover and amplified sensitivity quantify a physically and dynamically motivated hopping transition in a canonical smoothed circle-map family; it is a natural structural response law, not an arbitrary numeric parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
