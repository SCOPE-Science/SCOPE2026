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

The classical simple ordered prolate modes identify the top normalized sinc eigenfunction with the no-node Sturm–Liouville mode. In unweighted Lebesgue normalization F_c^*F_c=(2π/c)K_c; differentiating the sinc kernel gives the cosine kernel divided by π. The finite-Fourier equation at x=1 and Hellmann–Feynman therefore give Λ'=2Λb/c. The smooth simple differential eigenfunction branch in L² is also smooth up to the endpoints, by expressing it as F_c applied to the branch divided by its nonzero Fourier eigenvalue. Its endpoint value does not vanish: if it were zero, pψ'(x)=−∫_x^1(qt²−χ)ψ(t)dt would bound |ψ'| by a constant times the supremum of |ψ| on a short endpoint interval; integrating would force ψ to vanish there. For q=c², differentiating the differential equation gives W'= (x²−m_q)ψ², with W(0)=W(1)=0 by evenness, normalization/mean, and endpoint regularity. The integrand changes sign once, so W<0 in 0<x<1. Thus ∂_q log(ψ_q(x)/ψ_q(1))=−∫_x^1 W/(pψ_q²)>0 for x<1; the quotient has a finite endpoint limit since W vanishes linearly and ψ_q(1)>0. Differentiating the squared normalized ratio integral explicitly gives ∂_q(1/b)>0, not just weak monotonicity. Also 0<χ<=q/3 and the same single-sign-change argument applied to (pψ')' gives ψ strictly decreasing spatially, hence 0<b<1/2. Differentiating Λ' then gives strict concavity for every c>0. Analytical replay: RESULT.md lines 23–61; no required numerical claim. The reported Nyström checks are consistency only and were not replayed.

## originality

PASS

The classical eigenfunction correspondence and first derivative identity are inputs, not the distinct result. The actual primary and indexed passages inspected do not give the strict bandwidth derivative of the normalized endpoint amplitude or the resulting strict concavity of the top concentration eigenvalue. Nearby spatial-endpoint, shape-optimization, and eigenvalue-index-decay results have different quantifiers. This bounded pass does not settle exhaustive historical priority.

## value

PASS

Strict diminishing marginal gain across the entire bandwidth range is a meaningful qualitative control of the canonical optimal concentration profile. The Wronskian comparison gives a short structural reason and a stronger strict endpoint-amplitude statement, rather than extrapolating asymptotics, pointwise monotonicity, or numerical checks. The result is expressly confined to the leading one-interval mode.

The dated certificate retains the supplied scientific assessment, sources and limitations.
