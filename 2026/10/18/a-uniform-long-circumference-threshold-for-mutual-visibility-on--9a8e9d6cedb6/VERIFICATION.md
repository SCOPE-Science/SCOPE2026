---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A shortest path in a fixed cycle layer cannot move in the path coordinate. Four marks in such a layer obstruct both arcs between an alternating pair, proving the upper bound 3s. For the stated M, h=floor(t/3)>=2s separates the three width-s windows and makes all marked columns distinct. In one window a move in the starting column followed by a move in the destination row has length 2|a-b| and no marked interior. Across windows orient from one to its cyclic successor. The forward column distance is h+b-a, or h+r+b-a across the wrap with r=t-3h. Thus t-2D is at least h+r-2(s-1) before the wrap and h-r-2(s-1)>=0 at the wrap. Equality is harmless: the selected arc is still shortest. Switch rows in the empty column immediately after the first window; each row segment encounters only its own marked endpoint. This also works when the endpoints have identical first coordinates. The resulting length is D+|a-b|. Independently, reachable-set expansion on the graph with other marks removed checked 699 endpoint pairs including all three residues at s=3 and s=5; replay: python3 -I /tmp/opencode/frozen_audit_small_checks.py, visibility(). These finite checks corroborate the path argument; frozen scripts were inspected, not run.

## originality

PASS

The prior literature supplies the upper bound and predicts the numerical answer, but does not prove this long-cylinder case. The closest distinct catalogue record is a later mathematical strengthening of the numerical result and overlaps even in its construction for two residues. It is not evidence that the frozen October record was covered as of its date. The priority conclusion is qualified to the inspected, dated evidence and to ordinary mutual visibility.

## value

PASS

This explicitly realizes the conjectured optimum in a natural unbounded regime, including arbitrary path height and all cycle residue classes. The empty-column switch explains why both the cycle geodesic constraint and the avoidance constraint can be met simultaneously. It is a partial solution with a sufficient, not asserted sharp, threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
