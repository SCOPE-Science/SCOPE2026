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

For the stated equal-loss exponential-density ODE, dividing by total mass and changing time by dτ/dt=S exp(−γS) gives a common composition forcing q(τ) for every initial mass on a ray. The log product of the positive proportions has derivative 1−3q=(3/2)Σ(p_i−1/3)². The product is bounded above and stays bounded away from zero, so bounded derivatives and integrability imply q→1/3. Scalar mass solutions preserve strict order and are bounded above by comparison with F(S)=S/3−d exp(γS). Below S₋ they hit zero in finite auxiliary time, with slope −d at zero, corresponding to extinction only as physical time tends to infinity. A global positive auxiliary solution stays bounded away from zero. It cannot have distinct liminf and limsup: an intermediate level different from both roots has a fixed eventual crossing direction. A limit must be a root of F. Extinction is open; the upper-root basin is open by trapping in small intervals at sufficiently late τ. A finite boundary initial mass therefore tends to S₋, and two such solutions cannot converge to S₋ because the logarithmic derivative of their separation tends to (1−γS₋)/3>0. On nonuniform rays, starting at S₋ immediately enters the extinction region; close to uniform, monotonicity of the composition product makes the upper trapping interval valid from τ=0. For the cone, q≤(p₂(0)+p₃(0)) exp(τ); up to T=2/(dγ) the aperture gives q<dγe/2, so (exp(−γS))′≥dγ/2, impossible up to T for any finite positive initial mass. The proof also gives the uniform-ray and infinite-threshold cases. The frozen CHECK.py and VERIFICATION.md are supplementary; the grid and illustrative roots do not certify the global theorem. The supplied script was inspected, not executed.

## originality

PASS

The distinct contribution supported by the comparison is the complete positive-composition ray classification for the specified three-member model, plus explicit cones on which increasing initial mass never rescues coexistence. The model, equilibria, local stability and uniform-ray behavior are not credited as novel. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

For the minimal three-member model at parameters allowing coexistence, the result answers a global question that local stability and a sufficient recovery core cannot: on a fixed composition ray, exactly how the two outcome basins meet, and whether increasing total mass can ever reach coexistence. The strictly positive-measure explicit extinction cone rules out a universal high-biomass rescue rule within the model. Neither an optimal aperture nor a general biological or larger-cycle conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
