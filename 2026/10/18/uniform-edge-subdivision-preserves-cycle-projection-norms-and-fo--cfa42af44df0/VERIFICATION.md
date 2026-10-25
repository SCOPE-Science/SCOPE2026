---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For any finite connected loopless simple graph (trees included), consistency of subdivision path flows yields Z(G_r)=UZ(G), UᵀU=diag(r_e). Orthogonal projection is U B(Bᵀ R B)^{-1}BᵀUᵀ, entries H_fe replicated on each path, so ℓ1 norm C is max_e Σ_f r_f|H_fe| and Q column sum is 1+A_e−2H_ee. Weighted projection diagonal satisfies 0≤r_e H_ee<1 because no one-edge circulation. Thus all r_e≥2 force strict per-column cut domination. For uniform r, H=C_G/r gives invariant cycle norm, exact monotone cut norm, limit 1+∥C_G∥, gap≤2/r. Direct independent incidence-Laplacian calculation for K5 reproduces cut 8/5, cycle 9/5 before and cut 11/5, cycle 9/5 after r=2; source verify_subdivision.py was read as corroboration, not proof. Boundary case tree gives C=0,Q=I.

## originality

PASS

Novelty appears to be the explicit weighted subdivision transfer law for the canonical ℓ1/ℓ∞ orthogonal cycle/cut projections on any finite connected graph, plus strict cut dominance for all lengths≥2 and sharp K5 reversal. Existing graph cycle projection texts include different graph families and projection minimization questions.

## value

PASS

The same graph after series subdivision has exact canonical projection ℓ1 norms; universal r=2 reversal of cut/cycle dominance is a sharp structural boundary for graph-flow and transportation-space projections. Distinct from routine basis change because absolute column norms and strict inequality demand an additional argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
