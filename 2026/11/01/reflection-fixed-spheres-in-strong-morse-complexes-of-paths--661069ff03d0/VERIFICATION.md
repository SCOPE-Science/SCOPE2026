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

# Reproducibility and scope

The mathematical conclusion is an all-parameter theorem proved in `RESULT.md`; finite computation is a supplementary check, not an infinite proof or an independent audit.

Execute `python3 verify.py` with Python 3 and its standard library in the same directory. A successful run prints `VERIFY_OK` after four groups of assertions:

1. Exhaustive reconstruction from all strict vertex permutations of the original gradient algorithm for path edge counts 1 through 8, compared with fixed-orbit graph independence faces (409,112 permutations total).
2. Independent enumeration of all comparator-consistent orientation words for path edge counts 2 through 12 (797,157 ternary words), followed by a second geometric-fixed-face comparison.
3. Direct graph-isomorphism checks of the closed-neighborhood removal recurrence for graph indices 3 through 30.
4. Exact bitset Gaussian elimination over the two-element field for reduced homology of the orbit graphs with indices 1 through 7, compared with the stated sphere/contractible pattern.

The proof of comparator sufficiency depends on the absence of cycles in the path's comparison constraints. The graph recurrence and its explicit vertex bijection are written out in the proof, not inferred from samples. The finite checks do not establish uniqueness among unindexed published findings. No independent mathematical verification has been carried out.
