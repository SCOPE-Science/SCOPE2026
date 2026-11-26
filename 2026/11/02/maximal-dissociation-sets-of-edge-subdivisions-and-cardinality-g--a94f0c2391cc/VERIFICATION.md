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

With selected originals A and omitted originals C, edge-nodes inside A are impossible (induced degree two), and all edge-nodes inside C must be selected since otherwise they could be added as isolated vertices. Each chosen original with a neighbor in C needs exactly one chosen crossing edge-node, by addability and the degree bound. An omitted original is blocked exactly when it has at least two selected C–C edge-nodes or has a selected crossing neighbor that would acquire a second endpoint. This is precisely the required image condition at degrees zero and one. The same obstructions prove the converse and the exponents, with empty domains and isolated originals handled. In the biclique, omission counts s,t yield independent shore maps; when a target shore is nonempty, it must be hit surjectively iff its vertices have omitted-induced degree at most one. For a=2, s=0 contributes (1+b(b−1))z^(b+2)+bz^(b+3), s=1 contributes (2+2b)z^(2b+1), and s=2 contributes [2^b−2+b(2^(b−1)−2)+sum_{t=2}^b binom(b,t)2^(b−t)]z^(2b). This proves the claimed four-term expression with addition at coincident exponents. At b≥5 all four coefficients are positive and their exponents strictly increase, giving the stated gap; summing gives 3^b+b²+1. The graph is connected and bipartite, with subdivision vertices of degree two and independent originals, so is 2-degenerate. Independent replay: python3 /workspace/branches/14513289-c07e-48dd-bed6-0acccec146b8/independent_check.py --full (75 labeled base graphs through order four, nine small bicliques, and direct K_(2,b) through b=6); K_(2,6) yielded {8:31,9:6,12:715,13:14}. The finite sets of maximal masks were checked against the structural construction. The supplied successful-output record is distinct evidence, not the basis for the present all-order proof.

## originality

PASS

The closest same-family catalogue statements enumerate maximal induced matchings or maximal independent sets. The closest same-set catalogue statement treats deleting a matching from a biclique, not subdividing the biclique. The inspected literature and catalogue results do not supply the selected-original/crossing-edge bijection or its precise cardinality support for this family. This is a best-of-available-evidence distinction, not a publication-priority conclusion.

## value

PASS

The bijection gives an explicit structural enumeration on every one-fold subdivision and a genuine closed form on bicliques. The four degrees isolate an unbounded internal gap for connected bipartite 2-degenerate graphs, a meaningful sparsity constraint; it is not just a total-count improvement or a re-encoding of another type of maximal set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
