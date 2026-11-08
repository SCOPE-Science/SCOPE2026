---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a finite irreducible reversible resident generator Q with empty state 0 and constant invader reset rate b and return-to-empty extinction rate v, stationary balance solves p_I=b/(b+v), p_0=v*h(b)/(b+v), h(b)=b[(bI−Q)^{-1}]_{00}. Reversible diagonal spectral resolution gives h(b)=π0+Σ c_j b/(b+λ_j), c_j>=0, Σc_j=1−π0>0, λ_j>0; thus h''(b)<0. The derivative sign is that of F=(b+v)h'−h, with F'<0, F(0+)=vT−π0 and F(∞)=−1, T=Σc_j/λ_j. Therefore O(b)=1−p_0 rises for v<=π0/T and otherwise falls then rises through exactly one minimum. For two-state resident Q=[[-1,1],[1,-1]], v=10, π0/T=2 and O(2)=3/8; independent exact differentiation confirms global min. This all-finite-state result follows from spectral positivity, not selected numerical checks.

## originality

PASS

Best-of-knowledge PASS for the explicitly motivated ecological occupancy one-dip criterion vT/π0 for arbitrary reversible resident networks with full competitive invasion. Resolvent/renewal resetting representation and spectral mixtures are prior mathematical tools (Pakes, Meylahn et al, Rose et al); the ecological one-turn necessary/sufficient sharp threshold is a particular conclusion absent from inspected open primary work. The complete 1997 Pakes article was inaccessible; potential equivalent reset-shape theorem remains a material risk, not automatic failure.

## value

PASS

Even a competitively superior invader with strictly increasing own abundance can initially lower the fraction of occupied patches. The theorem gives the exact extinction-pressure frontier and excludes multiple dips for any finite reversible resident baseline, a useful qualitative classification and sharp counterexample for competition/occupancy models. Assumes one homogeneous patch, not a spatial metacommunity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
