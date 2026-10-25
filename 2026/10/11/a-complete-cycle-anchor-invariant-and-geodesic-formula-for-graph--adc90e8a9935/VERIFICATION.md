---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Read the complete actual frozen RESULT.md, verification program, slogan and metadata/audit/review files. Equality of integral cycle evaluations is equivalent to exactness of (a_X-a_Y)/2, so spanning-tree integration defines integer h unique modulo constants, with h(u)-h(v)∈{0,1} along every X-arc. A fully X-directed cycle saturates its signature and so every cycle edge is fixed in Y, giving equal cyclic-vertex sets and h constant on each directed cycle. A flex can never occur at a cyclic vertex, forcing all h-values there to equal one common gauge. Conversely choose that common anchor as zero (or a median when acyclic); for positive maximal h-level U, no X-arc enters U and U contains no directed cycle because all cyclic h-levels are zero; its induced DAG has a source that is a full source, whose flex decreases its h-value by one. The negative minimal level gives a full sink and increases h by one. This terminates after sum|h| legal moves at Y. Since every vertex move changes exactly one h-coordinate ±1, every path requires at least min_k sum|h-k| flips, with gauge fixed to the frozen anchor when cyclic: the construction meets that lower bound. Boundary cases: nonempty connected simple graph with at least one edge, identical X/Y distance zero, orientation pairs with unequal signatures disconnected, multiple cyclic SCCs anchor obstruction, acyclic case unrestricted gauge. Independent Kosaraju-SCC/BFS/relative-potential program (not copied from verify_flex.py) checked all 620,468 ordered orientation pairs on 62 separately generated connected graphs with 2–6 vertices and at most 8 edges, matching exact BFS distances and reachability for every pair; 584,208 were unreachable. This corroborates, not replaces, the all-finite-graph proof.

## originality

PASS

Best-of-knowledge statement-level comparison supports originality of the exact reachability and geodesic theorem on ALL orientations of arbitrary finite connected simple graphs, specifically multiple mutually frozen directed-cycle SCCs. Classical fixed-circulation lattice/height theories were materially read, including Propp’s full original PDF and Knauer’s SCC-cut theorem, and credited for acyclic components and supervertex pushes. Kozlov explicitly supplies a same-signature disconnected example and leaves full algebraic classification as Question 2. The new constraint is not implied without changing to strictly broader strong-component flips. No prior exact original-graph cycle-anchor plus median/anchor geodesic formula was identified; historical unindexed equivalence remains a genuine risk.

## value

PASS

Kozlov’s explicit 2026 Question 2 asks for an algebraic invariant completing the cycle signature after demonstrating equal-signature disconnected orientations. The proposed frozen cyclic-anchor relative potential answers that motivated all-graph structural question, yields an effective finite if-and-only-if component test, and constructs geodesics with a closed ℓ1 median/anchor length. The distinction between individual legal flexes and cyclic SCC supervertex pushes is substantive and potentially useful for orientation reconfiguration and flex complex 1-skeleta. The acyclic special case and SCC-lattice machinery are prior work; value derives from the cyclic obstruction and exact metric, not merely an accessible proof of a textbook special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
