---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reintegrated V_c e_n=(log c)/(log(cn))e_{cn}; direct composition gives [V_a,V_b]e_n=uv(u−v)/[(log n+t)(log n+u)(log n+v)] e_{abn}. Output indices for distinct basis vectors remain distinct for all powers, so (C^k)*C^k is diagonal with strictly decreasing weights d_n^(k)=∏_{j=0}^{k−1}K/[(log n+(j+1)t)(log n+jt+u)(log n+jt+v)]. Norm is d_1^(k)=(K/t³)^k/[k!(u/t)_k(v/t)_k], yielding Γ(u/t)Γ(v/t) k (K/t³)^k/(k!)³ and spectral radius zero; fixed-k singular values ∼K^k/(log n)^{3k}, compact but not any finite Schatten class by divergence of log-power sums. s1=|u−v|/t fixes the unordered ratio u/t,v/t; for this ratio, s2/s1 is a strictly increasing function of t>0, recovering log a/log b uniquely. Independently checked symbolic/numerical weights for four distinct integer pairs and k=1,2,3. The a=b commutator vanishes as boundary.

## originality

PASS

Independently compared the exact final mathematical statement, not just title or matching parameter, with the primary material identified below and a new semantic research-index search. No inspected stronger statement implies the precise final claim; foundational results and methods are credited. This is a qualified best-of-knowledge judgment with explicitly retained gaps, not a certification of priority.

## value

PASS

The exact compact-but-non-Schatten singular spectrum of an explicit noncommuting operator family, all power norms, and two-measurement recovery of the generator pair are precise natural operator invariants not mechanically supplied by individual-operator Schatten exclusion. The weighted shift method is standard, but the inverse rigidity is a substantive distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
