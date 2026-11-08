---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the explicitly defined 24-vertex LCF([-12,7,-7]^8) graph, forming the integral 23x23 reduced Laplacian and computing its Smith invariants gives exactly nineteen unit factors followed by 11,44,132,2640; these divide successively and multiply to 168,664,320. The package supplies 471 individual unimodular row/column operations in certificate.json, with complete diagonal [1]*19+[11,44,132,2640], and separately a prime-power valuation check. I reconstructed its LCF adjacency/Laplacian independently and computed the exact Smith normal form directly with SymPy, obtaining the same four nonunit factors and determinant; this is a complete finite calculation for the specified graph, not an inference from its eigenvalues or spanning-tree count. The 2,3,5,11 primary exponents recombine to that invariant-factor chain.

## originality

PASS

The exact Smith invariant factors, not the known 24-vertex cage, known LCF, 1960 girth extremum or existing spanning-tree count, form the candidate contribution. No equivalent published invariant-factor statement was identified among searched literature and known graph database entries; an unindexed table remains plausible.

## value

PASS

The McGee graph is the canonical unique (3,7) cubic cage. Its integral graph Jacobian (sandpile group), minimal number of generators, exponent, and 11-primary structure are natural exact invariants of the graph, sharper than the known spanning-tree count; exact values are relevant for chip-firing and integral lattice comparisons. This is a motivated, reproducible single-graph classification, not an inflated claim about all cages or a mere known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
