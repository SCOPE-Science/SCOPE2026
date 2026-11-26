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

The ordinary grid has 24 cells, 12+16+18 adjacency edges and 8+9+12 elementary squares. The first-uncovered-cell branching is exhaustive and duplicate-free, since a matching chooses exactly one branch at that cell; the floor transfer count is an additional independent count in the frozen package. Single-square replacement gives all and only the required flips. The frozen four-edge symmetric-difference test is equivalent: the difference consists of even alternating cycles, and a four-cycle in this grid is an elementary square. A separately implemented enumeration using tuples of cell pairs and explicit local replacements, followed by component search, reflection tests and all-source BFS, reproduced 1,845 vertices, 6,949 edges, components of sizes (1825,5,5,5,5) and edge counts (6933,4,4,4,4), minimum degree 1, the single reflection orbit on exceptional components, and the full eccentricity and pair-distance histograms (1,664,400 unordered pairs in the giant component). The exceptional connected trees with degrees (1,1,2,2,2) are paths with radius 2 and diameter 4; the giant radius and diameter are 10 and 16. This is exhaustive finite computation, not formal verification or a general box result.

## originality

PASS

The supported distinct result is the fixed-volume component census and metric, with exceptional paths, no frozen tiling and the symmetry orbit. Neither disconnectedness, the choice of box, nor an unrefined tiling count alone is the novelty basis. The strongest checked prior passages do not supply or imply this classification.

## value

PASS

This is a previously motivated small nonperiodic box used in domino-group constructions. Its local dynamics distinguish global disconnectedness from the presence of immobilized tilings: every state moves, yet four entire nontrivial path components are trapped. The decomposition, reflection orbit and complete distance data supply a useful exact benchmark for studying unrefined flips on this specific box, rather than a routine recount of tilings or a claim about all boxes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
