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

PASS: At coexistence, prey equation yields u<K=a/b; predator equation divides by v^m to eu^p=d v^(1-m)+qv^(r-m). For r>m, the RHS is strictly increasing from 0 to infinity, defining V_q(u)>0; for u∈[K/2,K], V_q(u)<= (eK^p/q)^(1/(r-m)) uniformly. The undivided prey residual is positive at K/2 and negative at K for large q, giving a root. Compactness and limit prey equation yield u->K and predator balance yields qv^(r-m)->eK^p. Jacobian at positive root satisfies F_u=-bu+c(1-p)u^(p-1)v^m ->-bK, F_v<0, G_u>0, G_v=-(1-m)d-(r-m)qv^(r-1)<0, forcing negative trace/positive determinant. For r=m<1, u(v)=((q+d v^(1-m))/e)^(1/p) crosses K iff q<eK^p; for m=r=1 fixed u=((d+q)/e)^(1/p) and prey residual crosses iff u<K. Independent numerical equilibrium root/trace/determinant for q=100,1000,10000 in the source Example 1 tracks scaled coefficient 37.462416, corroborating but not proving infinite-q asymptotics.

## originality

PASS

PASS (best knowledge): The source Antwi-Fordjour et al introduced the same qv^r harvesting model, analytically discussed r>=m, and numerically suggested prey carrying-capacity recovery and predator near-extinction for large q. Its full paper does not give the exact coexistence iff thresholds at r=m, the power law q^(-1/(r-m)) nor general high-q Jacobian stability proof. The result converts a published heuristic into a sharp exponent-driven theorem, without claiming novelty for the ecology model itself.

## value

PASS

PASS: Whether arbitrarily intense harvest eliminates coexistence or leaves an extremely dilute yet stable positive predator is a motivating model question. The exact r=m boundary, coefficient, and local stability distinguish presence from asymptotic detectability and give explicit analytic context for earlier numerical observations, not a trivial variable renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
