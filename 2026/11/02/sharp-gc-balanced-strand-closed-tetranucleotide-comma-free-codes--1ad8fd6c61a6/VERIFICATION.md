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

The balanced universe has choose(4,2)·2⁴=96 words; a fixed reverse complement is determined by its first two letters, exactly one of which is from the GC pair, giving eight fixed words and 52 orbits. Closure is exactly taking unions of these orbits. Forbidden orbit supports encode every off-frame substring of two concatenated words, including repeated words/orbits, and every distinct pair below the distance cut. I independently regenerated the constraints from the word definitions and ran an exact binary include/exclude search without a prescribed target size. At inclusion it removes conflict pairs and completions of forbidden triples with a previously selected vertex. Its bound partitions remaining vertices into cliques of pairwise conflict, summing maximal clique weights; it discards only branches strictly below the current best, preserving all ties. It recovered maximum sizes 21,17,7; labeled counts 136,16,72; fixed counts 3,1,1 in every maximizer; and 17,2,9 symmetry classes, each of size eight. Distance-ordered forbidden-support totals were 4668,4732,5174 and independent search visits were 5565,2717,673. Every complete maximizing inventory matches the frozen JSON word for word. Complement-commuting letter permutations exchange/flip the two complementary pairs; exchanging them preserves exact half composition, and the whole action preserves Hamming and comma constraints. In known frames, a single substitution is detectable at distance two and correctable at distance three by disjoint radius-one balls; no corrupted-frame synchronization follows.

## originality

PASS

Inspected prior sources establish unrestricted comma-free variants, constant-GC packing with reverse-complement separation, or proper-overlap/closed Hamming variants. None inspected gives or mechanically implies the three-way exact constrained maximum or classification. This is a bounded literature judgment, not a priority certification.

## value

PASS

A balanced uncorrupted quaternary frame presents a natural smallest case to ask about both strand closure and compatibility with substitutions. The complete exact frontier quantifies the cardinality cost of known-frame single-error detection and correction under the same synchronization rule. Counting every optimizer and checking the symmetry stabilizers make the result more than a single feasible construction or an arbitrary numerical sample and supply a reusable benchmark for other finite code constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
