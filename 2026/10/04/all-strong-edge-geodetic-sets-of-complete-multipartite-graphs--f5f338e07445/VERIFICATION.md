---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The proof reduces the problem to the exact packing number of pairwise edge-disjoint edge covers of \(K_s\). The counting upper bound gives at most \(s-1\) covers for even \(s\) and \(s-2\) for odd \(s\); one-factorization attains the even bound, while the explicit near-perfect-matching construction plus distinct Hamilton-path edges attains the odd bound. If two multipartite parts both omit vertices, their cross-edge cannot lie on any selected-endpoint geodesic; hence there is one incomplete part. For each omitted vertex and each full part, its incident edges require one edge cover of that full part, and endpoint-pair uniqueness makes these covers pairwise disjoint. This gives exactly \(r\le R_i\); the converse construction assigns the packed edge covers and covers all remaining cross-edges directly. The enumerator and minimum formulas then follow by counting omissions.

## originality

PASS

Klavžar–Zmazek determine the scalar strong edge geodetic number for complete multipartite graphs and prove related necessity/constructions, but their inspected article does not classify every feasible vertex set or give the all-set polynomial/minimum-set count. The audited theorem supplies an iff membership rule using the exact edge-cover packing number, so it is not implied by the published scalar value theorem.

## value

PASS

A complete membership theorem and cardinality enumerator for a natural NP-style geodetic covering invariant materially strengthen a published scalar extremal result. The exact edge-cover packing mechanism also explains the parity split in the known value formula and yields all minimum-set counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
