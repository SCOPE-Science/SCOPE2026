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

Deleting the forbidden u->v leaves one excess incoming edge at u and one excess outgoing edge at v. Every admissible tour adds an integral u-to-v unit flow; an optimal flow uses a shortest permitted path alone. All original edges lie on directed cycles, so deletion leaves the underlying graph connected and a balanced augmentation really does have an Euler tour. For end-position markers the all-zero vertex cannot be entered or cannot be left, respectively. For an interior marker, d=1 is forbidden. At 2<=d<n the spelled word is covered by its prescribed prefix and suffix; the two forced ones must lie outside the opposing block but inside the first and last forbidden-candidate windows. This forces d=i+1=j+1. In that case every window of the unique spelling contains both ones. Off center d=n leaves one free bit, and zero there makes the first window forbidden. One there prevents the first and last ones from creating a forbidden window and cannot itself be preceded by i and followed by j zeros. A shortest path is simple, so its factors are distinct and the set of extra traversals is unique; this is not uniqueness of the cyclic word. Complementation preserves all conclusions. Independent replay `cd /workspace && python3 review_replay.py 1` checked all 75 deletion cases of orders 3..12, including shortest-path counts and the prescribed spellings, plus literal existence at length 9 versus nonexistence at length 8 for 010. This supports, not replaces, the all-order argument. The frozen verification and code (including its Euler-witness checks) were inspected but not executed.

## originality

PASS

The Eulerian extension problem and reduction are established, and exact-once obstruction is already known. The supported distinct result is the explicit host-avoiding all-order one-hot formula, including the central saving, impossible boundary cases and rigid duplication profile. The closest indexed covering results allow the forbidden edge in the covering host and give demonstrably different optima on the same required sets.

## value

PASS

Deleting the unique sparse marker pattern is a motivated perturbation of universal cyclic coverage. Knowing whether coverage can coexist with avoidance, exactly how much repetition is forced, and exactly which factors must repeat gives a concrete construction and obstruction benchmark. Neither the odd-centered shortcut nor the uniqueness of the duplication pattern follows from being able to compute a shortest path in each example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
