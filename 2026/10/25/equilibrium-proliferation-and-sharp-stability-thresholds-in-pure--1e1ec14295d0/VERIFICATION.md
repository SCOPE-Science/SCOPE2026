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

Taking leaf coordinate differences yields exactly −(1+λh)(u_j−v_j), so all active pairs are equal and either zero or y=1−1/(λh). The scalar cubic is strictly single-peaked on 0<y<1−1/λ, with maximum 4k(λ−1)^3/(27λ); hence precisely 0/1/2 branches and exact binomial subset count. Every inactive petal has Jacobian eigenvalue −1+λh>0. For full support, the two-dimensional hub-symmetric block has negative trace, determinant (3λy−2(λ−1))/(λ(1−y)−1), positive only on upper branch, and all transverse leaf modes have negative real parts. Independently checked the exact Jacobian determinant reduction, fold maximum, and rational m=2,λ=4,y=1/4 equilibrium using symbolic arithmetic, corroborating the inspected verify.py. Boundary λ=λ_m is nonhyperbolic, not claimed exponentially stable.

## originality

PASS

Simplicial SIS bistability and generic multi-group dynamics are established prior work, but the exact graph-family active-petal subset census and sharp partial-support stability classification do not follow from the inspected homogeneous/irreducible-pairwise models. A different hypergraph/chemical-network reformulation might encode the same subset bifurcations.

## value

PASS

The friendship graph is the canonical overlapping-triangle sparse family. Unlike the usual two-branch mean-field picture, it yields an explicit exponentially large set of physical but unstable partial-support equilibria, ordered sharp fold thresholds and a complete local stability classification. These structural facts reveal how localized higher-order contagion affects equilibrium multiplicity; no claims are made about global basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
