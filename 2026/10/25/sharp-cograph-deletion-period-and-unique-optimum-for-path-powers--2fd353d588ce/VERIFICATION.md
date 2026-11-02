---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Every 2k+2 consecutive vertices split into k+1 opposite pairs. Selecting k+3 forces two complete opposite pairs, which induce P4; hence at most k+2 per block. Periodic 1^(k+2)0^k choices reach the bound. The saturated suffix forces its preceding k zeros, yielding backward uniqueness when r=k+2; shifting/reversing witnesses show nonuniqueness otherwise. Independent exhaustive induced-P4 subset enumeration checked n<=11 and 1<=k<=6 (66 pairs). The symbolic window proof covers all integers, including n<=k+2.

## originality

PASS

Ribbon two-subcolorability guarantees partition into two cluster graphs, not exact largest induced cograph or residue-wise uniqueness. No directly covering sharp formula identified, subject to older interval-graph transversal literature.

## value

PASS

Exact natural P4 vertex-deletion invariant and sharp period on standard proper/unit interval graphs, plus complete uniqueness criterion, quantitatively stronger than two-subcolorability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
