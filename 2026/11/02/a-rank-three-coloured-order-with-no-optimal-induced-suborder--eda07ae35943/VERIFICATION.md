---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The first-move EF recursion makes the set of (left rank-2 fingerprint, colour, right rank-2 fingerprint) an exact rank-3 equivalence invariant. Every position gives at most one such character, so the 70-character A is optimal. An independently implemented C++ program reconstructs both literal words and 32-bit rank-2 masks, confirms lengths 70/73, equality of all 70 characters, and exhausts all C(73,3)=62,196 three-deletion induced subwords; NONE has the same signature, and the maximum reference-type overlap is 68. This is full finite exhaustion, not sampling. The original source verifier and a separate Python EF implementation were read, not blindly relied on.

## originality

PASS

The 70-letter class and rank-three EF recurrence are credited to Mwesigye–Truss, which explicitly anticipates the failure of induced-suborder optimality in rank three. The additional 73-letter witness with full 62,196-case nonembedding is a concrete solution of that open construction problem. No stronger overlapping primary theorem was found in the compared material; possible other unindexed witnesses are a bounded priority risk.

## value

PASS

The example resolves a specific advertised finite-model-theoretic obstacle: in three moves a shortest representative need not embed as an induced coloured order, unlike the two-round setting. A fully reproducible finite counterexample with exact minimal class size gives a reusable boundary example; no global minimality of the counterexample length is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
