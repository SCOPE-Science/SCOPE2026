---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently enumerated connected chordal graphs at each order from the singleton, adjoining a vertex with a nonempty clique neighbourhood. This obviously preserves connectedness and rules out new induced cycles of length ≥4. Conversely a simplicial vertex exists by perfect elimination; deleting one preserves chordality, and paths between surviving vertices can bypass it using an edge of its neighbour clique. I deduplicated by exact canonical adjacency encodings over invariant degree blocks, without the source atlas or hash. The counts are 1,1,2,5,15,58,272,1614; there are 7268 attachments before deduplication at order eight. Joint refinement by exact previous-colour and neighbour-multiset tuples, continuing until the colour partition stops splitting, yielded the same counts of classes through seven and 1612 classes at eight, with nontrivial class sizes 2,2. The order-eight exceptions have 13 and 14 edges. Their degree-cell sizes and quotient rows match the finding: (4,2,2) with rows (0,1,1),(2,0,2),(2,2,1), and (4,4) with rows (0,2),(2,3). The two graphs within each pair have 2 versus 4 distinct degree-two open neighbourhoods, confirming the stated nonisomorphism and agreeing with the doubled-matching versus cycle constructions. The source verifier checks equitability and prints the matrices; the independent replay checks their actual numerical values. The result is restricted to competitors that are themselves connected chordal graphs.

## originality

PASS

Earlier inspected sources supply ordinary 1-WL/C² equivalence, structural recognition of amenable graphs, and the chordal object counts, not the first connected-chordal collision census. The strongest substantive match is the later November 8 Resultary result for all chordal graphs, which gives these very two pairs and subsumes the frozen connected version. This is demonstrable equivalent coverage on the connected subdomain, not evidence of earlier priority; the frozen publication_date is October 18 and the inspected matching catalog record is later-dated. The later result alludes to earlier witness identifications without an identified external source; independent priority for the witnesses is not certified. The supported distinct contribution relative to the earlier sources is the minimality and complete first layer in the connected chordal class.

## value

PASS

Chordal graphs form a natural graph class and ordinary refinement is a standard structural invariant. This establishes the first loss of separation in that class and describes every minimal exception, not just one computational example. The explicit quotient profiles and pair shapes give minimal benchmarks and separate this relative threshold from global amenability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
