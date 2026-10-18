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

The geometric spherical log mean H_n is orthogonally invariant and a norm by Kovalev, used as an explicit prior input rather than newly proved. For a real rank-two diagonal (a,b) the angular logarithmic identity gives exp integral=C_n(a+b); the radial beta log moment gives C_n=exp[(ψ(1/2)−ψ(n/2))/2]. Rank-k projectors satisfy H_n(P_k)=C_n exp[(ψ(k/2)−ψ(1/2))/2]=C_n r_k, with exact r1=1, r2=2, r3=e, r4=2√e, r5=e^{4/3}, r6=2e^{3/4}. For real x=k/2≥5/2, ψ1≤1/x+1/x² and ψ2≤−1/x² imply r″(k)<0; the finitely remaining increments decrease by exact rational exponential enclosures in inspected verify_hardy_rational.py (I independently checked the exact formulas and high-precision gaps, not an infinite numerical extrapolation). Therefore r_j−r_{j−1}≤e−2 for j≥3. Projector decomposition diag(s)=Σ(s_k−s_{k+1})P_k, triangle inequality, and Abel summation give the claimed spectral-tail bound for all real n×n A,n≥3. Rank≥3 forces strict nuclear inequality because 3−e>0, and rank3 tP_3 attains coefficient sharpness. No assertion of equality in refined inequality for all matrices beyond stated witnesses.

## originality

PASS

The parent paper Hardy-type norms of matrices supplies the norm axiom and projection formula, which are credited, but its accessible abstract/synopsis does not establish the dimension-free sharp (3−e) trace-tail inequality or if-and-only-if rank-two nuclear equality. Primary PDF is inaccessible through lawful public routes and the separately authenticated Oxford route reported disconnected institutional VPN; this is a MATERIAL comparison risk, not alone a failed O assessment. Resultary found the exact indexed research item but not another stronger distinct Hardy-matrix spectral-tail result. Best-of-knowledge PASS qualified by uninspected primary sections: no fabricated assertion that whole paper is NOT_COVERING.

## value

PASS

Quantitative sharp stability of a geometrically defined matrix norm against its natural nuclear envelope controls every singular-value tail, determines the nontrivial rank-two equality stratum, and gives an optimal rank-three obstruction with a dimension-free constant. This is a natural all-dimension spectral inequality rather than a renaming of projection values; the nonstandard global projection concavity is the substantive ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
