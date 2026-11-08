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

The finite nonperiodic n×n knight attack graph has row-column squares and |Δrow|,|Δcol|=(1,2); Ind consists of all nonattacking sets, not just maximal placements. At n<=2 no edges, and at n=3 the center is isolated, so all these complexes are contractible. Independently regenerated both exhaustive face sets for n=4,5 (1,365 and 55,213 augmented faces), the source-specified maximal-toggle sequential Morse matchings (680 and 27,605 pairs), and all 5,788/353,749 Hasse cover orientations; both are acyclic. Removing the augmented empty-face pair leaves a single 0-cell and respectively five/three critical 3-cells, proving the integral S3 wedges. Signed fixed-face Lefschetz sums for all 8 geometric square symmetries independently yield characters (5,-1,1,-1,3,3,-1,-1) and (3,1,-1,1,-1,-1,-1,-1); direct inner products give A1+2B1+E and A2+E. The unverified larger boards and equivariant homotopy type are not inferred.

## originality

PASS

Direct comparison of distinct graph/complex or fixed-locus objects and their known implications: First noncontractible square-knight complexes and a dihedral homology transition. Inspected sources and Resultary searches below support a best-of-knowledge novelty finding, not a worldwide priority guarantee.

## value

PASS

The knight graph is a canonical non-grid move graph, and the exact first noncontractible square board size and contrasting D4 third-homology representations resolve natural structural questions about its entire independence complex. The claimed representation transition is not implied by the known maximum knight count, and complete finite classifications through a meaningful first topological threshold have independent use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
