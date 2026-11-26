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

A shortest path between vertices of one factor never leaves it, since leaving and returning would repeat the articulation. Between factors every shortest path goes through the root and consists of two factor geodesics. Thus rooted convex sets glue freely, and any nonempty unrooted convex set lies in one factor. For a root-free support meeting two or more factors, each nonempty local trace can be tested together with a positive vertex of another factor, forcing a rooted hypothesis; the empty local trace is realized by the root alone. Conversely the rooted factor witnesses glue to realize every trace. A support containing the root and meeting two factors elsewhere fails the trace with two cross-factor positives and the root negative. Single-factor supports are shattered exactly in their factor. Hence the product counts exactly the root-free supports coming from the rooted factors, the differences add the remaining single-factor supports, and the only duplicate is the singleton root, counted t times. Taking the maximum of the achievable product and single-factor sizes proves the dimension law, including trivial factors. On a cycle a rooted shattered pair chooses one nonantipodal vertex per side; same-side or antipodal pairs cannot be shattered. An unrooted triple is shattered precisely when each gap is strictly less than half the circumference; a gap at least half gives a shortest path through the third point, including the equality case. Among four cyclic points some pair of consecutive gaps totals at most half, ruling out every four-point support. Inclusion-exclusion of the upper gap bounds yields the two stated T_m formulas. All single-factor cycle corrections have degree at most three, so only the product contributes at degree 2t when t>=2, with coefficient the product of h_i^2.

## originality

PASS

Pass is for the rooted articulation polynomial, the associated dimension law, and the heterogeneous cycle-bouquet polynomial and maximum-support counts. A distinct same-date indexed record covers the unrooted cycle profile exactly; that ingredient receives no originality credit, and the indexed date alone does not order the results. The strongest inspected hull and bouquet results do not give the rooted identity or the bouquet census.

## value

PASS

Cut vertices give a natural decomposition for geodesic convexity, but a scalar VC bound alone does not determine how supports spanning factors are counted. The rooted law locates that missing constraint and gives an exact computation from strictly smaller graphs. For heterogeneous cycle bouquets it explains why dimension is independent of cycle length while extremal multiplicities depend sharply on the lengths. The useful new content is the gluing structure and the resulting bouquet census, not a repeat of the unrooted single-cycle numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
