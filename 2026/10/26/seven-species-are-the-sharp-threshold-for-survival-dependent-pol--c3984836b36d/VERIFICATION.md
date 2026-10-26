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

# Verification of the finite classification

The accompanying `verify.py` is a standalone Python 3 program using only the standard library. It is run with `python3 -S verify.py`; its stdout is one sorted JSON object matching `certificate.json` byte for byte, followed by a newline.

The program visits all possible bipartite adjacency matrices of every plant/pollinator split with two through seven total species, filters each for connectivity and absence of isolated vertices, and stores counts by split. The analytical lemma proves uniform optimality whenever the plant guild has at most three species or the pollinator guild has at most two. In the sole remaining seven-species split (four plants and three pollinators), the program calculates each protection-benefit polynomial and exactly compares every pair by checking nonnegativity of a quadratic over the entire closed unit interval. It enumerates all pollinator permutations and unordered plant rows to compute guild-preserving canonical classes.

The independently calculated expected surviving-plant counts from enumerating pollinator survival states at \(q=1/4\) and \(q=3/4\) agree with the separately derived gain formula for both exceptional classes. These checks give opposite best targets on the two sides of \(q=1/2\).

**Verified output:** \(1795\) connected labeled \(4\times3\) graphs; \(108\) without a universal optimal protected pollinator; two exceptional classes with \(72\) and \(36\) labeled realizations. The exact all-\(q\) threshold is proved algebraically in `RESULT.md`. No sampling or floating-point root finder supplies the universal inequalities. The computation is a complete finite census for the specified range, not a claim of exhaustive classification on larger networks.
