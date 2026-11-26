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

The trace inverse on the constant-vector complement is strictly convex: along a nonzero symmetric variation H its second derivative is 2 tr(A⁻¹HA⁻¹HA⁻¹)>0 for positive definite A. The edge-to-Laplacian map is injective, the trace diverges at disconnection, and scaling to exhaust the budget improves the objective. Thus the minimizer exists, is unique, and is invariant under every original-vertex permutation, with positive spokes. The unsigned incidence Gram matrix (n−2)I+J yields one nonzero constant-block eigenvalue (n+1)y, n−1 two-dimensional blocks with trace nx+(n+1)y and determinant ny(2x+y), and m−n eigenvalues 2y; this includes n=3 and x=0. Summing reciprocal eigenvalues gives the stated A_n and C_n. On substituting y=B/[m(Pt+2Q)], the derivative is PA_n+C_n(P−4Q)/(2t+1)^2. It is positive for P≥4Q; otherwise it increases strictly to a positive limit. This gives the positive root or the unique boundary minimizer, including equality at 4C_n/(A_n+C_n). As a boundary cross-check, at x=0,y=1 the squared norm of L⁺ applied to an original-edge difference is 2(n+2)/n², obtained by eliminating the new-vertex coordinates. This agrees with the derivative of the trace formula per original edge. The cutoff reduces to n²−7n−6>0 at equal prices, equivalent to n≥8 for these integer sizes, and the exact ratio satisfies nr_c(n)→8. The supplied rational checker was read but not executed.

## originality

PASS

The supported distinct content is the two-priced, topology-specific optimizer and its sharp support frontier on T(K_n), not general Kirchhoff-index design, strict convexity, or an unweighted graph index formula. The strongest inspected exact-topology and priced-transition comparisons do not supply that frontier or mechanically imply it.

## value

PASS

This is an exact design decision for a standard graph transformation and a physical all-pairs objective. It identifies when all direct clique connections are useless even at equal edge prices, without disconnecting the network, and quantifies the transition on the 1/n price-ratio scale. The unrestricted optimizer, its support, and unique behavior at the exact threshold are useful beyond computing an index at a fixed allocation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
