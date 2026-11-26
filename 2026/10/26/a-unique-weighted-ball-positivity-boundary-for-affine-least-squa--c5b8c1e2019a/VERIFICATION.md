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

For d≥1 and α>−1, the beta coordinate density has variance 1/s and the affine kernel is 1+s⟨x,y⟩. Its absolute integral is an even convex function of the evaluation radius, maximized at 1. The signed kernel attains the norm and its negative-set indicator minimizes the fit over 0≤f≤1, with value (1−Φ(s))/2 since the kernel has mass one. Boundary extrema apply to the essential norm by continuity and full interior support. Equivalently Φ(s)=E max(1,|Z_s|), Z_s=sT. Cauchy–Schwarz gives Φ(s)<3 for 1<s≤8, including strictness at 8. For s≥6 the mixed derivative z(s²−6s+z²)/(s²−z²)² is strictly positive for 0<z<s. The increasing density ratio on the common support and positive tail extension force one crossing of densities and strict ordering of tail probabilities on the common support; integrating the tails above 1 proves strict norm increase in this range, not asserted on the whole of (1,∞). Beta-density domination on compact s-intervals gives continuity. Independent rational integration gives Φ(13)=5441398251829/1792160394037>3, and Φ(12)<19136/(2079π)<3. Thus σ∈(12,13) is the only crossing on s>1, and d=11 is first for α=0. Strict undershoot persists at a nearby interior point and under bounded smooth approximation of the negative-kernel indicator (e.g. a smooth sigmoid), with a further small rescaling if needed. The gamma ratio gives E|Z_s|=√(2s/π)[1+1/(4s)+O(s^−2)]; the triangular correction is C_s/s[1+O(s^−1)], yielding the relative 3/(4s) term. Endpoint replay: branches/9be8530f-254a-4c58-b960-93f7d99480ad/record2_endpoint_reproduction.py (independent exact arithmetic). Frozen verify.py was not run.

## originality

PASS

The norm formula at integral effective dimension is already an exact special case of the degree-at-most-one spherical norm; the moment/kernel calculation is not the originality basis. The supported distinct contribution is the sharp continuous-weight threshold, including strict ordering in the relevant parameter range and classification of attainable strict undershoot. The strongest checked earlier statements do not establish that continuum boundary. This decision does not certify earliest priority.

## value

PASS

The useful result is a complete boundary for a concrete sharp loss of positivity of a common fit, as the actual radial weight varies over reals. It supplies a sharp extremal value with a smooth, interior witness when the boundary is exceeded. It is not just substituting a dimension parameter in an existing spherical formula or reporting the value of an endpoint integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
