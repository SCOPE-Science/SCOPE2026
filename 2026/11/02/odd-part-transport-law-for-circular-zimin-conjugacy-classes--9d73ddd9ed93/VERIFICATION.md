---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the circular conjugacy transport theorem

The proof in `RESULT.md` is self-contained. Its decisive steps are the exact partition by the unique new symbol, the valuation criterion for equality of adjacent new-symbol representatives, and the sampled-position argument proving different blocks are pairwise inequivalent. The latter is necessary: inequality of adjacent words alone would not establish global distinctness.

The standalone `checker.py` uses ordinary Python 3. It generates literal Zimin words of ranks two through seven; for each admissible window length, it enumerates every circular window and then every rotation, taking the lexicographically least rotation as its class representative. It independently constructs new-symbol candidates and compares the literal sets of old, new, and current classes, checks class disjointness and the exact odd-part increment, and confirms the proposed partition of the new-symbol windows. All cases tested passed; a total of 10,548 indexed circular starts were enumerated.

Run `python checker.py`. The finite checks are not a proof for all ranks. The unrestricted theorem is derived symbolically in `RESULT.md`. No external validation or independent audit is asserted.
