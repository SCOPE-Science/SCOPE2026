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

# Verification of the four-letter classification

Run `python3 verify.py` with standard-library Python 3. Expected final line: `VERIFY_OK`. This source is complete and has no external inputs or dependencies.

The reproducible process independently recomputes every element of the finite domain and its proper prefix–suffix comparisons. It checks all 256 words, 180 individually admissible words, 56 internally compatible reverse-complement orbits (12 singleton, 44 paired), and 540 undirected graph edges. An exact weighted-clique dynamic recurrence over 398 distinct reachable masks gives weight 17 with 32 achieving cliques; these are reconstructed as 32 codebooks and each word-pair constraint is checked directly. It verifies the exact singleton/doubleton profile and the four orbits of eight under the eight Watson–Crick-preserving alphabet permutations.

An independent weighted branch-and-bound with a greedy stable-set coloring upper bound returns the same optimum and equality count after 293 calls. This is a second exhaustive algorithm using the same explicitly described finite graph. The mathematical recurrence and graph–code equivalence are justified in `RESULT.md`.

The verification proves the finite claimed combinatorial result, not novelty, extrapolation to larger lengths, physical functionality or an independently conducted audit. Sources are cited in `RESULT.md`; `REVIEW.md` discusses originality limits.
