---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The concept domain is path vertices and hypotheses are all inclusion-minimal dominating sets, not only minimum-cardinality sets. Reconstructed the private-neighbor criterion, independently enumerated all masks and computed VC dimension through all shattering trace projections and Littlestone dimension by exact adaptive-split recurrence for n=1..11. Values for n=1..10 coincide, and n=11 has exactly 36 hypotheses, VCdim=4, Ldim=5. Independently decoded the actual attached certificates.json blob da3a9118dd7a49cfa5a26c3076b26f04920deb91: all 16 labels on zero-based {0,2,7,9} have valid minimal-dominator witnesses, and all 31 query nodes and 32 distinct leaves of the depth-five decision tree satisfy their path labels and minimal domination; checks returned no errors. All 462 possible 5-query subsets fail shattering, while 36<64 excludes depth six. For disjoint copies of P11, minimal dominating concept class is a product; VCdim and Ldim add on disjoint domains by trace/product and the standard minimax split induction, hence VC=4s,Ldim=5s for all positive s. Finite enumeration is exact for its bounded cases; the product lemma supplies the infinite extension.

## originality

PASS

Best-of-knowledge PASS for the natural first connected-path VC/Littlestone separation threshold and its disjoint-union amplification. Compared full primary papers: Mofidi studies dominating-set reconfiguration geometry and product components; Guingona et al prove equality for zero sets of linear combinations, whose hypotheses are not the path minimal-dominator membership class. Mary studies VC properties of the input hypergraph for transversal enumeration, not adaptivity of all minimal transversals. A published SCOPE matching-edge example is a different incidence family and does not imply the present values. Older tabulations of learning dimensions for minimal transversals remain a risk.

## value

PASS

PASS because inclusion-minimal dominating sets are a canonical combinatorial solution class, and static versus adaptive membership shattering are mathematically distinct learning dimensions. The smallest separating path P11 is a well-motivated exact finite cutoff, not an arbitrary slice, and the disjoint-union product yields an unbounded linear separation inside forests of degree at most two. The result does not need a general formula for larger connected paths to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
