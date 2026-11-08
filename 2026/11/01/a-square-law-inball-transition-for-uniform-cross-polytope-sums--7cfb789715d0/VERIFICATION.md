---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. For n>=k>=3 and the unweighted complete k-uniform rank layer, reconstruct support h(u)=sum_{j=k}^n C(j-1,k-1)a_j for sorted absolute coordinates, hence the full signed-subset halfspace system sum_{i in J}epsilon_i x_i<=B_j with B_j=C(n,k)-C(n-j,k). Centered insphere distance is min_j B_j/sqrt(j). The binomial increment sequence A_j=C(n-j-1,k-1) is nonincreasing and log-concave, and the proved ratio argument makes S_j/sqrt(j) first increase then decrease, hence the minimum is at j=1 or j=n. Strict intermediate inequalities follow from the strict last decrease, and when n>=k^2 from the strict first increase. Endpoint distances are C(n-1,k-1) and sqrt(n)/k times this number; equality is exactly n=k^2. Full-dimensional exposed sign simplices and coordinate facets justify counts 2^n,2^n+2n,2n; opposite active normals spanning R^n force unique center zero. For k=n recover the usual cross-polytope. The inspected integer verifier tests n<=150 only as corroboration, not as infinite proof.

## originality

PASS

PASS on accessible best-of-knowledge evidence. General coordinate-cross-polytope support and facet inequalities are substantially prior (Wang et al Proposition 3.5); the claimed increment is the evaluated Euclidean distance minimum, exact n=k^2 phase boundary, uniqueness and tangent *facet* counts for all n>=k>=3. Related type-B/signed permutohedra and other inball phases concern broader frameworks or different polytope families and do not logically determine these values. Full Wang article was unavailable in this session; only abstract, metadata and technical accessible overview were inspected, so explicit previously unstated distance corollaries remain a material priority risk.

## value

PASS

PASS. The complete rank-k hypergraph is a canonical infinite class of Minkowski sums; Euclidean inradius and its contact face orbits are intrinsic invariants. The precise k^2 threshold switches the contact count between exponentially many sign facets and 2n coordinate facets, a structural phase classification not a tiny arithmetic gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
