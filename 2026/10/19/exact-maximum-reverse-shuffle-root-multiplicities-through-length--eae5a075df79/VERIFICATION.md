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
# Verification and reproducibility

All checks described below were executed from the accompanying standalone files; no external datasets are required.

Compile `enumerate.cpp` as described in `RESULT.md`. Run the binary with each argument from `1` to `10`. The exact output for those ten runs is embedded in `profile.txt`. The code enumerates every fixed-weight position mask and every candidate root, constructs the unique reverse interleaving, deduplicates roots with bitsets, and scans all resulting word indices. For \(n=10\) its exhaustive count is \(189,190,144\) processed root--mask pairs, \(184,756\) admissible position masks, \(1,048,576\) inspected source indices, with maximum \(170\) and exactly eight maximizers.

Run `python verify_small.py` to enumerate every source word and each possible partition **in the opposite direction** for \(n=1,\ldots,6\). It agrees with the independent exhaustive maxima and optimizer counts. Run `python verify_witnesses.py` in the directory containing `witnesses_n10.tsv`; every listed position mask selects the corresponding distinct root and leaves its reversal at the remaining positions. There are exactly \(170\) distinct checked certificates.

A separate coverage cross-check uses the known binary abelian-square characterization: the number of words with at least one reverse-shuffle root is exactly \(\binom{2n}{n}\). This independently checks the enumerated nonempty-word count for all ten sizes. The program's source and resulting profile are part of this package; no external proof solver or opaque data source is required.

**Limits:** Exhaustive checks prove only the ten stated finite cases. The stand-alone witness list proves the lower bound at \(n=10\), not maximality without `enumerate.cpp`. Direct-word independent enumeration goes through \(n=6\); for \(n=7\) through \(10\), exhaustive maximality comes from the complete C++ search plus the separate coverage and witness checks. No independent audit has been performed.
