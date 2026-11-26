---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a fixed supercritical q the final susceptibility is on the lower branch below the peak q^(1/p); taking the seed to zero selects the nontrivial root of 1-s=q integral_s^1 u^(-p)du by strict concavity and continuity. Every interior s produces q in (0,1) with s<q^(1/p)<1, and the objective is positive inside and vanishes at the endpoints. For fixed s, h_p is the reciprocal L^p norm of the nonconstant 1/U_s, so evaluation at the larger exponent's interior maximizer gives strict decrease. At p=2 the objective is sqrt(s)-s, maximized at s=1/4. At large p, the bound on s<=1-epsilon loses a fixed fraction of log p; the band 1-s<=p^(-1/2) has at most (1/2+o(1))log p. On the intervening band, the exponent in h_p/s has size O(log p/p), so the uniform error in p(h_p-s) is O((log p)^2/p) plus an exponentially small term. The resulting strictly concave F_L has interior maximizer y=1/(1+z) with z+log z=L-1 and value z; it beats both edges. This proves the o(1) remainder and the claimed log-log correction. A separate 20,000-point grid with local refinement gave M(2)=0.25, M(2.5)=0.2323013, M(3)=0.2174250 and M(20)=0.0812554; this is finite corroboration only.

## originality

PASS

Pass for the strict ordering of the optimized envelope and its sharp large-exponent asymptotic, to the best of current knowledge. The method for general nonlinear incidence and the cubic optimum are prior coverage, and the variational formula and elementary quadratic evaluation are not the basis for this pass.

## value

PASS

The classical post-peak burden question motivates the same maximization for nonlinear incidence. Known individual values do not describe how that bound changes as the exponent varies. Strict decay and the sharp log-log correction resolve that family-level question rather than just supplying another numerical instance. This is an abstract-model result, not a forecast or claim about arbitrary epidemics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
