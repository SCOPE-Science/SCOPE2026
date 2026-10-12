---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was replayed from the construction rather than from numerical samples.

For \(D_{3,s}\), the quotient field is algebraic over \(k(u_1,\ldots,u_{s-2},t)\), so its transcendence degree is \(s-1\). The general \(D_{m,n}\) starts from \(s=n-m+3\) and applies \(m-3\) one-variable suspensions, giving quotient-field transcendence degree \(n-1\).

The source gives \(\dim\operatorname{Int}(D_{m,n})=n\) and the inequality \(\dim\operatorname{Int}(D)\le\dim_vD+1\), hence \(\dim_vD_{m,n}\ge n-1\). Every valuation overring has dimension at most \(n-1\) by the finite-transcendence-degree bound, so equality follows. The standard identity \(\dim_vD[X]=\dim_vD+1\) yields \(\dim_vD_{m,n}[X]=n\). Since \(\operatorname{Int}(D_{m,n})\) has ordinary dimension \(n\) and quotient field of transcendence degree \(n\), its valuative dimension is also \(n\).

For the weak coefficient transform, \(D_{3,n}\subseteq C_{3,n}\subseteq\Omega_n\), hence \(\operatorname{Frac}(C_{3,n})=\Omega_n\). The source’s strict prime chain has length \(n-1\), while the quotient-field transcendence degree is \(n-1\). Therefore both the Krull and valuative dimensions of \(C_{3,n}\) equal \(n-1\). The source’s length-\(n\) chain in \(C_{3,n}[X,1/F]\), together with the Jaffard polynomial-ring upper bound, gives both Krull and valuative dimension \(n\) for that localization.

No classification of individual valuation overrings is claimed, and no computation is used to replace any of these infinite arguments.
