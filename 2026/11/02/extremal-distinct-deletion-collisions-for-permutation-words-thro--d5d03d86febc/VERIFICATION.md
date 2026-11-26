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

Each inverse insertion (choose a missing value, lift child values, insert at a chosen position) produces a parent, and every deletion witness is obtained this way. Deduplication within each child bucket ensures each unordered pair receives one increment per distinct shared child. Thus the positive counters are exactly the desired intersection sizes, and omitted zero-overlap pairs cannot maximize. An independently written exact enumerator reproduced both incidence maps, all histograms, maxima (2,4,4,4,4,4), counts (6,1,4,18,96,600) and set equality of the entire extremal set with the proposed construction for n=4,...,8. The n=8 histogram for positive intersections of sizes 1,2,3,4 is (5521776,324432,320,600). For n=3, the four nonmonotone permutations have both children, giving six pairs. The four deletions in each block give the same four different local patterns. Contiguity in position preserves the outside pattern and consecutive block values leave each outside letter below or above the entire block, so the agreement extends to four different global children for all n>=4. All four block positions change and all other entries coincide, so the differing interval and value range are recoverable; counting the block as one atom gives (n-3)(n-3)!. This is no upper bound or classification past n=8. The frozen verify.py was inspected only. Independent replay: /workspace/branches/948953eb-8454-4d5c-9704-101c109a7983/independent_check.py (Python 3.12.3, NumPy 2.5.3; accepts --min-n and --max-n); the retained independent_check_n3-8.jsonl and independent_check_notes.md in that directory give the exact counts, set comparisons and recorded runs. Pair keys are exact uint32 with two 16-bit lexicographic IDs, safe since 8! < 2^16.

## originality

PASS

The supported distinction is the finite distinct-shadow extremal profile and complete equality sets, chiefly the n=7 and n=8 results. Earlier multiset extrema substantially overlap in small orders; neither the known 2413/3142 collision nor those overlapping small-order upper bounds are credited as new. At n=7 and n=8 the prior multiset bound is five, whereas the distinct bound is four. The multiset-maximal pair table does not classify all pairs with four distinct common children; the distinct optimum and its equality set require additional work. No exact distinct-shadow match was found in the bounded comparisons.

## value

PASS

Distinct possible standardized channel outputs, rather than deletion-position multiplicities, parameterize worst-case ambiguity in reconstruction from different received words. The finite range directly resolves the distinct analogue of a published length-eight multiset census, including its first two lengths where the multiset cap of five is not sharp. The exhaustive equality sets isolate a structural local obstruction rather than only reporting six numbers; the result gives a precise finite baseline for testing larger-length bounds. The scope does not assert an eventual cutoff or an all-length upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
