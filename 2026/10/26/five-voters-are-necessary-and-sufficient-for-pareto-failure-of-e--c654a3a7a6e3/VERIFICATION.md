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

A dominating pair overlapping W would be one strictly profitable swap. For disjoint pairs, only the restrictions to their four names enter the four necessary swap inequalities. In units of ordinary PAV the six compatible per-ballot swap sums at (u,v)=(0,0),(0,1),(0,2),(1,1),(1,2),(2,2) are 0,2,4,-1/2,1,0. Thus (0,2) needs nine voters, and (0,1) needs at least five; with five and one (0,1), all four gains must vanish. Naming its approval a0, the gains for w0→a1 and w1→a0 are -x+y/2 and 1-y+x/2, where x and y count {w0,a0} and {w1,a1}, forcing x=2/3. For a (1,2) approving {w0,a0,a1}, the two swaps dropping w1 force both w1 cross types, since a negative contribution to a swap requires approving the dropped winner and just the alternative not added. Those two cross ballots then each add +1/2 to one swap dropping w0, forcing both w0 cross types by the same rule. This exhausts all five ballots. In the four-candidate witness the W and O scores are 5 and 11/2, the swap gains are (-1/2,-1/2,0,0), and just the final ballot is strictly better under O. Four candidates are necessary by disjointness. Outside approvals can affect swaps to outsiders but do not change the necessary profile restrictions. Independent exact replay /workspace/branches/replay_2.py enumerated all four-name ballot multisets through five voters and returned counts [0,0,0,0,2], with the two labeled patterns one within-pair orbit; the unrestricted candidate result is analytic.

## originality

PASS

The ordinary Pareto failure of exact local PAV is already known. The supported distinction is the sharp voter lower bound and the classification of all minimal restrictions, not failure itself or the cross-ballot construction idea. The strongest checked primary counterexample and nearby exact indexed record do not entail that boundary.

## value

PASS

This gives a sharp electorate boundary for a natural efficiency guarantee of the simplest nontrivial PAV committee size and a complete extremal pattern valid even with arbitrary extra candidates. It characterizes where single-swap tests first fail to detect a Pareto improvement and shows that at the first failure the swap ties matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
