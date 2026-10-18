---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For every integer m>=2 over C, the torus Jacobian for Q=x^m y^m+y^m z^m+x^m z^m excludes singularities and intersections away from the two pencils and axes. At p_x and p_z the unit-reduced germ U(U+y^m z^m), U=y^m+z^m, has m transverse tangent directions, each containing two smooth branches of pairwise intersection m+1; all cross-direction contacts are one. The first blowup has multiplicity 2m; each tangency of contact m then requires exactly m subsequent blowups with multiplicities 2m+2k (1<=k<=m). A'Campo's Euler characteristics (2-m) for the central open divisor, 0 for intermediate tails, -1 for each terminal tail, give the local H1 characteristic polynomial (1-t)(1-t^(2m))^(m-2)(1-t^(4m))^m. Delta=3m²-m, mu=6m²-4m+1 and degree of the monodromy polynomial agree. Universal polynomial syzygies with Saito determinant -4f give freeness exponents 2m-1,2m and total Tjurina 12m²-6m+1, consistent with known Dimca et al results. Subtract m² nodes and ordinary m-fold point to obtain tau=5m²-2m at each nonordinary vertex. The all-m analytic blowup proof is the justification, not 2,3,4 sample tests; independently rederived Saito identities and resolution numerics in independent_math_checks.py.

## originality

PASS

The defining polynomial, free exponents and vertex Tjurina values are explicitly prior work in Dimca et al. The separately obtained all-m embedded resolution and A’Campo local first-homology monodromy for the two enlarged vertices were not found in inspected primary sections or semantic corpus. These are distinguishable geometric/topological invariants, even though general resolution methods are classical; best-of-knowledge with unindexed-history risk.

## value

PASS

The explicit embedded resolution and local geometric Milnor monodromy of a free arrangement’s two high-contact singularities are natural topological invariants. The m identical tangent-pair tails give a nontrivial parametric calculation, resolve which nonquasihomogeneous singularities occur, and separate analytic-local topology from previously known freeness/Tjurina data. It is not mere naming or a single tiny numerical substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
