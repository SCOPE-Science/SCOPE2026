---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A rank7 b omits exactly one output, so unique cyclic conjugacy normalizes its image to {1,...,7}; choose repeated output (7), preimage pair C(8,2), bijection of remaining six outputs 6! for exactly 141120 cases without duplication. BFS from full 8-bit set on subset transitions induced by rotation and b gives exact shortest word or non-synchronizing (at most 255 nonempty subsets); no search length cutoff. In this run an independently written C++ complete generator/BFS visited all 141120 normalized cases and matched all 32 bins in repository spectrum.csv, including rare thresholds and no missing values. The 1856 nonsync count equals 1728 mod2 +192 mod4−64 overlap, consistent with primitive/defect-one theorem. This is an exhaustive finite proof for this precise family, not a claim about all binary automata.

## originality

PASS

Černý extremal 49, general rotation-letter synchronization criteria, and the congruence/non-sync principle are prior work; they do not imply exact conditional 8-state histogram. Previous small automata exhaustive tables cited by de Bondt–Don–Zantema top out at smaller n and compare different sampling spaces. Exact 32-bin 8-state rank7 count not located, but unindexed computer tables remain a concrete priority risk.

## value

PASS

A full exact conditional distribution of shortest reset lengths for a canonical constrained eight-state automaton family quantifies rarity of extremal cases (exactly one at 49) and all intermediate thresholds, useful to synchronizing-automata classification and algorithm benchmarking. It is a natural complete finite class rather than an arbitrary slice chosen after computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
