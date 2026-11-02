---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Given a fixed latent N∼Pois(λ) across independent visits and per-individual detection q, p_N=1−(1−q)^N. The total covariance equals Var(p_N)=e^(−λ(2q−q²))−e^(−2λq), not zero (which would arise from independently redrawing N at each visit). Independently symbolically differentiated it: C′=2λe^(−λ(2q−q²))[e^(−λq²)−(1−q)]. For q∈(0,1) its sign is that of R(q)−λ, R(q)=−log(1−q)/q². Its derivative numerator H=q/(1−q)+2log(1−q) has H′=(2q−1)/(1−q)², so R has a unique minimum q0≈0.715331863, proving exactly two critical points for λ>λloc and monotonicity below. For the interior local maximum q−, the ratio G=C(q−)/C(1) has log derivative 1−q−−1/(e^λ−1)>1/4−1/(e²−1)>0 since λloc>2, proving exactly one λglob. Independent high-accuracy bisection found λloc≈2.455407482284 and λglob≈2.610227149204, and checked the λ=3,q=.5 witness. As λ→∞, λq−→1 and C(q−)∼e^(−2)/λ. Endpoint λ=λloc has one horizontal tangent, and λglob has precisely two tied global maxima.

## originality

PASS

Qualified PASS: Royle–Nichols 2003 and Donovan–Hines 2007 already set out the exact Poisson mixture and binary detection formula p_N=1−(1−q)^N, so the observation model and elementary covariance identity are not claimed new. Their inspected abstract and full training chapter optimize inference likelihood, not the unstandardized cross-visit covariance as a function of q. The two mathematically distinct local/global λ thresholds and unique optimizer switching theorem were not found; full original 2003 article could not be read and remains a priority risk.

## value

PASS

PASS: this is a complete sharp phase diagram for an immediately motivated dependence statistic in the classical repeated-presence/absence abundance model. It demonstrates that more sensitive binary detection can reduce observed between-visit dependence because saturation hides abundance heterogeneity. It is not presented as a recommendation to reduce detection or as optimal survey design, and covariance is not interchangeable with correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
