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

For each pattern, applying a letter map sums the exact occurrence counts of its preimages since admissible position tuples are independent of the labels. A disagreement survives a map assigning its two symbols distinct labels. If a third symbol is present, preserve it as a third label; that would give a genuinely three-symbol ternary collision. The independently reproduced census excludes this and establishes the stated exact binary pairs and binary injectivity for lengths 3 through 12. At length 13 the exhaustive run finds 8188 distinct binary decks among 8192 words and 1594311 distinct ternary decks among 1594323 words. The only nonsingletons are four and twelve doubletons, respectively, and the ternary pairs are exactly the unordered two-letter embeddings of the binary pairs. Replay with Python 3 and NumPy using evidence/1/owned_deck_census.py; the exact class output is evidence/1/full_census.txt. The reproduction decodes all words by base-q digits, enumerates each allowed tuple and groups full fixed-width byte keys, not hashes; each count fits in one byte since it is bounded by max(13,66,165), and every repeated fiber was required to have size two. The frozen C++ and supplementary Python code were inspected, not executed. The four binary pairs are closed under swapping labels, and every endpoint uses both symbols, so arbitrary-q collisions form a matching with four disjoint edges per support pair. Choosing all isolated vertices and one endpoint per edge proves both codebook formulas. The lower lengths follow by binary projection at a disagreement. Literal length 2 is degenerate (01 and 10 collide), excluded explicitly by the frozen Finding.

## originality

PASS

Pass is for the first nondegenerate arbitrary-alphabet classification and exact labeled maximum-codebook count, not the known binary threshold, the exhibited example, or a claim to priority for the four binary pairs. The ternary-support exclusion is an additional finite mathematical fact, and the aggregation argument transfers it to all finite alphabet sizes.

## value

PASS

This determines every confusion at the first nondegenerate collision length, including the new exclusion of genuine three-symbol support, and gives the exact reconstruction-code optimum and number of labeled optimizers for any alphabet size. The first finite cutoff is a natural one fixed by the binary threshold; the exhaustive ternary check supplies a structural conclusion that is then uniform in the alphabet rather than a standalone tally for an arbitrary parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
