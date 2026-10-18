---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Every binary rank-at-most-four fooling-set matrix admits M=UV^T with u_i,v_i in F_2^4 and u_i dot v_i=1. There are exactly (2^4-1)2^3=120 admissible ordered types. Pairwise fooling compatibility is exactly an edge of the associated graph; repetitions are impossible, so the matrix optimum is its clique number. An independent exact Python reconstruction generated all 120 types, 5040 compatible edges, and used a valid greedy-color branch-and-bound proof to obtain maximum clique 11 (12096 visited branch nodes). Independent elimination confirmed the displayed 11-by-11 witness has rank four, all diagonal ones, and never has both opposite off-diagonal entries nonzero. Consequently the global maximum is exactly 11.

## originality

PASS

The closest finite-characteristic construction treats r=p^t+1, excluding binary rank four; the characteristic-zero construction of order binomial(r+1,2) gives ten at r=4, not an upper bound for F2. The classical field-independent upper bound is 16 and the known exact SCOPE rank-three result does not fix rank four. Hence 11 is not a stated or mechanically implied value in those primary sources.

## value

PASS

Rank four is the next natural binary fooling-set frontier after the known exact rank-three case. Closing the concrete 11–15 or 11–16 gap with a full upper certificate and witness gives a nontrivial exact discrete extremal invariant relevant to communication complexity and rank-vs-fooling-set bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
