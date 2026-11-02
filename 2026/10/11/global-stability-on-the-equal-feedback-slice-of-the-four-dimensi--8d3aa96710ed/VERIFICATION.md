---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For all a,b,d,h,k,s>0 on k0=m=s and h²<ab, direct symbolic differentiation of V=(x²+y²+(s/k)u²)/2 gives Vdot=-(a x²-2hxy+b y²). This quadratic form is positive definite, so V is nonincreasing, bounding x,y,u for all forward time; stable scalar zdot=-dz+xy is bounded by variation of constants, excluding finite escape. LaSalle on the precompact trajectory yields omega limit in x=y=0, whose invariant core forces u=0; on the remaining z-axis zdot=-dz, so all states tend to origin. Local stability follows from small V and the forced z inequality. For compactly supported invariant measures, integrated Vdot=0 gives exact moment equality, Q positive definite forces x=y=0 almost surely; support invariance forces u=0 and integrating derivative z² then z=0. This proves unique compact invariant measure delta_0. We do not claim h²=ab or unequal feedback. Independent SymPy identity residual is zero; assigned seven Git blob identities yield source-tree SHA a2130de8f355eed896ab7a13b908c189645e3cc7.

## originality

PASS

Best-of-knowledge originality: the source-motivated exact equal dual-feedback cancellation yields a global theorem not implied by the inspected original boundedness/local stability statements; a publicly indexed identical Resultary record is the audited finding itself, not independent prior coverage. A shorter equivalent calculation in unindexed research remains possible.

## value

PASS

The equal dual-feedback slice is the very one used at k0=m=0.8 in the original Li–Cui numerical experiments, yet omitted by that paper’s k0>m boundedness theorem. A genuinely nonlinear all-initial-data convergence region and absence of any nonzero compact recurrent invariant measure are meaningful dynamical conclusions, stronger than local equilibrium stability and a numerical time series. Their motivation is specific to the exact published vector field, not a random parameter slice. This is a limited sufficient global-stability certificate, not complete phase classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
