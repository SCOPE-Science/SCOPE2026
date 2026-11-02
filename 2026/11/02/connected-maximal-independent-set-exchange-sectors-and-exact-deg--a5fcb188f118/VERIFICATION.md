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

# Computational verification and limits

The theorem is proved symbolically in `RESULT.md`. For a finite cross-check, `verify_subsets.py` enumerates every binary subset of each cycle with \(4\le n\le18\), checks independence and domination directly, then considers every possible deletion/insertion pair. It asserts that every legal jump is an adjacent slide, compares the full degree distribution and edge totals, and explicitly traverses all connected components. `verify_gaps.cpp` independently generates circular two/three-gap arrangements for \(4\le n\le22\), constructs actual slide neighbors using bit masks, and independently traverses components.

Reproduction commands: `python3 verify_subsets.py` and `g++ -O2 -std=c++17 verify_gaps.cpp -o verify_gaps && ./verify_gaps`. Successful completion prints `DIRECT_SUBSET_ENUMERATION_PASS` and `INDEPENDENT_GAP_ENUMERATION_PASS`, respectively.

These bounded tests cover all configurations at the specified sizes but are not proofs of the infinite claims. The proof derives legal moves, connectivity, degree classes, and all asserted formulas for every integer \(n\ge4\). Literature comparisons remain nonexhaustive. An independent audit has not been performed.
