---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Take m=2d and integral cyclic companion A of x^m+k. Direct linear algebra gives det A=k, A^m=-kI and m simple nonreal eigenvalues, each modulus r=k^(1/m)>1. Pair complex-conjugate eigenlines into invariant real planes; on each choose a complex structure J commuting with rotation-scaling rR_θ, and choose an orthogonal basis making A an exact similarity. J and the resulting flat Hermitian inner product are constant and descend to R^m/Z^m even when J is not lattice-integral, so A defines a holomorphic expanding torus self-cover of degree k. Independent exact integer determinant calculations in d=1,2,3,5, k=2,3,7 and several n reproduced det(I-A^n)=[1-(-k)^(n/g)]^g, g=gcd(n,m); the cyclotomic root multiset argument proves all d,k,n. Necessity degree≥2 follows the covering-change-of-variables Jacobian lower bound λ^(2d)>1. Generic torus fixed-point determinant facts are explicitly credited, not rediscovered.

## originality

PASS

PASS best-of-knowledge: inspected general holomorphic expanding map classification supplies broad infra-nilmanifold models but does not in its stated results prescribe every positive integer covering degree in a fixed complex dimension under exact Hermitian metric homothety. The existing torus fixed-point theory supplies |det(I-A^n)| generically, not the all-degree companion realization. Resultary search found only the assigned record with exact universal degree-spectrum/homothety and no independent stronger published equivalent; an explicit older expanding-torus folklore construction remains a residual risk.

## value

PASS

PASS: for each fixed complex dimension d≥1 the exact attainable positive degree spectrum {2,3,...} under the simultaneous strong requirements of holomorphicity, uniform expansion and exact flat-Hermitian homothety is a natural sharp realizability classification. The explicit companion map additionally provides a coherent periodic-count family; while its determinant mechanism is classical, the simultaneous all-d, all-k construction is useful and not implied by the inspected structural classification statements alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
