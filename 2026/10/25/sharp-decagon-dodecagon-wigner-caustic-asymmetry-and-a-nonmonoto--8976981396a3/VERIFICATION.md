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

Parameterize opposite edge lengths by s±d_j with ∑_{j<n}d_j u_j=0 and |d_j|<s. The midpoint Wigner edge is d_j u_j and the symmetral area is fixed A(Q)=ns²/(2 tan(π/(2n))). A(P)=A(Q)−2F_n(d), F_n=-A*(W), positive definite on closure subspace from Brunn–Minkowski (with equality only for centrally symmetric P). Since F_n is strictly convex, its constrained maxima are at vertices of cube∩kernel(U), each with ≥n−2 saturated coordinates. All vertices arise from choosing 2 free coordinates and signs; 80 candidates for n=5 and 240 for n=6. Source exact symbolic checker inspects full orbit table. Independent double-precision enumeration found exactly 12 and 28 vertices, maxima 12 and 4, and ratios 0.0590169943749 and 0.0915063509461. The analytic reduction plus exact source algebra supports the continuum result, not numerical enumeration alone.

## originality

PASS

The exact submitted statement was compared against equivalent terminology, general bounds, named exact prior tables and their logical implications. Inspected relevant sources support a distinct increment; missing full texts and hidden equivalent special cases remain documented best-of-knowledge risks.

## value

PASS

The Wigner oriented-area ratio measures asymmetry inside the natural equality family of CPPOS isoperimetry. Exact consecutive higher-side cases beyond the published octagon yield a nonmonotone transition and radically different extremal spectra, an interpretable structural phenomenon useful for conjectures about side-count or Wigner limits; only these n are classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
