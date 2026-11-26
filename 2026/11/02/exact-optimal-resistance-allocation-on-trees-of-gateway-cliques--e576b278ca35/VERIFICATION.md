---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For connected weights, restrict the Laplacian to the orthogonal complement of constants. The trace-inverse second derivative along a nonzero symmetric increment D is 2 tr(A^-1 D A^-1 D A^-1)>0, and distinct conductances give distinct Laplacians on a simple graph. Averaging over peripheral permutations never increases the objective and preserves connectivity and budget. Since each clique has a single gateway, unit current between different cliques crosses exactly the bridges on the intervening path; attachments cannot change internal resistance. The bridge coefficients therefore count unordered cross-cut pairs. In a size-n clique the hub eigenvalue is nb, and ell=b+(n-1)a has multiplicity n-2. The hub and peripheral projection squared lengths of e_g-e_v are n/(n-1) and (n-2)/(n-1), respectively. This gives the clique's contribution (N-n+1)/b+N(n-2)/ell and its budget n b/2+(n-2)ell/2. For n=2 both ell terms vanish. Equality in weighted Cauchy–Schwarz fixes all positive conductances as stated, sums to B, and satisfies ell>b whenever n≥3. The exhibited optimizer is connected and strict convexity gives unrestricted uniqueness; disconnected assignments cannot compete. The common contrast eigenvalue claim applies only to n≥3.

## originality

PASS

Both the general optimization principle and the equal-barbell and tree cases are known and already credited. The explicit allocation on arbitrarily heterogeneous disjoint clique blocks linked by a gateway tree, and the resulting common within-clique contrast eigenvalue, are supported as distinct within the inspected material; absolute priority is not certified.

## value

PASS

This is an explicit all-edge network design for a natural class between trees and dense graphs. It distinguishes the bridge cut and clique contributions without numerical optimization, recovers sharp known endpoints, and exposes an unexpected common optimum contrast eigenvalue even for heterogeneous clique sizes. Neither the raw strict-convexity fact nor merely reproducing the known barbell would have this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
