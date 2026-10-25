---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Bridge-cut subgroup obstruction forbids a once-used edge; minimal 2|E| full-support identity words therefore use every edge twice. For a locally noncrossing double-occurrence word, cancellation of the closest complete pair inside any contiguous factor removes only a transposition commuting with all intervening ones; iterating leaves pairwise distinct forest edges. Their product merges precisely the forest components, proving the fixed-vertex parity lemma. Leaf-edge deletion and this lemma prove the iff statement by induction, with leaf and one-edge boundaries checked. Independent enumerator checked exactly 7,740 complete double-occurrence words on five explicit path/star/branching trees (3 or 4 edges): permutation identity agreed with incident-pair nonalternation on each. This does not replace the all-tree induction.

## originality

PASS

The exact criterion is explicitly stated as Conjecture 1(iii) in Shapiro arXiv:2610.14373v1, rather than proved there. The present all-tree leaf induction supplies the missing direction beyond the previously known star/Catalan counting and enumerated <=5-edge instances. Checked support-factorization work is related but did not establish this iff statement in material read.

## value

PASS

The criterion resolves a specifically posed all-tree genus-zero factorization conjecture with a local decision procedure. It is a natural structural description of minimal transitive identity words, not an arbitrary finite instance or a recasting of known star counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
