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

The deficiency sum for an n-coloring permits at most one singleton. Except at at most two vertices, the code is therefore determined by its one missing color, giving a contradiction for n>=3. The proposed proper (n+1)-coloring distinguishes the incident-color complements, which are exactly the nonzero coordinates of the locating codes. I checked the terminal-versus-bulk congruences, the complete four-collision list in the divisible-by-three case, and the replacement pairs including k=3 and k=4. The three small permutations work. Unused colors are ruled out by the number of distinct two-element complements.

## originality

PASS

No inspected source covers the sharp edge-locating invariant for this deletion family. The same numerical answer for two vertex-coloring invariants on the same graph is not the theorem being audited.

## value

PASS

This computes a sharp, naturally defined invariant on an infinite family adjacent to the motivating complete bipartite case. The one-color savings under matching deletion is nontrivial because locating constraints need not survive deletion; the explicit modular construction and separate lower bound establish the exact change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
