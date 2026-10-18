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

## Reproducible checks
`python3 verify_heawood.py` constructs the seven Fano lines, the Heawood incidence graph and all 336 induced edge permutations, then directly evaluates the alternating sum over invariant forest unions for every automorphism. The exact expected multiplicity/trace table is asserted, as are 14 full-group invariants, 18 subgroup invariants and four negative duality directions within that subgroup-fixed space.

`g++ -std=c++17 -O2 heawood_forest_crosscheck.cpp -o heawood_check && ./heawood_check` independently scans every one of the 2,097,152 edge masks, counts 1,469,920 forests and computes the eight representative alternating signed fixed-forest traces. Both programs were executed from the actual source files supplied here.

The topological deduction uses the published theorem that matroid independence complexes are shellable; finite enumeration verifies the Heawood-specific traces, not that general theorem. The literature overlap comparison is reasoned but cannot establish the absence of unindexed equivalent results. No independent audit was performed.
