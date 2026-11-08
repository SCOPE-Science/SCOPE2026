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

The exact weak-composition universe has 715 and 1001 vectors, respectively; every received (n-1)-multiset is a 5-parent clique and a pair conflicts precisely under one unit transfer. Independent exact enumeration reproduced 495 and 715 shadows, 4950 and 7150 distinct pair-conflicts and valid syndrome-zero codewords of sizes 143 and 201. Four supplied *complete*, not sampled, MIP models in actual verification/ programs explicitly implement binary constraints and zero integrality gap, with source-recorded HiGHS dual upper bounds 143 and 201 below the next integer. The independently reconstructed n=10 MIP also returned primal=dual=201 and zero gap; a new n=9 solver rerun timed out, not treated as negative evidence. Thus the numerical upper bound is conditional on trusted HiGHS branch-and-bound semantics, not a standalone rational certificate. It is not extrapolated beyond n=10.

## originality

PASS

The published five-symbol n<=8 exact table and Conjecture 21 identify n=9 and 10 as first unresolved lengths. The syndrome construction, exact formulation and generic deletion-ball bounds are prior art; the computed sharp upper bounds are the assessed addition, without an all-n theorem.

## value

PASS

It settles two immediately adjacent, explicitly motivated finite instances of a published five-symbol multiset-deletion conjecture, identifying exact code capacities and sharp optimal constructions. They are not arbitrary tiny examples: they extend the published complete finite table in the first uncovered cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
