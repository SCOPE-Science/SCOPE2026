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

Let q_i=ρ_i^-2 and c_i²=1-q_i. If some q_i+q_j>1 then c_i²+c_j²<1, so there is an open positive quadrant unit-circle arc u=(a,b) with a>c_i,b>c_j. Choose a nearby distinct nonparallel u′ also on the arc, with w=(u′-u)/2 small enough that z=√(1-||w||²)>c_k. The unit vectors v1=(u,0),v2=(-u′,0),v3=(w,z),v4=(w,-z) sum to zero and any first three span R³; they positively span R³ and satisfy all six strict vertex tests. The inspected Ivanov–Strachan cap-body lemma extends vertex+positive-spanning illumination to the entire body. Every 3D body needs at least four directions. If all pair inequalities are equalities then q_i=1/2 all i; each unit direction can strictly illuminate at most one of the six spikes, so at least six, achieved by coordinate directions.

## originality

PASS

The 2020 Ivanov–Strachan and 2025 Arman–Kaire–Prymak theorems establish universal six upper bounds and the octahedral example; a published 2026 equal-radius Resultary finding gives the 4→6 diagonal transition. None of these claims mathematically implies the sharp three-parameter anisotropic classification, including configurations with two exact cap tangencies. Dedicated semantic searches found no dominating special-family theorem.

## value

PASS

The natural full anisotropic deformation family of the extremal six-spike 3D cap body has an exact rigidity phase diagram: I=6 only at the octahedral point, otherwise minimum four, with no intermediate five even on tangency strata. This is a meaningful structural boundary, not a tiny numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
