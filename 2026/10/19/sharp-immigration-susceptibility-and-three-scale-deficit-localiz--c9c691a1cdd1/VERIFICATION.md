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

The zero-current identity yields the stated speed density, integrable for every fixed alpha>0 and epsilon>=0. In log coordinates the diffusion is nondegenerate, with smooth drift pointing inward at both ends; the generator applied to 1+R² is bounded above, giving nonexplosion by stopping. The integrable speed law is the unique invariant probability on the positive state space (not on an enlarged space including the epsilon=0 absorbing state). Scaling gives Y=bX/D and s=b epsilon/D². For normalization loss δ=1-Z, rescaling y=sz gives δ/s^alpha→Gamma(1-alpha)/Gamma(1+alpha) when alpha<1, using integrability at both ends and integration by parts. At alpha=1 the contribution on [s,1] is s log(1/s)+O(s) by Taylor with integrated O(s²/y²) error; the tails are O(s). For alpha>1, 1/y is Gamma-integrable and δ/s→1/(alpha-1). The sign crossing is y*=s/(-log Z). For alpha<=1, the positive difference divided by δ converges pointwise to f0 and is dominated by f0/Z. Thus TV, with the factor 1/2 in L1, is asymptotic to δ. For alpha>1, the L1 signed derivative is f0[(alpha-1)^(-1)-1/y]; integrating it above alpha-1 via the incomplete-Gamma recurrence gives the stated coefficient. For the negative part, dominated convergence after y=sz gives the subcritical TV limit, the L1 derivative gives bulk TV convergence for alpha>1, and integrating to y=s^(1-t) gives critical mass s t log(1/s)+o(s log(1/s)) for each 0<t<1, hence the uniform limit. Independent quadrature in log abundance, using the negative side and direct normalization loss rather than the frozen Bessel/positive-side algorithm, supports the constants and critical CDF (python /workspace/branches/independent_replay.py 4). At log(1/s)=130 the critical TV/leading ratio is 0.95846 and its CDF at .2,.5,.8 is .21242,.52542,.83843; finite quadrature is not proof and the critical convergence is slow. The uploaded script was inspected, not executed.

## originality

PASS

The stationary GIG/Gamma identities, TV convergence, density crossing and prior rate upper bounds are not new. The supported contribution is the joint fixed-shape leading TV coefficients and the three normalized negative-deficit limits. No inspected result implies this conjunction. The signed profiles in particular are not determined by upper bounds on an unsigned distance.

## value

PASS

The shape-one boundary already changes whether the stationary density favors near-zero abundance. The theorem determines both how much an immigration perturbation moves the stationary law and what abundance ranges carry the deficit. The critical log-uniform result is not conveyed by the TV order or by the normalizer and rules out a single narrow layer at that boundary. The conclusions are meaningful for the scalar equilibrium model; they are not evidence about finite-population extinction, inferential efficiency, interacting communities or joint shape-immigration scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
