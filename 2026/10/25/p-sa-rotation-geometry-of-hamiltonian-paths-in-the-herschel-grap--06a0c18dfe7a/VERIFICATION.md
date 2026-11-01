---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The explicit eleven-vertex bipartite graph has five blue and six red vertices, eighteen edges, and red degree three. Both endpoints of a spanning path are red; four distinct Pósa moves follow. An independently written exhaustive red-start DFS recovered exactly 222 reversal classes. A separate construction of the complete rotation graph recovered 444 edges and eccentricities 8:198 and 9:24, connected from every root. The enumeration has no truncation; a one-edge exchange rejoining two split paths is an endpoint rotation because there is no Hamiltonian cycle.

## originality

PASS

Pósa rotations themselves and the graph identity are classical. Krivelevich Section 2.3 bounds rotated endpoints in expanding graph settings; it does not classify the entire Herschel spanning-path reconfiguration graph. The computed diameter/eccentricity profile was not found in actual searches. This is a qualified priority assessment, not exhaustive novelty certification.

## value

PASS

The smallest non-Hamiltonian polyhedral graph is a motivated test case for complete Hamiltonian-path reconfiguration. Connectivity, exact diameter and full eccentricity distribution distinguish the path-state geometry from existence of one Hamiltonian path, and have finite exact combinatorial meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
