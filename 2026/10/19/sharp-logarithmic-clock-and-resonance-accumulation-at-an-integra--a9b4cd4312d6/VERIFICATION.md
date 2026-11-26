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

The exact change q=(r/d)^γ and w=z−d gives qdot=γwq and qddot=c²(q−q^p) in the original time, with angular speed β. The potential minimum is at q=1 with the stated E_*, and its positive zero is Y. For E_*<E<0 there are exactly two positive simple turning points, hence a minimal radial period given by the two-way quadrature. To justify the delicate lower-end constant, set ν=2/γ, ε=2(−E)/(c²Y²), u=q/Y, and fix a sufficiently small cutoff a. On the lower piece use v=u√(1−u^ν), whose inverse derivative is 1+O(v^ν). The turning point is then exactly √ε and the main integral is arcosh(v(a)/√ε)=log(2a/√ε)+O(a^ν)+o_ε(1). The inverse-derivative error has absolute integral O(a^ν) uniformly for small ε: split at 2√ε and bound the rest by a multiple of v^(ν−1). For fixed a the upper piece tends to ∫_a^1 du/[u√(1−u^ν)], by the simple upper root and a uniform square-root bound after shifting to the moving endpoint. Its finite part after subtracting log(1/a) is 2log(2)/ν by v=u^ν. Together these give cT=log(2^(1+2γ)c²Y²/(−E))+o(1), including the factors from a full radial period and the energy normalization. Independently, with ξ=q−1, ω₀=d√(2γ) and signed potential coordinate s=sgn(ξ)√(2(V(q)−E_*))/ω₀, the inverse has expansion ξ=s−(p/6)s²+[p(p+3)/36]s³+O(s⁴). The even part of its derivative in the center-period integral yields the displayed linear energy coefficient and an O((E−E_*)²) remainder. The period is continuous between the two boundaries and bounded away from E=0. It therefore hits 2πn/|β| for every sufficiently large n, with every such selection tending to E=0; exponentiating the verified finite-part law gives the resonant energy prefactor. The geometric wording is in the stated energy sense: E=(γ²/2)(r/d)^(2γ)[w²+γr²/(γ+1)−d²], so approach to the ellipsoid follows at radii bounded away from zero. This is not uniform spatial convergence of entire cycles to the ellipsoid; the small-radius turning points approach the axis at z=d. The uploaded numerical checker was inspected, not used as proof.

## originality

PASS

Integrability, the center family and separatrix geometry have prior coverage. The leading logarithmic divergence, the inversion to resonance energies, the local twist technique and the cubic elliptic special case are not distinct contributions on their own. The supported distinction is the evaluated finite logarithmic constant in physical time at normalized energy E for arbitrary real γ>0, equivalently the explicit sharp energy prefactor. Neither the available same-family integrability statements nor the exact later cubic clock covers that all-γ finite part. The access and general-normal-form risks are noted rather than treated as evidence for or against priority.

## value

PASS

This is a natural global boundary of a known integrable locus, not an arbitrary choice of parameters or a claim to rediscover its geometry. An unspecified log remainder would at best yield the exponential rate and would not fix the energy scale of one-radial-period phase locking. The evaluated constant supplies that missing scale for every real positive γ, including powers not treated by the cubic elliptic formula, and the center check identifies the local period variation. The meaningful increment is the normalized finite period part and its calibration of the resonance energies, not the routine inversion or local expansion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
