---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The tangential unit-circle polygon has cyclic normal gaps Δ_i∈(0,π), sum2π. At any radial direction θ the nearest supporting normal of each of m independently rotated whole polygons bounds the ray by sec D_m(θ), so E area=πE sec² D_m. For a uniformly rotated full polygon, P(D_1>t)=Σ(Δ_i−2t)_+/(2π)=p_P(t); independent rotations give p_P(t)^m and the exact layer-cake area integral π+π∫2tan t sec² t p^m dt. Convexity of z↦(z−2t)_+ gives p_P≥(1−nt/π)_+ by Jensen, strict for nonregular P on (Δmin/2,π/n), proving unique area minimum. Set a=Δmin/2,s=#minimal gaps,q=1−na/π; p_P and p_reg agree for t≤a and have respective slopes −(n−s)/π and −n/π immediately to its right. One-sided Laplace integration yields exact leading excess (2π²s/[n(n−s)])tan(a)sec²(a)q^(m+1)/m, with faster tail. The difference O(q^m) transfers the entire beta-integral inverse-power expansion from the regular polygon to every fixed P. Independent quadrature checks at m=1,4,20,35 showed positivity and asymptotic ratio approaching one, strictly diagnostic, not proof.

## originality

PASS

Buck–Siddon give deterministic circumscribed polygon area identities; Fodor–Hug–Ziebarth study independently sampled supporting hyperplanes around arbitrary bodies, not independently rotated rigid clusters of n tangency normals. Those complete primary statements do not imply the all-m strict regular minimizer and exact shortest-gap exponential coefficient. Brazitikos–Stavrakakis (2014) is a plausible exact random-rotations predecessor (intersection of symmetric convex bodies); only its public abstract was obtainable, with complete paper inaccessible, so the possible specialized planar overlap is explicitly retained as risk and NOT_COVERING is not asserted for its full paper.

## value

PASS

This is a natural stochastic convex-geometric extremal problem for n tangent support directions under independent rigid rotations. It identifies the regular polygon as uniquely optimal for every finite copy number, and a precise exponentially small shape fingerprint recoverable from expected-area excess while all algebraic asymptotic coefficients are identical. This is a structural exact theorem, not an arbitrary narrow computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
