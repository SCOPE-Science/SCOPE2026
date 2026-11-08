---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Geometric strict tangent cone at -e1 is u1>sum_{j>1}|uj|, so 2d cones disjoint modulo boundaries. Gaussian radial invariance, half-normal simplex substitution, radial Gamma integral yield exact Dirichlet prefactor. Dirichlet factorial moments give EY=(d-1)/(d+1), Var Y=1/d+O(1/d²), and E S²=4/d²+O(d^-3), hence EW=e^-1[1+7/(2d)+O(d^-3/2)] with fourth-moment control. Under W-tilted Dirichlet, W->e^-1 and boundedness imply total-variation closeness; independent Exp representation proves fixed-k signed Laplace limits and d(1-U1)->1. Independent sampling and symbolic spot checks support but do not replace the analytic proof.

## originality

PASS

Kabluchko–Seidel 2020 Proposition 2.3 (full PDF) already gives the exact cone/vertex solid angle as Gaussian coordinate dominance, hence no originality credit for finite-dimensional exact probability. A newer Kabluchko–Schange 2026 general exact-angle formula also subsumes some finite integrals. The specific first relative correction 7/(2d) AND fixed-k conditional symmetric Laplace law were not found in inspected primary statements; inaccessible newest full paper explicitly remains a priority risk.

## value

PASS

PASS. It quantifies a canonical rare random illumination event in high dimension to sharp first correction, and establishes the local conditional geometry of successful directions. This goes beyond already-known exact cone-angle integrals and is a natural asymptotic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
