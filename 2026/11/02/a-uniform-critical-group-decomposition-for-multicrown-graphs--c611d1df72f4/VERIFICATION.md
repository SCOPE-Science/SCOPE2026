---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Let m=k−1, t=n+m, q=n+2m. The integer Laplacian blocks tI and −J−mI lead, under the unimodular coordinates u=b_n, z=a_n−b_n, d_i=a_i−a_n, e_i=b_i−b_n, to one free u, r=n−1 copies of t d_i−m e_i and t e_i−m d_i, with global relations t z−Σ e_i=0 and −t z−Σd_i=0. Replace first d/e coordinates by their sums via a simultaneous integral determinant-one transformation, eliminate them via the global relations, giving a single cyclic Z_{tq} and n−2 blocks [[t,−m],[−m,t]]. Each block has Smith invariant gcd(t,m)=g and determinant t²−m²=nq, hence g,nq/g. Spectral eigenvalues 0,2t,n^(n−1 times),q^(n−1 times) give matrix-tree product. Independent full weighted Laplacian reduced Smith forms and exact determinant computations matched (n,k)=(3,0),(4,3),(6,3),(8,1), including two even noncoprime examples. The proof does not divide by nonunits and addresses k=0 and connectedness n≥3.

## originality

PASS

Best-of-knowledge originality assessment: the exact new claim was compared by implications with same-object primary results; known definitions/source results are credited, and no directly covering proved theorem was identified in the inspected material. This is not exhaustive priority certification. A uniform critical-group decomposition for multicrown graphs. The integral reduction determines the additional torsion factors; it cannot be obtained just by plugging excluded parameters into a conditional prior theorem.

## value

PASS

An integral Smith-group classification on a natural complete bipartite graph family, including infinite even-order noncoprime parameters excluded by the previously published explicit formulas. Critical groups retain torsion/extension information absent from spanning tree totals; the n mod 4 distinction at k=3 gives a substantive arithmetic effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
