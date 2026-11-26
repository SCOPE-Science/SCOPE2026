---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A legal move is a matching of all source guards into distinct vertices of an equal-sized dominating destination, with closed neighborhoods giving allowed edges and the attacked vertex required in the destination. I reconstructed the labeled graph and enumerated every subset of sizes 0–7, with counts (0,0,0,0,0,0,10,780). For each unordered equal-size dominating pair A,B, an independent Hall test exhausts all nonempty X⊆A and requires |B∩⋃ₐ∈ₓN[a]|≥|X|; this tests all responses, including impossibility, and reversibility gives both directions. All 10 six-sets have two fatal attacks, and the seven-set histogram is 20 with one fatal attack, 760 with none. Independent all-pairs distances yield the sphere profile (1,3,6,6,3,1) and the trap-to-fatal-vertex bijection. Restricting targets to the 760 survivors gives a response for each of 9,880 source/attack pairs; the minimum number of distinct destination sets is 26, attained for instance at source mask 19621 and attack 8. Because the survivor set is closed under at least one response to every legal attack, choosing a safe response at every turn is a perpetual strategy; by contrast the other 20 and all six-sets can be defeated immediately. The exact 26 counts destination sets, not different bijections to a single set, as the proof specifies.

## originality

PASS

Pass for the complete viable-state classification, the geometric single-attack traps, and the sharp number of distinct safe destinations. The domination number and reportedly known seven-guard construction do not carry this originality decision.

## value

PASS

This natural finite game instance distinguishes minimum guard budget from the exact set of viable positions. The distance-shell obstruction gives a succinct description rather than a list of masks, and the positive sharp reply count shows that every other one-step-safe configuration is indefinitely safe with multiple distinct choices. This makes it an informative exact benchmark for safety-region enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
