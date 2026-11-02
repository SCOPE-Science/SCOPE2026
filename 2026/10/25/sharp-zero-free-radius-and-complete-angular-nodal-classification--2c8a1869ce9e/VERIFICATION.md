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

Beta(a,2) radial moments (a=d/2) yield m_n=a(a+1)/((a+n)(a+n+1)). Applied to the spherical Poisson kernel P=(1-u²)/(1-2ut+u²)^a, the exactly justified multiplier is [R²+(d+1)R+d(d+2)/4]/[d(d+2)/4], R=u∂u. Direct numerator differentiation yields ∂_t N=24u³[(d+4)+(4-d)u²-8ut]>0 for d>=3, 0<u<1 and -1<=t<=1; antipodal numerator factors (1-u²)³[d(d+2)-12(d+2)v²-48v³]. The strictly decreasing cubic bracket has one positive v. At t=1 the spectral sum has strictly positive terms; monotonicity yields uniqueness, sign and transversality. Implicit function and boundary polynomial N(1,t)=-96(t-1)² prove t_d(u)->1. Dividing cubic by d(d+2) establishes monotone dimension threshold and asymptotic. Independent exact symbolic polynomial checks for dimensions d=3,4,5,10, plus generic antipodal factor and angular derivative match; not an inference from truncated spectral sums.

## originality

PASS

Engliš 2016 derives weighted harmonic reproducing kernel via spherical-harmonic moments and investigates high-power asymptotics, not the exact angular sign threshold for this linear weight. Miao treats unweighted harmonic Bergman kernels. Holomorphic Bergman zero-free results in related published records are different function spaces. Otáhalová 2008 is plausible same-weight literature, but full text could not be obtained owing to disconnected authorized VPN; this is explicitly a priority uncertainty, not a reason to infer novelty.

## value

PASS

A canonical nonconstant radial weight on real harmonic Bergman balls leads to a natural question of kernel positivity and zeros. A complete product-radius and angular nodal classification, exact dimension-dependent sharp threshold, and transverse sign change furnish usable quantitative reproducing-kernel information absent from a general series formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
