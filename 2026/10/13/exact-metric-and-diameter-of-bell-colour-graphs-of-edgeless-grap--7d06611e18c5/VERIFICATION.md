---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For partitions P,Q of [n] with <=k blocks, any length-t single-element-move path leaves at least n-t elements unmoved, which induce a matching of initial and final partition blocks; hence t>=n-mu(P,Q), where mu is maximum intersection-weight bipartite matching. Conversely pad each block family to k common temporary labeled slots, match maximum overlap via slot bijection and recolor each of the n-mu mismatched elements exactly once to its target slot. At most k nonempty slots occur; removing no-change steps gives a path of length <=n-mu. Thus d=n-mu for all 1<=k<=n, and truncated Bell partition graph is isometric in full Bell graph. Random k-slot perfect matching has expected total overlap n/k, so mu>=ceil(n/k); taking P balanced k blocks and Q the one-block partition attains equality, proving diameter n-ceil(n/k). Independent from-scratch BFS and dynamic-programming matching checks agree across every pair for n<=5/all k, 7,777 tested ordered pairs. Unlimited statement is from the matching proof, not finite BFS.

## originality

PASS

Classical partition comparison gives transfer/matching distance n-mu as minimum number of ground elements needing reassignment; this expression itself is NOT claimed new. Finbow–MacGillivray Bell-colour paper defines partition-move graph and studies connectivity/Hamiltonicity, and Hearn reconstructs source graphs; their inspected statements do not give the exact isometric truncation theorem or diameter. A publication equating the classical transfer metric with this identical partition reconfiguration graph under other terminology remains the most material originality risk.

## value

PASS

Determining the exact shortest-path metric and sharp diameter simultaneously for all n and every block cap k is a natural complete invariant of Bell-colour reconfiguration graphs; the cap surprisingly never creates a geodesic detour, which does not follow from knowing classical transfer distance in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
