---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The ℓ1² fiber optimization for z=(α,1−α), 0<=α<=1/2, proves m_z(a)=1+max{0,a−2α}, 0<=a<=1, using attained two-sign witnesses and casewise ℓ1 upper bounds. With a=||yγ||_1, all other ℓp mass equals 1−a^p, so the min-chord pth power is 1−a^p+m_z(a)^p. It is maximized at a=0 or 1, yielding max{2,(2−2α)^p}. A fresh outer coordinate gives σ(x)>=2^(1/p) for arbitrary x and balanced z attains equality. Independently checked 16 fiber/outer exponent combinations by bounded numerical optimization; analytic casework proves all real p>=1.

## originality

PASS

Important exact coverage limitation: the already-published Resultary ℓ_p(Γ;ℓ_q²) phase law for q=∞ yields the same global index s=2^(1/p), because real ℓ_1² and ℓ_∞² are isometric via (u,v)↦(u+v,u−v). The global number is therefore NOT novel. But that source evaluates an upper witness at one chosen coordinate fiber vector and determines only an infimum; it does NOT state or mathematically imply the full varying-point profile max{2^(1/p),2||z||∞}. The latter precise pointwise family remains original on inspected evidence.

## value

PASS

The full sharp pointwise profile separates outer unused-coordinate witnesses from genuinely in-fiber witnesses and locates a nontrivial continuous phase transition as the diamond direction changes. This classifies a natural family of quantitative local-octahedrality strengths; knowing the previously published global infimum does not answer which specific vectors have larger local radii.

The dated certificate retains the supplied scientific assessment, sources and limitations.
