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

For the real six-vertex weighted cycle w=(1,2,2,2,2,2), Lipschitz dual ball equals zero-sum weighted-edge increment section. Every dual vertex has at least five edge constraints saturated and comes from fixing five signs; exactly 60 vertices. The primal ball has exactly 12 signed normalized edge molecules, each exposed because its edge is strictly shorter than its complementary path. The finite extreme-pair numerical-radius principle reduces operator norm to 360 unique rank-one tensors and numerical radius to 150 norming-contact tensors. FROZEN actual `c6_exact_certificate.json` (Git blob 588e48168e1d6266873c94c2bf63ea16373f7cb2) and `c6_verify_exact.py` (blob 715f609c54b818c4eff2196d10e4c3d47b5cecfe) were inspected. Independent custom exact BigInt rational reconstruction regenerated all 60 dual,12 primal,150 contacts,360 norm tensors; equality with stored full sets held, all 360 certificate rational linear decompositions matched coordinatewise with ℓ1 coefficient sums ≤17/14 (zero failures), and the explicit 5x5 witness had v(T)=1 and ||T||=17/14. This is mathematically exhaustive because the vertex enumeration and reduction are proved, not a sample. Thus n(X)=14/17 exactly.

## originality

PASS

Existing general indexed result for arbitrary positive weighted cycles determines numerical-index-one threshold only; it explicitly does not determine subunit numerical indices. The unit-edge parity law gives n=1 for uniform even six cycles, but cannot imply a rational 14/17 after shortening one edge. Cobollo et al classify three-point free spaces and establish reduction principle, not this five-dimensional exact invariant. Exact certificate supplies a new benchmark for first simple higher even weighted cycle despite possibility of an unindexed old rational table.

## value

PASS

The single shortened edge of the smallest higher even cycle is a natural new benchmark: its unweighted even counterpart has index 1, while positivity rigidity guarantees only strict <1 for nonuniform weights. Determining exact 14/17, with exhaustive reusable rational certificate and sharp witness, quantifies the first nonuniform five-dimensional test case. A natural exact invariant is independently useful even without the full weighted-cycle census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
