---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Checked the exact distance taxonomy for original vertices u∈U,v∈V and subdivision vertices e_ij: original same-part distance4, opposite-part distance2; midpoints distance2 iff their edges share an endpoint, else distance4; every original-to-midpoint distance1 or3. Hence the scale3 threshold graph is EXACTLY K_{m,n} joined with the rook graph L(K_{m,n}), and its clique complex is the simplicial join. The row/column maximal-simplex cover of the rook clique complex has contractible nonempty intersections and nerve K_{m,n}, so each factor is wedge^b S1; their join is wedge^{b²} S3 integrally. At scale2 Adamaszek Theorem 5.1 and the explicit triangle-free total-graph collapse identify the subdivided 1-cycle lattice with K_{m,n}; this proves the persistence isomorphism, not just equal ranks. At scale4 all vertex distances ≤4. Independently computed all-pairs graph distances and basic ranks for (m,n)=(2,2),(2,3),(3,3),(3,4),(4,5); exact symbolic taxonomy covers all parameters.

## originality

PASS

Best-of-knowledge originality after comparing implications of inspected foundational primary literature and closely related published results. Prior components are explicitly credited; the complete asserted added representation, character, filtration, or signed trace is not supplied by the checked stronger objects. This is not an absolute priority guarantee.

## value

PASS

The natural vertex-metric graph filtration has an exact dimension jump from b persistent circles to b² three-spheres while leaving integral H1 unchanged at radius2. The all-parameter barcode and exact scale3 join are intrinsically useful in graph metric topology and persistent homology; this is not merely recomputing a known square graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
