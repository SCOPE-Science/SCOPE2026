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
# Exact reproducibility checks

Run `python3 verify.py` with an ordinary Python 3 interpreter. All arithmetic is integer-exact and no external packages are needed. The script computes the halving counts using a generalized algebraic recurrence, separately counts chains by direct halving backtracking, and enumerates every hyperbinary expansion and every eligible cut for small representative cases. It compares all three algorithms and the proposed binary run count.

Executed output from the program embedded in this finding:

```text
BINARY_ZERO_EXACT_OK checked_odd_inputs 1365 deficit_histogram {1: 12, 2: 198, 3: 660, 4: 495}
DIRECT_HALVING_OK inputs 384
INDEPENDENT_HYPERBINARY_CUT_OK inputs 35 expansions_examined 750
EXAMPLE 17 a 4 stern 5 deficit 1 ones_runs 1
EXAMPLE 35 a 7 stern 9 deficit 2 ones_runs 2
EXAMPLE 75 a 15 stern 18 deficit 3 ones_runs 3
EXAMPLE 171 a 30 stern 34 deficit 4 ones_runs 4
VERIFY_OK exact=True independent_methods=3 finite_only=True
```

**Limits.** These are finite checks only. The unrestricted digit theorem is established by the complete carrying and admissible-cut argument in RESULT.md; no computational search proves its infinite scope or historical novelty. Independent audit has not been performed.
