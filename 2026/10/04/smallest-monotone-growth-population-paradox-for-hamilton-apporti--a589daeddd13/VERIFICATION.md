---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

With one seat, a seat can move from state i to state j only if the population ordering reverses, which forces j to have the larger relative growth and therefore cannot make the faster-growing loser. With two states, Hamilton's assignment is the nearest-integer/lower-quota rule for one quota; increasing state i's population relative to state j monotonically increases that quota, so i cannot lose a seat to j when i grows faster. Thus any paradox needs at least three states and two seats. A fresh exhaustive search over positive integer old/new triples, componentwise nondecreasing, all strict Hamilton cutoffs, and increasing combined population total found the first paradoxes at total 46 and exactly six of them, the coordinate permutations of the displayed example. The representative indeed has loser growth \(18/14=9/7\) exceeding gainer growth \(5/4\).

## originality

PASS

Classical apportionment literature explains Hamilton's population paradox and gives historical or pedagogical examples, while separate minimality literature treats the Alabama paradox. Targeted searches did not locate the sharp population-paradox boundary \((s,h)=(3,2)\), the minimum combined population 46, or the six-example orbit. The result is therefore a new exact finite boundary rather than a rediscovery of the well-known existence of the paradox.

## value

PASS

This is a natural sharp boundary for a classical apportionment pathology: it proves the minimum dimensions in which the paradox can occur and then completely classifies the smallest integer witnesses. Such minimal-counterexample results are useful for teaching, testing implementations and isolating the mechanism of failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
