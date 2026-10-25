---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Ostrovski establishes the invariant polygon Γ_K^0 and rotation order for each exceptional θ_K, K≥3. With t=sin²θ, s=sinθcosθ, v_j=B^j(t,1−s), det B=1 makes det(v_j,v_{j+1})=−t(1−2s) for all K sides. Centered shoelace over four quarter-turn copies telescopes to area(U_K)=1−2t−2Kt(1−2s), giving the exact ε expression. The preserved indefinite Q and endpoint B^Kv0=Rv0 imply cosh(Kμ)=1/(2t), while cosh μ=1+2 sin³ ε/(cos ε−sin ε), hence K=ε^−1+1/3+O(ε), ε_K=K^−1+(1/3)K^−2+O(K^−3). Leading O(ε) terms in area cancel, leaving 10/(3K²)+O(K^−3). Independent 65-digit bisection solved parameter relation for K=3,4,8,12,25,100,500, checked two algebraic area expressions, and found K² area converging toward 3.333... . Source establishes Jordan boundary and annulus foliation; this result does not claim dynamics of the residual region.

## originality

PASS

Ostrovski 2013/2014 gives the original nine-piece map, θ_K, exact polygon vertices and invariant-circle outer foliation. The additional area identity and sharp 10/3 coefficient were checked against the primary relevant Sections 2–6 and Appendix, including parameter/eigenvalue data; none of the inspected earlier source passages gives that exact Lebesgue-area asymptotic. This is a refinement of the same geometric construction rather than a new dynamical theorem; equivalent unpublished shoelace calculations remain possible.

## value

PASS

The quadratic core area law quantifies how much of a natural area-preserving square map is rigorously protected by an explicit integrable foliation along an infinite exceptional parameter family; the cancellation of the linear term is a meaningful asymptotic geometric fact, while no chaoticity or maximality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
